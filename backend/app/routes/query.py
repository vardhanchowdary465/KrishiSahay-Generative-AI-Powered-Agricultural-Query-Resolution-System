from fastapi import APIRouter
from app.models import QueryRequest, QueryResponse
from app.services.llm_service import get_llm_response

router = APIRouter()

@router.post("/", response_model=QueryResponse)
def handle_query(request: QueryRequest):
    answer = get_llm_response(request.question)
    return QueryResponse(answer=answer)