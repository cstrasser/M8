from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch

# PAGE_HEIGHT=defaultPageSize[1]; PAGE_WIDTH=defaultPageSize[0]
# styles = getSampleStyleSheet()
# 
# Title = "<Document Title>"
# def myTitlePage(canvas, doc):
#     canvas.saveState() 
#     canvas.setFont('Times-Bold',48)
#     canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, Title)
#     canvas.restoreState()
# 
# pageinfo = " - <some document info here>"
# def myRegularPage(canvas, doc):
#     canvas.saveState()
#     canvas.setFont('Times-Roman',9)
#     canvas.drawString(inch, 0.75 * inch, "page %d %s" % (doc.page, pageinfo))
#     canvas.restoreState()
#     
    
    ####################################################
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Frame
styles = getSampleStyleSheet()
H6 = styles['Normal']
H1 = styles['Heading1']

def lipsum():
    return "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam ultrices ligula et libero tempus, ac pretium velit ultricies.
           Pellentesque sit amet vestibulum quam. Maecenas turpis ante, feugiat eu ultricies feugiat, ultricies ac elit. Praesent eleifend,
           nibh eu tempor consequat, nisi nunc hendrerit mi, at rhoncus massa sem quis nulla. Nunc ullamcorper mi a risus pretium, ac faucibus massa vehicula.
           Vestibulum venenatis aliquam felis eget hendrerit. Nulla porta massa placerat velit ultrices dictum. Curabitur mattis, lacus in convallis porta,
           ligula enim dignissim est, vel aliquam elit metus nec dolor. Vestibulum lacinia ac magna adipiscing iaculis. Suspendisse potenti. Nunc adipiscing magna
           id suscipit viverra. Sed tristique tortor ac erat mattis aliquam. Etiam nunc libero, iaculis non lectus quis, tincidunt adipiscing lacus. Aliquam in auctor dui."



pdfContent = []
pdfContent.append(Paragraph("This is a Heading",H1))
for i in range(100):
    pdfContent.append(Paragraph(lipsum(),H6))
    pdfContent.append(Spacer(1,0.2*inch))
c = Canvas('test5.pdf')
f = Frame(3*inch, inch, 3*inch, 9*inch, showBoundary=1)
f.addFromList(pdfContent,c)
c.save()