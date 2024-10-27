from telebot import asyncio_filters
from telebot.asyncio_storage import StateMemoryStorage
from telebot.asyncio_handler_backends import State, StatesGroup

class BroadcastState(StatesGroup):
    msg = State()
    
    
class ImportWalletState(StatesGroup):
    wallet = State()