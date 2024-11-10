import smtplib
import ssl
import email.message

setor = 'B'
nome = 'Equipe do financeiro'

msg = email.message.Message()
msg['Subject'] = f"Planilha Financeiro departamento: {setor}"

body = f"""
Ola , {nome}
Segue o anexo a planilha com os resultados desse mês
Atenciosamente ,
Gerente ADM
"""
msg['From'] = 'ryan06outlier@gmail.com'
senha = 'Rocket06'
msg['To'] = 'ryanbussines06@gmail.com'
msg.add_header('Content-Type', 'text/html')
msg.set_payload(body)

context = ssl.create_default_context()
with smtplib.SMTP('smtp.gamil.com', 587) as conexao :
    conexao.ehlo()
    conexao.starttls(context=context)
    conexao.login(msg['From'] , senha)
    conexao.sendmail(msg['From'] , msg['To'] , msg.as_string().encode('utf-8'))
    