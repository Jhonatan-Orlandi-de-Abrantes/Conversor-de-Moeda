import customtkinter as ctk
import requests

# Moedas suportadas
moedas = {
    'Dólar Americano (USD)': 'USD',
    'Real Brasileiro (BRL)': 'BRL',
    'Euro (EUR)': 'EUR'
}

# Função de conversão
def converter():
    moeda_base_val = moedas[moeda_base.get()]
    moeda_alvo_val = moedas[moeda_alvo.get()]
    valor_digitado = valor.get().strip().replace(',', '.')

    try:
        valor_digitado = float(valor_digitado)
    except:
        resultado.configure(text='Digite um número válido!', text_color='red')
        return

    # API
    url = f'https://economia.awesomeapi.com.br/json/last/{moeda_base_val}-{moeda_alvo_val}' # Site que inseriremos e receberemos a conversão
    response = requests.get(url).json()

    try:
        par = f'{moeda_base_val}{moeda_alvo_val}'
        taxa = float(response[par]['bid'])
        conversao = valor_digitado * taxa
        resultado_text = f'{conversao:,.2f} {moeda_alvo_val}'.replace('.', ',')
        resultado.configure(text=resultado_text, text_color='yellow')
    except:
        resultado.configure(text='Erro na conversão!', text_color='red')

############# Tkinter ############

win = ctk.CTk()
ctk.set_appearance_mode('system')
ctk.set_default_color_theme('blue')
win.geometry('330x580')
win.resizable(False, False)
win.title('Conversor de Moedas')

titulo = ctk.CTkLabel(win, text='Conversor de Moedas', font=('',20)).pack(padx=10, pady=10)

text1 = ctk.CTkLabel(win, text='Moeda de Origem:').pack(padx=10)

moeda_base = ctk.CTkOptionMenu(win, values=list(moedas.keys()))
moeda_base.pack(padx=10,pady=15)

text2 = ctk.CTkLabel(win, text='Moeda de Destino:').pack(padx=10)

moeda_alvo = ctk.CTkOptionMenu(win, values=list(moedas.keys()))
moeda_alvo.pack(padx=10,pady=15)

text3 = ctk.CTkLabel(win, text='Valor:').pack(padx=10)

valor = ctk.CTkEntry(win)
valor.pack(padx=10,pady=15)

botao_executar = ctk.CTkButton(win, text='Converter', command=converter)
botao_executar.pack(padx=10,pady=15)

text4 = ctk.CTkLabel(win, text='Resultado:').pack(padx=20)

resultado = ctk.CTkLabel(win, text='', font=('',16), text_color='yellow')
resultado.pack(padx=10, pady=10)

lista_moedas = ctk.CTkScrollableFrame(win)

for moeda in moedas.keys():
    texto_moeda = ctk.CTkLabel(lista_moedas, text=moeda)
    texto_moeda.pack()

lista_moedas.pack(padx=10,pady=10)

########### Janela aberta ############
win.mainloop()