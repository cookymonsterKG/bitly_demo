import unittest
from io import StringIO
from unittest.mock import patch
from index import read_encodes_csv, read_decodes_json, filter_decodes_by_year, calculate_clicks


class TestClicks(unittest.TestCase):

    def test_read_encodes_csv(self):
        '''
        Test if the read_encodes_csv function correctly reads and parses the CSV data.
        '''
        with patch('builtins.open', return_value=StringIO('long_url,domain,hash\nhttps://google.com/,bit.ly,31Tt55y\n')) as mock_file:
            print(mock_file)
            encodes = read_encodes_csv('mock_file')
            expected = {'http://bit.ly/31Tt55y': 'https://google.com/'}
            self.assertDictEqual(encodes, expected)

    def test_read_decodes_json(self):
        '''
        Test if the read_decodes_json function correctly reads and parses the JSON data.
        '''
        with patch('builtins.open', return_value=StringIO('[{"bitlink": "http://bit.ly/31Tt55y", "timestamp": "2021-02-15T00:00:00"}]')) as mock_file:
            decodes = read_decodes_json('fake_path')
            expected = [{'bitlink': 'http://bit.ly/31Tt55y', 'timestamp': '2021-02-15T00:00:00'}]
            self.assertEqual(decodes, expected)

    def test_filter_decodes_by_year(self):
        '''
        Test if the filter_decodes_by_year function correctly filters decodes by the given year.
        '''
        decodes = [
            {'bitlink': 'http://bit.ly/31Tt55y', 'timestamp': '2021-02-15T00:00:00'},
            {'bitlink': 'http://bit.ly/21Gt35a', 'timestamp': '2021-02-15T00:00:00'},
            {'bitlink': 'http://bit.ly/31Tt55y', 'timestamp': '2020-02-15T00:00:00'}
        ]
        filtered_decodes = filter_decodes_by_year(decodes, 2021)
        expected = [{'bitlink': 'http://bit.ly/31Tt55y', 'timestamp': '2021-02-15T00:00:00'},
                    {'bitlink': 'http://bit.ly/21Gt35a', 'timestamp': '2021-02-15T00:00:00'}]
        self.assertEqual(filtered_decodes, expected)

    def test_calculate_clicks(self):
        '''
        Test if the calculate_clicks function correctly calculates the number of clicks for each URL.
        '''
        encodes = {'http://bit.ly/31Tt55y': 'https://google.com/'}
        decodes = [
            {"bitlink": "http://bit.ly/31Tt55y", "user_agent": "Mozilla/5.0 (Linux; U; Android 4.3; en-us; HUAWEI Y530-U00 Build/HuaweiY530-U00) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FBAN/FB4A;FBAV/23.0.0.22.14;]", "timestamp": "2021-04-09T00:00:00Z", "referrer": "t.co", "remote_ip": "2.17.160.0"},
            {"bitlink": "http://bit.ly/31Tt55y", "user_agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7", "timestamp": "2021-02-15T00:00:00Z", "referrer": "t.co", "remote_ip": "4.14.247.63"},
            {"bitlink": "http://bit.ly/21Gt35a", "user_agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7", "timestamp": "2021-02-15T00:00:00Z", "referrer": "t.co", "remote_ip": "4.14.247.63"}
        ]
        clicks_data = calculate_clicks(encodes, decodes)
        expected = [{'https://google.com/': 2}]
        self.assertEqual(clicks_data, expected)


if __name__ == '__main__':
    unittest.main()
