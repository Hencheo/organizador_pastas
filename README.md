# 📂 Organizador de Pastas Automático

Este é um script Python simples, mas poderoso, projetado para organizar o caos em suas pastas. Ele varre um diretório específico, identifica as extensões dos arquivos presentes e os move automaticamente para pastas correspondentes.

## 🚀 Funcionalidades

- **Identificação Inteligente**: O script detecta automaticamente todos os tipos de arquivos presentes na pasta.
- **Criação de Pastas Dinâmica**: Cria pastas nomeadas de acordo com as extensões (ex: `.pdf`, `.jpg`, `.mp4`).
- **Organização em Segundos**: Move centenas de arquivos para seus devidos lugares instantaneamente.
- **Interface Minimalista**: Basta inserir o caminho da pasta e deixar o script trabalhar.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Biblioteca `os`**: Para manipulação de caminhos e arquivos.
- **Biblioteca `shutil`**: Para operações de movimentação de pastas.
- **Biblioteca `time`**: Para controle de fluxo.

## 📖 Como Usar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório ou baixe o arquivo `app.py`.
3. Execute o script via terminal:
   ```bash
   python app.py
   ```
4. Quando solicitado, cole o **caminho completo** da pasta que deseja organizar.
5. O script irá:
   - Analisar os arquivos.
   - Criar as pastas necessárias.
   - Mover os arquivos para as pastas criadas.

## 📁 Exemplo de Estrutura

**Antes:**
```text
C:/Downloads/
  ├── ferias.jpg
  ├── relatorio.pdf
  ├── aula_01.mp4
  └── notas.txt
```

**Depois:**
```text
C:/Downloads/
  ├── jpg/
  │   └── ferias.jpg
  ├── pdf/
  │   └── relatorio.pdf
  ├── mp4/
  │   └── aula_01.mp4
  └── txt/
      └── notas.txt
```

## ⚠️ Observações

- O script atualmente identifica extensões a partir dos arquivos físicos presentes no diretório.
- Certifique-se de que o caminho digitado seja válido e que você tenha permissões de escrita na pasta.

---
Desenvolvido como parte do aprendizado de automação com Python. 🐍✨
