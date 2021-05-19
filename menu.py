from graphics import *
import time

# Variáveis globais
resolucao = 500
fundo = color_rgb(33, 33, 33)
botoes = color_rgb(255, 248, 171)
dificuldade = 2

# Cria o Menu Principal
menu = GraphWin('Menu do Jogo', resolucao, resolucao)
menu.setBackground(fundo)

# Função de animação (futura)
def animacao(self, x, y):
    self.undraw()
    self.move(x, y)
    self.draw(menu)
    time.sleep(1)
    self.undraw()
    self.move(-x, -y)
    self.draw(menu)
    time.sleep(1)

# Animação de seleção
def resetar_outline(listaop, s):
    global fundo
    for element in listaop:
        if listaop.index(element) == s - 1:
            element.setOutline('white')
        else:
            element.setOutline(fundo)

# Função do Texto
def texto(ret, msg):
    global fundo
    self = Text(ret.getCenter(), msg)
    self.setStyle('bold')
    self.setTextColor(fundo)
    self.setFace('times roman')
    self.draw(menu)
    return self

# Função do Retângulo
def retangulo(x1, y1, x2, y2):
    global botoes
    self = Rectangle(Point(x1, y1), Point(x2, y2))
    self.setWidth(3)
    self.setFill(botoes)
    self.draw(menu)
    return self

# Função para Mudar a Resolução
def mudar_resolucao():
    global menu, resolucao, fundo
    menu.close()
    menu = GraphWin('Menu do Jogo', resolucao, resolucao)
    menu.setBackground(fundo)

# Função de limpar o Menu
def limpar(lista):
    for _ in lista:
        _.undraw()

# Menu de Resolução
def menu_resolucao():
    global resolucao, menu, fundo
    selecionou, selecionado = False, 1

    op1 = retangulo(resolucao * 0.05, resolucao * 0.15, resolucao * 0.95, resolucao * 0.05)
    op2 = retangulo(resolucao * 0.05, resolucao * 0.30, resolucao * 0.95, resolucao * 0.20)
    op3 = retangulo(resolucao * 0.05, resolucao * 0.45, resolucao * 0.95, resolucao * 0.35)
    op4 = retangulo(resolucao * 0.05, resolucao * 0.60, resolucao * 0.95, resolucao * 0.50)
    op5 = retangulo(resolucao * 0.05, resolucao * 0.75, resolucao * 0.95, resolucao * 0.65)
    op6 = retangulo(resolucao * 0.05, resolucao * 0.90, resolucao * 0.95, resolucao * 0.80)

    texto1 = texto(op1, '250x250')
    texto2 = texto(op2, '500x500')
    texto3 = texto(op3, '750x750')
    texto4 = texto(op4, '1000x1000')
    texto5 = texto(op5, '1500x1500')
    texto6 = texto(op6, '< Voltar')

    lista = (op1, op2, op3, op4, op5, op6, texto1, texto2, texto3, texto4, texto5, texto6)

    while not selecionou:
        teclas = menu.checkKey()

        # Setinha p/ cima
        if teclas == 'Up':
            if selecionado != 1:
                selecionado -= 1
        # Setinha p/ baixo
        elif teclas == 'Down':
            if selecionado != 6:
                selecionado += 1
        # Enter
        elif teclas == 'Return':
            if selecionado != 6:
                opcoes = [250, 500, 750, 1000, 1500]
                resolucao = opcoes[selecionado-1]
                mudar_resolucao()
            limpar(lista)
            return True
        # ESC
        elif teclas in ['Escape', 'BackSpace']:
            limpar(lista)
            menu_principal()

        # Função para checagem do selecionado
        listaop = [op1, op2, op3, op4, op5, op6]
        resetar_outline(listaop, selecionado)

def menu_dificuldade():
    global fundo, resolucao, dificuldade
    selecionou, selecionado = False, 1

    op1 = retangulo(resolucao * 0.05, resolucao * 0.30, resolucao * 0.95, resolucao * 0.20)
    op2 = retangulo(resolucao * 0.05, resolucao * 0.45, resolucao * 0.95, resolucao * 0.35)
    op3 = retangulo(resolucao * 0.05, resolucao * 0.60, resolucao * 0.95, resolucao * 0.50)
    op4 = retangulo(resolucao * 0.05, resolucao * 0.75, resolucao * 0.95, resolucao * 0.65)

    texto1 = texto(op1, 'FÁCIL')
    texto2 = texto(op2, 'NORMAL')
    texto3 = texto(op3, 'DIFÍCIL')
    texto5 = texto(op4, '< Voltar')

    dificuldades = ('FÁCIL', 'NORMAL', 'DIFÍCIL')
    texto4 = Text(Point(resolucao * 0.5, resolucao * 0.1), f'DIFICULDADE ATUAL: {dificuldades[dificuldade-1]}')
    texto4.setStyle('bold')
    texto4.setTextColor('white')
    texto4.draw(menu)

    lista = (op1, op2, op3, op4, texto1, texto2, texto3, texto4, texto5)

    while not selecionou:
        teclas = menu.checkKey()

        # Setinha p/ cima
        if teclas == 'Up':
            if selecionado != 1:
                selecionado -= 1
        # Setinha p/ baixo
        elif teclas == 'Down':
            if selecionado != 4:
                selecionado += 1
        # Enter
        elif teclas == 'Return':
            if selecionado != 4:
                opcoes = [1, 2, 3]
                dificuldade = opcoes[selecionado - 1]
            limpar(lista)
            return True
        # ESC
        elif teclas in ['Escape', 'BackSpace']:
            limpar(lista)
            menu_principal()

        # Função para checagem do selecionado
        listaop = [op1, op2, op3, op4]
        resetar_outline(listaop, selecionado)


# Menu Principal
def menu_principal():
    global fundo, resolucao, menu
    selecionado = 1
    selecionou, selecionou_opcao = False, False

    op1 = retangulo(resolucao * 0.05, resolucao * 0.30, resolucao * 0.95, resolucao * 0.20)
    op2 = retangulo(resolucao * 0.05, resolucao * 0.45, resolucao * 0.95, resolucao * 0.35)

    # Função texto em prática
    texto0 = Text(Point(resolucao * 0.5, resolucao * 0.1), f'MENU PRINCIPAL')
    texto0.setStyle('bold')
    texto0.setTextColor('white')
    texto0.draw(menu)
    texto1 = texto(op1, 'RESOLUÇÃO')
    texto2 = texto(op2, 'DIFICULDADE')

    while not selecionou:

        teclas = menu.checkKey()

        # Setinha p/ cima
        if teclas == 'Up':
            if selecionado != 1:
                selecionado -= 1
        # Setinha p/ baixo
        elif teclas == 'Down':
            if selecionado != 2:
                selecionado += 1
        # Enter
        elif teclas == 'Return':
            lista = [op1, op2, texto0, texto1, texto2]
            limpar(lista)
            if selecionado == 1:
                selecionou_opcao = menu_resolucao()
            if selecionado == 2:
                selecionou_opcao = menu_dificuldade()
        # ESC
        elif teclas in ['Escape', 'BackSpace']:
            exit()

        # Função para checagem do selecionado
        if selecionou_opcao:
            selecionou_opcao = False
            menu_principal()

        listaop = [op1, op2]
        resetar_outline(listaop, selecionado)


# Abre o Menu
menu_principal()
