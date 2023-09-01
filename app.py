from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('pagina.html')

@app.route('/criar_monstrinho', methods=['POST'])
def criar_monstrinho():
    try:
        tipo = request.form['tipo']
        olho = request.form['olho']
        boca = request.form['boca']
        acessorio = request.form['acessorio']
 
        # Abra o arquivo "monstro.txt" em modo de anexação (append) e escreva as informações do monstrinho
        with open('monstro.txt', 'a') as file:
            file.write(f'Tipo: {tipo}, Olho: {olho}, Boca: {boca}, Acessório: {acessorio}\n')

        return "Monstrinho criado com sucesso!"
    except Exception as e:
        print('Erro ao criar o monstrinho:', str(e))
        return "Algo deu errado ao criar o monstrinho."

if __name__ == '__main__':
    app.run(debug=True)
