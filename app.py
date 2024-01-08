from flask import Flask, render_template, redirect, url_for
import pandas as pd
import random

app = Flask(__name__)

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = []

try:
    data = pd.read_csv("data/words_to_learn.csv", encoding='ISO-8859-1')
except FileNotFoundError:
    original_data = pd.read_csv("data/words_to_learn.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


@app.route('/')
def display_flashcard():
    global current_card
    current_card = random.choice(to_learn)
    return render_template('flashcard.html', card=current_card, background_color=BACKGROUND_COLOR)


@app.route('/mark_known', methods=['POST'])
def mark_known():
    global current_card
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    return redirect('/')


@app.route('/next_card')
def next_card():
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
