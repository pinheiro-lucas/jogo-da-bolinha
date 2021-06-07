from graphics import *
from random import randrange
import time

# Variáveis Globais
RESOLUCAO, DIFICULDADE = 500, 2
FUNDO, BOTOES = color_rgb(33, 33, 33), color_rgb(163, 103, 127)
ACABOU, PLACAR, LATERAL, EXTRA = False, None, True, False
_COMECOU, _CAIU = False, False
PONTOS = 0
XRANDOM, YRANDOM = 0, 0
MUDOU_RESOLUCAO = False

# Cria o Menu Principal
jogo = GraphWin('Jogo da Bolinha', RESOLUCAO, RESOLUCAO, autoflush=False)
jogo.setBackground(FUNDO)


# Animação de seleção
def resetar_outline(listaop, s):
    global FUNDO
    for element in listaop:
        if listaop.index(element) == s - 1:
            element.setOutline('white')
        else:
            element.setOutline(FUNDO)


# Função do Retângulo
def retangulo(x1, y1, x2, y2):
    global BOTOES, RESOLUCAO, jogo
    self = Rectangle(Point(RESOLUCAO * (x1 / 100), RESOLUCAO * (y1 / 100)),
                     Point(RESOLUCAO * (x2 / 100), RESOLUCAO * (y2 / 100)))
    self.setWidth(3)
    self.setFill(BOTOES)
    self.draw(jogo)
    return self


# Função do Texto
def texto_ret(ret, msg):
    global FUNDO, RESOLUCAO, jogo
    self = Text(ret.getCenter(), msg)
    self.setTextColor(FUNDO)
    self.setStyle('bold')
    self.setFace('times roman')
    tamanho_normal = {250: 10, 500: 15, 750: 20, 1000: 25}
    self.setSize(tamanho_normal[RESOLUCAO])
    self.draw(jogo)
    return self


# Função de Texto sem Retângulo
def texto_sem_ret(x, y, t, msg):
    global BOTOES, RESOLUCAO, jogo
    self = Text(Point(RESOLUCAO * (x / 100), RESOLUCAO * (y / 100)), msg)
    self.setStyle('bold')
    self.setTextColor(BOTOES)
    self.setFace('times roman')
    if t:
        tamanho_maior = {250: 15, 500: 20, 750: 25, 1000: 30}
        self.setSize(tamanho_maior[RESOLUCAO])
        self.draw(jogo)
        return self
    tamanho_normal = {250: 10, 500: 15, 750: 20, 1000: 25}
    self.setSize(tamanho_normal[RESOLUCAO])
    self.draw(jogo)
    return self


# Função da Bolinha
def bola(x, y):
    global jogo, RESOLUCAO, BOTOES
    # Fórmula para o raio da circunferência
    if DIFICULDADE == 3:
        r = (9 / 500) * RESOLUCAO
    else:
        r = RESOLUCAO / 50
    self = Circle(Point(RESOLUCAO * (x / 100), RESOLUCAO * (y / 100)), r)
    self.setFill(BOTOES)
    # self.setOutline('white')
    self.draw(jogo)
    return self


# Função de Criar a Barrinha
def criar_barra(x1, y1, x2, y2):
    global BOTOES, RESOLUCAO, jogo
    self = Rectangle(Point(RESOLUCAO * (x1 / 100), RESOLUCAO * (y1 / 100)),
                     Point(RESOLUCAO * (x2 / 100), RESOLUCAO * (y2 / 100)))
    self.setFill(BOTOES)
    self.setWidth(2)
    self.setOutline(BOTOES)
    self.draw(jogo)
    return self


# Função para Mudar a Resolução
def mudar_resolucao():
    global jogo, RESOLUCAO, FUNDO, MUDOU_RESOLUCAO
    jogo.close()
    jogo = GraphWin('Menu do Jogo', RESOLUCAO, RESOLUCAO)
    jogo.setBackground(FUNDO)
    MUDOU_RESOLUCAO = True


# Função de limpar o Menu
def limpar(lista):
    for _ in lista:
        _.undraw()


# Sub-Menu de Resolução
def menu_resolucao():
    global RESOLUCAO, jogo, FUNDO
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
                RESOLUCAO = opcoes[selecionado - 1]
                mudar_resolucao()
            limpar(lista)
            return True
        # ESC
        elif teclas in ('Escape', 'BackSpace'):
            limpar(lista)
            return True

        # Função para checagem do selecionado
        listaop = (op1, op2, op3, op4, op5)
        resetar_outline(listaop, selecionado)


# Sub-Menu de Dificuldade
def menu_dificuldade():
    global FUNDO, RESOLUCAO, DIFICULDADE
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
    texto4 = texto_sem_ret(50, 10, True, f'DIFICULDADE ATUAL: {dificuldades[DIFICULDADE - 1]}')

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
                DIFICULDADE = opcoes[selecionado - 1]
            limpar(lista)
            return True
        # ESC
        elif teclas in ('Escape', 'BackSpace'):
            # Volta para o Menu Principal
            limpar(lista)
            return True

        # Função para checagem do selecionado
        listaop = (op1, op2, op3, op4)
        resetar_outline(listaop, selecionado)


# Sub-Menu de Tutorial
def menu_comojogar():
    global FUNDO, RESOLUCAO
    selecionou, selecionado = False, 1

    op1 = retangulo(5, 95, 95, 85)

    texto1 = texto_ret(op1, '< Voltar')

    texto2 = texto_sem_ret(50, 15, True, 'COMO JOGAR:')
    texto3 = texto_sem_ret(50, 35, False, 'Não deixe a bolinha cair')
    texto4 = texto_sem_ret(50, 40, False, 'A velocidade aumenta conforme o tempo')
    texto5 = texto_sem_ret(50, 45, False, 'Utilize as setinhas para controlar a barra')
    texto6 = texto_sem_ret(50, 50, False, 'Aproveite as dificuldades mais desafiadoras')
    texto7 = texto_sem_ret(50, 55, False, 'Aproveite também o modo extra')

    lista = (op1, texto1, texto2, texto3, texto4, texto5, texto6, texto7)

    while not selecionou:
        teclas = jogo.checkKey()

        # Enter ou esc faz a mesma coisa
        if teclas in ('Return', 'space', 'Escape', 'BackSpace'):
            limpar(lista)
            return True

        # Função para checagem do selecionado
        listaop = op1,
        resetar_outline(listaop, selecionado)

# Jogo Principal
def jogo_principal():
    global RESOLUCAO, FUNDO, jogo, ACABOU, PONTOS, PLACAR, LATERAL, DIFICULDADE, _CAIU, _COMECOU, EXTRA

    # Ativa o 'autoflush' para a manipulação dos quadros
    jogo.autoflush = True

    # Variáveis necessárias
    ACABOU, _CAIU = False, False
    PONTOS = 0
    """
       --- X ---
       1 = Direita
      -1 = Esquerda
       --- Y ---
       1 = Baixo
      -1 = Cima
    """
    # Gera pra onde a bolinha vai (random e para cima)
    x, y = randrange(-1, 2, 2), -1
    # Cria a primeira posição da bolinha (random com limites)
    bolinha = bola(randrange(45, 56), 72)
    # Cria as barras da margem
    self, self2 = margem()
    self3 = None
    # Variável da lateral da barra
    LATERAL = True

    # Gera a barra dependendo da dificuldade
    # Fácil
    if DIFICULDADE == 1:
        barra = criar_barra(30, 75, 70, 77)
    # Difícil
    elif DIFICULDADE == 3:
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

    # Gera o PLACAR
    PLACAR = atualizar_placar()

    # Gera os Cubos se for a fase Extra
    if EXTRA:
        self3 = cubos()

    # Pressione Enter para iniciar
    pausar()
    _COMECOU = True

    # Núcleo do Jogo
    while not ACABOU:

        teclas = jogo.checkKey()

        p2x = barra.getP2().getX()
        p1x = barra.getP1().getX()

        # Barra vai para a direita até o limite da margem
        # 9 = Margem-1 para corrigir quando não bate na parede por conta da velocidade variável
        # To-do (Bug Visual): Dependendo do movimento, fica sobrando ou não 1px
        if teclas in ('Right', 'D', 'd'):

            # Cálculo do movimento da barra
            if x > 0:
                if 5 + x * DIFICULDADE <= RESOLUCAO - 9 - p2x:
                    barra.move((5 + x * DIFICULDADE)*(RESOLUCAO/500), 0)
                else:
                    barra.move(RESOLUCAO - 9 - p2x, 0)
            else:
                if -(-5 + x * DIFICULDADE) <= RESOLUCAO - 9 - p2x:
                    barra.move(-(RESOLUCAO/500)*(-5 + x * DIFICULDADE), 0)
                else:
                    barra.move(RESOLUCAO - 9 - p2x, 0)

        # Barra vai para a esquerda até o limite da margem
        # 9 = Margem-1 para corrigir quando não bate na parede por conta da velocidade variável
        # To-do (Bug Visual): Dependendo do movimento, fica sobrando ou não 1px
        elif teclas in ('Left', 'A', 'a'):

            # Cálculo do movimento da barra
            if x > 0:
                if 5 + x * DIFICULDADE <= p1x - 9:
                    barra.move(-(5 + x * DIFICULDADE)*(RESOLUCAO/500), 0)
                else:
                    barra.move((-p1x + 9), 0)
            else:
                if -(-5 + x * DIFICULDADE) <= p1x - 9:
                    barra.move((-5 + x * DIFICULDADE)*(RESOLUCAO/500), 0)
                else:
                    barra.move((-p1x + 9), 0)

        # Pausa o Jogo
        elif teclas in ('Escape', 'BackSpace'):
            pausar()

        # Checa se bateu a cada atualização
        x, y = bateu(bolinha, x, y, barra)
        if EXTRA:
            x, y = bateu_extra(bolinha, x, y, self3)
        # Cálculo do movimento da bolinha
        bolinha.move(RESOLUCAO * (x / 1000 * DIFICULDADE), RESOLUCAO * (y / 1000 * DIFICULDADE))
        # Debug
        # print(RESOLUCAO*(x/1000*DIFICULDADE), RESOLUCAO*(y/1000*DIFICULDADE))
        # Taxa de atualização (60hz)
        update(60)

    # Limpar tudo ao acabar
    if EXTRA:
        limpar(self3)
    lista = (bolinha, PLACAR, self, self2, barra)
    limpar(lista)
    # Mostrar o placar final
    resultado()
    # Retorna as Variáveis Globais
    _COMECOU, EXTRA = False, False
    # Voltar ao Menu
    return True


# Resultado final
def resultado():
    # Variáveis necessárias
    global PONTOS, _CAIU, EXTRA
    dificuldades_string = 'FÁCIL', 'NORMAL', 'DIFÍCIL'

    if EXTRA and not _CAIU and PONTOS == 76:
        texto0 = texto_sem_ret(50, 35, False, '>>> PARABÉNS! VOCÊ VENCEU! <<<')
    elif _CAIU:
        texto0 = texto_sem_ret(50, 35, False, '>>> VOCÊ DEIXOU A BOLINHA CAIR <<<')
    else:
        texto0 = texto_sem_ret(50, 35, False, '>>> VOCÊ FINALIZOU O JOGO <<<')
    texto1 = texto_sem_ret(50, 45, False, f'PONTUAÇÃO FINAL: {PONTOS}')
    texto2 = texto_sem_ret(50, 55, False, f'DIFICULDADE: {dificuldades_string[DIFICULDADE-1]}')
    texto3 = texto_sem_ret(50, 65, False, '[ESC] Menu')

    voltar = False

    while not voltar:

        teclas = jogo.checkKey()

        # Retornar ao Menu
        if teclas in ('Return', 'space', 'Escape', 'BackSpace'):
            texto = (texto0, texto1, texto2, texto3)
            limpar(texto)
            voltar = True


# Função de Pause
def pausar():
    # Variáveis necessárias
    global ACABOU, PONTOS, _COMECOU
    if not _COMECOU:
        texto0 = texto_sem_ret(50, 30, True, '>>> INICIE O JOGO <<<')
    else:
        texto0 = texto_sem_ret(50, 30, True, '>>> JOGO PAUSADO <<<')
    texto1 = texto_sem_ret(50, 40, True, '[ENTER] Jogar')
    texto2 = texto_sem_ret(50, 50, True, '[ESC] Menu')

    pausa, selecionou_opcao = True, False

    # Salvar os objetos do menu pausar para quando alguém selecionar uma opção
    objetos_do_pausar = texto0, texto1, texto2
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
            pausa = confirmar()
            selecionou_opcao = True

        if selecionou_opcao and pausa:
            selecionou_opcao = False
            for objeto in objetos_do_pausar:
                objeto.draw(jogo)


# Confirmar ao voltar p/ o Menu
def confirmar():
    # Variáveis necessárias
    global ACABOU, RESOLUCAO
    # Se o cliente estiver em uma calculadora
    if RESOLUCAO == 250:
        menor = False
    else:
        menor = True
    texto0 = texto_sem_ret(50, 30, menor, '>> Você perderá seu progresso <<')
    texto1 = texto_sem_ret(50, 40, menor, '[ENTER] Confirmar')
    texto2 = texto_sem_ret(50, 50, menor, '[ESC] Voltar')

    confirma = True

    while confirma:

        teclas = jogo.checkKey()

        # Retornar ao clicar Enter
        if teclas in ('Return', 'space'):
            texto = (texto0, texto1, texto2)
            limpar(texto)
            confirma, ACABOU = False, True
            return False

        # Acabar ao clicar ESC
        elif teclas in ('Escape', 'BackSpace'):
            texto = (texto0, texto1, texto2)
            limpar(texto)
            confirma = False
            return True


# Função de criação da Margem
def margem():
    global RESOLUCAO, FUNDO, BOTOES
    # Criar um retângulo de margem nas bordas
    self = Rectangle(Point(1, 1), Point(RESOLUCAO - 1, RESOLUCAO * (80 / 100)))
    self.setOutline(BOTOES)
    self.setWidth(10)
    self.draw(jogo)
    # Deletar a parte de baixo
    self2 = Rectangle(Point(0, RESOLUCAO * (80 / 100)), Point(RESOLUCAO - 1, RESOLUCAO - 1))
    self2.setOutline(BOTOES)
    self2.setWidth(10)
    self2.setFill(BOTOES)
    self2.draw(jogo)
    return self, self2


# Função para checar se bateu
def bateu(ball, x, y, barra):
    global ACABOU, DIFICULDADE, PONTOS, PLACAR, LATERAL, _CAIU, EXTRA, XRANDOM, YRANDOM

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
    # DIFICULDADE
    d = DIFICULDADE * 0.1
    # Fórmula para o raio da circunferência
    if DIFICULDADE == 3:
        r = (9 / 500) * RESOLUCAO
    else:
        r = RESOLUCAO / 50

    # Verificando o intervalo entre o ponto mais à esquerda da barra e o mais a direita da barra
    # (duas primeiras condições) e as duas últimas condições o intervalo do ponto mais e baixo e mais acima
    if p1x - r <= bx <= p2x + r and p1y - r <= by <= p2y + r:

        # Debug
        print(f"P1({p1x}, {p1y})")
        print(f"P2({p2x}, {p2y})")
        print(f"B({bx}, {by})")
        print("BATEU")

        # Verificando se a bola está no topo da barra
        if p1y == by + r and LATERAL:
            # Randomização do movimento da bola
            x -= XRANDOM
            y -= YRANDOM
            XRANDOM = randrange(1, 10)/100
            YRANDOM = randrange(1, 10)/100

            # Aumentar o x, que representa a velocidade da bola para os lados, com base na dificuldade
            if x > 0:
                if EXTRA:
                    x += XRANDOM
                else:
                    x += d + XRANDOM
            else:
                if EXTRA:
                    x -= XRANDOM
                else:
                    x -= d + XRANDOM
            if y > 0:
                if EXTRA:
                    y += YRANDOM
                else:
                    y += d + YRANDOM
            else:
                if EXTRA:
                    y -= YRANDOM
                else:
                    y -= d + YRANDOM

            # Inverter a direção da bola para cima, já que ela bateu no topo da barra
            if y > 0:
                y = -y

            # Incrementar os pontos no placar
            if not EXTRA:
                PONTOS += 1
                atualizar_placar()

        # Lateral da barra (se bater uma vez já era, não tem como recuperar a bolinha)
        elif LATERAL:
            # Inverter a posição na hora da batida dependendo da condição (fixado alguns bugs)
            if p2x + r >= bx >= p2x and x < 0 or p1x - r <= bx <= p1x and x > 0:
                x = -x
            # Aumentar a velocidade quando bate na lateral (efeito visual)
            x *= 3
            # Variável para bater apenas uma vez
            LATERAL = False

    # Lado esquerdo e direito
    if bx < r + 5 and x < 0 or bx > RESOLUCAO - r - 5 and x > 0:
        x = -x
    # Lado superior
    if by < r + 5 and y < 0:
        y = -y
    # Lado inferior
    if by >= RESOLUCAO - r - 5 - 0.2 * RESOLUCAO:
        ACABOU, _CAIU = True, True

    return x, y


# Função para checar se bateu nos cubos
def bateu_extra(ball, x, y, lista_cubos):

    # Criação de variáveis repetitivas:
    # BolaX
    bx = ball.getCenter().getX()
    # BolaY
    by = ball.getCenter().getY()
    # Fórmula para o raio da circunferência
    if DIFICULDADE == 3:
        r = (9 / 500) * RESOLUCAO
    else:
        r = RESOLUCAO / 50

    for cubo in lista_cubos:
        # Pontos do cubo
        bateu_no_cubo = False

        # Criação de variáveis repetitivas:
        c1x = cubo.getP1().getX()
        c1y = cubo.getP1().getY()
        c2x = cubo.getP2().getX()
        c2y = cubo.getP2().getY()

        if c1x - r <= bx <= c2x + r and c1y - r <= by <= c2y + r:
            # Debug
            print(f"C1({c1x}, {c1y})")
            print(f"C2({c2x}, {c2y})")
            print(f"B({bx}, {by})")
            print("BATEU")
            # Se bateu embaixo ou se bateu em cima
            if c2y - RESOLUCAO*(1/100) <= by - r <= c2y and y < 0 or RESOLUCAO*(1/100) + c1y >= by + r >= c1y and y > 0:
                y = -y
                bateu_cubo(cubo, lista_cubos)
                bateu_no_cubo = True
            # Se bateu na direita ou se bateu na esquerda
            if c2x - RESOLUCAO*(1/100) <= bx - r <= c2x and x < 0 or c1x + RESOLUCAO*(1/100) >= bx + r >= c1x and x > 0:
                x = -x
                if not bateu_no_cubo:
                    bateu_cubo(cubo, lista_cubos)
    return x, y


# Comandos repetitivos quando batia no Cubo
def bateu_cubo(cubo, lista_cubos):
    global PONTOS
    PONTOS += 1
    atualizar_placar()
    cubo.undraw()
    lista_cubos.remove(cubo)


# Função de Criação e Atualização do Placar
def atualizar_placar():
    global PONTOS, PLACAR, FUNDO, EXTRA, ACABOU
    # Não deixa dar undraw caso não exista (0 pts)
    if PONTOS > 0:
        PLACAR.undraw()
    if PONTOS == 76 and EXTRA:
        ACABOU = True
    # Fica dando undraw e draw
    PLACAR = texto_sem_ret(50, 90, True, f'PONTUAÇÃO ATUAL: {PONTOS}')
    PLACAR.setTextColor(FUNDO)
    return PLACAR

# Função de Criação dos Cubos
def cubos():
    global RESOLUCAO, BOTOES, jogo

    # Armazena todos os cubos na lista
    lista_cubos = []
    for y in range(2, 20+1, 5):
        for x in range(2, 96+1, 5):
            self = Rectangle(Point(RESOLUCAO * (x / 100 + 1 / 100), RESOLUCAO * (y / 100 + 1 / 100)),
                             Point(RESOLUCAO * (x / 100 + 5 / 100), RESOLUCAO * (y / 100 + 5 / 100)))
            cor = color_rgb(randrange(0, 256), randrange(0, 256), randrange(0, 256))
            self.setOutline(cor)
            self.setFill(cor)
            self.setWidth(2)
            self.draw(jogo)
            lista_cubos.append(self)
    return lista_cubos

def objetos_menu_principal(lista):
    for objeto in lista:
        objeto.draw(jogo)

# Menu Principal
def menu_principal():
    global FUNDO, RESOLUCAO, jogo, MUDOU_RESOLUCAO, EXTRA

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
    texto4 = texto_ret(op5, 'FASE EXTRA')

    # Salvá-los para quando o usuário retornar ao menu principal, eles serem mostrados novamente
    lista_dos_objetos = op1, op2, op3, op4, op5, texto0, texto5, texto1, texto2, texto3, texto4

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
                selecionou_opcao = jogo_principal()
            elif selecionado == 2:
                selecionou_opcao = menu_resolucao()
            elif selecionado == 3:
                selecionou_opcao = menu_dificuldade()
            elif selecionado == 4:
                selecionou_opcao = menu_comojogar()
            elif selecionado == 5:
                selecionou = True
                EXTRA = True
                selecionou_opcao = jogo_principal()

        # ESC
        elif teclas in ('Escape', 'BackSpace'):
            exit()

        # Função para checagem do selecionado
        if selecionou_opcao and not MUDOU_RESOLUCAO:
            # Mostrar novamente os objetos após o retorno do usuário
            selecionou, selecionou_opcao = False, False
            jogo.autoflush = False
            objetos_menu_principal(lista_dos_objetos)
        elif selecionou_opcao:
            # Trocar as dimensões dos objetos do menu principal após a mudança de resolução
            selecionou, selecionou_opcao, MUDOU_RESOLUCAO = False, False, False
            jogo.autoflush = False
            op1 = retangulo(5, 35, 95, 20)
            op2 = retangulo(5, 50, 95, 40)
            op3 = retangulo(5, 65, 95, 55)
            op4 = retangulo(5, 80, 95, 70)
            op5 = retangulo(5, 95, 95, 85)
            texto0 = texto_sem_ret(50, 10, True, 'MENU PRINCIPAL')
            texto5 = texto_ret(op1, 'JOGAR')
            texto1 = texto_ret(op2, 'RESOLUÇÃO')
            texto2 = texto_ret(op3, 'DIFICULDADE')
            texto3 = texto_ret(op4, 'COMO JOGAR')
            texto4 = texto_ret(op5, 'FASE EXTRA')
            # Atualizar a lista dos objetos com as dimensões corretas
            lista_dos_objetos = op1, op2, op3, op4, op5, texto0, texto5, texto1, texto2, texto3, texto4

        listaop = (op1, op2, op3, op4, op5)
        resetar_outline(listaop, selecionado)


# Inicia o Jogo
menu_principal()
