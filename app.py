
import streamlit as st
import os
import base64
from PIL import Image
import time
import json

USER_FILE = "users.json"
if not os.path.exists(USER_FILE):
    with open(USER_FILE, "w") as f:
        json.dump({"teste@exemplo.com": "123456"}, f)

with open(USER_FILE, "r") as f:
    user_db = json.load(f)

st.set_page_config(
    page_title="Portal de Ativação Divina",
    page_icon="🌟",
    layout="centered",
)

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
    table, th, td {
        border: none;
        padding: 6px 12px;
    }
</style>
""", unsafe_allow_html=True)

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
                with open(USER_FILE, "w") as f:
                    json.dump(user_db, f)
                st.success("Cadastro realizado com sucesso! Faça login.")

    elif menu_option == "Esqueci a Senha":
        recovery_email = st.text_input("Digite seu email cadastrado")
        if st.button("Recuperar"):
            if recovery_email in user_db:
                st.info(f"Sua senha é: {user_db[recovery_email]}")
            else:
                st.error("Email não encontrado na base de dados.")
elif st.session_state.logged_in:
    with st.spinner('✨ Ativando energias sagradas... Aguarde um momento...'):
        time.sleep(2)

    banner_path = "top_banner.png"
    if os.path.exists(banner_path):
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        st.image(Image.open(banner_path), width=320)
        st.markdown("</div>", unsafe_allow_html=True)

    st.title("🌟 Bem-vindo ao Portal de Ativação Divina")
    st.markdown("""
    <div style='text-align: center; font-size: 18px; margin-bottom: 30px;'>
    Descubra ferramentas espirituais que alinham sua alma com a frequência divina original.
    </div>
    """, unsafe_allow_html=True)

    menu = st.selectbox("Escolha uma experiência:", [
        "📜 Lista das 22 Palavras Sagradas",
        "🙏 Orações com as Palavras Sagradas",
        "🔊 Áudio de Ativação da Frequência Divina"
    ])

    palavras_tabela = [
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

    def render_audio(folder):
        path = os.path.join("audios", folder)
        if os.path.exists(path):
            for f in sorted([x for x in os.listdir(path) if x.endswith(".mp3")],
                            key=lambda x: int(''.join(filter(str.isdigit, x)) or 0)):
                st.markdown(f"#### 🎧 {f.replace('_', ' ').replace('.mp3', '').title()}")
                with open(os.path.join(path, f), "rb") as audio_file:
                    st.audio(audio_file)
                    st.download_button("⬇️ Baixar Áudio", audio_file, file_name=f)
                st.markdown("---")

    if menu == "📜 Lista das 22 Palavras Sagradas":
        st.header("📜 As 22 Palavras Hebraicas Sagradas")
        table_html = '''
        <table style="width:100%; border-collapse: collapse; font-size: 18px;">
            <tr>
                <th style="text-align: left; border-bottom: 1px solid white;">Nº</th>
                <th style="text-align: left; border-bottom: 1px solid white;">Palavra Hebraica</th>
                <th style="text-align: left; border-bottom: 1px solid white;">Transliteração</th>
                <th style="text-align: left; border-bottom: 1px solid white;">Tradução</th>
            </tr>
        '''
        for i, (hebraico, translit, traducao) in enumerate(palavras_tabela, 1):
            table_html += f'''
            <tr>
                <td>{i}</td>
                <td>{hebraico}</td>
                <td>{translit}</td>
                <td>{traducao}</td>
            </tr>
            '''
        table_html += '</table>'
        st.markdown(table_html, unsafe_allow_html=True)

        pdf_path = "pdfs/As-22-Palavras-Sagradas-22-Oracoes-para-ativacao-de-bencaos.pdf"
        if os.path.exists(pdf_path):
            with open(pdf_path, "rb") as f:
                st.download_button("📥 Baixar PDF com as 22 Palavras + Orações", f, file_name="As-22-Palavras-Sagradas-22-Oracoes-para-ativacao-de-bencaos.pdf")

    elif menu == "🙏 Orações com as Palavras Sagradas":
        st.header("🙏 Orações com as 22 Palavras Sagradas")
        render_audio("oracoes")

    elif menu == "🔊 Áudio de Ativação da Frequência Divina":
        st.header("🔊 Frequências Divinas")
        render_audio("code")
