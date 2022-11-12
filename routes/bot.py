from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/bot", tags=["bot"])


class ChatBot(BaseModel):
    userId: int
    name: str


class InboxMessage(BaseModel):
    message: str


@router.post('/')
def start(bot: ChatBot):
    return {
        "userId": bot.userId,
        "message": f"Доброго времени суток, {bot.name}! Что бы вы хотели узнать?"
    }


@router.post('/receiptent_bot')
def receiptent(bot: InboxMessage):
    if bot.message.lower() == 'выбрать брокера':
        return {
            "type": "find_broker"
        }
    elif bot.message.lower() == 'курс валют':
        return {
            "type": "exchange_rate"
        }
    elif bot.message.lower() == 'тест на риск':
        return {
            "type": "risk_test"
        }
