## IMPORTANDO "PARTES" DO FLASK
from flask import Flask, render_template,request

app = Flask(__name__)


nome = "Imunes ao conhecimento"

### Criando Rotas
@app.route("/")
def principal():
    return "essa é a pagina principal"
## / Significa principal onde o site já vai de cara

# agora vou cria a rota olá
@app.route("/ola")
def olá():
   return f"olá {nome}"

##cria uma rota chamada motivacional e deixe uma mensagem motivacional
@app.route("/motivacional")
def motivacional():
   return "viva o agora pois o amanhã pertence a Deus"


## crie uma rota chamada adues e deixe uma mensagem de despidida
@app.route("/despedida")
def despedida():
   return "foi um prazer ter te conhecido,até a proxima"

##crie uma rota chamada hobbies:
@app.route("/hobbies")
def hobbies():
   lista_hobbies = ["comer","dormir","assistir netflix","tiktok","instagram","andar de bicicleta","joga","me arrumar","fica na rua com amigos"]
   return render_template("hobbies.html",hobbies=lista_hobbies)

## executando o arquivo 
if __name__ == '__main__':
    app.run(debug=True) 