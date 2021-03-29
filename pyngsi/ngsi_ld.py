#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pyngsi.ngsi import DataModel
from typing import Any
from collections.abc import Sequence, Callable

class DataModelLD(DataModel):

    def __init__(self, id: str, type: str, serializer: Callable = str):
        self.serializer = serializer
        self["id"] = id
        self["type"] = type
        if self.transient_timeout:
            self.add_transient(self.transient_timeout)

    def add(self, name: str, value: Any,
            isdate: bool = False, isurl: bool = False, urlencode=False, metadata: dict = {}):
        if isinstance(value, str) or isinstance(value, bool) or isinstance(value, int) or isinstance(value, float):
            t, v = "Property", value
        self[name] = {"value": v, "type": t}

    def add_attr_timestamp(self, name:str, value:str):
        if name in self:
            self[name]["observedAt"] = value
        else:
            raise ValueError("Name not known")

    def add_context(self, urls:list):
        self["@context"] = urls
