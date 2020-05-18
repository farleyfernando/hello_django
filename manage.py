#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello_django.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Não foi possível importar o Django. Tem certeza de que está instalado e  "
            "disponível na sua variável de ambiente PYTHONPATH? Você "
            "Não esqueça de ativar um ambiente virtual"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
