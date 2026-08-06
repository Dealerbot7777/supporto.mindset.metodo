import os
from dotenv import load_dotenv

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("💰🎰 CLICCA QUI", url="https://beacons.ai/communitygames_09")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    testo = """
👋 Benvenuto!

Grazie per aver completato il test.
Se sei qui è perché vuoi far parte del 10% vincente nelle slot e minigames.

Per premiare la tua determinazione, avrai la possibilità di avere gratuitamente non 1️⃣, non 2️⃣, non 3️⃣, ma bensì 4️⃣ guide su slot games 🎰, dove saranno presenti strategie e soprattutto gestione del denaro 💰, il punto debole del 90% dei giocatori. Porta la 🍀 fortuna dalla tua parte con studio e metodo.

Per farlo dovrai iscriverti ad uno dei due siti che trovi cliccando su CLICCA QUI 👇, siti con le RTP più alte sul mercato. (Non sai cosa significhi RTP? Non ti preoccupare ci sono le guide 😉)

La registrazione 📄deve essere di almeno 25€ (laddove seguite le indicazioni del sito avrete un bonus del 100% sulla prima ricarica + freespin omaggio).

Una volta fatto mandate una foto o screen shot del deposito e la mail di iscrizione alla mail supporto.mindset.metodo@gmail.com, vi arriveranno le guide alla mail 📧 che avete utilizzato. Le guide, con strategie e money management, sono frutto di mesi e mesi di esperienza e analisi dei dati. Le riceverai per i seguenti giochi:
✈️ Aviator
🐔 Chicken Road
⚽️ Penalty Unlimited
🐔 Chicken Game

Detto questo buona fortuna a tutti/e quelle che vogliono iniziare a provare a guadagnare con metodo e disciplina.

"""

    await update.message.reply_text(
        testo,
        reply_markup=reply_markup
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("✅ Bot avviato!")

    app.run_polling()

if __name__ == "__main__":
    main()
    