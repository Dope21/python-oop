from pydantic import BaseModel


class CateName(BaseModel):
    cate_name: str


class FindById(BaseModel):
    pro_id: str
    cate_name: str


class ProName(BaseModel):
    name: str
