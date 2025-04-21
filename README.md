# Jogo do Galo (Tic-Tac-Toe) em Python

Este é um simples jogo do galo (Tic-Tac-Toe) implementado em Python. O jogador compete contra o computador (CPU) que faz jogadas aleatórias.

## Funcionalidades Principais

* Tabuleiro interativo exibido no terminal.
* Jogada do jogador com validação de entrada.
* Jogada da CPU aleatória.
* Verificação automática de vitória (linhas, colunas e diagonais).
* Detecção de empate.
* Opção de jogar novamente.
* Cores para melhor visualização (requer a biblioteca `colorama`).

## Pré-requisitos

* **Python 3.x** instalado no seu sistema.
* **Biblioteca `colorama`** instalada. Você pode instalá-la usando pip:
    ```bash
    pip install colorama
    ```

## Como Usar

1.  **Salve o código:** Salve o código Python fornecido em um arquivo com a extensão `.py` (por exemplo, `jogo_galo.py`).

2.  **Execute o jogo:** Abra o terminal ou prompt de comando, navegue até o diretório onde você salvou o arquivo e execute o script usando o comando:
    ```bash
    python jogo_galo.py
    ```

3.  **Siga as instruções:** O jogo exibirá o tabuleiro e pedirá que você digite a linha e a coluna desejada para sua jogada (representada por "X"). A CPU fará suas jogadas aleatoriamente (representada por "O").

4.  **Fim do jogo:** O jogo terminará quando um jogador vencer ou houver um empate (todas as casas forem preenchidas). Uma mensagem indicará o resultado.

5.  **Jogar novamente:** Após o fim de uma partida, o jogo perguntará se você deseja jogar novamente. Digite "s" para jogar outra partida ou "n" para sair.

## Explicação do Código

* **Variáveis Globais:**
    * `jogar_novamente`: Controla o loop principal do jogo.
    * `numero_jogadas`: Mantém o controle do número de jogadas realizadas.
    * `vez_do_jogador`: Indica de quem é a vez de jogar (1 para CPU, 2 para Jogador).
    * `maximo_jogadas`: Define o número máximo de jogadas possíveis (9).
    * `vencedor`: Armazena o símbolo do vencedor ("X" ou "O") ou "n" se não houver vencedor.
    * `tabuleiro`: Uma lista de listas representando o tabuleiro do jogo.

* **`exibir_tabuleiro()`:** Limpa a tela do terminal e imprime o estado atual do tabuleiro com as coordenadas de linha e coluna. Utiliza a biblioteca `colorama` para colorir o número de jogadas.

* **`jogada_jogador()`:** Permite que o jogador insira a linha e a coluna para sua jogada. Valida a entrada do usuário e verifica se a posição escolhida já está ocupada.

* **`jogada_cpu()`:** Faz uma jogada aleatória para a CPU em uma posição vazia do tabuleiro.

* **`verificar_vitoria()`:** Verifica se há um vencedor, examinando todas as linhas, colunas e diagonais do tabuleiro. Retorna o símbolo do vencedor ou "n" se não houver.

* **`reiniciar_jogo()`:** Reseta o tabuleiro e as variáveis de controle para iniciar uma nova partida.

* **Loop Principal (`while jogar_novamente.lower() == "s":`)**: Controla o fluxo geral do jogo, permitindo que o jogador jogue várias partidas seguidas. O loop interno (`while True:`) executa uma única partida até que haja um vencedor ou um empate.

## Observações

* A lógica da CPU é puramente aleatória, o que significa que ela não possui nenhuma estratégia para vencer.
* A biblioteca `colorama` é usada para adicionar cores ao texto no terminal, o que pode melhorar a experiência do usuário. Se a biblioteca não estiver instalada, o código ainda funcionará, mas sem as cores.

Divirta-se jogando!