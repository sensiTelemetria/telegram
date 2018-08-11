import time
from reportlab.lib.enums import TA_JUSTIFY,TA_CENTER
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm

doc = SimpleDocTemplate("arquivo.pdf", pagesize=A4,
                        rightMargin=72, leftMargin=72,
                        topMargin=72, bottomMargin=18)
Story = []

# SENSI
logo = "logo.png"
textoSensi = "Sensi telemetria"
siteSensi = "www.sensitelemtria.com.br"
nomeRelatorio = "relat 1"
qtdSensiTags = str(10)


magName = "Pythonista"
issueNum = 12
subPrice = "99.00"
limitedDate = "03/05/2010"
freeGift = "tin foil hat"

formatted_time = time.ctime()
full_name = "Mike Driscoll"
address_parts = ["411 State St.", "Marshalltown, IA 50158"]

#LOGO
im = Image(logo, 8 * cm, 7 * cm )
Story.append(im)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
styles.add(ParagraphStyle(name='center', alignment=TA_CENTER))
ptext = '<font size=14>%s</font>' % formatted_time
Story.append(Paragraph(ptext, styles["center"]))
Story.append(Spacer(1, 12))

# SENSI
ptext = '<font size=14>%s</font>' % textoSensi
Story.append(Paragraph(ptext, styles["center"]))
Story.append(Spacer(1, 12))

# SENSI site
ptext = '<font size=14>%s</font>' % siteSensi
Story.append(Paragraph(ptext, styles["center"]))
Story.append(Spacer(1, 36))

# DADOS RELATORIOS

styles.add(ParagraphStyle(name='tab', leftIndent = 1 *cm ,alignment=TA_JUSTIFY))
ptext = '<font size=14>Dados relatório</font>'
Story.append(Paragraph(ptext, styles["tab"]))
Story.append(Spacer(1, 12))

ptext = '<font size=14>Relatório: %s</font>' % nomeRelatorio
Story.append(Paragraph(ptext, styles["Justify"]))
Story.append(Spacer(1, 12))

ptext = '<font size=14>Qtd de SensiTags: %s</font>' % qtdSensiTags
Story.append(Paragraph(ptext, styles["Justify"]))
Story.append(Spacer(1, 12))


#fazer para cada gráfico
Story.append(PageBreak())
im = Image("foo.png", 20 * cm, 15 * cm )
Story.append(im)

ptext = '<font size=14>SensiTag MAC: 12345789</font>'
Story.append(Paragraph(ptext, styles["Justify"]))
Story.append(Spacer(1, 12))

ptext = '<font size=14>SensiTag localização: freezer 1</font>'
Story.append(Paragraph(ptext, styles["Justify"]))
Story.append(Spacer(1, 12))

ptext = '<font size=14>Valor médio: -20.00 </font>'
Story.append(Paragraph(ptext, styles["Justify"]))
Story.append(Spacer(1, 12))

ptext = '<font size=14>Valor máximo: -10.00 </font>'
Story.append(Paragraph(ptext, styles["Justify"]))
Story.append(Spacer(1, 12))

ptext = '<font size=14>Valor mínimo: -30.00 </font>'
Story.append(Paragraph(ptext, styles["Justify"]))
Story.append(Spacer(1, 12))

doc.build(Story)