### Telegram ping bot
Ping hosts defined in config.yaml file. Send notification to telegram chat when host is offline.

##### Config.yaml
Before run in docker update config.yaml with your botid and userid:
````yaml
botid: 123456789:abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz
userid: 123456789
hosts:
  - "8.8.8.8:Google DNS"
  - "77.88.8.8:Yandex DNS"
````