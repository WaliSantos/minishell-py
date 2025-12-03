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
os.read(): busca os bytes que chegam a um descritor de arquivo (como a entrada do teclado) e entrega esses bytes ao programa exatamente como estão.

os.write(): envia bytes do programa para um descritor de arquivo (como a tela ou a saída de erro) exatamente como foram fornecidos.

os.fork(): responsável por criar um novo processo filho.

os.execvp(): substitui o processo filho pelo programa solicitado pelo usuário.

os.wait(): utilizada pelo processo pai para aguardar o término do processo filho.

## Exemplos de comandos testados e suas saídas. 
echo
```bash
mini-shell> echo Ola mundo
Ola mundo
```

ls
```bash
mini-shell> ls
README.md  arquivo.txt  main.py
```

cat
```bash
mini-shell> cat arquivo.txt
Este é o conteúdo do arquivo.txt.
```

## Limitações conhecidas da implementação. 
A principal limitação que ocorreu na implementação foi o uso do WSL (Windows Subsystem for Linux) no Windows. O WSL implementa um Linux “traduzido” para Windows — e isso traz várias limitações importantes, especialmente para programas que usam fork, execvp, etc. Dentre as limitações, pode-se destacar:

1. fork() é caro e mais lento que no Linux real. Embora o WSL suporte fork(), ele não usa o mesmo mecanismo Copy-on-Write nativo do Linux, precisa sincronizar estados com o Windows, cria custos adicionais na camada de tradução. 

2. execvp() não é tão fiel quanto em Linux nativo. Embora funcione para um mini shell simples, mas há overhead na criação de novos processos, o mapeamento de permissões/arquivos não é 100% POSIX, além de algumas flags de execução não existirem (por exemplo, Linux capabilities, namespaces, setuid, etc).

3. Devido ao fato do processo Linux no WSL não ser um processo Windows nativo, isso causa latência maior em syscalls.

## Vídeo curto demonstrando o uso do shell (máximo 5 min).
O vídeo está anexado nos arquivos do repositório.
