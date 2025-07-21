import streamlit as st

# Armazenamento temporário
if "usuarios" not in st.session_state:
    st.session_state.usuarios = {}

if "logado" not in st.session_state:
    st.session_state.logado = False

if "usuario_atual" not in st.session_state:
    st.session_state.usuario_atual = ""

# Opções principais
opcao = st.radio("Escolha uma opção:", ["Login", "Cadastro", "Recomendações"])

# Página de Login
if opcao == "Login":
    st.title("Login - Music RecC")
    
    email_login = st.text_input("Email:")
    senha_login = st.text_input("Senha:", type="password")
    
    if st.button("Entrar"):
        if not email_login or not senha_login:
            st.error("Por favor, preencha todos os campos.")
        elif email_login in st.session_state.usuarios:
            if senha_login == st.session_state.usuarios[email_login]["senha"]:
                st.success("Login realizado com sucesso!")
                st.session_state.logado = True
                st.session_state.usuario_atual = email_login
            else:
                st.error("Senha incorreta.")
        else:
            st.warning("Usuário não encontrado. Cadastre-se primeiro.")

# Página de Cadastro
elif opcao == "Cadastro":
    st.title("Cadastro - Music RecC")
    
    nome = st.text_input("Nome de usuário:")
    email = st.text_input("Email:")
    senha = st.text_input("Senha:", type="password")
    
    if st.button("Cadastrar"):
        if not nome or not email or not senha:
            st.error("Por favor, preencha todos os campos.")
        elif "@" not in email or "." not in email:
            st.warning("Digite um email válido.")
        elif email in st.session_state.usuarios:
            st.warning("Este email já está cadastrado.")
        else:
            st.session_state.usuarios[email] = {"nome": nome, "senha": senha}
            st.success(f"Cadastro realizado com sucesso, {nome}!")

# Página de Recomendação de Música
elif opcao == "Recomendações":
    st.title("Recomendações de Música")

    if st.session_state.logado:
        nome_usuario = st.session_state.usuarios[st.session_state.usuario_atual]["nome"]
        st.write(f"Bem-vindo(a), {nome_usuario}!")

        genero = st.selectbox("Escolha um gênero musical:", [
            "Pop", "Rock", "Hip Hop", "Eletrônica", "MPB", "Sertanejo", "Jazz"
        ])

        st.write("Aqui estão algumas músicas recomendadas:")

        if genero == "Pop":
            st.write("- Blinding Lights - The Weeknd")
            st.write("- Levitating - Dua Lipa")
        elif genero == "Rock":
            st.write("- Smells Like Teen Spirit - Nirvana")
            st.write("- Bohemian Rhapsody - Queen")
        elif genero == "Trap":
            st.write("- Sicko Mode - Travis Scott")
            st.write("- God's Plan - Drake")
        elif genero == "Eletrônica":
            st.write("- Strobe - Deadmau5")
            st.write("- Wake Me Up - Avicii")
        elif genero == "Drill":
            st.write("- Love Sosa - Chief Keef")
            st.write("- Sprinter - Central Cee")
        elif genero == "Sertanejo":
            st.write("- Evidências - Chitãozinho & Xororó")
            st.write("- Dona Maria - Thiago Brava")
        elif genero == "Jazz":
            st.write("- Take Five - Dave Brubeck")
            st.write("- So What - Miles Davis")
    else:
        st.warning("Você precisa estar logado para ver recomendações.")
