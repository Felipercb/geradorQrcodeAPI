import qrcode
from PIL import Image, ImageFont, ImageDraw

def gerarQr(responsavel, evento, descricao):
    background = Image.open('backgrounds/background3.jpg') # abrindo o background.
    fontTitulo = ImageFont.truetype("fonts/ComicSansMS3.ttf", 20) 
    fontNormal = ImageFont.truetype("fonts/ComicSansMS3.ttf", 15)

    qr = qrcode.QRCode(box_size=4)
    qr.add_data('Nome do Responsável: ' + responsavel)
    qr.make()
    img_qr = qr.make_image()
    background.paste(img_qr, (20, 135))

    draw = ImageDraw.Draw(background)
    
    draw.text((185, 72), "Responsável:", fill='black', font= fontTitulo, stroke_width=1, stroke_fill="grey")
    draw.text((185, 107), responsavel, fill='black', font= fontNormal)

    draw.text((185, 170), "Evento:", fill='black', font= fontTitulo, stroke_width=1, stroke_fill="grey")
    draw.text((185, 205), evento, fill='black', font= fontNormal)

    draw.text((185, 258), "Descrição:", fill='black', font= fontTitulo, stroke_width=1, stroke_fill="grey")
    draw.text((185, 293), descricao, fill='black', font= fontNormal)

    background.save('qrCodes/agendamento.png')