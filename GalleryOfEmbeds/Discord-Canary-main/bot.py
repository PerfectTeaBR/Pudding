import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# 1. Carregar o Token do .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    print("ERRO: O Token do Discord não foi carregado. Verifique seu arquivo .env")
    exit()

# 2. Configurar as INTENTS (Intenções)
# Você deve habilitar as Intents necessárias no Portal do Desenvolvedor do Discord.
intents = discord.Intents.default()
intents.message_content = True # Necessário para ler o conteúdo das mensagens (comandos '!')
intents.members = True # Necessário para funcionalidades que envolvem membros

# 3. Criar a instância do Bot
# O '!' é o prefixo para comandos de texto (como !ping)
bot = commands.Bot(command_prefix='!', intents=intents)

# 4. Evento de Inicialização
# Este evento é disparado quando o bot está pronto e online
@bot.event
async def on_ready():
    # Define a atividade do bot (ex: Jogando com a API)
    await bot.change_presence(activity=discord.Game(name="com a API do Discord!"))
    print('----------------------------------------------------')
    print(f'🤖 Bot logado como: {bot.user.name} ({bot.user.id})')
    print('----------------------------------------------------')
    
    # ⚠️ REGISTRAR SLASH COMMANDS (Comandos de Barra)
    # Tenta sincronizar todos os comandos de barra com o Discord.
    # O comando tree.sync() pode demorar um pouco para aparecer no Discord!
    try:
        synced = await bot.tree.sync()
        print(f"Comandos de Barra sincronizados: {len(synced)}")
    except Exception as e:
        print(f"Erro ao sincronizar comandos de barra: {e}")

# 5. Comando de Texto (Prefixado com !)
@bot.command(name='diga')
async def diga(ctx, *, texto):
    """
    Faz o bot repetir o que você disse.
    Uso: !diga Olá mundo!
    """
    await ctx.send(f'{ctx.author.name} disse: {texto}')

# 6. Comando de Barra (Slash Command /)
@bot.tree.command(name="olacanary", description="Um comando de barra simples.")
async def slash_hello(interaction: discord.Interaction):
    """
    Comando que só aparece se for usado o prefixo /
    """
    # Responde diretamente à interação.
    await interaction.response.send_message(f"Olá, {interaction.user.mention}! Você usou o comando de barra no Discord Canary (ou Stable)!")

@bot.command(name='info')
async def send_embed_info(ctx):
    # --- Step 2: Embed Creation ---

    # 2.1. Create the Embed instance.
    # Color: 0xFF8C00 (Orange)
    embed = discord.Embed(
        title="Your Title",
        description="This is a simple Embed example created with discord.py for the guide!",
        color=0xFF8C00,
        url="https://discord.com/"
    )

    # 2.2. Add Fields
    embed.add_field(
        name="Main Language",
        value="```python```",
        inline=True
    )
    embed.add_field(
        name="Framework/Library",
        value="`discord.py`",
        inline=True
    )
    
    # 2.3. Add Visual Elements (Thumbnail)
    # embed.set_thumbnail(url="YOUR_SMALL_IMAGE_URL_HERE")

    # 2.4. Footer 
    # The timestamp has been removed.
    embed.set_footer(
        text=f"Command executed by {ctx.author.display_name} | {bot.user.name}",
        icon_url=ctx.author.avatar.url
    )
    
    # Linha removida: embed.timestamp = datetime.datetime.now(datetime.timezone.utc)
    
    # --- Step 3: Sending the Embed ---
    
    await ctx.send(embed=embed)

# 7. Execução
bot.run(TOKEN)