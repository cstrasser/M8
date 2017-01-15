from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Frame, Spacer,Image
from reportlab.lib import colors
from reportlab.lib.units import cm, inch
from reportlab.lib.pagesizes import A3, A4, landscape, portrait, letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader


PAGE_HEIGHT=defaultPageSize[1]; PAGE_WIDTH=defaultPageSize[0]
styles = getSampleStyleSheet()
normalStyle = styles['Normal']

ADDRESS = '''<font size="6">11-333 California Ave [PO Box 372]<br/>
          Brockville, Ont K6V 5Y6<br/>613-704-1463</font>'''


def firstPage(canvas, doc):
    print (PAGE_HEIGHT-4*cm)
    canvas.saveState()
    canvas.drawImage("swlogo.jpg", 20, PAGE_HEIGHT-5*cm, width=2*inch,height=.75*inch,
                     preserveAspectRatio=False, mask='auto')
    canvas.setFontSize(size=16)
    canvas.drawRightString(PAGE_WIDTH-1*cm,PAGE_HEIGHT-3.8*cm, 'Quotation')
    canvas.setFont('Courier',8)
    canvas.drawRightString(PAGE_WIDTH-1*cm,PAGE_HEIGHT-4.3*cm, '11-333 California Ave')
    canvas.drawRightString(PAGE_WIDTH-1*cm,PAGE_HEIGHT-4.6*cm, 'PO Box 372')
    canvas.drawRightString(PAGE_WIDTH-1*cm,PAGE_HEIGHT-4.9*cm, 'Brockville Ont')
    canvas.drawRightString(PAGE_WIDTH-1*cm,PAGE_HEIGHT-5.2*cm, 'K6V 5Y6')
    canvas.setFont('Courier-Bold',8)
    canvas.drawString(1*cm,PAGE_HEIGHT-5.5*cm, 'Quote#: SYQA17A')
    canvas.setFontSize(size=8)
    canvas.drawString(1*cm,PAGE_HEIGHT-6.2*cm, 'DATE: JAN 12 2017')
    canvas.drawString(1*cm,PAGE_HEIGHT-6.6*cm, 'Valid until: JAN 12 2017')
    canvas.drawString(1*cm,PAGE_HEIGHT-7*cm, 'Title: INstallation of dog fence')
    canvas.drawString(1*cm,PAGE_HEIGHT-7.4*cm, 'Quoted By: Chris Strasser cstrasser@secureway.ca 613-704-1463 x1101')
    canvas.drawString(1*cm,PAGE_HEIGHT-7.8*cm, 'Quoted For: Brad Bradley brad@gmail.com 613-123-3343')
    canvas.drawString(1*cm,PAGE_HEIGHT-8.2*cm, 'Description:  Lorem Ipsum....')
    canvas.line( .75*cm,PAGE_HEIGHT-8.5*cm, PAGE_WIDTH,PAGE_HEIGHT-8.5 * cm)
    canvas.setFontSize(size=9)
    canvas.drawString(inch, 0.75 * inch, "First Page / %s" % 'pageinfo')
    canvas.restoreState()
  
def LaterPages(canvas, doc):
    canvas.saveState()
    canvas.drawImage("swlogo.jpg", 20, PAGE_HEIGHT-4*cm, width=2/2*inch,height=.75/2*inch,
                     preserveAspectRatio=False, mask='auto')
    canvas.setFontSize(size=16)
    canvas.drawRightString(PAGE_WIDTH-1*cm,PAGE_HEIGHT-3.8*cm, 'Quotation')
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch, "Page %d %s" % (doc.page, 'pageinfo2'))
    canvas.restoreState()
    

def go():
    doc = SimpleDocTemplate("phello.pdf",
                                rightMargin=inch/4,
                                leftMargin=inch/4,
                                topMargin=inch/2,
                                bottomMargin=inch,
                                pagesize=letter)
    Story = []
    Story.append(Spacer(1,.75*inch))
    Story.append(Spacer(1,1.75*inch))
    for i in range(100):
        bogustext = ("<li>This is Paragraph number %s. " % i) *20
        p = Paragraph(bogustext,normalStyle)
        Story.append(p)
        Story.append(Spacer(1,0.2*inch))
    doc.build(Story, onFirstPage=firstPage, onLaterPages=LaterPages)

        
if __name__ == '__main__':
   go()
    