from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/index', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/resultado', methods=['POST'])
def resultado():
    numero1 = request.form.get('numero1', type=float)
    numero2 = request.form.get('numero2', type=float)

    soma = numero1 + numero2

    return render_template('resultado.html', soma=soma, numero1=numero1, numero2=numero2)

@app.route('/novoautor', methods=['GET'])
def novoautor():
    return render_template("cadastro_autor.html")

@app.route('/autor', methods=['POST'])
def autor():
    autor = request.form.get('autor', type=str)
    curso = request.form.get('curso', type=str)
    instituicao = request.form.get('instituicao', type=str)
    ano = request.form.get('ano', type=str)
    funcao = request.form.get('funcao', type=str)
    empresa = request.form.get('empresa', type=str)
    ano_inst = request.form.get('ano_prof', type=str)

    return render_template('autor.html', autor=autor, curso=curso, instituicao=instituicao, ano=ano, funcao=funcao, empresa=empresa, ano_inst=ano_inst)


if __name__ == "__main__":
    app.run(debug=True)