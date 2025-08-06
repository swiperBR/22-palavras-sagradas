import streamlit as st
import streamlit.components.v1 as components
import os
import base64
from PIL import Image
import time
import json

# --- Banco de usuários simulado ---
USER_FILE = "users.json"
if not os.path.exists(USER_FILE):
    with open(USER_FILE, "w", encoding="utf-8") as f:
        json.dump({"teste@exemplo.com": "123456"}, f)

with open(USER_FILE, "r", encoding="utf-8") as f:
    user_db = json.load(f)

# --- Configuração de página ---
st.set_page_config(
    page_title="Portal de Ativação Divina",
    page_icon="🌟",
    layout="centered",
)

# --- Estilos gerais ---
st.markdown("""
<style>
    .stApp {
        background-color: #0b1a2e;
        font-family: 'Georgia', serif;
        color: white;
    }
    h1, h2, h3, h4 {
        color: #ffffff;
        text-align: center;
    }
    .stDownloadButton button {
        background-color: #4A90E2;
        color: white;
        width: 100%;
        border-radius: 8px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- Login / Registro ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_email" not in st.session_state:
    st.session_state.user_email = None

if not st.session_state.logged_in:
    st.title("🔒 Acesso Divino - Login")
    menu_option = st.radio("Selecione uma opção:", ["Login", "Registrar", "Esqueci a Senha"])

    if menu_option == "Login":
        email = st.text_input("Email")
        password = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            if email in user_db and user_db[email] == password:
                st.session_state.logged_in = True
                st.session_state.user_email = email
                st.success("Login realizado com sucesso!")
                st.rerun()
            else:
                st.error("Email ou senha inválidos")

    elif menu_option == "Registrar":
        new_email = st.text_input("Digite seu email")
        new_password = st.text_input("Crie uma senha", type="password")
        if st.button("Registrar"):
            if new_email in user_db:
                st.warning("Usuário já existe.")
            else:
                user_db[new_email] = new_password
                with open(USER_FILE, "w", encoding="utf-8") as f:
                    json.dump(user_db, f)
                st.success("Cadastro realizado com sucesso! Faça login.")

    elif menu_option == "Esqueci a Senha":
        recovery_email = st.text_input("Digite seu email cadastrado")
        if st.button("Recuperar"):
            if recovery_email in user_db:
                st.info(f"Sua senha é: {user_db[recovery_email]}")
            else:
                st.error("Email não encontrado na base de dados.")

# --- Conteúdo protegido ---
else:
    with st.spinner('✨ Ativando energias sagradas... Aguarde um momento...'):
        time.sleep(2)

    # Banner
    banner_path = "top_banner.png"
    if os.path.exists(banner_path):
        st.image(Image.open(banner_path), width=320)

    st.title("🌟 Bem-vindo ao Portal de Ativação Divina")
    st.markdown("""
    <div style='text-align: center; font-size: 18px; margin-bottom: 30px;'>
    Descubra ferramentas espirituais que alinham sua alma com a frequência divina original.
    </div>
    """, unsafe_allow_html=True)

    # Menu principal
    menu = st.selectbox("Escolha uma experiência:", [
        "📜 Lista das 22 Palavras Sagradas",
        "🙏 Orações com as Palavras Sagradas",
        "🔊 Áudio de Ativação da Frequência Divina"
    ])

    # Função para renderizar áudios
    def render_audio(folder):
        path = os.path.join("audios", folder)
        if os.path.exists(path):
            for f_name in sorted([x for x in os.listdir(path) if x.endswith(".mp3")],
                                 key=lambda x: int(''.join(filter(str.isdigit, x)) or 0)):
                st.markdown(f"#### 🎧 {f_name.replace('_', ' ').replace('.mp3', '').title()}")
                with open(os.path.join(path, f_name), "rb") as audio_file:
                    st.audio(audio_file)
                    st.download_button("⬇️ Baixar Áudio", audio_file, file_name=f_name)
                st.markdown("---")

    # --- Seção: Lista das Palavras ---
    if menu == "📜 Lista das 22 Palavras Sagradas":
        st.header("📜 As 22 Palavras Hebraicas Sagradas")

        html_code = """
        <style>
        .table-scroll {
          width: 100%;
          border-collapse: collapse;
        }
        .table-scroll th, .table-scroll td {
          border: 1px solid #ffffff55;
          padding: 8px;
          text-align: center;
          color: white;
        }
        .table-scroll th {
          background-color: #1e2c48;
        }
        .table-scroll tr:nth-child(even) {
          background-color: #162338;
        }
        </style>
        <table class="table-scroll">
          <thead>
            <tr>
              <th>Nº</th>
              <th>Hebraico</th>
              <th>Transliteração</th>
              <th>Tradução</th>
            </tr>
          </thead>
          <tbody>
        """
        palavras = [
            ("אוֹר", "Or", "Luz"),
            ("שָׁלוֹם", "Shalom", "Paz"),
            ("אֱמוּנָה", "Emunah", "Fé"),
            ("רְפוּאָה", "Refuah", "Cura"),
            ("סְלִיחָה", "Slichah", "Perdão"),
            ("אֵשׁ", "Esh", "Fogo"),
            ("חֵן", "Chen", "Graça"),
            ("חַיִּים", "Chayim", "Vida"),
            ("אֱמֶת", "Emet", "Verdade"),
            ("תַּכְלִית", "Tachlit", "Propósito"),
            ("עֹז", "Oz", "Força"),
            ("חָכְמָה", "Chokhmah", "Sabedoria"),
            ("בְּרִית", "Brit", "Aliança"),
            ("תְּדִירוּת", "Tedirut", "Frequência"),
            ("נֵס", "Nes", "Milagre"),
            ("דְּמָמָה", "Demamah", "Silêncio"),
            ("מַפְתֵּחַ", "Mafteach", "Chave"),
            ("שַׁעַר", "Sha'ar", "Porta"),
            ("הִתְעוֹרְרוּת", "Hit'or'rut", "Despertar"),
            ("תִּקוָה", "Tikvah", "Esperança"),
            ("מַרְגּוֹעַ", "Margoa", "Alívio"),
            ("קְרִיאָה", "Kri'ah", "Chamado")
        ]
        for i, (heb, tr, pt) in enumerate(palavras, 1):
            html_code += f"<tr><td>{i}</td><td>{heb}</td><td>{tr}</td><td>{pt}</td></tr>"
        html_code += "</tbody></table>"

        components.html(html_code, height=600, scrolling=True)

    # --- Seção: Orações ---
    elif menu == "🙏 Orações com as Palavras Sagradas":
        st.header("🙏 Orações com as 22 Palavras Sagradas")
        render_audio("oracoes")

    # --- Seção: Áudios de Frequência ---
    elif menu == "🔊 Áudio de Ativação da Frequência Divina":
        st.header("🔊 Frequências Divinas")
        render_audio("code")

    # --- Oferta Extra: Novena da Transformação ---
    st.markdown("---")
    st.header("✨ Novena da Transformação")
    st.markdown(
        "🚀 Embarque em uma jornada de 9 dias para renovar sua mente, corpo e espírito. "
        "Experimente bênçãos profundas e transforme sua vida!"
    )
    st.markdown(
        "[👉 Garanta sua vaga na Novena da Transformação](https://lastlink.com/p/C0962EF86/checkout-payment/)"
    )
