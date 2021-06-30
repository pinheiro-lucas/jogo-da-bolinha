# Utilização da biblioteca Graphics + função randrange() da Random
from graphics import *
from random import randrange
from random import choice

# Variáveis Globais
RESOLUCAO, DIFICULDADE = 500, 2
FUNDO, BOTOES = color_rgb(201, 238, 242), color_rgb(9, 27, 38)
ACABOU, PLACAR, LATERAL, EXTRA = False, None, True, False
_COMECOU, _CAIU = False, False
XRANDOM, YRANDOM, PONTOS = 0, 0, 0
RECORD, RECORD_EXTRA = [], []
MUDOU_RESOLUCAO = False
TECLAS_JOGO = ''

# Cria o Menu Principal
JOGO = GraphWin('Jogo da Bolinha', RESOLUCAO, RESOLUCAO, autoflush=False)
JOGO.setBackground(FUNDO)

# Animação de seleção
def resetar_outline(listaop, s):
    global FUNDO
    for element in listaop:
        if listaop.index(element) == s - 1:
            element.setWidth(4)
            element.setOutline(FUNDO)
        else:
            element.setWidth(0)


# Função do Retângulo
def retangulo(x1, y1, x2, y2):
    global BOTOES, RESOLUCAO, JOGO
    self = Rectangle(Point(RESOLUCAO * (x1 / 100), RESOLUCAO * (y1 / 100)),
                     Point(RESOLUCAO * (x2 / 100), RESOLUCAO * (y2 / 100)))
    self.setWidth(3)
    self.setFill(BOTOES)
    self.draw(JOGO)
    return self


# Função do Texto
def texto_ret(ret, msg):
    global FUNDO, RESOLUCAO, JOGO
    self = Text(ret.getCenter(), msg)
    self.setTextColor(FUNDO)
    self.setStyle('bold')
    self.setFace('times roman')
    tamanho_normal = {250: 10, 500: 15, 750: 20, 1000: 25}
    self.setSize(tamanho_normal[RESOLUCAO])
    self.draw(JOGO)
    return self


# Função de Texto sem Retângulo
def texto_sem_ret(x, y, t, msg, cor=BOTOES, fonte='times roman'):
    global BOTOES, RESOLUCAO, JOGO, FUNDO
    self = Text(Point(RESOLUCAO * (x / 100), RESOLUCAO * (y / 100)), msg)
    self.setStyle('bold')
    self.setTextColor(cor)
    self.setFace(fonte)
    # Tamanho maior ou menor
    if t:
        tamanho_maior = {250: 15, 500: 20, 750: 25, 1000: 30}
        self.setSize(tamanho_maior[RESOLUCAO])
        self.draw(JOGO)
        return self
    tamanho_normal = {250: 10, 500: 15, 750: 20, 1000: 25}
    self.setSize(tamanho_normal[RESOLUCAO])
    self.draw(JOGO)
    return self


# Função da Bolinha
def bola(x, y):
    global JOGO, RESOLUCAO, FUNDO
    # Fórmula para o raio da circunferência
    if DIFICULDADE == 3:
        r = (9 / 500) * RESOLUCAO
    else:
        r = RESOLUCAO / 50
    self = Circle(Point(RESOLUCAO * (x / 100), RESOLUCAO * (y / 100)), r-5)  # DEBUG @thiago
    self.setFill(FUNDO)
    self.setOutline(FUNDO)
    self.draw(JOGO)
    return self


# Função de Imagem (Testes)
def img(x, y, png):
    global JOGO, RESOLUCAO
    self = Image(Point(RESOLUCAO * (x / 100), RESOLUCAO * (y / 100)), png)
    self.draw(JOGO)
    return self


# Função de Criar a Barrinha
def criar_barra(x1, y1, x2, y2):
    global RESOLUCAO, JOGO, BOTOES
    self = Rectangle(Point(RESOLUCAO * (x1 / 100), RESOLUCAO * (y1 / 100)),
                     Point(RESOLUCAO * (x2 / 100), RESOLUCAO * (y2 / 100)))
    self.setFill(BOTOES)
    self.setWidth(2)
    self.setOutline(BOTOES)
    self.draw(JOGO)
    return self


# Função para Mudar a Resolução
def mudar_resolucao():
    global JOGO, RESOLUCAO, FUNDO, MUDOU_RESOLUCAO, TECLAS_JOGO
    JOGO.close()
    JOGO = GraphWin('Menu do Jogo', RESOLUCAO, RESOLUCAO, autoflush=False)
    JOGO.setBackground(FUNDO)
    JOGO.bind_all('<KeyPress>', tecla_apertou)
    JOGO.bind_all('<KeyRelease>', tecla_soltou)
    TECLAS_JOGO = ''
    MUDOU_RESOLUCAO = True


# Função de limpar o Menu
def limpar(lista):
    for _ in lista:
        _.undraw()


# Função para pegar os Records de Sessões antigas
def records():
    global RECORD, RECORD_EXTRA
    arquivo = 'records.txt'
    if not os.path.isfile(arquivo):
        open(arquivo, mode='x').close()
        RECORD = [['N/A', 0], ['N/A', 0], ['N/A', 0]]
        RECORD_EXTRA = [['N/A', 0], ['N/A', 0], ['N/A', 0]]
        salvar_record()
    else:
        arquivo = open(arquivo, mode='r')
        flag = 0
        for linha in arquivo:
            if flag < 3:
                RECORD.append(linha.replace('\n', '').split(' '))
            else:
                RECORD_EXTRA.append(linha.replace('\n', '').split(' '))
            flag += 1


# Salva os Records em records.txt
def salvar_record():
    global RECORD, RECORD_EXTRA
    arquivo = open('records.txt', mode='w')
    for record in RECORD:
        arquivo.write(record[0] + ' ' + str(record[1]) + '\n')
    for record in RECORD_EXTRA:
        arquivo.write(record[0] + ' ' + str(record[1]) + '\n')


# Fix para o Delay da biblioteca Graphics [1/2]
def tecla_apertou(tecla):
    global TECLAS_JOGO
    TECLAS_JOGO = tecla.keysym


# Fix para o Delay da biblioteca Graphics [2/2]
def tecla_soltou(tecla):
    global TECLAS_JOGO
    if TECLAS_JOGO == tecla.keysym:
        TECLAS_JOGO = ''


# Fix ao utilizar o AutoFlush
def tecla_menu():
    global JOGO, TECLAS_JOGO
    TECLAS_JOGO = ''
    if JOGO.isClosed():
        exit()
    JOGO.update()
    tecla = TECLAS_JOGO
    return tecla


# Sub-Menu de Resolução
def menu_resolucao():
    global RESOLUCAO, JOGO, FUNDO
    selecionou, selecionado = False, 1

    op1 = retangulo(5, 35, 95, 25)
    op2 = retangulo(5, 50, 95, 40)
    op3 = retangulo(5, 65, 95, 55)
    op4 = retangulo(5, 80, 95, 70)
    op5 = retangulo(5, 95, 95, 85)

    texto0 = texto_sem_ret(50, 12, True, f'Selecione uma resolução:\n(Atual: {RESOLUCAO}x{RESOLUCAO})')
    texto1 = texto_ret(op1, '250x250')
    texto2 = texto_ret(op2, '500x500')
    texto3 = texto_ret(op3, '750x750')
    texto4 = texto_ret(op4, '1000x1000')
    texto5 = texto_ret(op5, '< Voltar')

    lista = (op1, op2, op3, op4, op5, texto0, texto1, texto2, texto3, texto4, texto5)

    while not selecionou:
        teclas = tecla_menu()

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
            opcoes = (250, 500, 750, 1000)
            if selecionado == 5:
                limpar(lista)
                return True
            elif opcoes[selecionado - 1] != RESOLUCAO:
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
        teclas = tecla_menu()

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
            opcoes = (1, 2, 3)
            if selecionado == 4:
                limpar(lista)
                return True
            elif opcoes[selecionado - 1] != DIFICULDADE:
                # Muda a dificuldade
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


# Sub-Menu de Como Jogar
def menu_records():
    global FUNDO, RESOLUCAO, RECORD, RECORD_EXTRA
    selecionou, selecionado = False, 1

    op1 = retangulo(5, 95, 95, 85)

    texto1 = texto_ret(op1, '< Voltar')
    texto2 = texto_sem_ret(50, 10, True, f'FÁCIL: {RECORD[0][0]} {RECORD[0][1]}pts')
    texto3 = texto_sem_ret(50, 22, True, f'NORMAL: {RECORD[1][0]} {RECORD[1][1]}pts')
    texto4 = texto_sem_ret(50, 34, True, f'DIFÍCIL: {RECORD[2][0]} {RECORD[2][1]}pts')
    texto5 = texto_sem_ret(50, 48, True, f'[EXTRA] FÁCIL: {RECORD_EXTRA[0][0]} {RECORD_EXTRA[0][1]}pts')
    texto6 = texto_sem_ret(50, 60, True, f'[EXTRA] NORMAL: {RECORD_EXTRA[1][0]} {RECORD_EXTRA[1][1]}pts')
    texto7 = texto_sem_ret(50, 72, True, f'[EXTRA] DIFÍCIL: {RECORD_EXTRA[2][0]} {RECORD_EXTRA[2][1]}pts')

    lista = (op1, texto1, texto2, texto3, texto4, texto5, texto6, texto7)

    while not selecionou:
        teclas = tecla_menu()

        # Enter ou esc faz a mesma coisa
        if teclas in ('Return', 'space', 'Escape', 'BackSpace'):
            limpar(lista)
            return True

        # Função para checagem do selecionado
        listaop = op1,
        resetar_outline(listaop, selecionado)


# Jogo Principal
def jogo_principal():
    global RESOLUCAO, FUNDO, JOGO, ACABOU, PONTOS, PLACAR, LATERAL, DIFICULDADE, _CAIU, _COMECOU, EXTRA, TECLAS_JOGO

    # Variáveis necessárias
    ACABOU, _CAIU, ajustado = False, False, False
    PONTOS = 0
    """    --- X ---
           1 = Direita
          -1 = Esquerda
           --- Y ---
           1 = Baixo
          -1 = Cima     """
    # Gera pra onde a bolinha vai (random e para cima)
    x, y = choice([2, -2]), -2
    # Cria a primeira posição da bolinha (random com limites)
    fundo_gramado = img(50, 50, 'gramado.gif')
    x_inicial = randrange(45, 56)
    bolinha = bola(x_inicial, 72)
    pngbola = img(x_inicial, 72, 'bola' + str(RESOLUCAO) + '.gif')
    # Cria as barras da margem
    margem1, margem2, linha1, linha2 = margem()
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

    # Gera o PLACAR
    PLACAR = atualizar_placar()

    # Gera os Cubos se for a fase Extra
    if EXTRA:
        self3 = cubos()

    # Pressione Enter para iniciar
    pausar()
    _COMECOU = True

    # Raio da bolinha
    r = RESOLUCAO / 50

    velo_barra = RESOLUCAO / 100

    # Núcleo do Jogo
    while not ACABOU:

        # Checa se a janela foi fechada
        if JOGO.isClosed():
            exit()

        p2x = barra.getP2().getX()
        p1x = barra.getP1().getX()

        # Barra vai para a direita até o limite da margem
        # 9 = Margem-1 para corrigir quando não bate na parede por conta da velocidade variável
        # To-do (Bug Visual): Dependendo do movimento, fica sobrando ou não 1px
        if TECLAS_JOGO in ('Right', 'D', 'd'):

            # Cálculo do movimento da barra
            if p2x + velo_barra <= RESOLUCAO - 9:
                barra.move(velo_barra, 0)
            else:
                barra.move(RESOLUCAO - 9 - p2x, 0)

        # Barra vai para a esquerda até o limite da margem
        # 9 = Margem-1 para corrigir quando não bate na parede por conta da velocidade variável
        # To-do (Bug Visual): Dependendo do movimento, fica sobrando ou não 1px
        elif TECLAS_JOGO in ('Left', 'A', 'a'):

            # Cálculo do movimento da barra
            if p1x - velo_barra >= 9:
                barra.move(-velo_barra, 0)
            else:
                barra.move((-p1x + 9), 0)

        # Pausa o Jogo
        elif TECLAS_JOGO in ('Escape', 'BackSpace'):
            pausar()

        # Checa se bateu a cada atualização
        x, y = bateu(bolinha, x, y, barra, r)
        if EXTRA:
            x, y = bateu_extra(bolinha, x, y, self3)

        # Cálculo do movimento da bolinha
        if y > 0:
            if bolinha.getCenter().getY() + r + RESOLUCAO * (y / 1000 * DIFICULDADE) > barra.getP1().getY() and not ajustado:
                bolinha.move(RESOLUCAO * (x / 1000 * DIFICULDADE), barra.getP1().getY() - (bolinha.getCenter().getY() + r))
                pngbola.move(RESOLUCAO * (x / 1000 * DIFICULDADE), barra.getP1().getY() - (bolinha.getCenter().getY() + r))
                ajustado = True
            else:
                bolinha.move(RESOLUCAO * (x / 1000 * DIFICULDADE), RESOLUCAO * (y / 1000 * DIFICULDADE))
                pngbola.move(RESOLUCAO * (x / 1000 * DIFICULDADE), RESOLUCAO * (y / 1000 * DIFICULDADE))
        else:
            bolinha.move(RESOLUCAO * (x / 1000 * DIFICULDADE), RESOLUCAO * (y / 1000 * DIFICULDADE))
            pngbola.move(RESOLUCAO * (x / 1000 * DIFICULDADE), RESOLUCAO * (y / 1000 * DIFICULDADE))
            ajustado = False

        # Taxa de atualização (60hz)
        update(60)

    # Limpar tudo ao acabar
    if EXTRA:
        limpar(self3)
    lista = (bolinha, PLACAR, margem1, margem2, linha1, linha2, barra, pngbola, fundo_gramado)
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
    global PONTOS, _CAIU, EXTRA, FUNDO, RECORD, RECORD_EXTRA
    dificuldades_string = 'FÁCIL', 'NORMAL', 'DIFÍCIL'
    teclas = None

    # Condições de mensagem final
    if EXTRA and not _CAIU and PONTOS == 48:
        texto0 = texto_sem_ret(50, 35, False, '>>> PARABÉNS! VOCÊ VENCEU! <<<', fonte='courier')
    elif _CAIU:
        texto0 = texto_sem_ret(50, 35, False, '>>> VOCÊ DEIXOU A BOLINHA CAIR <<<', fonte='courier')
    else:
        texto0 = texto_sem_ret(50, 35, False, '>>> VOCÊ FINALIZOU O JOGO <<<', fonte='courier')
    texto1 = texto_sem_ret(50, 45, False, f'PONTUAÇÃO FINAL: {PONTOS}', fonte='courier')
    texto2 = texto_sem_ret(50, 55, False, f'DIFICULDADE: {dificuldades_string[DIFICULDADE - 1]}', fonte='courier')

    # Condições para Salvar o Record
    if EXTRA and PONTOS > int(RECORD_EXTRA[DIFICULDADE - 1][1]) \
            or not EXTRA and PONTOS > int(RECORD[DIFICULDADE - 1][1]):
        texto3 = texto_sem_ret(50, 65, False, '[ENTER/ESC] Salvar Recorde', fonte='courier')
    else:
        texto3 = texto_sem_ret(50, 65, False, '[ENTER/ESC] Para continuar', fonte='courier')

    while teclas not in ('Return', 'space', 'Escape', 'BackSpace'):
        teclas = tecla_menu()

    texto = (texto0, texto1, texto2, texto3)
    limpar(texto)
    formar_recorde()


# Função para a formação do recorde
def formar_recorde():
    global RECORD, EXTRA, RECORD_EXTRA, BOTOES

    # Variáveis da função
    primeiro, segundo, terceiro = None, None, None
    terminou, ultimo = False, False
    texto_primeiro, texto_segundo, texto_terceiro = None, None, None
    alfabeto = []

    # Cria as opções de letra do usuário
    for _ in range(65, 91):
        alfabeto.append(chr(_))
    for _ in range(97, 123):
        alfabeto.append(chr(_))
    alfabeto = tuple(alfabeto)

    if EXTRA and PONTOS > int(RECORD_EXTRA[DIFICULDADE - 1][1]) \
            or not EXTRA and PONTOS > int(RECORD[DIFICULDADE - 1][1]):

        # Criação de variáveis
        sel, x = 0, 38
        texto1 = texto_sem_ret(50, 45, True, 'INSIRA SEU NOME:', fonte='courier')
        letra = texto_sem_ret(x, 57, True, f'{alfabeto[sel]}', fonte='courier')
        ret = retangulo(x - 5, 60, x + 5, 60.5)
        ret.setOutline(BOTOES)

        while not terminou:

            teclas = tecla_menu()

            if teclas in ('Down', 'S', 's'):
                if sel != 51:
                    sel += 1
                else:
                    sel = 0
                letra = atualizar_letra(letra, alfabeto, sel, x)

            elif teclas in ('Up', 'W', 'w'):
                if sel != 0:
                    sel -= 1
                else:
                    sel = 51
                letra = atualizar_letra(letra, alfabeto, sel, x)

            elif teclas in ('Return', 'space'):
                if primeiro is None:
                    primeiro = alfabeto[sel]
                    texto_primeiro = texto_sem_ret(x, 57, True, f'{alfabeto[sel]}', fonte='courier')
                elif segundo is None:
                    segundo = alfabeto[sel]
                    texto_segundo = texto_sem_ret(x, 57, True, f'{alfabeto[sel]}', fonte='courier')
                elif terceiro is None:
                    terceiro = alfabeto[sel]
                    texto_terceiro = texto_sem_ret(x, 57, True, f'{alfabeto[sel]}', fonte='courier')
                    ultimo = True

                if not ultimo:
                    x += 12
                    sel = 0
                    ret = atualizar_ret(ret, x)
                    letra = atualizar_letra(letra, alfabeto, sel, x)
                else:
                    letra.undraw()
                    ret.undraw()
                    if EXTRA:
                        RECORD_EXTRA[DIFICULDADE - 1] = [f'{primeiro + segundo + terceiro}', PONTOS]
                    else:
                        RECORD[DIFICULDADE - 1] = [f'{primeiro + segundo + terceiro}', PONTOS]
                    salvar_record()
                    terminou = True

        teclas = None
        texto2 = texto_sem_ret(50, 70, False, '[ENTER/ESC] Para continuar')
        while teclas not in ('Return', 'space', 'Escape', 'BackSpace'):
            teclas = tecla_menu()

        lista = (letra, texto1, texto2, texto_primeiro, texto_segundo, texto_terceiro)
        limpar(lista)


# Função para Atualizar a Letra exibida
def atualizar_letra(letra, alfabeto, sel, x):
    letra.undraw()
    letra = texto_sem_ret(x, 57, True, f'{alfabeto[sel]}', fonte='courier')
    return letra


# Função para destacar a posição da letra
def atualizar_ret(ret, x):
    global BOTOES
    ret.undraw()
    ret = retangulo(x - 5, 60, x + 5, 60.5)
    ret.setOutline(BOTOES)
    return ret


# Função de Pause
def pausar():
    # Variáveis necessárias
    global ACABOU, PONTOS, _COMECOU, TECLAS_JOGO
    pausa, confirmou = True, False

    if not _COMECOU:
        texto0 = texto_sem_ret(50, 30, True, '>>> INICIE O JOGO <<<', color_rgb(0, 0, 0), 'courier')
    else:
        texto0 = texto_sem_ret(50, 30, True, '>>> JOGO PAUSADO <<<', color_rgb(0, 0, 0), 'courier')
    texto1 = texto_sem_ret(50, 40, True, '[ENTER] Jogar', color_rgb(0, 0, 0), 'courier')
    texto2 = texto_sem_ret(50, 50, True, '[ESC] Menu', color_rgb(0, 0, 0), 'courier')

    # Salvar os objetos do menu pausar para quando alguém selecionar uma opção
    objetos_do_pausar = texto0, texto1, texto2

    while pausa:

        teclas = tecla_menu()

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
            confirmou = True

        # Criar os objetos novamente caso volte ao Menu de pausa
        if confirmou and pausa:
            confirmou = False
            for objeto in objetos_do_pausar:
                objeto.draw(JOGO)


# Confirmar ao voltar p/ o Menu
def confirmar():
    # Variáveis necessárias
    global ACABOU, RESOLUCAO

    # Se o cliente estiver em uma calculadora
    if RESOLUCAO == 250:
        menor = False
    else:
        menor = True

    texto0 = texto_sem_ret(50, 30, menor, 'Você perderá seu progresso', color_rgb(0, 0, 0), 'courier')
    texto1 = texto_sem_ret(50, 40, menor, '[ENTER] Confirmar', color_rgb(0, 0, 0), 'courier')
    texto2 = texto_sem_ret(50, 50, menor, '[ESC] Voltar', color_rgb(0, 0, 0), 'courier')

    confirma = True

    while confirma:

        teclas = tecla_menu()

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
            return True


# Função de criação da Margem
def margem():
    global RESOLUCAO
    # Criar um retângulo de margem nas bordas
    self = retangulo2(1, 1, RESOLUCAO - 1, RESOLUCAO * (80 / 100))

    # Deletar a parte de baixo
    self2 = retangulo2(0, RESOLUCAO * (80 / 100), RESOLUCAO - 1, RESOLUCAO - 1, fundo=True)

    # Linhas
    self3 = criar_linha(2, 83, 98, 83)
    self4 = criar_linha(2, 96, 98, 96)

    return self, self2, self3, self4


# Função para criar Linhas (repetição de código)
def criar_linha(x1, y1, x2, y2):
    global FUNDO, JOGO, RESOLUCAO
    self = Line(Point(RESOLUCAO * (x1 / 100), RESOLUCAO * (y1 / 100)),
                Point(RESOLUCAO * (x2 / 100), RESOLUCAO * (y2 / 100)))
    self.setOutline(FUNDO)
    self.setWidth(5)
    self.setFill(FUNDO)
    self.draw(JOGO)
    return self


# Função para criar Retângulos específicos (repetição de código)
def retangulo2(x1, y1, x2, y2, fundo=False):
    global BOTOES, JOGO
    self = Rectangle(Point(x1, y1), Point(x2, y2))
    if fundo:
        self.setFill(BOTOES)
    self.setOutline(BOTOES)
    self.setWidth(10)
    self.draw(JOGO)
    return self


# Função para checar se bateu
def bateu(ball, x, y, barra, r):
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
    if EXTRA:
        d = DIFICULDADE * 0.1 * 0.25
    else:
        d = DIFICULDADE * 0.1
    # Fórmula para o raio da circunferência
    

    # Verificando o intervalo entre o ponto mais à esquerda da barra e o mais a direita da barra
    # (duas primeiras condições) e as duas últimas condições o intervalo do ponto mais e baixo e mais acima
    if p1x - r <= bx <= p2x + r and p1y - r <= by <= p2y + r:
        
        # Verificando se a bola está no topo da barra
        if p1y - r <= by <= p1y - r + (RESOLUCAO/100) and LATERAL:
            # Randomização do movimento da bola
            x -= XRANDOM
            y -= YRANDOM
            XRANDOM = randrange(1, 10) / 100
            YRANDOM = randrange(1, 10) / 100

            # Aumentar o x, que representa a velocidade da bola para os lados, com base na dificuldade
            if x > 0:
                x += d + XRANDOM
            else:
                x -= d + XRANDOM
            if y > 0:
                y += d + YRANDOM
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
    global ACABOU
    # Criação de variáveis repetitivas:
    # BolaX
    bx = ball.getCenter().getX()
    # BolaY
    by = ball.getCenter().getY()
    # Fórmula para o raio da circunferência

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
            # Se bateu embaixo ou se bateu em cima
            embaixo = c2y - RESOLUCAO * (1 / 100) <= by - r <= c2y and y < 0
            cima = RESOLUCAO * (1 / 100) + c1y >= by + r >= c1y and y > 0
            if embaixo or cima:
                y = -y
                bateu_no_cubo = True

            # Se bateu na direita ou se bateu na esquerda
            direita = c2x - RESOLUCAO * (1 / 100) <= bx - r <= c2x and x < 0
            esquerda = c1x + RESOLUCAO * (1 / 100) >= bx + r >= c1x and x > 0
            if direita or esquerda:
                if len(lista_cubos) != 1:
                    if bateu_no_cubo:
                        list_cubos2, bateu_no_cubo, condicao = pode_quinar(lista_cubos, cima, embaixo, esquerda,
                                                                           direita, c1x, c1y, c2x, c2y)

                        if condicao:
                            x = -x

                        if len(list_cubos2) == 2:
                            for indice in list_cubos2:
                                lista_cubos[indice].undraw()
                                lista_cubos.remove(lista_cubos[indice])

                    else:
                        bateu_no_cubo = True
                        x = -x
                else:
                    bateu_no_cubo = True

            if bateu_no_cubo:
                x, lista_cubos = bateu_cubo(cubo, lista_cubos, x)

    return x, y


def pode_quinar(lista_cubos, cima, embaixo, esquerda, direita, c1x, c1y, c2x, c2y):
    list_cubos = []
    indice = 0
    if cima and direita:
        for outro_cubo in lista_cubos:
            o1x = outro_cubo.getP1().getX()
            o1y = outro_cubo.getP1().getY()
            o2x = outro_cubo.getP2().getX()
            o2y = outro_cubo.getP2().getY()

            if c2x == o1x and c1y == o1y and c2y == o2y or c2x == o2x and c1y == o2y and c1x == o1x:
                list_cubos.append(indice)
                if len(list_cubos) == 2:
                    return list_cubos, False, True
            indice += 1

        if len(list_cubos) == 1:
            return list_cubos, True, False

    elif cima and esquerda:
        for outro_cubo in lista_cubos:
            o1x = outro_cubo.getP1().getX()
            o1y = outro_cubo.getP1().getY()
            o2x = outro_cubo.getP2().getX()
            o2y = outro_cubo.getP2().getY()

            if c2x == o2x and c1y == o2y and c1x == o1x or c1x == o2x and c1y == o1y and c2y == o2y:
                list_cubos.append(indice)
                if len(list_cubos) == 2:
                    return list_cubos, False, True
                indice += 1

        if len(list_cubos) == 1:
            return list_cubos, True, False

    elif embaixo and direita:
        for outro_cubo in lista_cubos:
            o1x = outro_cubo.getP1().getX()
            o1y = outro_cubo.getP1().getY()
            o2x = outro_cubo.getP2().getX()
            o2y = outro_cubo.getP2().getY()

            if c2x == o1x and c1y == o1y and c2y == o2y or c2x == o2x and c2y == o1y and c1x == o1x:
                list_cubos.append(indice)
                if len(list_cubos) == 2:
                    return list_cubos, False, True
            indice += 1

        if len(list_cubos) == 1:
            return list_cubos, True, False

    elif embaixo and esquerda:
        for outro_cubo in lista_cubos:
            o1x = outro_cubo.getP1().getX()
            o1y = outro_cubo.getP1().getY()
            o2x = outro_cubo.getP2().getX()
            o2y = outro_cubo.getP2().getY()

            if c1x == o2x and c1y == o1y and c2y == o2y or c2x == o2x and c2y == o1y and c1x == o1x:
                list_cubos.append(indice)
                if len(list_cubos) == 2:
                    return list_cubos, False, True
            indice += 1

        if len(list_cubos) == 1:
            return list_cubos, True, False

    return list_cubos, True, True


# Comandos repetitivos quando batia no Cubo
def bateu_cubo(cubo, lista_cubos, x):
    global PONTOS, DIFICULDADE
    PONTOS += 1
    atualizar_placar()
    cubo.undraw()
    lista_cubos.remove(cubo)
    x += DIFICULDADE * 0.1 * 0.25
    return x, lista_cubos


# Função de Criação e Atualização do Placar
def atualizar_placar():
    global PONTOS, PLACAR, FUNDO, EXTRA, ACABOU
    # Não deixa dar undraw caso não exista (0 pts)
    if PONTOS > 0:
        PLACAR.undraw()
    # Ganhou a fase extra
    if PONTOS == 48 and EXTRA:
        ACABOU = True
    # Fica dando undraw e draw
    PLACAR = texto_sem_ret(50, 90, True, f'PONTUAÇÃO ATUAL: {PONTOS}')
    PLACAR.setTextColor(FUNDO)
    return PLACAR


# Função de Criação dos Cubos
def cubos():
    global RESOLUCAO, BOTOES, JOGO, FUNDO
    JOGO.autoflush = True
    # Armazena todos os cubos na lista
    lista_cubos = []
    for y in range(2, 14 + 1, 6):
        for x in range(2, 96 + 1, 6):
            self = Rectangle(Point(RESOLUCAO * (x / 100), RESOLUCAO * (y / 100)),
                             Point(RESOLUCAO * ((x + 6) / 100), RESOLUCAO * ((y + 6) / 100)))
            cores = (color_rgb(9, 27, 38), color_rgb(37, 75, 89), color_rgb(84, 130, 140), color_rgb(201, 238, 242),
                     color_rgb(67, 96, 115), color_rgb(40, 70, 89))
            cor = cores[randrange(0, 4)]
            self.setOutline(BOTOES)
            self.setFill(cor)
            self.setWidth(2)
            self.draw(JOGO)
            lista_cubos.append(self)
            # Animação visual
            time.sleep(0.01)
    JOGO.autoflush = False
    return lista_cubos


def objetos_menu_principal(lista):
    for objeto in lista:
        objeto.draw(JOGO)


# Função para montar os objetos do Menu Principal
def montar_menu():
    global JOGO, RESOLUCAO

    img(50, 50, 'fundo.gif')

    op1 = retangulo(5, 35, 95, 20)
    op2 = retangulo(5, 50, 95, 40)
    op3 = retangulo(5, 65, 95, 55)
    op4 = retangulo(5, 80, 95, 70)
    op5 = retangulo(5, 95, 95, 85)

    # Função texto em prática
    texto0 = texto_sem_ret(50, 10, True, 'MENU PRINCIPAL')
    texto1 = texto_ret(op1, 'JOGAR')
    texto2 = texto_ret(op2, 'RESOLUÇÃO')
    texto3 = texto_ret(op3, 'DIFICULDADE')
    texto4 = texto_ret(op4, 'RECORDES')
    texto5 = texto_ret(op5, 'FASE EXTRA')

    return op1, op2, op3, op4, op5, texto0, texto1, texto2, texto3, texto4, texto5


# Menu Principal
def menu_principal():
    global FUNDO, RESOLUCAO, JOGO, MUDOU_RESOLUCAO, EXTRA, TECLAS_JOGO

    # Variáveis necessárias
    selecionado = 1
    selecionou, jogou = False, False

    # Monta o Menu
    op1, op2, op3, op4, op5, texto0, texto1, texto2, texto3, texto4, texto5 = montar_menu()

    # Salvá-los para quando o usuário retornar ao menu principal, eles serem mostrados novamente
    lista_dos_objetos = op1, op2, op3, op4, op5, texto0, texto1, texto2, texto3, texto4, texto5

    # Fix no atraso das teclas
    JOGO.bind_all('<KeyPress>', tecla_apertou)
    JOGO.bind_all('<KeyRelease>', tecla_soltou)
    TECLAS_JOGO = ''

    # Enquanto não selecionar nada, continua no Menu
    while not selecionou:

        teclas = tecla_menu()

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
                selecionou = jogo_principal()
                jogou = True
            elif selecionado == 2:
                selecionou = menu_resolucao()
            elif selecionado == 3:
                selecionou = menu_dificuldade()
            elif selecionado == 4:
                selecionou = menu_records()
            elif selecionado == 5:
                EXTRA = True
                selecionou = jogo_principal()
                # Ao voltar, ele seleciona o primeiro botão do Menu
                selecionado = 1
                jogou = True

        # ESC
        elif teclas in ('Escape', 'BackSpace'):
            exit()

        # Função para checagem do selecionado
        if selecionou and not MUDOU_RESOLUCAO and not jogou:
            # Mostrar novamente os objetos após o retorno do usuário
            selecionou = False
            objetos_menu_principal(lista_dos_objetos)

        elif selecionou:
            # Trocar as dimensões dos objetos do menu principal após a mudança de resolução
            selecionou, MUDOU_RESOLUCAO, jogou = False, False, False

            # Monta o Menu novamente
            op1, op2, op3, op4, op5, texto0, texto1, texto2, texto3, texto4, texto5 = montar_menu()

            # Atualizar a lista dos objetos com as dimensões corretas
            lista_dos_objetos = op1, op2, op3, op4, op5, texto0, texto1, texto2, texto3, texto4, texto5

        listaop = (op1, op2, op3, op4, op5)
        resetar_outline(listaop, selecionado)


# Inicia o Jogo
try:
    # Pega os Records de Sessões anteriores e depois executa o jogo
    records()
    menu_principal()
# Se a aba for fechada, o jogo finaliza
except GraphicsError:
    exit()
