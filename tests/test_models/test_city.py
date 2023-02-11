#!/usr/bin/python3
"""Defines unittests for models/city.py
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestC_instantiation(unittest.TestCase):
    """ instantiation of class"""
   
    def test_no_or_arg_instances(self):
        self.assertEqual(City, type(City()))

    def test_id_is_publc_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_update_at(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_new_instance_stored(self):
        self.assertIn(City(), models.storage.all().values())

    def test_state_id_public_attribute(self):
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(City()))
        self.assertNotIn("state_id", City().__dict__)

    def test_ciies_unique_id(self):
        self.assertNotEqual(City().id, City().id)

    def test_unused_arg(self):
        self.assertNotIn(None, City(None).__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        c = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(c.id, "345")
        self.assertEqual(c.created_at, dt)
        self.assertEqual(c.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

class TestCity_save(unittest.TestCase):
    """Unittests for testing save method of the City class."""

    @classmethod
    def setup(self):
        try:
            os.rename("file.json", tmp)
        except IOError:
            pass

    def destroy(self):
        try:
           os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            City().save(None)

    def test_save_updates_file(self):
        c = City()
        c.save()
        cyid = "City." + c.id
        with open("file.json", "r") as f:
            self.assertIn(cyid, f.read())

class TestCity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the City class."""

    def test_to_dict(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_correct_keys(self):
        c = City()
        self.assertIn("id", c.to_dict())
        self.assertIn("created_at", c.to_dict())
        self.assertIn("updated_at", c.to_dict())
        self.assertIn("__class__", c.to_dict())

    def test_to_dict_datetime_attributes_are_str(self):
        c = City()
        c_dict = c.to_dict()
        self.assertEqual(str, type(c_dict["id"]))
        self.assertEqual(str, type(c_dict["created_at"]))
        self.assertEqual(str, type(c_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        cy = City()
        cy.id = "123456"
        cy.created_at = cy.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(cy.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        cy = City()
        self.assertNotEqual(cy.to_dict(), cy.__dict__)

    def test_to_dict_with_arg(self):
        cy = City()
        with self.assertRaises(TypeError):
            cy.to_dict(None)


if __name__ == "__main__":
    unittest.main()
