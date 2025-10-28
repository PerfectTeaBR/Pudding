# What is GalleryOfEmbeds?
GalleryOfEmbeds is like a little helper to help beginners on discord.py!

# How to use
To use GalleryOfEmbeds follow the steps below:
---
 1. install discord.py
 ```bash
pip install discord.py
```
2. import Discord lib
```python
import discord
from discord.ext import commands
```
3. Configure Bot
```python
intents = discord.Intents.default()
intents.members = True
intents.members = True

bot = commands.Bot(command_prefix='+', intents=intents)

```
4. use the bot's main event to make her online
```python
@bot.event
async def on_ready():
    print(f"GalleryOfEmbed's are ready to use!! {bot.user}")
    await bot.tree.sync()
```