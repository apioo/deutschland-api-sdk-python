"""
autobahn_charging_station_collection automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union
from .autobahn_charging_station import AutobahnChargingStation
class AutobahnChargingStationCollection(BaseModel):
    entries: Optional[List[AutobahnChargingStation]] = Field(default=None, alias="entries")
    pass
