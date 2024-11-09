from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/responder', methods=['POST'])
def responder():
    resposta = request.form.get('resposta')
    if resposta == 'sim':
        mensagem = "YES! 🎉 Vamos marcar então um horário!"
    elif resposta == 'opcao1':
        mensagem = "YES! 🎉 Vamos com a Opção 1, então!"
    else:
        mensagem = "Se você não marcar uma opção, vou aí pessoalmente e te fazer morrer de rir com cosquinhas!"
    return render_template('index.html', mensagem=mensagem)

if __name__ == '__main__':
    app.run(port=5001)
