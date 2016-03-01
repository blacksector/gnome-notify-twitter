# gnome-notify-twitter
Gnome Notifications Twitter - Get direct Gnome Notifications from Twitter using Twitter User Stream.

The app is not 100% complete, its a quick hack I made up just for small things for example favorites, unfavorites, retweet (undo of a retweet is not working), and direct message notifications.

### Setting up your keys

First you will need to create an app and generate access tokens. Here is how to do it easily: http://iag.me/socialmedia/how-to-create-a-twitter-app-in-8-easy-steps/


### Setting up the program

First, lets get our required modules installed, install using `pip` its the quickest and easiest. Here is how to install pip:
Windows: http://stackoverflow.com/a/12476379
Linux (You should have it installed but here goes): http://python-packaging-user-guide.readthedocs.org/en/latest/install_requirements_linux/
Mac OS X: http://stackoverflow.com/a/18947390

Next, install the following:
https://github.com/sixohsix/twitter
Then: pip install pygobject

Next, change these lines on the gnomeNotify.py:
```python
token = "Access Token Here"
token_key = "Access Key Here"
con_secret = "Consumer Key Here"
con_secret_key = "Consumer Secret Here"
```

Next just run the script and it should automatically start to identify new likes or retweets and messages and will forward them to your Gnome notification tray :)

### Contributions
Please feel free to send in any pull requests you feel is towards something better :)
