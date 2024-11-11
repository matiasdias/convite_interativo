from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/responder', methods=['POST'])
def responder():
    resposta = request.form.get('resposta')
    if resposta == 'sim':
        mensagem = "Yes! 🎉 Vamos então marcar um dia!"
    elif resposta == 'opcao1':
        mensagem = "Yes! 🎉 Vamos com a Opção 1, então!"
    else:
        mensagem = "Se você não marcar nenhuma opção, vou até aí pessoalmente e te fazer morrer de rir com cosquinhas!"
    return mensagem  # Retorna apenas a mensagem em texto para o AJAX

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
