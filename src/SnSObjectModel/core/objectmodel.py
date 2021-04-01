# SnSObjectModel.core.objectmodel
# EXPLANATION
"""
The core module of SnSObjectModel
Content:
    ObjectModel Class
Required Packages:
    os
"""

# Content #
    # C1. ObjectModel

import os

# C1 'ObjectModel'
# EXPLANATION
class ObjectModel:
    """
    ObjectModel
    DOCSTRING
    """

    # Special Methods #
    def __init__(self, base_objects=[], name='default_ObjectModel', cache={}):
        """
        'attributes': A list of attributes most methods have access to
        'base_objects': Objects to serve as base models
        'name': The name of this ObjectModel
        'models': A dictionary of object names and attribute values
        All objects given to ObjectModel must have a 'name' attribute
        """
        self.attributes = ['name', 'models', 'cache']
        self.name = name
        self.models = {}
        # Add all given base objects to models
        for item in base_objects:
            try:
                if item.__class__.__name__ in self.models:
                    self.models[item.__class__.__name__]['preset'][item.name] = item.__dict__
                else:
                    self.models[item.__class__.__name__] = {
                        'base':item,
                        'preset': {
                            item.name:item.__dict__,
                        },
                    }
            except:
                print(f"Could not add {item} to models")

        self.cache = cache

    def __str__(self):
        return f"ObjectModel"

    def __repr__(self):
        return f"<class ObjectModel | {self.name}>"

    # Getters and Setters #
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def clear_name(self):
        self.name = None

    def set_models(self, models_dict):
        self.models = models_dict

    def get_models(self):
        return self.models

    def clear_models(self):
        self.models = {}

    def set_cache(self, cache_dict):
        self.cache = cache_dict

    def get_cache(self):
        return self.cache

    def clear_cache(self):
        self.cache = {}

    # Attribute Methods #

    # 'set_attribute' and 'set_attributes' methods are redundant with the getters and setters,
    # but are included to customize access to attributes

    # Return the attributes of this object as a dictionary
    def to_dict(self):
        """
        Returns a dictionary of the object's attributes
        { 'attribute_name':attribute_value }
        """
        attribute_dict = {
            "attributes":self.attributes,
            "name": self.name,
            "models":self.models,
            "cache":self.cache,
        }

        return attribute_dict

    # Set the value of a single attribute of this object
    def set_attribute(self, attribute_name, attribute_value):
        """
        Set the value of a single attribute of this object
        given the attribute's name and the new value
        """
        for attribute in self.attributes:
            if attribute == attribute_name:
                setattr(self, attribute, attribute_value)
                break

    # Set the value of one or more attributes of this object
    def set_attributes(self, attribute_dict):
        """
        Set the value of every attribute of this object
        matching a key in the given dictionary
        to the corresponding value
        """
        for attribute in self.attributes:
            if attribute in attribute_dict:
                setattr(self, attribute, attribute_dict[attribute])

    # Set the value of the given attribute to 'None'
    # This can be dangerous if an attribute requires a specific type to be used
    def clear_attribute(self, attribute_name):
        for attribute in self.attributes:
            if attribute == attribute_name:
                setattr(self, attribute, None)

    # Utility Methods #

    # Save an item to the cache
    def to_cache(self, target_object):
        try:
            self.cache[target_object.name] = target_object
        except:
            print(f"Could not save {target_object} to cache")

    # Return an object from the cache
    def from_cache(self, object_name):
        if object_name in self.cache:
            return self.cache[object_name]
        else:
            return None

    # Primary Methods #
    
    # Return an object with preset attributes
    def create(self, object_name, class_name):
        try:
            new_object = self.models[class_name]['base']
            for attribute_name, attribute_value in self.models[class_name]['preset'][object_name].items():
                setattr(new_object, attribute_name, attribute_value)
            self.to_cache(new_object)
            return new_object
        except:
            print("Could not create object from model")
            return None

    # Return an object created from a preset
    def get(self, object_name, class_name):
        if class_name not in self.models:
            print(f"{class_name} not in models")
            return None
        else:
            target_object = self.from_cache(object_name)
            if (target_object.__class__.__name__ != class_name) or (target_object == None):
                return self.create(object_name, class_name)
            else:
                return target_object

    # Add an object to models
    def add_model(self, target_object):
        try:
            if target_object.__class__.__name__ in self.models:
                self.models[target_object.__class__.__name__]['preset'][target_object.name] = target_object.__dict__
            else:
                self.models[target_object.__class__.__name__] = {
                    'base':target_object,
                    'preset': {
                        target_object.name:target_object.__dict__,
                    },
                }
        except:
            print(f"Could not add {target_object} to models")

    # Set model preset values from a source
    def load_models(self, model_dict):
        self.clear_models()
        self.set_models(model_dict)
        