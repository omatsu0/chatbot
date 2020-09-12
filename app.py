from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

@app.route("/")
def test():
  return "OK"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == "ありがとう":
        reply_message = "さぎ"
    elif event.message.text == "さよなら":
        reply_message = "いおん"
    elif event.message.text == "こんにちは":
        reply_message = "ん"
    elif event.message.text == "こんばんわ":
        reply_message = "に"
    elif event.message.text == "魔法の言葉で楽しい仲間が":
        reply_message = "ぽぽぽぽ～ん"
    elif event.message.text == "おはよう":
        reply_message = "なぎ"
    elif event.message.text == "いただき":
        reply_message = "まうす"
    elif event.message.text == "いってきます":
        reply_message = "かんく"
    elif event.message.text == "ただいま":
        reply_message = "んぼう"
    elif event.message.text == "ごちそうさま":
        reply_message = "うす"
    elif event.message.text == "おやすみなさい":
        reply_message = "さい"
    elif event.message.text == "すてきな言葉でゆかいな仲間が":
        reply_message = "ぽぽぽーん"
    else:
        reply_message = event.message.text

    line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_message))


if __name__ == "__main__":
    app.run()