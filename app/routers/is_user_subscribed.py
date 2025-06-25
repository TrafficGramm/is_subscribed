from fastapi import APIRouter, HTTPException
from app.schemas.request import SubscriptionCheckRequest
from app.services.telegram import is_user_subscribed

router = APIRouter()


@router.post("/check-subscription")
async def check_subscription(req: SubscriptionCheckRequest):
    try:
        result = await is_user_subscribed(req.user_id, req.channel)
        return {"subscribed": result}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error checking subscription: {str(e)}"
        )
