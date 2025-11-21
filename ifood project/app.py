import streamlit as st
import styles 
import logic  

st.set_page_config(page_title="iFood: Menu Mágico", page_icon="🍔", layout="centered")

# 1. APLICAR O NOVO CSS E MOSTRAR O CABEÇALHO
styles.aplicar_css_avancado()
styles.mostrar_cabecalho_com_logo()

# 2. Formulário (Inputs)
col1, col2 = st.columns(2)
with col1:
    nome_prato = st.text_input("Nome do Prato", placeholder="Ex: Hambúrguer Artesanal Duplo")
with col2:

    tom = st.selectbox("Tom de Voz", ["🔥 Vendedor (Alta Conversão)", "🍷 Gourmet (Premium)", "🤪 Divertido (Casual)"])

ingredientes = st.text_area("Ingredientes Principais", placeholder="Pão brioche selado na manteiga, 2 burgers de costela 180g, queijo cheddar inglês, bacon caramelizado...")

# 3. Botão e Ação
# Usei um emoji diferente no botão
if st.button("✨ Gerar Descrição Irresistível ✨"):
    
    if not nome_prato or not ingredientes:
        # Usando st.error para validação
        st.error("⚠️ Opa! Você esqueceu de preencher o nome do prato ou os ingredientes.")
    
    else:
        # Chama a simulação de espera (UX)
        logic.processar_ia()
        
        # Gera o texto usando a lógica
        resultado_final = logic.gerar_descricao_simulada(nome_prato, ingredientes, tom)
        
        # --- AQUI ESTÁ A MÁGICA VISUAL ---
        # Em vez de texto solto, usamos HTML para colocar dentro do CARD que criamos no CSS
        st.markdown(f"""
            <div class="result-box">
                <div class="result-title">🎯 Resultado da IA:</div>
                <div class="result-text">{resultado_final}</div>
            </div>
        """, unsafe_allow_html=True)

        # Um balãozinho de sucesso discreto no canto
        st.toast('Descrição gerada com sucesso!', icon='✅')

# Rodapé Profissional
st.markdown('<div class="footer">Desenvolvido por Gustavo Piumbini</div>', unsafe_allow_html=True)