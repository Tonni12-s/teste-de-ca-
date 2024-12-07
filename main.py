import PySimpleGUI as ys

# - - - Layout - - -
#Escolher o tema
ys.theme('Black')

#Colunas e linhas
colunasLinhas = [[ys.Text("CADASTRO", size=(30,1),font=100, justification="c")],
                 [ys.Text(" ")],
                 [ys.Text("Login: "), ys.Input(key='login', size=(30,1))],
                 [ys.Text("Senha: "), ys.Input(key='senha', size=(30,1),password_char="*")],
                 [ys.Checkbox("Salvar senha")],
                 [],
                 [ys.Button("Entrar"), ys.Button("Sair")]]

# - - - Usar Layout
janela = ys.Window('Tela Login', colunasLinhas)

# - - - Ações
while True:
    evento, valores = janela.read()
    if evento == "Sair" or evento == ys.WIN_CLOSED:
        break
    if evento == "Entrar":
        if valores["Login"] == 'Camilol' and valores['senha'] == "123":
            print("você entrou camilol!")




