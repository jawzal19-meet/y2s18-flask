from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
# def home_page():
#     return ("voleyball")

def favSport():
    return render_template(
"index.html")

@app.route('/')
def Color():
    return render_template(
"index.html")

@app.route('/players')
def favPlayers():
	players=["yaman","yanal","hawzan", "lobna"]
	return render_template(
		"index.html", 
		players=players,
		likes_same_sport=True)



if __name__ == '__main__':
   app.run(debug = True)