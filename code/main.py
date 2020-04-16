from telegram import Bot
from pythonping import ping
import sys
import time
import yaml
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(mn)s][%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("output.log"),
        logging.StreamHandler()
    ]
)

class address:

    def __init__(self, address, comment):

        self.address = address
        self.comment = comment
        self.status = True


def init():
    global bot, userid


    with open('./volume/config.yaml') as f:
        try:
            docs = yaml.load_all(f, Loader=yaml.FullLoader)

            for doc in docs:
                for k, v in doc.items():
                    if k == "botid":
                        bot = Bot(v)
                    elif k == "userid":
                        if v == 123456789:
                            logging.error("Wrong config.yaml data. Update config with correct botid and userid", extra={'mn': 'YAML'})
                            sys.exit()
                        else:
                            userid = v
                    elif k == "hosts":
                        set_hosts(v)

        except yaml.YAMLError as exc:
            logging.error(exc, extra={'mn': 'YAML'})


def set_hosts(hosts):
    global hosts_list
    hosts_list = []

    for item in hosts:
        ac = item.split(":")
        hosts_list.append(address(ac[0], ac[1]))


def send_message(message):
    bot.send_message(userid, message, parse_mode='HTML',
                     disable_web_page_preview=True)


def ping_host(address):
    if ping_url(address.address):
        if not address.status:
            address.status = True
            send_message(address.comment + " is up again")
            logging.info(address.comment + " is alive", extra={'mn': 'ping_host'})
    else:
        if (address.status):
            address.status = False
            send_message(address.comment + " is down")
            logging.info(address.comment + " is down", extra={'mn': 'ping_host'})


def ping_url(url):
    i = 0

    try:
        response_list = ping(url)

        for response in response_list:
            if (not response.success):
                i += 1

        if (i == 4):
            return False
        else:
            return True

    except Exception as e:
        send_message(str(e))
        logging.error(e, extra={'mn': 'ping_host'})



def main():
    init()
    logging.info("Pingbot started", extra={'mn': 'main'})
    send_message("Pingbot started")
    while True:

        for host in hosts_list:
            ping_host(host)

        time.sleep(30)


if __name__ == '__main__':
    main()
