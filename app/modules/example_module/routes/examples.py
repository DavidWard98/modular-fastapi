from fastapi import APIRouter

router = APIRouter()
router = APIRouter(
    prefix="/examples",
    tags=["examples"],
)

@router.get("/")
async def index():
    return {"examples": []}

@router.get("/{id}")
async def show(id: int):
    return {"example": id}
