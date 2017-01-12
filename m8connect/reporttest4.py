#scp -i vpctesting1.pem ubuntu@10.0.0.131:~/webapps/m8connect/m8connect/example.pdf exampl.pdf
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm, inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Image, Paragraph, Table, SimpleDocTemplate, TableStyle
from reportlab.lib import colors
 
 
########################################################################
#Make the pdf object
class PDFMake(object):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, pdf_file_name):
        pdf_file_name = pdf_file_name + '.pdf'
        self.c = canvas.Canvas(pdf_file_name , pagesize=letter)
        self.styles = getSampleStyleSheet()
        self.width, self.height = letter
        self.rightMargin = inch/4
        self.leftMargin = inch/4
        self.topMargin=inch/10,
        self.bottomMargin=inch/4,
        self.pagesize=letter
        

    #header information (company logo address Quote number...-)-----------------------------------------
    def DocumentHeader(self):
        ADDRESS = '''<font size="14"><b>Quotation</b></font><br/><font size="8">11-333 California Ave<br/>
                     PO Box 372<br/>  Brockville, Ont K6V 5Y6<br/>613-704-1463 </font>'''
        #w, h = header.wrap(self.width, self.topMargin)
        spot = ((self.height - self.topMargin[0]) - 75) #fixes topmargin tuple error
        #header.drawOn(self.c, self.leftMargin, spot)
        print (self.leftMargin, spot) #for debugging
       
        # ---------create return address
        p = Paragraph(ADDRESS, self.styles["Normal"])        
 
        # add a logo and size it
        logo = Image("swlogo.jpg")
        logo.drawHeight = .75*inch
        logo.drawWidth = 2*inch       
        data = [[logo ,' ',p ]]
        table = Table(data, colWidths=[2.25*inch,4.25*inch, 1.5*inch])
        table.setStyle(TableStyle([("VALIGN", (0,0), (0,0), "TOP"),
             ('ALIGN', (1,-1), (1,-1), 'RIGHT'),
             ('ALIGN', (-1,-1), (-1,-1), 'RIGHT'),
             ('ALIGN', (-1,0), (-1,-1), 'RIGHT'),
             ('TEXTCOLOR',(0,0),(-2,-2),colors.red)
             #('BOX', (0,0), (-1,-1), 0.25, colors.grey),
             #('INNERGRID', (0,0), (-1,-1), 0.25, colors.grey)
             ]))
         
        table.wrapOn(self.c, self.width, self.height)
        table.drawOn(self.c, self.leftMargin ,spot)
 
    #----------------------------------------------------------------------
    # Helper class to help position flowables in Canvas objects
    def coord(self, x, y, unit=1):
        x, y = x * unit, self.height -  y * unit
        print(x,y)
        return x, y    

        # http://stackoverflow.com/questions/4726011/wrap-text-in-a-table-reportlab
        
    #----------------------------------------------------------------------
    def createParagraph(self, ptext, x, y, style=None):
       
        if not style:
            style = self.styles["Normal"]
        p = Paragraph(ptext, style=style)
        p.wrapOn(self.c, self.width, self.height)
        p.drawOn(self.c, *self.coord(x, y, mm))
        
     #--Quote details section
          #Quote Title
          #Quote Description
     
     #---Equipment/Materials section ---
         #Table ...
     #---Installation Section
        #or put it into equipent section 
     #---Option Section
     
     #-- Notes Section
            
     #document footer ---paginator goes here Footer is :  page x of y  REF:{quotenumber} rightjustify
 
    #----------------------------------------------------------------------
    def savePDF(self):
        """"""
        self.c.save()   
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    doc = PDFMake("ey")
    doc.DocumentHeader()
    doc.savePDF()