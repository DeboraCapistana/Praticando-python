import tkinter as tk
from tkinter import simpledialog, messagebox
import calendar
import datetime

# Dicionário para armazenar os compromissos
agenda = {}

# Função para lidar com o clique em um dia
def abrir_agenda(dia):
    data = f"{mes_atual}/{dia}/{ano_atual}"
    compromisso = agenda.get(data, "")

    novo = simpledialog.askstring("Agenda", f"Compromissos para {data}:", initialvalue=compromisso)
    if novo is not None:
        agenda[data] = novo
        messagebox.showinfo("Salvo", f"Compromissos salvos para {data}.")

# Criar janela principal
janela = tk.Tk()
janela.title("Calendário com Agenda")

# Obter mês e ano atual
hoje = datetime.date.today()
mes_atual = hoje.month
ano_atual = hoje.year

# Gerar calendário
cal = calendar.monthcalendar(ano_atual, mes_atual)

# Títulos dos dias da semana
dias_semana = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]
for i, dia in enumerate(dias_semana):
    tk.Label(janela, text=dia, font=("Arial", 10, "bold")).grid(row=0, column=i)

# Mostrar os dias
for i, semana in enumerate(cal):
    for j, dia in enumerate(semana):
        if dia != 0:
            btn = tk.Button(janela, text=str(dia), width=5, command=lambda d=dia: abrir_agenda(d))
            btn.grid(row=i+1, column=j)

janela.mainloop()
