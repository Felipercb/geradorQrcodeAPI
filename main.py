# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, send_file
import qrcode
from agendamentos_eniac import gerarQr
import base64
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
	return send_file('qrCodes/agendamento.png', mimetype='image/png', as_attachment=True)

@app.route('/teste', methods = ['POST'])
def ola():
	try:
		gerarQr(request.json['nome'], request.json['evento'], request.json['descricao'])
		with open("qrCodes/agendamento.png", "rb") as image_file:
			encoded_string = base64.b64encode(image_file.read())
		return encoded_string
	except:
		return 'Verifique seus parâmetros'

@app.route('/post', methods = ['POST'])
def qrcode():
	print(request.json)
	try:
		gerarQr(request.json['nome'], request.json['evento'], request.json['descricao'])
		with open("qrCodes/agendamento.png", "rb") as image_file:
			encoded_string = base64.b64encode(image_file.read())
		return encoded_string
	except:
		return 'Verifique seus parâmetros'

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run(port = 9090, debug = True, host='192.168.178.100')
