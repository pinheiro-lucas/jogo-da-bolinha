from graphics import *
import random, math, time

# Variáveis globais
resolucao = 500
fundo = color_rgb(33, 33, 33)
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
def reset_outline(listaop, s, fundo):
    for element in listaop:
        if listaop.index(element) == s - 1:
            element.setOutline('white')
        else:
            element.setOutline(fundo)

# Função do Texto
def texto(self, ret, fundo, msg):
    self = Text(ret.getCenter(), msg)
    self.setStyle('bold')
    self.setTextColor(fundo)
    self.setFace('times roman')
    self.draw(menu)
    return self

# Função do Retângulo
def retangulo(self, x1, y1, x2, y2):
    self = Rectangle(Point(x1, y1), Point(x2, y2))
    self.setWidth(3)
    self.setFill(color_rgb(255, 248, 171))
    self.draw(menu)
    return self

# Função para Mudar a Resolução
def MudarResolucao():
    global menu, resolucao
    menu.close()
    menu = GraphWin('Menu do Jogo', resolucao, resolucao)
    menu.setBackground(color_rgb(33, 33, 33))

# Função de Limpar o Menu
def Limpar(lista):
    for a in lista:
        a.undraw()

# Menu de Resolução
def MenuResolucao():
    global resolucao, menu, fundo
    selecionou, selecionado = False, 1

    op1, op2, op3, op4, op5, op6 = None, None, None, None, None, None
    op1 = retangulo(op1, resolucao * 0.05, resolucao * 0.15, resolucao * 0.95, resolucao * 0.05)
    op2 = retangulo(op2, resolucao * 0.05, resolucao * 0.30, resolucao * 0.95, resolucao * 0.20)
    op3 = retangulo(op3, resolucao * 0.05, resolucao * 0.45, resolucao * 0.95, resolucao * 0.35)
    op4 = retangulo(op4, resolucao * 0.05, resolucao * 0.60, resolucao * 0.95, resolucao * 0.50)
    op5 = retangulo(op5, resolucao * 0.05, resolucao * 0.75, resolucao * 0.95, resolucao * 0.65)
    op6 = retangulo(op6, resolucao * 0.05, resolucao * 0.90, resolucao * 0.95, resolucao * 0.80)

    texto1, texto2, texto3, texto4, texto5, texto6 = None, None, None, None, None, None
    texto1 = texto(texto1, op1, fundo, '250x250')
    texto2 = texto(texto2, op2, fundo, '500x500')
    texto3 = texto(texto3, op3, fundo, '750x750')
    texto4 = texto(texto4, op4, fundo, '1000x1000')
    texto5 = texto(texto5, op5, fundo, '1500x1500')
    texto6 = texto(texto6, op6, fundo, '< Voltar')

    lista = [op1, op2, op3, op4, op5, op6, texto1, texto2, texto3, texto4, texto5, texto6]

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
                MudarResolucao()
            Limpar(lista)
            return True
        # ESC
        elif teclas in ['Escape', 'BackSpace']:
            Limpar(lista)
            Menu()

        # Função para checagem do selecionado
        listaop = [op1, op2, op3, op4, op5, op6]
        reset_outline(listaop, selecionado, fundo)

def MenuDificuldade():
    global fundo, resolucao, dificuldade
    selecionou, selecionado = False, 1

    op1, op2, op3, op4 = None, None, None, None
    op1 = retangulo(op1, resolucao * 0.05, resolucao * 0.30, resolucao * 0.95, resolucao * 0.20)
    op2 = retangulo(op2, resolucao * 0.05, resolucao * 0.45, resolucao * 0.95, resolucao * 0.35)
    op3 = retangulo(op3, resolucao * 0.05, resolucao * 0.60, resolucao * 0.95, resolucao * 0.50)
    op4 = retangulo(op4, resolucao * 0.05, resolucao * 0.75, resolucao * 0.95, resolucao * 0.65)

    texto1, texto2, texto3, texto4, texto5 = None, None, None, None, None
    texto1 = texto(texto1, op1, fundo, 'FÁCIL')
    texto2 = texto(texto2, op2, fundo, 'NORMAL')
    texto3 = texto(texto3, op3, fundo, 'DIFÍCIL')
    texto5 = texto(texto4, op4, fundo, '< Voltar')

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
            Limpar(lista)
            return True
        # ESC
        elif teclas in ['Escape', 'BackSpace']:
            Limpar(lista)
            Menu()

        # Função para checagem do selecionado
        listaop = [op1, op2, op3, op4]
        reset_outline(listaop, selecionado, fundo)


# Menu Principal
def Menu():
    global fundo, resolucao, menu
    selecionado = 1
    selecionou, selecionouOpcao = False, False
    op1, op2, texto1, texto2 = None, None, None, None

    op1 = retangulo(op1, resolucao * 0.05, resolucao * 0.15, resolucao * 0.95, resolucao * 0.05)
    op2 = retangulo(op2, resolucao * 0.05, resolucao * 0.30, resolucao * 0.95, resolucao * 0.20)

    # Função texto em prática
    texto1 = texto(texto1, op1, fundo, 'RESOLUÇÃO')
    texto2 = texto(texto2, op2, fundo, 'DIFICULDADE')

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
            lista = [op1, op2, texto1, texto2]
            Limpar(lista)
            if selecionado == 1:
                selecionouOpcao = MenuResolucao()
            if selecionado == 2:
                selecionouOpcao = MenuDificuldade()
        # ESC
        elif teclas in ['Escape', 'BackSpace']:
            exit()

        # Função para checagem do selecionado
        if selecionouOpcao:
            selecionouOpcao = False
            Menu()

        listaop = [op1, op2]
        reset_outline(listaop, selecionado, fundo)

# Abre o Menu
Menu()