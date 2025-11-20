import subprocess
import shlex
import os
import sys
import waitress

# Garante que o interpretador Python do venv seja usado
PYTHON_EXEC = sys.executable


def iniciar_waitress():
    """
    Inicia o servidor Waitress para a aplicação Django, usando o
    módulo Python para garantir que ele seja encontrado no venv.
    """

    # 1. Configurações baseadas em variáveis de ambiente ou valores padrão
    WSGI_APP = os.getenv("WSGI_APP", "core.wsgi:application")
    PORTA = os.getenv("PORT", "8000")
    THREADS = os.getenv("THREADS", "4")

    # 2. O comando completo (AGORA CORRIGIDO)
    # Chama o interpretador Python do venv para executar o módulo 'waitress'
    comando = f"{PYTHON_EXEC} -m waitress --threads={THREADS} --port={PORTA} {WSGI_APP}"

    print(f"--- 💻 Iniciando Waitress ---")
    print(f"Comando: {comando}")
    print(f"Aplicação WSGI: {WSGI_APP}")
    print(f"Threads: {THREADS}")
    print(f"Porta: {PORTA}")
    print(f"-----------------------------")

    args = shlex.split(comando)

    # Verifica se o pacote 'waitress' está disponível antes de rodar
    try:
        import waitress
    except ImportError:
        print("\n❌ ERRO FATAL: O pacote 'waitress' não está instalado.")
        print("Execute: pip install waitress==3.0.2")
        return

    try:
        subprocess.run(args, check=True, text=True)

    except subprocess.CalledProcessError as e:
        print(f"\n❌ ERRO: Waitress encerrou com código {e.returncode}.")
    except FileNotFoundError:
        # Este erro agora é menos provável graças à correção,
        # mas pode acontecer se o sys.executable falhar por algum motivo
        print("\n❌ ERRO CRÍTICO: Interpretador Python não encontrado.")
    except KeyboardInterrupt:
        print("\n\n✅ Servidor Waitress interrompido pelo usuário.")
    except Exception as e:
        print(f"\n❌ ERRO INESPERADO: Ocorreu um erro: {e}")


if __name__ == "__main__":
    iniciar_waitress()
