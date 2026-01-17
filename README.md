# 🎮 Monitor de Jogos Gratuitos (Steam)

Este projeto automatiza a busca por jogos que estão com **100% de desconto** na Steam. Ele verifica as promoções atuais e envia uma notificação direta no Telegram sempre que encontra um jogo novo que ficou gratuito (R$ 0,00).

## 🚀 O que o projeto faz

- **Busca Inteligente:** Consulta a API do CheapShark para encontrar jogos gratuitos na Steam.
- **Filtro Anti-Erro:** Verifica se o preço é realmente zero para evitar falsas promoções.
- **Memória (SQLite):** Utiliza um banco de dados local para salvar os jogos já encontrados. Assim, ele só me avisa sobre as novidades, evitando notificações repetidas.
- **Notificação no Celular:** Integrado com um Bot do Telegram que envia o nome do jogo e o link direto para resgate.

## 🛠️ Tecnologias Utilizadas

- **Python:** Linguagem principal do projeto.
- **SQLite:** Para persistência de dados e histórico de promoções.
- **Telegram Bot API:** Para o sistema de notificações em tempo real.
- **Requests:** Para comunicação com APIs externas.

## 📋 Como utilizar

**🤖 Configurando o seu Bot no Telegram**

- Para receber as notificações, você precisará criar o seu próprio bot:

- Crie o Bot: Procure o @BotFather no Telegram e use o comando /newbot. Siga as instruções para receber o seu API Token.

- Inicie o Bot: Procure pelo bot que você acabou de criar e clique em "Começar" ou "Start".

- Obtenha seu ID: Procure o bot @userinfobot e envie uma mensagem para descobrir o seu ID numérico.

- Configure no Código: Insira o Token e o seu ID nas variáveis correspondentes dentro do arquivo main.py.

1. **Ative o ambiente virtual:**

   ```bash
   venv\Scripts\activate

   ```

2. **Instale as dependências::**

   ```bash
   pip install requests python-dotenv

   ```

3. **Configuração: Edite o arquivo main.py com o seu TOKEN e CHAT_ID do Telegram.**
4. **Execução**
   ```bash
   python main.py
   ```

O script verificará as promoções e enviará uma mensagem no Telegram confirmando se novos jogos foram encontrados ou se o sistema está atualizado.
