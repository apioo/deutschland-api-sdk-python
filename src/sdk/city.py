"""
city automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union
class City(BaseModel):
    id: Optional[int] = Field(default=None, alias="id")
    state: Optional[str] = Field(default=None, alias="state")
    rb: Optional[str] = Field(default=None, alias="rb")
    district: Optional[str] = Field(default=None, alias="district")
    verb: Optional[str] = Field(default=None, alias="verb")
    gem: Optional[str] = Field(default=None, alias="gem")
    name: Optional[str] = Field(default=None, alias="name")
    zip_code: Optional[str] = Field(default=None, alias="zipCode")
    area: Optional[int] = Field(default=None, alias="area")
    pass
