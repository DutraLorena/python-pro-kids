import random
import tkinter as tk
from tkinter import messagebox

class MathGame:
    def __init__(self, root):
        self.root = root
        self.root.title('Jogo Matemático Infantil')
        self.root.geometry('420x320')

        self.score = 0
        self.rounds = 0
        self.current_answer = 0

        self.title_label = tk.Label(root, text='Desafio Matemático', font=('Arial', 18, 'bold'))
        self.title_label.pack(pady=10)

        self.score_label = tk.Label(root, text='Pontos: 0 | Rodada: 0', font=('Arial', 12))
        self.score_label.pack(pady=5)

        self.question_label = tk.Label(root, text='Clique em "Nova Conta" para começar!', font=('Arial', 14))
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(root, font=('Arial', 14), justify='center')
        self.answer_entry.pack(pady=10)

        self.feedback_label = tk.Label(root, text='', font=('Arial', 12))
        self.feedback_label.pack(pady=10)

        self.new_button = tk.Button(root, text='Nova Conta', command=self.new_question, width=16)
        self.new_button.pack(pady=5)

        self.check_button = tk.Button(root, text='Responder', command=self.check_answer, width=16)
        self.check_button.pack(pady=5)

    def new_question(self):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        operation = random.choice(['+', '-'])

        if operation == '-':
            a, b = max(a, b), min(a, b)
            self.current_answer = a - b
        else:
            self.current_answer = a + b

        self.question_label.config(text=f'Quanto é {a} {operation} {b}?')
        self.answer_entry.delete(0, tk.END)
        self.feedback_label.config(text='')

    def check_answer(self):
        answer = self.answer_entry.get().strip()
        if not answer:
            messagebox.showwarning('Atenção', 'Digite uma resposta antes de continuar.')
            return

        self.rounds += 1
        if answer == str(self.current_answer):
            self.score += 1
            self.feedback_label.config(text='Muito bem! Você acertou!')
        else:
            self.feedback_label.config(text=f'Quase! A resposta certa era {self.current_answer}.')

        self.score_label.config(text=f'Pontos: {self.score} | Rodada: {self.rounds}')

if __name__ == '__main__':
    root = tk.Tk()
    app = MathGame(root)
    root.mainloop()
