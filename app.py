from groq import Groq
import os
from flask import Flask, render_template, redirect, request
import random
from opposite_generator import createOpposite

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/actioning')
def actioning():
    actions = get_actions()
    chosen_action = random.choice(actions)
    
    if "redirect" in chosen_action:
        return redirect(chosen_action["redirect"])
    else:
        return render_template('search.html', action=chosen_action)

@app.route('/search', methods=["POST"])
def searching():
    sentence = request.form.get("search")
    opposite_sentence = createOpposite(sentence)
    #return render_template('search.html', sentence=opposite_sentence)
    return redirect("https://google.com/search?q=" + opposite_sentence)




if __name__ == "__main__":
    app.run(debug=True)


'''
original_sentence = "The sun is shining brightly."
opposite_sentence = createOpposite(original_sentence)

print("Original:", original_sentence)
print("Opposite:", opposite_sentence)
''' 