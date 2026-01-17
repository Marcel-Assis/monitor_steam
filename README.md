🎮 Monitor de Jogos Gratuitos (Steam)

Este projeto automatiza a busca por jogos que estão com 100% de desconto na Steam. Ele verifica as promoções atuais e me envia uma notificação direta no Telegram sempre que encontra um jogo novo que ficou gratuito (R$ 0,00).
🚀 O que o projeto faz

    Busca Inteligente: Consulta a API do CheapShark para encontrar jogos gratuitos na Steam.

    Filtro Anti-Erro: Verifica se o preço é realmente zero para evitar falsas promoções.

    Memória (SQLite): Utiliza um banco de dados local para salvar os jogos já encontrados. Assim, ele só me avisa sobre as novidades, evitando notificações repetidas.

    Notificação no Celular: Integrado com um Bot do Telegram que me envia o nome do jogo e o link direto para resgate.

🛠️ Tecnologias Utilizadas

    Python: Linguagem principal do projeto.

    SQLite: Para persistência de dados e histórico.

    Telegram Bot API: Para o sistema de notificações em tempo real.

    Requests: Para comunicação com APIs externas.

📋 Como utilizar

    Ative o ambiente virtual: venv\Scripts\activate

    Instale as dependências: pip install requests python-dotenv

    Configure o seu TOKEN e CHAT_ID do Telegram no script.

    Execute a aplicação:
    Bash

    python main.py

    O script verificará as promoções e enviará uma mensagem no seu Telegram confirmando o status da busca.
