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
pyautogui.click(x=853, y=400)
pyautogui.write("emaildeteste@gmail.com")
pyautogui.press("tab")
pyautogui.write("password")
pyautogui.press("enter")
time.sleep(5)

#Passo 3: Importar a base de dados

import pandas

tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:

#Passo 4: Cadastrar um produto

    pyautogui.click(x=824, y=303)

    #codigo
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")

    #marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    #tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    #preço_unitario
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    #custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    #OBS
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    #enviar formulário
    pyautogui.press("enter")
    pyautogui.press("home")

#Passo 5: Repetir isso até acabar a base de dados

