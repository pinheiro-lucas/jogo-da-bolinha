from graphics import *
import random, math

# deixa ela quietinha aí
def animacao(self, menu, x, y):
    self.undraw()
    self.move(x, y)
    self.draw(menu)
    time.sleep(1)
    self.undraw()
    self.move(-x , -y)
    self.draw(menu)
    time.sleep(1)

# coloquei tudo q precisava aki dentro pra alterar os retangulos selecionados
def reset_outline(op1, op2, s, fundo):
    if s == 1:
        op2.setOutline(fundo)
        op1.setOutline('white')
    elif s == 2:
        op1.setOutline(fundo)
        op2.setOutline('white')    
        
"""    
def reset_outline(op1, op2, s, fundo):
    if s == 1:
        op2.setOutline(fundo)
    elif s == 2:
        op1.setOutline(fundo)
"""

# funcao do texto
def texto(self, ret, jan, fundo, msg):
    self = Text(ret.getCenter(), msg)
    self.setStyle('bold')
    self.setTextColor(fundo)
    self.draw(jan)
    return self

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
    
    # funcao texto em pratica
    texto1, texto2 = None, None
    texto1 = texto(texto1, op1, menu, fundo, 'Primeira opção')
    texto2 = texto(texto2, op2, menu, fundo, 'Segunda opção')
    
    """
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
    """
    
    while not selecionou:
        teclas = menu.checkKey()

        if teclas == 'Up':
            if selecionado != 1:
                selecionado -= 1
        elif teclas == 'Down':
            if selecionado != 2:
                selecionado += 1
                
        # coloquei em um if só o escape e o return, pq eles faziam o msm comando        
        elif teclas == 'Return' or teclas == 'Escape':
            selecionou = True
            menu.close()
            
        """
        elif teclas == 'Return':
            selecionou = True
            menu.close()
        elif teclas == 'Escape':
            selecionou = True
            menu.close()
        """
        
        # funcao épica
        # vc fez um novo retangulo mas era so mudar a cor da linha do retangulo
        reset_outline(op1, op2, selecionado, fundo)
        
        """
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
        """
        
        # o selecionado nunca vai ser 3
        """
        elif selecionado == 3:
            selecionou = True
        """
Menu()
