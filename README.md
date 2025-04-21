# TECH_flask_chat
Flask App as an educational lab for AI and IoT.

Aplicação Flask como laboratório didático para IA e IoT.

With many thanks to Miguel Grinberg (https://github.com/miguelgrinberg) for his Flask Mega-Tutorial (https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

AI-aided development.

___

## Aplicação inicial
O objetivo desta versão é apresentar o framework Flask.

Esta aplicação consiste em dois clientes de chat: usuario e atendente e cada cliente um mantém seu próprio log de conversa (`usuario.log` e `atendente.log`, respectivamente). No entanto, ainda não se conversam de fato.

### Recursos:
* Framework Flask: `flask`
* Para expansão modular: Blueprint e Jinja2
* Uso de variáveis de ambiente: `python-dotenv`

## Na primeira vez que usar este pacote
* Faça download do repositório.
* Descompacte o arquivo em uma pasta no seu computador, **DE FORMA ORGANIZADA**.
* Na pasta flask_app, clique com o botão direito do mouse e selecione `Mostrar mais opções` --> `Abrir com Code` (opção de menu com o ícone do VSCode).
* Crie e configure um ambiente virtual
    * Abra um terminal no VSCode e execute:
    * `python.exe -m venv .venv`
    * `.venv\Scripts\Activate`
    * Isso ativa o ambiente virtual e o prompt deverá mudar, passando a mostrar `(.venv)` no início da linha. Digite:
        * `python.exe -m pip install --upgrade pip`
        * `pip install flask python-dotenv`
        Agora você pode executar a aplicação:
        * `flask run`

## Quando usar nas próximas vezes, digite:
* `.venv\Scripts\Activate`
* `flask run`

___

## ramificação 'sync' - arquivo de log unificado
A partir desta versão, os clientes (usuario e atendente) conversam um com o outro, por meio do log de conversa unificado (arquivo `chat.log`). No entanto, a conversa ainda não acontece em tempo real.

O botão `Enviar` foi modificado para `Enviar/Atualizar`: ao ser pressionado sem a digitação de uma mensagem, fará a atualização da conversa. Quando houver alguma coisa digitada na caixa de texto, a mensagem será enviada.

Para implementar a comunicação em tempo real, devem ser usadas técnicas de programação assíncrona.

___

## ramificação 'realtime' - sessões de chat e atualização em tempo real
**Major update!**
1. Chat atualizado em tempo real nos dois clientes, com a introdução de:
- Recursos de programação assíncrona
    * JavaScript
    * WebSockets
- ID de sessão de chat
- Logs de chat por sessão
    * A versão `sync` mantinha um log unificado "eterno" na pasta `flask_chat/logs`
    * A partir desta versão, os logs de cada sessão têm a marcação de data/hora do início da sessão no nome do arquivo.
    * Nomenclatura: `chat_YYYYMMDD-hhmmss.log`
        * YYYY - ano; MM - mês; DD - dia
        * hh - hora; mm - minuto; ss - segundo

2. Cada cliente é aberto em uma janela separada.

3. O botão `Enviar/Atualizar` voltou a ser exibido como `Enviar/Atualizar`, pois não é mais necessário usar o artifício de pressioná-lo sem a digitação de uma mensagem para atualizar a conversa.

4. Ajuste na arquitetura: `routes.py` foi movido para a pasta `app` (boas práticas)

### Requisito adicional: 
`flask_socketio` (instale usando `pip install`)
