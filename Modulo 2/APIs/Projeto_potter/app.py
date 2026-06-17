import streamlit as  st
import requests

st.title('projeto harry potter')
st.sidebar.title("Busca de Personagens")
st.sidebar.image('logo.png')

url = "https://hp-api.onrender.com/api/characters"
resposta = requests.get(url)
dados = resposta.json()
 
nomes = []
for personagens in dados:
        nomes.append(personagens['name'])

nomes.sort()
nome_escolhido = st.sidebar.selectbox('selecione:',nomes)
# Peocura o personagem escolhido na lista de dados 

personagens = None
for p in dados:
    if p ['name'] == nome_escolhido:
        personagens = p
        break
# mostra o nome do personagem 
st.header(personagens['name'])
# ===== IMAGEM EM DESTAQUE =====
#Verifica se o personagem tem imagem 
if personagens ['image'] and personagens ['image'] !="":
     st.image(personagens['image'], width=300)
else: 
     st.write(" este personagem não possui imagem")


 #Linha divisória 
st.divider()  

# informações pricipais 
st.write(f"**casa** {personagens['house']}")
st.write(f"**especie** {personagens['species']}")
st.write(f"**gênero** {personagens['gender']}")
st.write(f"**data de nascimento** {personagens['dateOfBirth']}")
st.write(f"**ano de nascimento:** {personagens['yearOfBirth']}")

#informações de varinha 
st.write("**varinha**")
st.write(f"- madeira: {personagens['wand']['wood']}")
st.write(f"nucleo: {personagens['wand']['core']}")
st.write(f"- tamanho: {personagens['wand']['length']} poilegadas")

st.write(f"**patrono** {personagens[ 'patronus']}")
st.write(f"**ator/atriz**{personagens['actor']}")

if personagens['alive']:
     st.write(f"**Está vivo?** sim")

else:
     st.write(f"**Está vivo?** não") 