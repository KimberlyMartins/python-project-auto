#                     PYAUTOGUI
# O PyAutoGUI é uma biblioteca da linguagem Python que automatiza tarefas no computador. Ela funciona como um "robô", assumindo o controle do mouse e do teclado para clicar, mover, rolar e digitar, permitindo que você execute processos repetitivos exatamente como um humano faria.

#                       TIME 
#  A biblioteca time do Python é um módulo nativo usado para lidar com o tempo, medir a performance do código e pausar a execução do programa. O padrão é segundos.

#                      PANDAS
# O Pandas é a principal biblioteca para análise de dados e utiliza o openpyxl como motor padrão nos bastidores para ler e escrever arquivos .xlsx no Python. Enquanto o Pandas foca na manipulação de grandes volumes de dados, o openpyxl é focado na formatação e estrutura do Excel.

# No python usamos aspas sejam simples ou duplas para digitar palavras

#                   PASSO  A PASSO 
# 1- ENTRAR NO SISTEMA DA EMPRESA 
# automatizar a entrada no windows para abrir o navegador
# import pyautogui #Importamos a biblioteca pyautogui
# import time  # importamos tempo que já é padrão e não precisa baixar

# pyautogui.PAUSE = 1  #Seleciona o tempo de pausa para realizar as tarefas
# link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" # Criamos a variável link

# pyautogui.press("win") # Clica automaticamente na tecla windows
# pyautogui.write("chrome") # Na aba windows digita chrome
# pyautogui.press("enter") # Dá o enter no navegador chrome

# pyautogui.write(link) # Escrevemos de forma automatica a variável criada no link
# pyautogui.press("enter") # Pressionamos para a busca do link no navegador
# time.sleep(2)  # Chamamos o time.sleep para fazer uma pausa maior evitando sobrecarga no site

# 2- LOGIN 
# pyautogui.click(x=595, y=417) #Acha a posição no arquivo auxiliar e seleciona onde é para clicar
# pyautogui.write("pythonimpressionador@gmail.com") # Digita no campo selecionado

# pyautogui.press("tab")  # Tab para pular para  a próxima seleção
# pyautogui.write("essasenhaéinfinita") # Digita no campo selecionado
# pyautogui.press("tab")  # Tab para pular para  a próxima seleção
# pyautogui.press("enter") # Enter para click no botão de login
#time.sleep(3)  # Chamamos o time.sleep para fazer uma pausa maior evitando sobrecarga no site

# 3- ABRIR  A BASE DE DADOS


# 4- Cadastrar um produto


# 5- Repetir passo 4 até o fim da lista de produtos

# pip install pyautogui 

# pyautogui.click   = Clica
# pyautogui.write   = Escreve um texto
# pyautogui.press   = Aperta uma tecla
# pyautogui.hotkey  = Aperta um atalho (Hotkey)

import pyautogui #Importamos a biblioteca pyautogui
import time

pyautogui.PAUSE = 1  #Seleciona o tempo de pausa para realizar as tarefas
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" # Criamos a variável link

pyautogui.press("win") # Clica automaticamente na tecla windows
pyautogui.write("chrome") # Na aba windows digita chrome
pyautogui.press("enter") # Dá o enter no navegador chrome

pyautogui.write(link) # Escrevemos de forma automatica a variável criada no link
pyautogui.press("enter") # Pressionamos para a busca do link no navegador
time.sleep(3)  # Chamamos o time.sleep para fazer uma pausa maior evitando sobrecarga no site

pyautogui.click(x=595, y=417) #Acha a posição no arquivo auxiliar e seleciona onde é para clicar
pyautogui.write("pythonimpressionador@gmail.com") # Digita no campo selecionado

pyautogui.press("tab")  # Tab para pular para  a próxima seleção
pyautogui.write("essasenhaéinfinita") # Digita no campo selecionado
pyautogui.press("tab")  # Tab para pular para  a próxima seleção
pyautogui.press("enter") # Enter para click no botão de login

time.sleep(3)  # Chamamos o time.sleep para fazer uma pausa maior evitando sobrecarga no site

#  pip install pandas openpyxl  # Instalamos a bibioteca pandas
import pandas

table = pandas.read_csv("produtos.csv")