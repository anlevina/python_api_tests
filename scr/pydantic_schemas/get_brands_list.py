from pydantic import BaseModel
from typing import List


class Brand(BaseModel):
    id: int
    brand: str


class GetBrandsListResponse(BaseModel):
    responseCode: int
    brands: List[Brand]
