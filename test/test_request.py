import unittest
from src import funcs
import cerberus

class TestMethods(unittest.TestCase):

    def test_get_request(self):

        schema = {
            'patients': {
                'type': 'list', 
                'schema': {
                    'type': 'dict', 
                    'schema': {
                        'id': {'type': 'string'},
                        'first': {'type': 'string'}, 
                        'last': {'type': 'string'}
                    }
                }
            }
        }
        v = cerberus.Validator(schema)
        self.assertEqual(v.validate(funcs.get_request("https://augusto-test.free.beeceptor.com/patient"), schema), True)

if __name__ == '__main__':
    unittest.main()