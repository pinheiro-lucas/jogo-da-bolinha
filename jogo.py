from graphics import *
from random import randrange
import time

# Variáveis globais
resolucao = 500
fundo = color_rgb(33, 33, 33)
# Antigo: botoes = color_rgb(255, 248, 171)
botoes = color_rgb(163, 103, 127)
dificuldade = 2

# Varíaveis em desenvolvimento
acabou = False
pontos = 0
placar = None
lateral = True

# Cria o Menu Principal
jogo = GraphWin('Jogo da Bolinha', resolucao, resolucao, autoflush=False)
jogo.setBackground(fundo)

# Função de animação (futura)
def animacao(self, x, y):
    self.undraw()
    self.move(x, y)
    self.draw(jogo)
    time.sleep(1)
    self.undraw()
    self.move(-x, -y)
    self.draw(jogo)
    time.sleep(1)

# Animação de seleção
def resetar_outline(listaop, s):
    global fundo
    for element in listaop:
        if listaop.index(element) == s - 1:
            element.setOutline('white')
        else:
            element.setOutline(fundo)

# Função do Retângulo
def retangulo(x1, y1, x2, y2):
    global botoes, resolucao, jogo
    self = Rectangle(Point(resolucao * (x1 / 100), resolucao * (y1 / 100)),
                     Point(resolucao * (x2 / 100), resolucao * (y2 / 100)))
    self.setWidth(3)
    self.setFill(botoes)
    self.draw(jogo)
    return self

# Função do Texto
def texto_ret(ret, msg):
    global fundo, resolucao, jogo
    self = Text(ret.getCenter(), msg)
    self.setTextColor(fundo)
    self.setStyle('bold')
    self.setFace('times roman')
    tamanho_normal = {250: 10, 500: 15, 750: 20, 1000: 25}
    self.setSize(tamanho_normal[resolucao])
    self.draw(jogo)
    return self

# Função de Texto sem Retângulo
def texto_sem_ret(x, y, t, msg):
    global botoes, resolucao, jogo
    self = Text(Point(resolucao*(x/100), resolucao * (y/100)), msg)
    self.setStyle('bold')
    self.setTextColor(botoes)
    self.setFace('times roman')
    if t:
        tamanho_maior = {250: 15, 500: 20, 750: 25, 1000: 30}
        self.setSize(tamanho_maior[resolucao])
        self.draw(jogo)
        return self
    tamanho_normal = {250: 10, 500: 15, 750: 20, 1000: 25}
    self.setSize(tamanho_normal[resolucao])
    self.draw(jogo)
    return self

# Função da Bolinha
def bola(x, y):
    global jogo, resolucao, botoes
    # Fórmula para o raio da circunferência
    if dificuldade == 3:
        r = (9/500)*resolucao
    else:
        r = resolucao/50
    self = Circle(Point(resolucao*(x/100), resolucao * (y/100)), r)
    self.setFill(botoes)
    # self.setOutline('white')
    self.draw(jogo)
    return self

# Função de Criar a Barrinha
def criar_barra(x1, y1, x2, y2):
    global botoes, resolucao, jogo
    self = Rectangle(Point(resolucao * (x1 / 100), resolucao * (y1 / 100)),
                     Point(resolucao * (x2 / 100), resolucao * (y2 / 100)))
    self.setFill(botoes)
    self.setWidth(2)
    self.setOutline(botoes)
    self.draw(jogo)
    return self

# Função para Mudar a Resolução
def mudar_resolucao():
    global jogo, resolucao, fundo
    jogo.close()
    jogo = GraphWin('Menu do Jogo', resolucao, resolucao)
    jogo.setBackground(fundo)

# Função de limpar o Menu
def limpar(lista):
    for _ in lista:
        _.undraw()

# Sub-Menu de Resolução
def menu_resolucao():
    global resolucao, jogo, fundo
    selecionou, selecionado = False, 1

    op1 = retangulo(5, 15, 95, 5)
    op2 = retangulo(5, 30, 95, 20)
    op3 = retangulo(5, 45, 95, 35)
    op4 = retangulo(5, 60, 95, 50)
    op5 = retangulo(5, 95, 95, 85)

    texto1 = texto_ret(op1, '250x250')
    texto2 = texto_ret(op2, '500x500')
    texto3 = texto_ret(op3, '750x750')
    texto4 = texto_ret(op4, '1000x1000')
    texto5 = texto_ret(op5, '< Voltar')

    lista = (op1, op2, op3, op4, op5, texto1, texto2, texto3, texto4, texto5)

    while not selecionou:
        teclas = jogo.checkKey()

        # Seleciona p/ cima
        if teclas in ('Up', 'W', 'w'):
            if selecionado != 1:
                selecionado -= 1
        # Seleciona p/ baixo
        elif teclas in ('Down', 'S', 's'):
            if selecionado != 5:
                selecionado += 1
        # Ao selecionar
        elif teclas in ('Return', 'space'):
            if selecionado != 5:
                opcoes = (250, 500, 750, 1000)
                resolucao = opcoes[selecionado - 1]
                mudar_resolucao()
            limpar(lista)
            return True
        # ESC
        elif teclas in ('Escape', 'BackSpace'):
            limpar(lista)
            menu_principal()

        # Função para checagem do selecionado
        listaop = (op1, op2, op3, op4, op5)
        resetar_outline(listaop, selecionado)

# Sub-Menu de Dificuldade
def menu_dificuldade():
    global fundo, resolucao, dificuldade
    selecionou, selecionado = False, 1

    op1 = retangulo(5, 30, 95, 20)
    op2 = retangulo(5, 45, 95, 35)
    op3 = retangulo(5, 60, 95, 50)
    op4 = retangulo(5, 95, 95, 85)

    texto1 = texto_ret(op1, 'FÁCIL')
    texto2 = texto_ret(op2, 'NORMAL')
    texto3 = texto_ret(op3, 'DIFÍCIL')
    texto5 = texto_ret(op4, '< Voltar')

    dificuldades = ('FÁCIL', 'NORMAL', 'DIFÍCIL')
    texto4 = texto_sem_ret(50, 10, True, f'DIFICULDADE ATUAL: {dificuldades[dificuldade - 1]}')

    lista = (op1, op2, op3, op4, texto1, texto2, texto3, texto4, texto5)

    while not selecionou:
        teclas = jogo.checkKey()

        # Seleciona p/ cima
        if teclas in ('Up', 'W', 'w'):
            if selecionado != 1:
                selecionado -= 1
        # Seleciona p/ baixo
        elif teclas in ('Down', 'S', 's'):
            if selecionado != 4:
                selecionado += 1
        # Ao selecionar
        elif teclas in ('Return', 'space'):
            if selecionado != 4:
                # Muda a dificuldade
                opcoes = (1, 2, 3)
                dificuldade = opcoes[selecionado - 1]
            limpar(lista)
            return True
        # ESC
        elif teclas in ('Escape', 'BackSpace'):
            # Volta para o Menu Principal
            limpar(lista)
            menu_principal()

        # Função para checagem do selecionado
        listaop = (op1, op2, op3, op4)
        resetar_outline(listaop, selecionado)

# Sub-Menu de Tutorial
def menu_comojogar():
    global fundo, resolucao
    selecionou, selecionado = False, 1

    op1 = retangulo(5, 95, 95, 85)

    texto1 = texto_ret(op1, '< Voltar')

    texto2 = texto_sem_ret(50, 10, True, 'COMO JOGAR:')
    texto3 = texto_sem_ret(50, 20, False, 'Você tem três vidas')
    texto4 = texto_sem_ret(50, 25, False, 'Não deixe a bolinha cair')
    texto5 = texto_sem_ret(50, 30, False, 'A velocidade aumenta conforme o tempo')
    texto6 = texto_sem_ret(50, 35, False, 'Utilize as setinhas para controlar a barra')
    texto7 = texto_sem_ret(50, 40, False, 'Recupere a vida coletando os corações')
    texto8 = texto_sem_ret(50, 45, False, 'Aproveite os modos mais desafiadores')

    lista = (op1, texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8)

    while not selecionou:
        teclas = jogo.checkKey()

        # Enter
        if teclas in ('Return', 'space'):
            limpar(lista)
            return True
        # ESC
        elif teclas in ('Escape', 'BackSpace'):
            limpar(lista)
            menu_principal()

        # Função para checagem do selecionado
        listaop = [op1]
        resetar_outline(listaop, selecionado)

# Sub-Menu de Créditos
def menu_creditos():
    global fundo, resolucao
    selecionou, selecionado = False, 1

    op1 = retangulo(5, 95, 95, 85)

    texto1 = texto_ret(op1, '< Voltar')

    texto2 = texto_sem_ret(50, 10, True, 'CRÉDITOS:')
    texto3 = texto_sem_ret(50, 20, False, 'Lucas Pinheiro')
    texto4 = texto_sem_ret(50, 25, False, 'Thiago Rabelo')
    texto5 = texto_sem_ret(50, 30, False, 'Giulia Yule')
    texto6 = texto_sem_ret(50, 35, False, 'Maria Antônia')
    texto7 = texto_sem_ret(50, 40, False, 'Luiz Falcão')

    lista = (op1, texto1, texto2, texto3, texto4, texto5, texto6, texto7)

    while not selecionou:
        teclas = jogo.checkKey()

        # Enter
        if teclas in ('Return', 'space'):
            limpar(lista)
            return True
        # ESC
        elif teclas in ('Escape', 'BackSpace'):
            limpar(lista)
            menu_principal()

        # Função para checagem do selecionado
        listaop = (op1,)
        resetar_outline(listaop, selecionado)

# Jogo Principal
def jogo_principal():
    global resolucao, fundo, jogo, acabou, pontos, placar, lateral, dificuldade

    # Ativa o 'autoflush' para a gente manipular quadros
    jogo.autoflush = True

    # Variáveis necessárias
    pausa, acabou = True, False
    pontos = 0
    """
    
       Para X:
       1 = Direita
      -1 = Esquerda
    
       Para Y:
       1 = Baixo
      -1 = Cima
      
    """
    # Gera pra onde a bolinha vai (random e para cima)
    x, y = randrange(-1, 2, 2), -1
    # Cria a primeira posição da bolinha (random com limites)
    bolinha = bola(randrange(45, 56), 72)
    # Cria as barras da margem
    self, self2 = margem()
    # Variável da lateral da barra
    lateral = True

    # Gera a barra dependendo da dificuldade
    # Fácil
    if dificuldade == 1:
        barra = criar_barra(30, 75, 70, 77)
    # Difícil
    elif dificuldade == 3:
        barra = criar_barra(45, 75, 55, 77)
    # Normal
    else:
        barra = criar_barra(40, 75, 60, 77)

    """
    TESTE
    if dificuldade == 1:
        barra = criar_barra(1, 75, 99, 77)
        dificuldade = 3
    """

    # Gera o placar
    placar = atualizar_placar()

    # Pressione Enter para iniciar (Obs: aqui é a introdução do jogo, não deveria aparecer que está pausado) ----------------------
    pausar()

    # Núcleo do Jogo
    while not acabou:

        teclas = jogo.checkKey()

        # Barra vai para a direita até o limite da margem
        # 9 = Margem-1 para corrigir quando não bate na parede por conta da velocidade variável
        # To-do (Bug Visual): Dependendo do movimento, fica sobrando ou não 1px
        if teclas in ('Right', 'D', 'd') and barra.getP2().getX() <= resolucao-9:

            # Cálculo do movimento da barra
            if x > 0:
                barra.move(5 + x * dificuldade, 0)
            else:
                barra.move(-(-5 + x * dificuldade), 0)

        # Barra vai para a esquerda até o limite da margem
        # 9 = Margem-1 para corrigir quando não bate na parede por conta da velocidade variável
        # To-do (Bug Visual): Dependendo do movimento, fica sobrando ou não 1px
        elif teclas in ('Left', 'A', 'a') and barra.getP1().getX() >= 9:

            # Cálculo do movimento da barra
            if x > 0:
                barra.move(-(5 + x * dificuldade), 0)
            else:
                barra.move(-5 + x * dificuldade, 0)

        # Pausa o Jogo
        elif teclas in ('Escape', 'BackSpace'):
            pausar()

        # Checa se bateu a cada atualização
        x, y = bateu(bolinha, x, y, barra)
        # Cálculo do movimento da bolinha
        bolinha.move(resolucao*(x/1000*dificuldade), resolucao*(y/1000*dificuldade))
        # Debug
        #print(resolucao*(x/1000*dificuldade), resolucao*(y/1000*dificuldade))
        # Taxa de atualização (60hz)
        update(60)

    # Limpar tudo ao acabar
    lista = (bolinha, placar, self, self2, barra)
    limpar(lista)
    # Mostrar o placar final
    resultado()
    # Voltar ao Menu
    menu_principal()

# Resultado final
def resultado():
    # Variáveis necessárias
    global pontos
    texto0 = texto_sem_ret(50, 45, False, 'VOCÊ DEIXOU A BOLINHA CAIR =(')
    texto1 = texto_sem_ret(50, 55, False, f'PONTUAÇÃO FINAL: {pontos}')
    texto2 = texto_sem_ret(50, 65, False, '[ESC] Menu')

    voltar = False

    while not voltar:

        teclas = jogo.checkKey()

        # Retornar ao Menu
        if teclas in ('Return', 'space', 'Escape', 'BackSpace'):
            texto = (texto0, texto1, texto2)
            limpar(texto)
            voltar = True

# Função de Pause
def pausar():
    # Variáveis necessárias
    texto0 = texto_sem_ret(50, 30, True, '>>> JOGO PAUSADO <<<')
    texto1 = texto_sem_ret(50, 40, True, '[ENTER] Jogar')
    texto2 = texto_sem_ret(50, 50, True, '[ESC] Menu')
    global acabou
    pausa = True

    while pausa:

        teclas = jogo.checkKey()

        # Retornar ao clicar Enter
        if teclas in ('Return', 'space'):
            texto = (texto0, texto1, texto2)
            limpar(texto)
            pausa = False

        # Acabar ao clicar ESC
        elif teclas in ('Escape', 'BackSpace'):
            texto = (texto0, texto1, texto2)
            limpar(texto)
            pausa = False
            confirmar()

# Confirmar ao voltar p/ o Menu
def confirmar():
    # Variáveis necessárias
    texto0 = texto_sem_ret(50, 30, True, '>> Você perderá seu progresso <<')
    texto1 = texto_sem_ret(50, 40, True, '[ENTER] Confirmar')
    texto2 = texto_sem_ret(50, 50, True, '[ESC] Voltar')
    global acabou
    confirma = True

    while confirma:

        teclas = jogo.checkKey()

        # Retornar ao clicar Enter
        if teclas in ('Return', 'space'):
            texto = (texto0, texto1, texto2)
            limpar(texto)
            confirma, acabou = False, True

        # Acabar ao clicar ESC
        elif teclas in ('Escape', 'BackSpace'):
            texto = (texto0, texto1, texto2)
            limpar(texto)
            confirma = False
            pausar()

# Função de criação da Margem
def margem():
    global resolucao, fundo, botoes
    # Criar um retângulo de margem nas bordas
    self = Rectangle(Point(1, 1), Point(resolucao-1, resolucao * (80 / 100)))
    self.setOutline(botoes)
    self.setWidth(10)
    self.draw(jogo)
    # Deletar a parte de baixo
    self2 = Rectangle(Point(0, resolucao * (80 / 100)), Point(resolucao-1, resolucao-1))
    self2.setOutline(botoes)
    self2.setWidth(10)
    self2.setFill(botoes)
    self2.draw(jogo)
    return self, self2

# Função para checar se bateu
def bateu(ball, x, y, barra):
    global acabou, dificuldade, pontos, placar, lateral

    # Fórmula para o raio da circunferência
    if dificuldade == 3:
        r = (9/500)*resolucao
    else:
        r = resolucao/50

    # Criação de variáveis repetitivas:
    # BolaX
    bx = ball.getCenter().getX()
    # BolaY
    by = ball.getCenter().getY()
    # Barra P1 X
    p1x = barra.getP1().getX()
    # Barra P1 Y
    p1y = barra.getP1().getY()
    # Barra P2 X
    p2x = barra.getP2().getX()
    # Barra P2 Y
    p2y = barra.getP2().getY()
    # Dificuldade
    d = dificuldade * 0.1

    # Verificando o intervalo entre o ponto mais à esquerda da barra e o mais a direita da barra
    # (duas primeiras condições) e as duas últimas condições o intervalo do ponto mais e baixo e mais acima
    if p1x <= bx + r and bx - r <= p2x and p1y <= by + r and by - r <= p2y:
        
        # Debug
        print(f"P1({p1x}, {p1y})")
        print(f"P2({p2x}, {p2y})")
        print(f"B({bx}, {by})")
        print("BATEU")
        
        
        # Verificando se a bola está no topo da barra
        if p1y == by + r and lateral:
            # Aumentar o x, que representa a velocidade da bola para os lados, com base na dificuldade
            if x > 0:
                x += d
            else:
                x -= d
            if y > 0:
                y += d
            else:
                y -= d
            # Inverter a direção da bola para cima, já que ela bateu no topo da barra
            y = -y
            # Incrementar os pontos no placar
            pontos += 1
            atualizar_placar()
        # Lateral da barra (se bater uma vez já era, não tem como recuperar a bolinha)
        elif lateral:
            # Variável para bater apenas uma vez
            lateral = False
            # Inverter a posição na hora da batida dependendo da condição (fixado alguns bugs)
            if bx - r <= p2x <= bx - r and x < 0 or bx - r <= p1x <= bx + r and x > 0:
                x = -x
            # Aumentar a velocidade quando bate na lateral (efeito visual)
            x *= 3    

    # Lado esquerdo
    if bx < r + 5:
        x = -x
    # Lado superior
    if by < r + 5:
        y = -y
    # Lado direito
    if bx > resolucao - r - 5:
        x = -x
    # Lado inferior
    if by >= resolucao - r - 5 - 0.2*resolucao:
        acabou = True


    return x, y

# Função de Criação e Atualização do Placar
def atualizar_placar():
    global pontos, placar, fundo
    # Não deixa dar undraw caso não exista (0 pts)
    if pontos > 0:
        placar.undraw()
    # Fica dando undraw e draw
    placar = texto_sem_ret(50, 90, True, f'PONTUAÇÃO ATUAL: {pontos}')
    placar.setTextColor(fundo)
    return placar

# Menu Principal
def menu_principal():
    global fundo, resolucao, jogo

    # Variáveis necessárias
    selecionado = 1
    selecionou, selecionou_opcao = False, False

    # Desativa o 'autoflush' caso o jogador venha do Jogo
    jogo.autoflush = False

    op1 = retangulo(5, 35, 95, 20)
    op2 = retangulo(5, 50, 95, 40)
    op3 = retangulo(5, 65, 95, 55)
    op4 = retangulo(5, 80, 95, 70)
    op5 = retangulo(5, 95, 95, 85)

    # Função texto em prática
    texto0 = texto_sem_ret(50, 10, True, 'MENU PRINCIPAL')
    texto5 = texto_ret(op1, 'JOGAR')
    texto1 = texto_ret(op2, 'RESOLUÇÃO')
    texto2 = texto_ret(op3, 'DIFICULDADE')
    texto3 = texto_ret(op4, 'COMO JOGAR')
    texto4 = texto_ret(op5, 'CRÉDITOS')

    # Enquanto não selecionar nada, continua no Menu
    while not selecionou:

        teclas = jogo.checkKey()

        # Seleciona p/ cima
        if teclas in ('Up', 'W', 'w'):
            if selecionado != 1:
                selecionado -= 1
        # Seleciona p/ baixo
        elif teclas in ('Down', 'S', 's'):
            if selecionado != 5:
                selecionado += 1
        # Ao selecionar
        elif teclas in ('Return', 'space'):
            lista = (op1, op2, op3, op4, op5, texto0, texto1, texto2, texto3, texto4, texto5)
            limpar(lista)
            if selecionado == 1:
                selecionou = True
                jogo_principal()
            elif selecionado == 2:
                selecionou_opcao = menu_resolucao()
            elif selecionado == 3:
                selecionou_opcao = menu_dificuldade()
            elif selecionado == 4:
                selecionou_opcao = menu_comojogar()
            elif selecionado == 5:
                selecionou_opcao = menu_creditos()
        # ESC
        elif teclas in ('Escape', 'BackSpace'):
            exit()

        # Função para checagem do selecionado
        if selecionou_opcao:
            selecionou_opcao = False
            menu_principal()

        listaop = (op1, op2, op3, op4, op5)
        resetar_outline(listaop, selecionado)


# Abre o Menu/Start
menu_principal()