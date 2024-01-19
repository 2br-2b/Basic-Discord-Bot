# "Basic" Discord Bot (BDB)

<a href="https://discord.gg/a28VUkyrxp"><img src="https://raw.githubusercontent.com/2br-2b/2br-2b/main/Join%20our%20discord%20icon.svg" alt= "Join our Discord!" width="280" ></a>

## About

This started out as part of [StoryBot](https://discord.com/application-directory/623698680574115841), a discord bot I wrote. I want to contribute back to the open source community, but I don't want someone to just yoink my code and just rip off all my work. This is my compromise: while StoryBot itself is not open source, it's framework is. Feel free to take this code and create your own Discord bots!

This bot is not meant for beginners. While a beginner could use it, this includes a lot of concepts (like translations, cogs, etc.) which might make it hard to get started. If you just wnat to make a simple discord bot, discord.py's [quickstart guide](https://discordpy.readthedocs.io/en/latest/quickstart.html) can help you create a simple response bot.

If you create a discord bot using this framework, let me know! Also, feel free to contribute back if you have any ways this could be improved.

## How to

To set up this bot, first, run these commands to set up a python virtual environment:

```bash
python -m venv ./.venv
```

Then, to activate the virtual environment, run this command:

- On Windows, `.venv/Scripts/Activate.ps1`. If you get an error about running scripts being disabled, you'll need to run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` first
- On MacOS or Unix, `.venv/scripts/activate`

You will need to run this command every time before you run the bot or update the dependencies

Next, after activating the virtual environment, you'll need to install the dependencies:

```bash
pip install -r requirements.txt
```

Next, you'll need to set up the bot's configuration. Copy `config.example.py` to `config.py` and fill in the values.

Finally, after all this setup and after you activate the virtual environment, you can run this to start the bot:

```bash
# Make sure to activate the virtual environment first!
python main.py
```

## Resources

Here are some good resources to learn more:

- [The discord.py docs](https://discordpy.readthedocs.io/en/latest/)
- [The official discord.py server](https://discord.gg/r3sSKJJ)
- [AbstractUmbra's guides](https://about.abstractumbra.dev/dpy)
- [thegamecrack's translation demo](https://github.com/thegamecracks/discord.py-i18n-demo)