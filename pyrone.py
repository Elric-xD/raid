
import sys
import asyncio

from os import execle, getenv, environ

from pyrogram import Client, filters, idle
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
from pyrogram.errors import FloodWait


# ------------- SESSIONS -------------

SESSION1 = getenv('SESSION1', default=None)
SESSION2 = getenv('SESSION2', default=None)
SESSION3 = getenv('SESSION3', default=None)
SESSION4 = getenv('SESSION4', default=None)
SESSION5 = getenv('SESSION5', default=None)


# ------------- CLIENTS -------------
M1 = Client(api_id=23114790, api_hash="8c0fb2eb81c68f1c7026d787f3b8eda6", session_name=SESSION1)

ONE_WORDS = ["KYU", "RE", "RANDI", "TERI", "MA", "K", "BHOSDA", "TERI", "BHN", "KI", "CHUT", "RAND", "KA", "BETA",
           "LODE", "SPED", "BDA", "BSDK", "DALLE", "GAND FATT", "GYA", "KYA 😂", "MAA ", "MT",
           "CHUDA", "YAHA", "BC", "TERI", "RANDI", "MA", "KA GAND", "FATT", "GYA", "JA", "TAILOR", "DHUNDNE",
           "RAND", "K", "BALK", "SPEED", "BDA", "WRNA", "TERI", "MA", "KI", "GAND", "MEBOMB",
           "RANDI", "K", "BETE", "TERI", "MA", "KA", "RAPE", "KR", "DIYE", "SAARE", "DOGS", "🤣🤣",
           "LODE","TERI","BHN","KO","NILAM","KR","DUNG😆","RANDI","K","PILE","TERI","MA","KA","BHSDA",
           "MC","SUAR","KE","14","TERI","MA","KE","GAND","ME","ATOM","BOMB","Daal","Dungi","😁😁",
           "KALP","RAND","K","BACHE","TERI","MAA","RANDI","BSDK","NALLE","MDRCHOD","AUKAT","BNA",
           "BSDK","TERI","RNDI","MAA","DAILY","CHUDTI","H","YHA 🤣","JAA","RAND","TU ","RADNI","H 🤣",
           "CHUTT","MARU","TERII","BEHEN","KAAA","BHOSDAA","MARU","RANDII","KEEE","CHODE","TERI","DADI","KAAA","BOOR",
           "GARAM","KARR","TERE","PUREE","KHANDAN","KOOO","CHODUNGAA","BAAP","SEE","BAKCHODI","KAREGAA","SUARR",
           "KEEE","PILLEE","NAAK","MEEE","NETAA","BAAP","KOO","KABHII","NAAH","BOLNAA","BETAA","CHUSS","LEEE",
           "MERAA","LODAA","JAISE","ALUU","KAAA","PAKODAA","TERI","MAAA","BEHEN","GFF","NANI","DIIN","RAAT","SOTEE",
           "JAGTEE","PELTAA","HUUU","LODEE","CHAAR","CHAWNII","GHODEE","PEEE","TUMM","MEREE","LODEE","PEE","TERI",
           "MAA","KAAA","BOOBS","DABATA HU", "TERI", "MAA", "KI", "CHUT", "AJA", "TERI", "MAA", "KI", "CHUT",
           "FAAD", "DUNGA", "HIJDE", "TERA", "BAAP","HU", "KIDXX", "SPEED", "PAKAD", "BHEN KE LAUDE", "AA BETA",
           "AAGYA", "TERI", "MAA ", "CHODNE","AB", "TERI ", "MAA", "CHUDEGI", "KUTTE", "KI", "TARAH", "BETA",
           "TERI", "MAA", "KE", "BHOSDE", "ME", "JBL", "KE", "SPEAKER", "DAAL", "KAR", "BASS", "BOOSTED", "SONG",
           "SUNUNGA", "PURI","RAAT", "LAGATAR", "TERI", "MAA", "KE", "SATH", "SEX", "KARUNGA🔥", "TERI", "MAA", "KE",
           "BOOBS","DABAUNGA","XXX","TERI","MAA","KAA","CHUT","MARU","RANDI","KEE","PILEE","TERI","MAA","KAA","BHOSDAA",
           "MARU","SUAR","KEE","CHODE","TERI","MAAA","KEEE","NUDES","BECHUNGA","RANDI","KEE","PILLE","TERI","MAAA",
           "CHODU","SUAR","KEEE","PILEE","TERIII","MAAA","DAILYY","CHUDTTI","HAII","MADHARCHOD","AUKAT","BANAA",
           "LODE","TERAA","BAAP","HUU","TERI","GFF","KAA","CHUD", "GAYA", "BACCHA", "BAAP SE",
           "AUKAT ME", "RAHO", "WARNA", "MAA CHOD DENGE TUMARI","BHOSDAA","MARUU","MADHARCHOD","TERI ","NANAI","KAA",
           "CHUTT","MARU","TERII","BEHEN","KAAA","BHOSDAA","MARU","RANDII","KEEE","CHODE","TERI","DADI","KAAA","BOOR",
           "GARAM","KARR","TERE","PUREE","KHANDAN","KOOO","CHODUNGAA","BAAP","SEE","BAKCHODI","KAREGAA","SUARR",
           "KEEE","PILLEE","NAAK","MEEE","NETAA","BAAP","KOO","KABHII","NAAH","BOLNAA","BETAA","CHUSS","LEEE",
           "MERAA","LODAA","JAISE","ALUU","KAAA","PAKODAA","TERI","MAAA","BEHEN","GFF","NANI","DIIN","RAAT","SOTEE",
           "JAGTEE","PELTAA","HUUU","LODEE","CHAAR","CHAWNII","GHODEE","PEEE","TUMM","MEREE","LODEE","PEE","TERI",
           "MAA","KAAA","BOOBS","DABATA HU", "TERA", "BAAP", "HU", "KIDXX", "SPEED", "PAKAD", "BHEN KE LAUDE",
           "AA BETA", "AAGYA", "TERI", "MAA ", "CHODNE",
           "AB", "TERI ", "MAA", "CHUDEGI", "KUTTE", "KI", "TARAH", "BETA", "TERI", "MAA", "KE", "BHOSDE",
           "ME", "JBL", "KE", "SPEAKER", "DAAL", "KAR", "BASS", "BOOSTED", "SONG", "SUNUNGA", "PURI",
           "RAAT", "LAGATAR", "TERI", "MAA", "KE", "SATH", "SEX", "KARUNGA🔥", "CHUD", "GAYA", "BACCHA", "BAAP SE",
           "AUKAT ME", "RAHO", "WARNA", "MAA CHOD DENGE TUMARI"]


async def pyrone(client: Client, message: Message):
    chat_id = message.chat.id
    ruser = None

    if message.reply_to_message:
        ruser = message.reply_to_message.message_id
    
    try:
        for word in ONE_WORDS:
            await M1.send_chat_action(chat_id, "typing")
            await M1.send_message(chat_id, word, reply_to_message_id=ruser)            
#            await asyncio.sleep(0.1)
    except FloodWait:
        pass


async def restart(_, __):
    args = [sys.executable, "pyrone.py"]
    execle(sys.executable, *args, environ)


# ADDING HANDLERS

M1.add_handler(MessageHandler(pyrone, filters.command(["T3RI", "KIDZ", "KYURERANDI", "AAJA", "TERU"], prefixes=None) & filters.me))
M1.add_handler(MessageHandler(restart, filters.command(["GANDFATT", "FATTT", "CHII", "FARAR"], prefixes=None) & filters.me))


# STARTING CLIENTS

M1.start()


print("Pyrone Started Successfully")

idle()


# STOPPING CLIENTS

M1.stop()
