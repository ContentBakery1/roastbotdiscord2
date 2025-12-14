import discord
import os
from groq import Groq

TOKEN = os.environ["DISCORD_TOKEN"]
GROQ_API_KEY = os.environ["GROQ_API_KEY"]

ROAST_PROMPT = """
Jesteś brutalnym botem Discord który roastuje ludzi bez litości. Mów po polsku, prosto i krótko - jak typowy Seba. Przekleństwa są ok. Używaj prostego języka ulicy, żadnych mądrych słów. Na "ai-stop" przestajesz gadać, na "ai-start" wracasz.
"""

RESPECT_PROMPT = """
Jesteś botem Discord który szanuje tego użytkownika. Mów po polsku, prosto i z szacunkiem. To jest szef, więc bądź miły i pomocny. Na "ai-stop" przestajesz gadać, na "ai-start" wracasz.
"""

VIP_IDS = [814854720337608705, 951875234791833610, 1387052375373643798]
ADMIN_ID = 1387052375373643798

groq_client = Groq(api_key=GROQ_API_KEY)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

roasting_enabled = True

@client.event
async def on_ready():
    print(f"Bot online as {client.user}")

@client.event
async def on_message(message):
    global roasting_enabled
    
    if message.author == client.user:
        return
    if message.author.bot:
        return
    
    if message.author.id == ADMIN_ID:
        if message.content.lower() == "ai-roast":
            roasting_enabled = True
            await message.channel.send("Roasty włączone, czas was jebać 🔥")
            return
        elif message.content.lower() == "ai-stoproast":
            roasting_enabled = False
            await message.channel.send("Roasty wyłączone, macie spokój... na razie")
            return
    
    if not roasting_enabled:
        return
    
    if message.author.id in VIP_IDS:
        prompt = RESPECT_PROMPT
    else:
        prompt = ROAST_PROMPT
    
    try:
        response = groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": message.content}
            ],
            max_tokens=500
        )
        await message.channel.send(response.choices[0].message.content[:2000])
    except Exception as e:
        print(f"AI Error: {e}")
        await message.channel.send("Błąd AI")

client.run(TOKEN)
