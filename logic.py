import random
import time
import streamlit as st

def gerar_descricao_simulada(prato, ingredientes, tom):
    """
    Simula uma geração de IA baseada em templates e aleatoriedade.
    """
    
    # Templates de texto (Engenharia de Prompt simulada)
    templates_gourmet = [
        f"✨ **Sofisticação em cada detalhe:** Apresentamos o {prato}. Uma combinação harmoniosa de {ingredientes}, selecionados para paladares exigentes. Permita-se viver essa experiência gastronômica.",
        f"🍷 **Arte comestível:** O {prato} redefine o sabor. Preparado com {ingredientes} frescos, é a escolha perfeita para quem não abre mão de qualidade suprema."
    ]
    
    templates_divertido = [
        f"🤤 **Alerta de Delícia:** O {prato} acabou de pousar na área! Recheado com muito {ingredientes}, ele vai destruir sua fome em 3, 2, 1... Peça logo!",
        f"🚀 **NASA, temos um problema:** O sabor do {prato} é de outro mundo! Turbinado com {ingredientes}. Cuidado: causa felicidade instantânea."
    ]
    
    templates_vendedor = [
        f"🔥 **O CAMPEÃO DE VENDAS:** {prato}! Feito no capricho com {ingredientes}. Saboroso, gigante e irresistível. Quem prova, pede de novo!",
        f"🍔 **Mata sua fome AGORA:** Não passe vontade, passe o cartão! {prato} com {ingredientes} é a melhor pedida do dia. Chega quentinho e rápido!"
    ]

    # Seleção Lógica
    if "Gourmet" in tom:
        escolha = random.choice(templates_gourmet)
    elif "Divertido" in tom:
        escolha = random.choice(templates_divertido)
    else:
        escolha = random.choice(templates_vendedor)
        
    return escolha

def processar_ia():
    # Simula o tempo de processamento da IA (UX)
    with st.spinner("🤖 A IA está analisando seus ingredientes..."):
        time.sleep(1.5)