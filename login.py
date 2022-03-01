from layouts import janela_login, popup_login_feito, erro_login
import PySimpleGUI as sg
import smtplib
import sys  

configs = sg.UserSettings(autosave=True) #salva configurações de usuário nesse caso senha, servidor e porta

###########################
#   variáveis globais     #
info_login = []           #
conexao = 0               #      
###########################

def start_login():
    janela1 = janela_login() #chama a janela
    while True:  #manter janela aberta
        window, event, values = sg.read_all_windows()   #lê todas as ações feitas na janela
        global info_login   
        info_login = []    #armazena em lista os valores coletados 
        for valores in values.values():    #inclui na lista info_login todas as interações coletadas
            info_login.append(valores)
            
        def salvar_senha():
            if values['salvar'] == True:
                configs['senha'] = info_login[1]
                configs['email'] = info_login[0]        
                
        def salvar_smtp():
            if values['salvar-smtp'] == True:
                configs['servidor'] = info_login[3]
                configs['porta'] = info_login[4]
            
        salvar_senha()
        salvar_smtp() 
            
        if event == 'Login':   
            try:    
                #faz a comunicação com o provedor de email
                nome_servidor = info_login[3]
                porta_servidor = info_login[4]
                global conexao
                conexao = smtplib.SMTP_SSL(nome_servidor, porta_servidor)
                email = info_login[0]
                senha = info_login[1]
                conexao.login(email, senha)
                popup_login_feito()
                janela1.hide()
                break
            except:
                erro_login()
        
        elif event == sg.WIN_CLOSED: #quebra loop fechando a janela
            sys.exit()
            
            