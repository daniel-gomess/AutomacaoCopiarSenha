
# Importando as bibliotecas necessárias
import pyautogui
from time import sleep
import pyperclip

# Pedindo ao usuário para digitar o e-mail
email = pyautogui.prompt('Informe seu e-mail: ', title='login')

# Pedindo ao usuário para digitar a senha
senha = pyautogui.password(text='Informe sua senha: ', title='Senha', mask='*')

sleep(1)

# Criando função para copiar o e-mail
def copiar_email(email):
    pyperclip.copy(email)
    pyautogui.hotkey('ctrl', 'v')

# Criando função para copiar a senha
def copiar_senha(senha):
    pyperclip.copy(senha)
    pyautogui.hotkey('ctrl', 'v')

# Abrindo a tarefa de Windows + R através do atalho do teclado
pyautogui.hotkey('Win', 'r')
sleep(1)

# Digitando o nome do programa que queremos abrir (Notepad)
pyautogui.write('notepad')
sleep(1)
pyautogui.press('enter')
sleep(2)

# Abrindo uma nova aba no bloco de notas
pyautogui.hotkey('ctrl', 'n')
sleep(1)

copiar_email(email)
sleep(1.5)
pyautogui.press('enter')
sleep(1)
copiar_senha(senha)

pyautogui.alert(text='Automação finalizada!', title='Mensagem!', button='OK'