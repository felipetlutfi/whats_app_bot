import tkinter as tk
import json

def gerar_json():
    ticker = entry_ticker.get()
    preco_alvo = entry_preco_alvo.get()
    tipo_operacao = var_tipo_operacao.get()

    dados = {
        "ticker": ticker,
        "preco_alvo": preco_alvo,
        "tipo_operacao": tipo_operacao
    }

    with open('dados.json', 'w') as arquivo_json:
        json.dump(dados, arquivo_json)

    print("JSON gerado com sucesso!")

# Criar a janela principal
janela = tk.Tk()
janela.title("Formulário de Ações")

# Criar os campos e rótulos
label_ticker = tk.Label(janela, text="Ticker:")
label_ticker.grid(row=0, column=0, padx=10, pady=10)
entry_ticker = tk.Entry(janela)
entry_ticker.grid(row=0, column=1, padx=10, pady=10)

label_preco_alvo = tk.Label(janela, text="Preço Alvo:")
label_preco_alvo.grid(row=1, column=0, padx=10, pady=10)
entry_preco_alvo = tk.Entry(janela)
entry_preco_alvo.grid(row=1, column=1, padx=10, pady=10)

label_tipo_operacao = tk.Label(janela, text="Tipo de Operação:")
label_tipo_operacao.grid(row=2, column=0, padx=10, pady=10)
var_tipo_operacao = tk.StringVar(value="Compra")
radiobutton_compra = tk.Radiobutton(janela, text="Compra", variable=var_tipo_operacao, value="Compra")
radiobutton_compra.grid(row=2, column=1, padx=10, pady=10)
radiobutton_venda = tk.Radiobutton(janela, text="Venda", variable=var_tipo_operacao, value="Venda")
radiobutton_venda.grid(row=2, column=2, padx=10, pady=10)

# Criar o botão para gerar o JSON
botao_gerar_json = tk.Button(janela, text="Gerar JSON", command=gerar_json)
botao_gerar_json.grid(row=3, column=0, columnspan=3, pady=10)

# Iniciar o loop da aplicação
janela.mainloop()
