#scp -i vpctesting1.pem ubuntu@10.0.0.131:~/webapps/m8connect/m8connect/a.pdf a.pdf
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib import colors

width, height = letter
styles = getSampleStyleSheet()
styleN = styles["BodyText"]
styleN.alignment = TA_LEFT
styleBH = styles["Normal"]
styleBH.alignment = TA_CENTER

def coord(x, y, unit=1):
    x, y = x * unit, height -  y * unit
    return x, y

# Headers
hdescrpcion = Paragraph('''<b>Line</b>''', styleBH)
hpartida = Paragraph('''<b>QTY</b>''', styleBH)
hcandidad = Paragraph('''<b>ITEM</b>''', styleBH)
hprecio_unitario = Paragraph('''<b>UNIT PRICE</b>''', styleBH)
hprecio_total = Paragraph('''<b>TOTAL PRICE</b>''', styleBH)

# Texts
descrpcion = Paragraph('Tribrid Dvr 16/32CH 4T with power supply', styleN)
partida = Paragraph('1', styleN)
candidad = Paragraph('120', styleN)
precio_unitario = Paragraph('$52.00', styleN)
precio_total = Paragraph('$6240.00', styleN)

data= [[hdescrpcion,hpartida ,hcandidad, hprecio_unitario, hprecio_total],
       [partida, candidad, descrpcion, precio_unitario, precio_total],
       [partida, candidad, descrpcion, precio_unitario, precio_total],
       [partida, candidad, descrpcion, precio_unitario, precio_total],
       [partida, candidad, descrpcion, precio_unitario, precio_total],
       [partida, candidad, descrpcion, precio_unitario, precio_total],
       [partida, candidad, descrpcion, precio_unitario, precio_total],
       [partida, candidad, descrpcion, precio_unitario, precio_total],
       [partida, candidad, descrpcion, precio_unitario, precio_total],
       [partida, candidad, descrpcion, precio_unitario, precio_total]]

table = Table(data, colWidths=[2 * cm, 2.7 * cm, 9 * cm,
                               3* cm, 3 * cm])

table.setStyle(TableStyle([
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ]))
  
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    
    c = canvas.Canvas("a.pdf", pagesize=letter)
    table.wrapOn(c, width, height)
    table.drawOn(c, *coord(1, 8, cm))
    c.save()
