from layouts import janela_Mensagem, janela_loop, popup_anexar, erro_msg, popup_iniciar_feito, popup_get_file
import time, login, PySimpleGUI as sg, smtplib
import schedule

#inicia janela de login
login.start_login()

def enviar():
    try:
        remetente = login.info_login[0]
        destinatario = info_mensagem[0]
        dest_list = destinatario.split(' ')
        mensagem = info_mensagem[1]
        enviar = login.conexao.sendmail(remetente, dest_list, mensagem.encode('utf-8'))
        #popup_iniciar_feito()
    except:
        erro_msg()


#inicia janela de mensagem
jenela2 = janela_Mensagem()
while True: #manter janela de mensagem aberta 
    window, event, values = sg.read_all_windows() #lê todas as ações feitas na janela
    info_mensagem = []  #armazena em lista os valores coletados     
    
    for valores  in values.values():  #coleta todas as ações feitas na janela 
        info_mensagem.append(valores)
    
    if event == 'Iniciar': #!!! TODO AJUSTAR LÓGICA PARA FUNCIONAR TIME DE ENVIO 
        hora = 20 #info_mensagem[2]
        janela3 = janela_loop()
        schedule.every(hora).seconds.do(enviar)
        while hora > 0:
            window, event, values = sg.read_all_windows() #lê todas as ações feitas na janela
            schedule.run_pending()
            time.sleep(1)
            janela3.un_hide()      
            if event =='Não':
                janela3.hide() 
                break
            elif event == sg.WIN_CLOSED: #quebra loop fechando a janela
                janela3.hide()
                break
            else:
                janela3.hide()
                continue
    elif event == 'Anexar arquivo':
        popup_get_file()
    elif event == sg.WIN_CLOSED: #quebra loop fechando a janela
        break
