from pydantic import BaseModel


class SubscriptionCheckRequest(BaseModel):
    user_id: int
    channel: str
