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

def HeadersFooters():
     
        # Save the state of our canvas so we can draw on it
        canvas.saveState()
        styles = getSampleStyleSheet()
 
        # Header
        header = Paragraph('This is a multi-line header.  It goes on every page.   ' * 5, styles['Normal'])
        w, h = header.wrap(doc.width, doc.topMargin)
        header.drawOn(canvas, doc.leftMargin, doc.height + doc.topMargin - h)
 
        # Footer
        footer = Paragraph('This is a multi-line footer.  It goes on every page.   ' * 5, styles['Normal'])
        w, h = footer.wrap(doc.width, doc.bottomMargin)
        footer.drawOn(canvas, doc.leftMargin, h)
 
        # Release the canvas
        canvas.restoreState()

# Table Headers
HD_LINE = Paragraph('''<b>LINE</b>''', styleBH)
HD_QTY= Paragraph('''<b>QTY</b>''', styleBH)
HD_ITEM= Paragraph('''<b>ITEM</b>''', styleBH) #Secureway part number
HD_DESCRIPTION = Paragraph('''<b>DESCRIPTION</b>''', styleBH)
HD_Unit_PRICE = Paragraph('''<b>PRICE</b>''', styleBH)
HD_EXTENDED = Paragraph('''<b>EXTENDED</b>''', styleBH)

# Texts

Line = Paragraph('11', styleN)
Qty = Paragraph('1200', styleN)
Item = Paragraph('TRB1632-4T-MMEXCE-edSS', styleN)
Description = Paragraph('Tribrid Dvr 16/32CH 4T with power supply', styleN)
Price = Paragraph('$52.00', styleN)
Extended = Paragraph('$6240.00', styleN)


# This is such a simple thing that is passively demonstrated but not explicitly addressed in the reportlab documentation:
# t = Table(tableData, style=tStyle)
# t.canv = myCanvas
# w, h = t.wrap(0, 0)
# The variables w and h will then store the table's width and height, respectively.

data= [[HD_LINE, HD_QTY,HD_ITEM,HD_DESCRIPTION, HD_Unit_PRICE, HD_EXTENDED],
       [Line, Qty,Item, Description, Price, Extended],
       [Line, Qty,Item, Description, Price, Extended],
       [Line, Qty,Item, Description, Price, Extended],
       [Line, Qty,Item, Description, Price, Extended],
       [Line, Qty,Item, Description, Price, Extended],
       [Line, Qty,Item, Description, Price, Extended],
       [Line, Qty,Item, Description, Price, Extended],
       [Line, Qty,Item, Description, Price, Extended],
       [Line, Qty,Item, Description, Price, Extended],
       [Line, Qty,Item, Description, Price, Extended],
       [Line, Qty,Item, Description, Price, Extended],
       [Line, Qty,Item, Description, Price, Extended],
       [Line, Qty,Item, Description, Price, Extended],
       [Line, Qty,Item, Description, Price, Extended],
       [Line, Qty,Item, Description, Price, Extended],
       [Line, Qty,Item, Description, Price, Extended],
       [Line, Qty,Item, Description, Price, Extended]
       ]

table = Table(data, colWidths=[1.25 * cm,1.5 * cm, 3 * cm,8 * cm,
                               3* cm, 3 * cm])

table.setStyle(TableStyle([
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.grey),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.grey),
                       ]))
  
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    
    c = canvas.Canvas("B.pdf", pagesize=letter)
    header = Paragraph('This is a multi-line header.  It goes on every page.   ' * 5, styles['Normal'])
    w, h = header.wrap(doc.width, doc.topMargin)
    header.drawOn(c, doc.leftMargin, doc.height + doc.topMargin - h)
   
   
   
   
   
   
    table.wrapOn(c, width, height)
    w, h = table.wrap(0, 0) # get width and height of table
    startpoint = 8 + h/cm
    if height/cm < startpoint:
        raise Exception('too many items in list')
    print('Height:',height/cm,' startpont',startpoint)
    #print('Height',((height-(8*cm)-h)/cm)) #this weird code is to find out where in cm to start the botom of the table
    table.drawOn(c, *coord(1,startpoint, cm))
    c.save()
