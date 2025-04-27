from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Sample "Story Quests"
QUESTS = [
    {
        'id': 1,
        'story': "You are a time traveler! Solve this math puzzle to continue your journey: What is 12 * 8?",
        'answer': '96'
    },
    {
        'id': 2,
        'story': "You've reached ancient Egypt. Solve the riddle to unlock the pyramid door: What is the square root of 144?",
        'answer': '12'
    },
    {
        'id': 3,
        'story': "In medieval Europe, scholars challenge you: What is the chemical symbol for water?",
        'answer': 'H2O'
    }
]

@app.route("/")
def index():
    quest = random.choice(QUESTS)
    return render_template("quest.html", quest=quest)

@app.route("/check/<int:quest_id>", methods=["POST"])
def check(quest_id):
    user_answer = request.form.get('answer').strip()
    quest = next((q for q in QUESTS if q['id'] == quest_id), None)

    if quest and user_answer.lower() == quest['answer'].lower():
        return render_template("success.html")
    else:
        return render_template("failure.html", correct_answer=quest['answer'])

if __name__ == "__main__":
    app.run(debug=True)