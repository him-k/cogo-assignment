from pydantic import BaseModel

class Shipment_detailsBase(BaseModel):
    origin: str
    destination: str
    size: str
    type: str
    commodity: str
    tot_weight:int
    count:int

class Shipment_detailsCreate(Shipment_detailsBase):
    pass

class Shipment(Shipment_detailsBase):
    id: int

class Shipment_detailsUpdate(Shipment_detailsBase):
    pass


    class Config:
        orm_mode = True

