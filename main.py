from flask import Flask, request, send_file
import qrcode
from agendamentos_eniac import gerarQr
import base64

app = Flask(__name__)

@app.route('/post', methods = ['POST'])
def qrcode():
	try:
		gerarQr(request.json['nome'], request.json['evento'], request.json['descricao'])
		with open("qrCodes/agendamento.png", "rb") as image_file:
			encoded_image = base64.b64encode(image_file.read())
		return encoded_image
	except:
		return 'Verifique seus parâmetros'

if __name__ == '__main__':
	app.run(debug=True)
