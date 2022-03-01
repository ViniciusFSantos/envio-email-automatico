from turtle import left
from typing import Sized, Text
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import ELEM_TYPE_IMAGE, Element, Image, Yes

icon = 'Iconemail.ico' #carrega icone das janelas
sg.theme('DarkGrey1')   # Tema
sg.set_options(font=('OpenSans',12), icon=(icon)) #fonte, tamanho fonte, icone
configs = sg.UserSettings(autosave=True) #salva configurações de usuário nesse caso senha, servidor e porta

#=========================================WINDOWS========================================================
def janela_login(): #janela1 Login
    layout = [  
            [sg.Text('E-mail')],
            [sg.Input(configs.get('email'), key='Seu E-mail', size=[30])], 
            [sg.Text('Senha')],
            [sg.Input(configs.get('senha', ''), key='Sua senha', password_char='*', size=[30])],
            [sg.Checkbox('Lembrar E-mail e Senha', key='salvar')],
            [sg.Text('Dados do seu provedor de E-mail: Servidor e Porta')],
            [sg.Input(configs.get('servidor', ''), key='Servidor', size=[19])],
            [sg.Input(configs.get('porta', ''), key='Porta', size=[5])],
            [sg.Checkbox('Lembrar Servidor e Porta',key='salvar-smtp')],
            [sg.Button('Login')],
    ]
    return sg.Window('Login', layout=layout, element_justification = "left" , enable_close_attempted_event=True, resizable=False, finalize=True).finalize()

def janela_Mensagem(): #Janela2 mensagem     
    layout = [
        [sg.Text('Informe o(s) destinatário(s) separados por espaço')],     
        [sg.Multiline('',key='Destinatario', size=(49,4), font=('OpenSans',10))],
        [sg.Text('Escreva sua mensagem')],
        [sg.Multiline('',key='Mensagem', size=(38,11))],
        [sg.Button('Anexar arquivo')],
        [sg.HorizontalSeparator(color='white', pad=((0,0),(4,15)))],
        [sg.Text('Informe abaixo o intervalo de disparo', pad=((50,0),(0,0)))],
        [sg.Spin([i for i in range(1,25)], initial_value=1, pad=((100,0),(5,0))), sg.Text('Intervalo em Horas')],
        [sg.Button('Iniciar', pad=((120,0),(10,0))),sg.Button('Parar', pad=((8,0),(10,0)))]
    ]
    return sg.Window('Enviar Mensagem', layout=layout, enable_close_attempted_event=True, resizable=False, finalize=True).finalize()

def janela_loop(): #Janela3 loop     
    layout = [
        [sg.Text('Deseja Continuar o envio?')],     
        [sg.Button('Sim'), sg.Button('Não')]
    ]
    return sg.Window('Caso queira para aperte o botao', layout=layout, enable_close_attempted_event=True, resizable=False, finalize=True).finalize()

#====================================================END WINDOWS==============================================

#========================================POP-UPS==============================================================
def popup_login_feito(): #popup                                                                             
    layout = [                                                                                              
        [sg.popup_ok('Login efetuado com sucesso!', title='Sucesso! :)',)]                                  
                                                                                                             
    ]                                                                                               
    
def popup_iniciar_feito(): #popup 
    layout = [
        [sg.popup_ok('Disparo de E-mails feito!', title='Sucesso! :)',)]
        
    ]

def popup_anexar(): #popup
    layout = [
        [sg.popup_get_file('Informe o caminho do arquivo ou clique em pesquisar')],
    ]

def erro_login(): #popup
    layout = [
        [sg.popup_ok('Não foi possível efetuar o login. Tente novamente!', title='Ops! :(')],
              
    ]
    return sg.Window('Erro!')

def erro_msg(): #popup
    layout = [
        [sg.popup_ok('Falha ao iniciar. Tente novamente!', title='Ops! :(')],
              
    ]
    return sg.Window('Erro!')

def popup_get_file():
    layout = [
      [sg.popup_get_file('Escolha ou informe o local do arquivo', title='Anexar arquivo')]
      
    ]
#===========================================END POP-UPS======================================================
