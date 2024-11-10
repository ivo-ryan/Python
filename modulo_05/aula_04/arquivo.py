import pydf

pdf = pydf.generate_pdf('<h2>Ola mundo</h2>')

with open('test_doc.pdf', 'wb') as arquivo :
    arquivo.write(pdf)