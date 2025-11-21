# mini shell em python

import os 
import sys

def main():
    while True:
        os.write(1, b"mini-shell> ") # escreve o prompt na saída padrão
        comando = os.read(0, 1024).decode().strip() # lê o comando da entrada padrão
        if comando == "exit":
            os.write(1, b"Valeu pela interacao! Mini Shell finalizado!\n")
            break
        
        args = comando.split() # divide o comando em uma lista de argumentos
        if len(args) == 0: # se nenhum comando foi digitado, recomeça o loop
            continue

        pid = os.fork() # Duplica o processo atual
        # Explicação dos processos existentes:
        # Processo pai: pid > 0. Função do pai: 
        #       - esperar o filho terminar,
        #       - continuar o loop para ler o próximo comando
        # Processo filho: pid == 0. Função do filho:
        #       - executar o comando digitado pelo usuário
        #       - Deve terminar após a execução do comando

        if pid == 0: # processo filho
            try:
                os.execvp(args[0], args) # substitui o processo filho pelo comando
            except FileNotFoundError:
                os.write(2, f"mini-shell: comando não encontrado: {args[0]}\n".encode())
            sys.exit(1) # Se execvp falhar, termina o processo filho com código de erro
        
        else: # processo pai
            os.wait() # espera o processo filho terminar




main()