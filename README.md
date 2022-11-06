# SecretSanta

If you organize a "Secret Santa" event, this script is for you !

Simply edit the ```config.yaml``` to your need and then execute it with the command :

```
python3 secrect_santa.py <config.yaml>
```

An email will be sent to every specified members with a randomly picked target before deleting the sent items from your mailbox (to prevent you from cheating :-P).

*For now the script is only compatible with gmail account as the Sender's mail address.*

## Configuration

Follow this link to create an Access Token for your gmail account :
https://support.google.com/accounts/answer/185833

If you are French, the "Sent items" folder is named :  "[Gmail]/Messages envoy&AOk-s"
