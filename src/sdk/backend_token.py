"""
backend_token automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union
import datetime
class BackendToken(BaseModel):
    id: Optional[int] = Field(default=None, alias="id")
    status: Optional[int] = Field(default=None, alias="status")
    name: Optional[str] = Field(default=None, alias="name")
    scopes: Optional[List[str]] = Field(default=None, alias="scopes")
    ip: Optional[str] = Field(default=None, alias="ip")
    expire: Optional[datetime.datetime] = Field(default=None, alias="expire")
    date: Optional[datetime.datetime] = Field(default=None, alias="date")
    pass
