"""
backend_user automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union
import datetime
from .backend_app import BackendApp
from .common_metadata import CommonMetadata
class BackendUser(BaseModel):
    id: Optional[int] = Field(default=None, alias="id")
    role_id: Optional[int] = Field(default=None, alias="roleId")
    plan_id: Optional[int] = Field(default=None, alias="planId")
    status: Optional[int] = Field(default=None, alias="status")
    name: Optional[str] = Field(default=None, alias="name")
    email: Optional[str] = Field(default=None, alias="email")
    points: Optional[int] = Field(default=None, alias="points")
    scopes: Optional[List[str]] = Field(default=None, alias="scopes")
    apps: Optional[List[BackendApp]] = Field(default=None, alias="apps")
    metadata: Optional[CommonMetadata] = Field(default=None, alias="metadata")
    date: Optional[datetime.datetime] = Field(default=None, alias="date")
    pass
