from graphics import *
import random, math

def reset_outline(op1, op2, s, fundo):
    if s == 1:
        op2.setOutline(fundo)
    elif s == 2:
        op1.setOutline(fundo)


def retangulo(self, jan, x1, y1, x2, y2):
    self = Rectangle(Point(x1, y1), Point(x2, y2))
    self.setWidth(3)
    self.setFill(color_rgb(255, 248, 171))
    self.draw(jan)
    return self

def Menu():
    fundo = color_rgb(33, 33, 33)
    resolucao = 500
    selecionado = 1
    selecionou = False
    menu = GraphWin('Menu do Jogo...', resolucao, resolucao)
    menu.setBackground(fundo)

    op1, op2 = None, None
    op1 = retangulo(op1, menu, resolucao * 0.05, resolucao * 0.15, resolucao * 0.95, resolucao * 0.05)
    op2 = retangulo(op2, menu, resolucao * 0.05, resolucao * 0.30, resolucao * 0.95, resolucao * 0.20)

    texto1 = Text(op1.getCenter(), 'PRIMEIRA OPÇÃO')
    texto2 = Text(op2.getCenter(), 'SEGUNDA OPÇÃO')
    texto1.setStyle('bold')
    texto1.setTextColor(fundo)
    texto1.setSize(22)
    texto2.setStyle('bold')
    texto2.setTextColor(fundo)
    texto2.setSize(22)
    texto1.draw(menu)
    texto2.draw(menu)

    while not selecionou:
        teclas = menu.checkKey()

        if teclas == 'Up':
            if selecionado != 1:
                selecionado -= 1
        elif teclas == 'Down':
            if selecionado != 2:
                selecionado += 1
        elif teclas == 'Return':
            selecionou = True
            menu.close()
        elif teclas == 'Escape':
            selecionou = True
            menu.close()

        if selecionado == 1:
            reset_outline(op1, op2, selecionado, fundo)
            op1 = Rectangle(Point(resolucao * 0.05, resolucao * 0.15), Point(resolucao * 0.95, resolucao * 0.05))
            op1.setOutline('white')
            op1.setWidth(3)
            op1.draw(menu)
        elif selecionado == 2:
            reset_outline(op1, op2, selecionado, fundo)
            op2 = Rectangle(Point(resolucao * 0.05, resolucao * 0.30), Point(resolucao * 0.95, resolucao * 0.20))
            op2.setOutline('white')
            op2.setWidth(3)
            op2.draw(menu)
        elif selecionado == 3:
            selecionou = True
Menu()