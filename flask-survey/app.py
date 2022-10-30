from flask import Flask, request, url_for, flash, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'scott'
toolbar = DebugToolbarExtension(app)

responses = []


@app.route('/')
def home():
    return render_template('index.html', survey=satisfaction_survey)

@app.route('/questions/<int:n>')
def question(n):
    if n > len(responses):
        n= len(responses)
        flash('DONT SKIP QUESTIONS')
        return redirect(f'/questions/{n}')
    return render_template('question.html', idx=n, survey=satisfaction_survey)

@app.route('/answers', methods=["POST"])
def answer():
    responses.append(request.form['choice'])
    if len(responses) < len(satisfaction_survey.questions):
        return redirect(f'/questions/{len(responses)}')
    else:
        flash('Thanks for taking our survey!!')
        return redirect(url_for('home'))

app.run()