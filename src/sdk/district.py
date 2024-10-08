"""
district automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union
class District(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    state: Optional[str] = Field(default=None, alias="state")
    type: Optional[str] = Field(default=None, alias="type")
    name: Optional[str] = Field(default=None, alias="name")
    nuts_: Optional[str] = Field(default=None, alias="nuts3")
    area: Optional[int] = Field(default=None, alias="area")
    pass
