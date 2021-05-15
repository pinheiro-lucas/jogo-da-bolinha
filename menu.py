from graphics import *
import random, math, time

# Variáveis globais
resolucao = 500
fundo = color_rgb(33, 33, 33)

# Cria o Menu Principal
menu = GraphWin('Menu do Jogo', resolucao, resolucao)
menu.setBackground(color_rgb(33, 33, 33))

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
def MenuResolucao(fundo):
    global resolucao, menu
    selecionou, selecionado = False, 1

    op1, op2, op3, op4, op5 = None, None, None, None, None
    op1 = retangulo(op1, resolucao * 0.05, resolucao * 0.15, resolucao * 0.95, resolucao * 0.05)
    op2 = retangulo(op2, resolucao * 0.05, resolucao * 0.30, resolucao * 0.95, resolucao * 0.20)
    op3 = retangulo(op3, resolucao * 0.05, resolucao * 0.45, resolucao * 0.95, resolucao * 0.35)
    op4 = retangulo(op4, resolucao * 0.05, resolucao * 0.60, resolucao * 0.95, resolucao * 0.50)
    op5 = retangulo(op5, resolucao * 0.05, resolucao * 0.75, resolucao * 0.95, resolucao * 0.65)

    texto1, texto2, texto3, texto4, texto5 = None, None, None, None, None
    texto1 = texto(texto1, op1, fundo, '250x250 (RECOMENDADO PARA <HD)')
    texto2 = texto(texto2, op2, fundo, '500x500 (RECOMENDADO PARA HD)')
    texto3 = texto(texto3, op3, fundo, '750x750 (RECOMENDADO PARA FULL-HD)')
    texto4 = texto(texto4, op4, fundo, '1000x1000 (RECOMENDADO PARA 4K)')
    texto5 = texto(texto5, op5, fundo, '1500x1500 (RECOMENDADO PARA 8K)')

    lista = [op1, op2, op3, op4, op5, texto1, texto2, texto3, texto4, texto5]

    while not selecionou:
        teclas = menu.checkKey()

        # Setinha p/ cima
        if teclas == 'Up':
            if selecionado != 1:
                selecionado -= 1
        # Setinha p/ baixo
        elif teclas == 'Down':
            if selecionado != 5:
                selecionado += 1
        # Enter
        elif teclas == 'Return':
            Limpar(lista)
            if selecionado == 1:
                resolucao = 250
                MudarResolucao()
                return True
            elif selecionado == 2:
                resolucao = 500
                MudarResolucao()
                return True
            elif selecionado == 3:
                resolucao = 750
                MudarResolucao()
                return True
            elif selecionado == 4:
                resolucao = 1000
                MudarResolucao()
                return True
            elif selecionado == 5:
                resolucao = 1500
                MudarResolucao()
                return True
        # ESC
        elif teclas in ['Escape', 'BackSpace']:
            Limpar(lista)
            Menu()

        # Função para checagem do selecionado
        listaop = [op1, op2, op3, op4, op5]
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
    texto1 = texto(texto1, op1, fundo, 'PRIMEIRA OPÇÃO')
    texto2 = texto(texto2, op2, fundo, 'SEGUNDA OPÇÃO')

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
                selecionouOpcao = MenuResolucao(fundo)
            if selecionado == 2:
                Limpar(lista)
        # ESC
        elif teclas in ['Escape', 'BackSpace']:
            menu.close()

        # Função para checagem do selecionado
        if selecionouOpcao:
            selecionouOpcao = False
            Menu()

        listaop = [op1, op2]
        reset_outline(listaop, selecionado, fundo)

# Abre o Menu
Menu()