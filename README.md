# GSA - Gerador de Senhas

GSA e um gerador de senhas simples feito em Python com interface grafica usando Tkinter.

O projeto permite escolher o tamanho da senha e quais tipos de caracteres serao usados: letras maiusculas, letras minusculas, numeros e caracteres especiais.

## Funcionalidades

- Interface grafica simples e leve
- Geracao de senhas com 4, 8 ou 12 caracteres
- Opcoes para incluir:
  - Letras maiusculas
  - Letras minusculas
  - Numeros
  - Caracteres especiais
- Executavel para Windows gerado com PyInstaller
- Codigo separado entre interface e logica de geracao

## Estrutura do projeto

```text
GSA_SENHAS/
├── GSA.py              # Interface grafica Tkinter
├── gerador.py          # Logica de geracao de senhas
├── GSA.spec            # Configuracao do PyInstaller
├── GSA_icone.ico       # Icone do executavel
├── GSA_icone.png       # Icone em imagem
├── dist/
│   └── GSA.exe         # Executavel gerado
└── build/              # Arquivos temporarios do PyInstaller
```

## Como usar pelo executavel

Abra o arquivo:

```text
dist/GSA.exe
```

Depois escolha:

1. O tamanho da senha
2. Os tipos de caracteres
3. Clique em `GERAR`

A senha sera exibida na area de resultado.

## Como executar pelo Python

Tenha o Python instalado e rode:

```powershell
python GSA.py
```

## Como gerar o executavel

Instale o PyInstaller:

```powershell
pip install pyinstaller
```

Depois gere o executavel usando o arquivo `.spec`:

```powershell
pyinstaller GSA.spec
```

O arquivo atualizado sera criado em:

```text
dist/GSA.exe
```

## Tecnologias usadas

- Python
- Tkinter
- PyInstaller

## Licenca

Este projeto esta sob a licenca MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
