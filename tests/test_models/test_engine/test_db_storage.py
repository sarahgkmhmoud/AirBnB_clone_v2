import unittest
from unittest.mock import patch, MagicMock
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review
from models import storage

class TestDBStorage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the database connection for testing
        storage._DBStorage__engine = MagicMock()
        storage._DBStorage__session = MagicMock()

    @classmethod
    def tearDownClass(cls):
        # Clean up resources after all tests are done
        storage._DBStorage__engine = None
        storage._DBStorage__session = None

    def setUp(self):
        # Set up any resources needed for each test case
        self.db_storage = storage.DBStorage()

    def tearDown(self):
        # Clean up resources after each test case
        storage._DBStorage__session.rollback.reset_mock()
        storage._DBStorage__session.commit.reset_mock()
        storage._DBStorage__session.close.reset_mock()

    def test_all_with_cls_none(self):
        # Test the 'all' method when cls is None
        with patch('sqlalchemy.orm.Session.query') as mock_query:
            mock_query.return_value.all.return_value = [
                State(), City(), User(), Place(), Review(), Amenity()
            ]
            result = self.db_storage.all()
            self.assertEqual(len(result), 6)

    def test_all_with_cls_specified(self):
        # Test the 'all' method when cls is specified
        with patch('sqlalchemy.orm.Session.query') as mock_query:
            mock_query.return_value.all.return_value = [User(), User(), User()]
            result = self.db_storage.all(User)
            self.assertEqual(len(result), 3)

    def test_new(self):
        # Test the 'new' method
        obj = BaseModel()
        self.db_storage.new(obj)
        self.assertTrue(obj in self.db_storage._DBStorage__session.add.call_args[0][0])

    def test_save(self):
        # Test the 'save' method
        self.db_storage.save()
        self.assertTrue(self.db_storage._DBStorage__session.commit.called)

    def test_delete(self):
        # Test the 'delete' method
        obj = BaseModel()
        self.db_storage.delete(obj)
        self.assertTrue(obj in self.db_storage._DBStorage__session.delete.call_args[0][0])

    def test_reload(self):
        # Test the 'reload' method
        with patch('sqlalchemy.ext.declarative.Base.metadata.create_all') as mock_create_all, \
             patch('sqlalchemy.orm.sessionmaker') as mock_sessionmaker:
            self.db_storage.reload()
            self.assertTrue(mock_create_all.called)
            self.assertTrue(mock_sessionmaker.called)

    def test_close(self):
        # Test the 'close' method
        self.db_storage.close()
        self.assertTrue(self.db_storage._DBStorage__session.close.called)

if __name__ == '__main__':
    unittest.main()
