from  flask import Flask

app = Flask(__name__)
@app.route('/')
def hello():
	return '<h1 style = "color :blue;">Feliz aniversario professor.Terca trago sua lembranca.<h1><h2 style="color:blue;">POR:Francisco Luiz <h2>'  
if __name__=='__main__':
	app.run()
