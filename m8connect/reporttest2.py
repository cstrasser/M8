#scp -i vpctesting1.pem ubuntu@10.0.0.131:~/webapps/m8connect/m8connect/example.pdf exampl.pdf
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm, inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Image, Paragraph, Table
 
 
########################################################################
class MakePdf(object):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, pdf_file, org, seconds):
        self.c = canvas.Canvas(pdf_file, pagesize=letter)
        self.styles = getSampleStyleSheet()
        self.width, self.height = letter
        self.organization = org
        self.seconds  = seconds
 
 
    #----------------------------------------------------------------------
    def createDocument(self):
        """"""
        voffset = 25  
 
        # create return address
        address = """Secureway<br/> 11-333 California Ave<br/>
        PO Box 372<br/>Brockville,Ont K6V 5Y6<br/> """
        
        p = Paragraph(address, self.styles["Normal"])        
 
        # add a logo and size it
        logo = Image("swlogo.jpg")
        logo.drawHeight = 1*inch
        logo.drawWidth = 3*inch
##        logo.wrapOn(self.c, self.width, self.height)
##        logo.drawOn(self.c, *self.coord(140, 60, mm  ))
##        
        data = [[p,logo]]
        table = Table(data, colWidths=3*inch)
        table.setStyle([("VALIGN", (0,0), (0,0), "TOP")])
        table.wrapOn(self.c, self.width, self.height)
        table.drawOn(self.c, *self.coord(18, 60, mm))
 
        # insert body of letter
        ptext = "Dear Sir or Madam:"
        self.createParagraph(ptext, 20, voffset+45)
 
        ptext = """
        The document you are holding is a set of requirements for your next mission, should you
        choose to accept it. In any event, this document will self-destruct <b>%s</b> seconds after you
        read it. Yes, <b>%s</b> can tell when you're done...usually.
        """ % (self.seconds, self.organization)
        p = Paragraph(ptext, self.styles["Normal"])
        p.wrapOn(self.c, self.width-120, self.height)
        p.drawOn(self.c, *self.coord(20, voffset+85, mm))
 
    #----------------------------------------------------------------------
    def coord(self, x, y, unit=1):
        """
        # http://stackoverflow.com/questions/4726011/wrap-text-in-a-table-reportlab
        Helper class to help position flowables in Canvas objects
        """
        x, y = x * unit, self.height -  y * unit
        return x, y    
 
    #----------------------------------------------------------------------
    def createParagraph(self, ptext, x, y, style=None):
        """"""
        if not style:
            style = self.styles["Normal"]
        p = Paragraph(ptext, style=style)
        p.wrapOn(self.c, self.width, self.height)
        p.drawOn(self.c, *self.coord(x, y, mm))
 
    #----------------------------------------------------------------------
    def savePDF(self):
        """"""
        self.c.save()   
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    doc = MakePdf("example.pdf", "The MVP", 10)
    doc.createDocument()
    doc.savePDF()