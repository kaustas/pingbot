### Telegram ping bot
Ping hosts defined in config.yaml file. Send notification to telegram chat when host is offline.

#### Docker
For build used small custom Python images: jfloff/alpine-python

#### Configuration
Need to define:
 - botid - Bot id from BotFather
 - userid - Private chat id with bot
 - hosts - list of hosts to ping

Two ways to define configs:
##### config.yaml file
````yaml
botid: 123456789:abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz
userid: 123456789
hosts:
  - "8.8.8.8:Google DNS"
  - "77.88.8.8:Yandex DNS"
````

##### docker-compose.yaml and BOT_ENV OS environment variable
````yaml
version: '3.7'
services:
  bot:
    container_name: pingbot
    image: pingbot
    restart: always
    environment:
      BOT_ENV: |
        botid: 123456789:abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz
        userid: 123456789
        hosts:
          - "8.8.8.8:Google DNS"
          - "77.88.8.8:Yandex DNS"
````
> Code try to load BOT_ENV first then config.yaml