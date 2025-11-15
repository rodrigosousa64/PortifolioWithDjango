import subprocess
import shlex
import os


def iniciar_gunicorn():
    """
    Inicia o servidor Gunicorn para a aplicação WSGI.
    """
    # O comando a ser executado
    comando = "waitress-serve --port=80 core.wsgi:application"

    # Opcional: Adicionar argumentos extras, por exemplo, para definir a porta
    # comando = "gunicorn --bind 0.0.0.0:8000 core.wsgi:application"

    print(f"Iniciando Gunicorn com o comando: {comando}")

    # Divide o comando em uma lista de argumentos, o que é mais seguro
    # shlex.split lida corretamente com aspas e espaços
    args = shlex.split(comando)

    try:
        # Executa o comando no terminal.
        # `subprocess.run` é recomendado para comandos simples e espera a conclusão.
        # Para um servidor que roda continuamente, pode ser melhor usar `subprocess.Popen`
        # se você precisar controlar o processo (parar, reiniciar) de dentro do Python.
        # No entanto, para simplesmente iniciar e deixar rodar, `run` funciona.

        # Usando subprocess.run com shell=False (padrão e mais seguro)
        # capture_output=True redireciona stdout e stderr, que podem ser úteis para log
        subprocess.run(args, check=True, capture_output=True, text=True)

    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando Gunicorn: {e.stderr}")
    except FileNotFoundError:
        print(
            "Erro: Gunicorn não encontrado. Certifique-se de que está instalado e no seu PATH."
        )
    except KeyboardInterrupt:
        print("\nServidor Gunicorn interrompido pelo usuário.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    # Garante que o script esteja rodando no diretório correto, se necessário
    # os.chdir("/caminho/para/seu/projeto")
    iniciar_gunicorn()
