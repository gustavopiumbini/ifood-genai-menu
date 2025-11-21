import streamlit as st
import base64

def aplicar_css_avancado():
    st.markdown("""
    <style>
        /* --- IMPORTANDO FONTE MODERNA (Inter) --- */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        /* --- TÍTULOS --- */
        h1 {
            color: #EA1D2C !important; /* Forçando vermelho iFood */
            font-weight: 800 !important;
            letter-spacing: -1px;
        }
        h2, h3 {
            color: #333 !important;
            font-weight: 600;
        }

        /* --- BOTÃO PRINCIPAL --- */
        .stButton > button {
            background: linear-gradient(45deg, #EA1D2C, #ff4b5c);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 16px 24px;
            font-size: 18px;
            font-weight: bold;
            width: 100%;
            box-shadow: 0 4px 15px rgba(234, 29, 44, 0.3);
            transition: all 0.3s ease;
        }

        .stButton > button:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(234, 29, 44, 0.5);
        }
        
        .stButton > button:active {
            transform: translateY(-1px);
        }

        /* --- INPUTS (Campos de texto) --- */
        .stTextInput > div > div > input, .stTextArea > div > div > textarea {
            border-radius: 10px;
            border: 1px solid #eee;
            padding: 10px;
        }

        /* --- CARD DE RESULTADO --- */
        .result-box {
            background-color: #FFFFFF;
            padding: 2rem;
            border-radius: 16px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.08);
            border-left: 6px solid #EA1D2C;
            margin-top: 2rem;
            animation: fadeIn 0.8s ease;
        }

        .result-title {
            font-size: 1.2rem;
            font-weight: 700;
            color: #EA1D2C;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
        }

        .result-text {
            font-size: 1.1rem;
            color: #555;
            line-height: 1.6;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        /* Rodapé */
        .footer {
            text-align: center;
            color: #999;
            margin-top: 50px;
            font-size: 0.9rem;
        }
        
    </style>
    """, unsafe_allow_html=True)

def mostrar_cabecalho_com_logo():
    # --- A MÁGICA PARA CENTRALIZAR IMAGEM LOCAL ---
    # Lemos o arquivo em modo binário e transformamos em texto base64
    # Isso permite colocar a imagem DENTRO do HTML, onde temos controle total.
    try:
        with open("img/ifoodlogo.png", "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
        img_tag = f'<img src="data:image/png;base64,{encoded}" width="150" style="margin-bottom: 10px;">'
    except Exception as e:
        st.error(f"Não consegui carregar a imagem. Erro: {e}")
        img_tag = "" # Se der erro, segue sem imagem para não quebrar

    # --- RENDERIZAÇÃO HTML ---
    # Como a imagem agora faz parte do HTML, o 'text-align: center' manda nela também!
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 20px; margin-top: -20px;">
            {img_tag}
            <h1 style='color: #EA1D2C; margin: 0; padding: 0;'>Menu Mágico: IA para Delivery</h1>
            <p style='color: #666; font-size: 1.1rem;'>Crie descrições irresistíveis em segundos.</p>
        </div>
    """, unsafe_allow_html=True)
    st.write("---")