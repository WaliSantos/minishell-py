# Mini Shell Py
## Como Compilar e rodar? 

Para rodar o Mini shell, execute os seguintes passos.

* Caso não esteja em um sistema Linux, será necessário rodar um ambiente Linux dentro do Windows. O WSL (Windows Subsystem for Linux) permite que utilizemos o fork(), execvp() e processos Linux dentro do Windows. É possível também usar uma máquina virtural, portanto fique a vontade para escolher o que achar mais adequado. Todavia, o passo a passo abaixo será o suficiente para rodar o mini shell de forma prática e rápida:
    1. Abra um terminal no vscode e execute o comando abaixo:

        ```bash
        wsl --install 
        ``` 
    2. Reinicie o sistema;
    3. Após reiniciar, abra novamente um terminal no vscode, clique na seta pra baixo, ao lado do símbolo "+", e procure por ubuntu (wsl).
    4. Defina o usuário e senha;
    5. Instale o python: 
        ```bash
        sudo apt update
        sudo apt install python3 python3-pip -y
 
        ```
    6. Execute, logo em seguida o comando:
        ```bash
        python3 main.py
        ```

## Quais chamadas ao sistema foram utilizadas?

## Exemplos de comandos testados e suas saídas. 

## Limitações conhecidas da implementação. 

## Vídeo curto demonstrando o uso do shell (máximo 5 min).