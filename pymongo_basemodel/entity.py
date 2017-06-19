
"""
pymongo_basemodel.entity
~~~~~~~~~~~~~~~~~~~~~~~~
This module defines the Entity and Entities interfaces. Entities is a cache of
Entity groups that allows for retrieval by name. Entity is a metaclass that
creates Model and Collection classes.
"""

from .delimited import DelimitedDict
from .exceptions import EntityNotSet


class EntityMeta(object):
    pass


class Entities(object):

    cache = {}

    @classmethod
    def set(cls, name, entity):
        Entities.cache[name] = entity

    @classmethod
    def get(cls, name):
        if name not in Entities.cache:
            raise EntityNotSet(name)
        else:
            return Entities.cache[name]


class Entity(type):

    def __new__(cls, name, m_options=None, c_options=None):
        from .model import Model
        from .collection import Collection

        configs = [{
            "type": "model",
            "bases": [Model, EntityMeta],
            "options": m_options
        }, {
            "type": "collection",
            "bases": [Collection, EntityMeta],
            "options": c_options
        }]

        entity = {}
        for c in configs:

            # special attributes
            if c["options"] is not None:

                # methods
                if "methods" in c["options"]:
                    methods = c["options"]["methods"]
                    del c["options"]["methods"]

                    if type(methods) is not list:
                        methods = [methods]

                    c["bases"] = methods + c["bases"]

            entity[c["type"]] = type(
                name + c["type"].title(),
                tuple(c["bases"]),
                {"__entity__": entity}
            )

            if c["options"] is None:
                continue

            for k, v in c["options"].items():
                if hasattr(entity[c["type"]], k):
                    existing = getattr(entity[c["type"]], k)
                    if isinstance(existing, DelimitedDict):
                        v = existing.__class__(v)

                setattr(entity[c["type"]], k, v)

        Entities.set(name, entity)

        return entity["model"], entity["collection"]
