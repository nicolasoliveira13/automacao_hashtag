#Passo a passo  do projeto
import pyautogui
import time

#Passo 1: Entrar no sistema da empresa

pyautogui.PAUSE = 1

pyautogui.press("win")

pyautogui.press("enter")

pyautogui.write("opera")

pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

pyautogui.press("enter")

time.sleep(5)

#Passo 2: Fazer login

pyautogui.click(x=2683, y=405)

pyautogui.write("teste")

pyautogui.press("tab")

pyautogui.write("senha")

#Passo 3: Importar a base de dados

#Passo 4: Cadastrar um produto

#Passo 5: Repetir isso até acabar a base de dados

