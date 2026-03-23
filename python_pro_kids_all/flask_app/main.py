import random
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'segredo-educativo'

QUESTIONS = [
    ('Quanto é 3 + 4?', '7'),
    ('Qual animal faz mu?', 'vaca'),
    ('Quanto é 9 - 3?', '6'),
    ('Qual cor do céu em um dia limpo?', 'azul'),
]

@app.route('/', methods=['GET', 'POST'])
def index():
    feedback = ''

    if 'score' not in session:
        session['score'] = 0
    if 'question' not in session:
        q, a = random.choice(QUESTIONS)
        session['question'] = q
        session['answer'] = a

    if request.method == 'POST':
        user_answer = request.form.get('answer', '').strip().lower()
        if user_answer == session['answer']:
            session['score'] += 1
            feedback = 'Parabéns! Você acertou.'
        else:
            feedback = f'Resposta incorreta. A certa era: {session["answer"]}'

        q, a = random.choice(QUESTIONS)
        session['question'] = q
        session['answer'] = a

    return render_template('index.html', question=session['question'], score=session['score'], feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)
