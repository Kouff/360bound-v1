import unittest
from converter import ConverterData


class TestCalculator(unittest.TestCase):
    def test_convert_data(self):
        data = [
            {'code': '1', 'name': 'name 1'},
            {'code': '1.1', 'name': 'name 1.1'},
            {'code': '1.2', 'name': 'name 1.2'},
            {'code': '1.2.1', 'name': 'name 1.2.1'},
            {'code': '1.2.2', 'name': 'name 1.2.2'},
            {'code': '2', 'name': 'name 2'}
        ]
        expected_result = [
            {'code': '1', 'name': 'name 1', 'children': [
                {'code': '1.1', 'name': 'name 1.1', 'children': []},
                {'code': '1.2', 'name': 'name 1.2', 'children': [
                    {'code': '1.2.1', 'name': 'name 1.2.1', 'children': []},
                    {'code': '1.2.2', 'name': 'name 1.2.2', 'children': []},
                ]}
            ]},
            {'code': '2', 'name': 'name 2', 'children': []},
        ]
        converter = ConverterData(data)
        self.assertEqual(
            converter.converted_data,
            expected_result
        )


if __name__ == "__main__":
    unittest.main()
