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
    canvas.drawRightString(PAGE_WIDTH-1*cm,PAGE_HEIGHT-4*cm, 'Quotation')
    canvas.setFont('Courier',9)
    canvas.drawString(inch, 0.75 * inch, "First Page / %s" % 'pageinfo')
    canvas.restoreState()
    #def line(self, x1,y1, x2,y2):
    #draw a line segment from (x1,y1) to (x2,y2) (with color, thickness and
    #other attributes determined by the current graphics state).

def LaterPages(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch, "Page %d %s" % (doc.page, 'pageinfo2'))
    canvas.restoreState()
    
def headerDetails():
    address = Paragraph(ADDRESS,normalStyle)
    return address

def go():
    doc = SimpleDocTemplate("phello.pdf",
                                rightMargin=inch/4,
                                leftMargin=inch/4,
                                topMargin=inch/2,
                                bottomMargin=inch/4,
                                pagesize=letter)
    Story = []
    Story.append(Spacer(1,.75*inch))
    Story.append(headerDetails())
    Story.append(Spacer(1,.25*inch))
    for i in range(100):
        bogustext = ("<li>This is Paragraph number %s. " % i) *20
        p = Paragraph(bogustext,normalStyle)
        Story.append(p)
        Story.append(Spacer(1,0.2*inch))
    doc.build(Story, onFirstPage=firstPage, onLaterPages=LaterPages)

        
if __name__ == '__main__':
   go()
    
