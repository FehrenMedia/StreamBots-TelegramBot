from telegram.ext import *
from telegram import Update
import paho.mqtt.client as mqtt
import json
import os

mqtt_hostname = os.environ['mqtt_hostname']
mqtt_username = os.environ['mqtt_username']
mqtt_password = os.environ['mqtt_password']

telegram_token = os.environ['telegram_token']
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.


client = mqtt.Client()
client.on_connect = on_connect

client.username_pw_set(username=mqtt_hostname, password=mqtt_password)
client.connect(mqtt_hostname, 1883, 60)


def say(update, context):
    print(f'message\n:{update.message}')
    text = update.message.text.split("/say ")[1]
    update.message.reply_text(f'OK {update.effective_user.first_name}, dann sag ich jetzt "{text}"')
    print(f'user:{update.message.chat.username}')
    print(f'text:{text}')
    client.publish("smartBots/tts/say", json.dumps({"text": text, "lang": "de"}))


def main():
    print("bot starting...")
    updater = Updater(telegram_token)

    updater.dispatcher.add_handler(CommandHandler('say', say))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()