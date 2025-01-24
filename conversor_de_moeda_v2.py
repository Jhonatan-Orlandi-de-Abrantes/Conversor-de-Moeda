import customtkinter as ctk
from requests import *



######################################################

# Moedas:
usd = 'Dólar Americano (USD)'
brl = 'Real brasileiro (BRL)'
eur = 'Euro (EUR)'
btc = 'Bitcoin (BTC)'

moedas_disponiveis = [
usd,
brl,
eur,
btc
]

# Validação do resultado
conversão = int()

###############################################################################################################################################

# Funções

def converter():
    global moeda_base
    global moeda_alvo
    global valor
    global resultado
    global conversão
    
    if moeda_base == usd and moeda_alvo == usd:
        ()
    
    if moeda_base == usd and moeda_alvo == brl:
        ()
    
    if moeda_base == usd and moeda_alvo == eur:
        ()
    
    if moeda_base == usd and moeda_alvo == btc:
        ()
    
    resultado.configure(text=conversão)

############# Tinker ############

# Janela
win = ctk.CTk()
ctk.set_appearance_mode('system')
ctk.set_default_color_theme('blue')
win.geometry('330x580')
win.title('Conversor de Moedas')

###################################

titulo = ctk.CTkLabel(win, text='Conversor de Moedas', font=('',20)).pack(padx=10, pady=10)

text1 = ctk.CTkLabel(win, text='Moeda de Origem:').pack(padx=10)
moeda_base = ctk.CTkOptionMenu(win, values=moedas_disponiveis).pack(padx=10,pady=15)

text2 = ctk.CTkLabel(win, text='Moeda de Destino:').pack(padx=10)
moeda_alvo = ctk.CTkOptionMenu(win, values=moedas_disponiveis).pack(padx=10,pady=15)

text3 = ctk.CTkLabel(win, text='Valor:').pack(padx=10)
valor = ctk.CTkEntry(win).pack(padx=10,pady=15)

botão_executar = ctk.CTkButton(win, text='Converter', command=converter).pack(padx=10,pady=15)

text4 = ctk.CTkLabel(win, text='Resultado:').pack(padx=20)
resultado = ctk.CTkLabel(win, text='', font=('',16))
resultado.pack(padx=10, pady=10)

lista_moedas = ctk.CTkScrollableFrame(win)

for moeda in moedas_disponiveis:
    texto_moeda = ctk.CTkLabel(lista_moedas, text=moeda)
    texto_moeda.pack()

lista_moedas.pack(padx=10,pady=10)

########### Janela aberta ############

win.mainloop()