from flask import Flask, render_template, request
from securitycheck_cli import verificar_tls

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None

    if request.method == "POST":
        dominio = request.form.get("dominio", '').strip()
        resultado = verificar_tls(dominio)
        print("Resultado:", resultado)

    return render_template("index.html", resultado=resultado)



if __name__ == "__main__":
    app.run(debug=True)

