import subprocess
import shlex
import os


def iniciar_gunicorn():

    PORTA = os.getenv("PORT", "8000")
    WSGI_APP = "core.wsgi:application"
    WORKERS = os.getenv("WORKERS", "1")
    # O comando a ser executado
    comando = f"gunicorn {WSGI_APP} --workers {WORKERS} --bind 0.0.0.0:{PORTA}"



    print(f"Iniciando Gunicorn com o comando: {comando}")

    args = shlex.split(comando)

    try:
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
  
    iniciar_gunicorn()
