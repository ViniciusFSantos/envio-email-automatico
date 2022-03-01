import smtplib
import PySimpleGUI as sg

#conecta no servidor do provedor de e-mail
nome_servidor = 'smtp.gmail.com'
porta_servidor = 465

conexao = smtplib.SMTP_SSL(nome_servidor, porta_servidor)
print('Conexão estabelecida..')

#loga no servidor com e-mail e senha
email = sg.popup_get_text('Digite seu E-mail abaixo', 'E-mail')
if email == None:
    pass
else:    
    senha = sg.popup_get_text('Digite sua senha', 'Senha')
    conexao.login(email, senha)
sg.popup('Aviso','Login feito com sucesso!\n','Enviando sua mensagem...')

#escolher e-mails e mensagem a ser enviada
remetente = 'meuemail@yahoo.com.br'
destinatario = 'cliente@gmail.com'
mensagem = 'Esta é uma mensagem automática'

conexao.sendmail(remetente, destinatario, mensagem.encode('utf-8'))
print('E-mail enviado com sucesso! ')
conexao.quit()

#pysimplegui
'''sg.theme('TanBlue') #tema e cor usados 

layout = [
    [sg.popup_get_text('Digite o seu E-mail', 'E-mail')]

]

#cria a janela
window = sg.window('Envio automático de E-mails', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break
window.close()'''