import smartpy as sp
        
class StringFromBytes(sp.Contract):
  def __init__(self, metadata):
    self.init(
      metadata=metadata,
      bytes_to_string = {
        sp.bytes('0x00'): '00',
        sp.bytes('0x01'): '01',
        sp.bytes('0x02'): '02',
        sp.bytes('0x03'): '03',
        sp.bytes('0x04'): '04',
        sp.bytes('0x05'): '05',
        sp.bytes('0x06'): '06',
        sp.bytes('0x07'): '07',
        sp.bytes('0x08'): '08',
        sp.bytes('0x09'): '09',
        sp.bytes('0x0A'): '0A',
        sp.bytes('0x0B'): '0B',
        sp.bytes('0x0C'): '0C',
        sp.bytes('0x0D'): '0D',
        sp.bytes('0x0E'): '0E',
        sp.bytes('0x0F'): '0F',
        sp.bytes('0x10'): '10',
        sp.bytes('0x11'): '11',
        sp.bytes('0x12'): '12',
        sp.bytes('0x13'): '13',
        sp.bytes('0x14'): '14',
        sp.bytes('0x15'): '15',
        sp.bytes('0x16'): '16',
        sp.bytes('0x17'): '17',
        sp.bytes('0x18'): '18',
        sp.bytes('0x19'): '19',
        sp.bytes('0x1A'): '1A',
        sp.bytes('0x1B'): '1B',
        sp.bytes('0x1C'): '1C',
        sp.bytes('0x1D'): '1D',
        sp.bytes('0x1E'): '1E',
        sp.bytes('0x1F'): '1F',
        sp.bytes('0x20'): '20',
        sp.bytes('0x21'): '21',
        sp.bytes('0x22'): '22',
        sp.bytes('0x23'): '23',
        sp.bytes('0x24'): '24',
        sp.bytes('0x25'): '25',
        sp.bytes('0x26'): '26',
        sp.bytes('0x27'): '27',
        sp.bytes('0x28'): '28',
        sp.bytes('0x29'): '29',
        sp.bytes('0x2A'): '2A',
        sp.bytes('0x2B'): '2B',
        sp.bytes('0x2C'): '2C',
        sp.bytes('0x2D'): '2D',
        sp.bytes('0x2E'): '2E',
        sp.bytes('0x2F'): '2F',
        sp.bytes('0x30'): '30',
        sp.bytes('0x31'): '31',
        sp.bytes('0x32'): '32',
        sp.bytes('0x33'): '33',
        sp.bytes('0x34'): '34',
        sp.bytes('0x35'): '35',
        sp.bytes('0x36'): '36',
        sp.bytes('0x37'): '37',
        sp.bytes('0x38'): '38',
        sp.bytes('0x39'): '39',
        sp.bytes('0x3A'): '3A',
        sp.bytes('0x3B'): '3B',
        sp.bytes('0x3C'): '3C',
        sp.bytes('0x3D'): '3D',
        sp.bytes('0x3E'): '3E',
        sp.bytes('0x3F'): '3F',
        sp.bytes('0x40'): '40',
        sp.bytes('0x41'): '41',
        sp.bytes('0x42'): '42',
        sp.bytes('0x43'): '43',
        sp.bytes('0x44'): '44',
        sp.bytes('0x45'): '45',
        sp.bytes('0x46'): '46',
        sp.bytes('0x47'): '47',
        sp.bytes('0x48'): '48',
        sp.bytes('0x49'): '49',
        sp.bytes('0x4A'): '4A',
        sp.bytes('0x4B'): '4B',
        sp.bytes('0x4C'): '4C',
        sp.bytes('0x4D'): '4D',
        sp.bytes('0x4E'): '4E',
        sp.bytes('0x4F'): '4F',
        sp.bytes('0x50'): '50',
        sp.bytes('0x51'): '51',
        sp.bytes('0x52'): '52',
        sp.bytes('0x53'): '53',
        sp.bytes('0x54'): '54',
        sp.bytes('0x55'): '55',
        sp.bytes('0x56'): '56',
        sp.bytes('0x57'): '57',
        sp.bytes('0x58'): '58',
        sp.bytes('0x59'): '59',
        sp.bytes('0x5A'): '5A',
        sp.bytes('0x5B'): '5B',
        sp.bytes('0x5C'): '5C',
        sp.bytes('0x5D'): '5D',
        sp.bytes('0x5E'): '5E',
        sp.bytes('0x5F'): '5F',
        sp.bytes('0x60'): '60',
        sp.bytes('0x61'): '61',
        sp.bytes('0x62'): '62',
        sp.bytes('0x63'): '63',
        sp.bytes('0x64'): '64',
        sp.bytes('0x65'): '65',
        sp.bytes('0x66'): '66',
        sp.bytes('0x67'): '67',
        sp.bytes('0x68'): '68',
        sp.bytes('0x69'): '69',
        sp.bytes('0x6A'): '6A',
        sp.bytes('0x6B'): '6B',
        sp.bytes('0x6C'): '6C',
        sp.bytes('0x6D'): '6D',
        sp.bytes('0x6E'): '6E',
        sp.bytes('0x6F'): '6F',
        sp.bytes('0x70'): '70',
        sp.bytes('0x71'): '71',
        sp.bytes('0x72'): '72',
        sp.bytes('0x73'): '73',
        sp.bytes('0x74'): '74',
        sp.bytes('0x75'): '75',
        sp.bytes('0x76'): '76',
        sp.bytes('0x77'): '77',
        sp.bytes('0x78'): '78',
        sp.bytes('0x79'): '79',
        sp.bytes('0x7A'): '7A',
        sp.bytes('0x7B'): '7B',
        sp.bytes('0x7C'): '7C',
        sp.bytes('0x7D'): '7D',
        sp.bytes('0x7E'): '7E',
        sp.bytes('0x7F'): '7F',
        sp.bytes('0x80'): '80',
        sp.bytes('0x81'): '81',
        sp.bytes('0x82'): '82',
        sp.bytes('0x83'): '83',
        sp.bytes('0x84'): '84',
        sp.bytes('0x85'): '85',
        sp.bytes('0x86'): '86',
        sp.bytes('0x87'): '87',
        sp.bytes('0x88'): '88',
        sp.bytes('0x89'): '89',
        sp.bytes('0x8A'): '8A',
        sp.bytes('0x8B'): '8B',
        sp.bytes('0x8C'): '8C',
        sp.bytes('0x8D'): '8D',
        sp.bytes('0x8E'): '8E',
        sp.bytes('0x8F'): '8F',
        sp.bytes('0x90'): '90',
        sp.bytes('0x91'): '91',
        sp.bytes('0x92'): '92',
        sp.bytes('0x93'): '93',
        sp.bytes('0x94'): '94',
        sp.bytes('0x95'): '95',
        sp.bytes('0x96'): '96',
        sp.bytes('0x97'): '97',
        sp.bytes('0x98'): '98',
        sp.bytes('0x99'): '99',
        sp.bytes('0x9A'): '9A',
        sp.bytes('0x9B'): '9B',
        sp.bytes('0x9C'): '9C',
        sp.bytes('0x9D'): '9D',
        sp.bytes('0x9E'): '9E',
        sp.bytes('0x9F'): '9F',
        sp.bytes('0xA0'): 'A0',
        sp.bytes('0xA1'): 'A1',
        sp.bytes('0xA2'): 'A2',
        sp.bytes('0xA3'): 'A3',
        sp.bytes('0xA4'): 'A4',
        sp.bytes('0xA5'): 'A5',
        sp.bytes('0xA6'): 'A6',
        sp.bytes('0xA7'): 'A7',
        sp.bytes('0xA8'): 'A8',
        sp.bytes('0xA9'): 'A9',
        sp.bytes('0xAA'): 'AA',
        sp.bytes('0xAB'): 'AB',
        sp.bytes('0xAC'): 'AC',
        sp.bytes('0xAD'): 'AD',
        sp.bytes('0xAE'): 'AE',
        sp.bytes('0xAF'): 'AF',
        sp.bytes('0xB0'): 'B0',
        sp.bytes('0xB1'): 'B1',
        sp.bytes('0xB2'): 'B2',
        sp.bytes('0xB3'): 'B3',
        sp.bytes('0xB4'): 'B4',
        sp.bytes('0xB5'): 'B5',
        sp.bytes('0xB6'): 'B6',
        sp.bytes('0xB7'): 'B7',
        sp.bytes('0xB8'): 'B8',
        sp.bytes('0xB9'): 'B9',
        sp.bytes('0xBA'): 'BA',
        sp.bytes('0xBB'): 'BB',
        sp.bytes('0xBC'): 'BC',
        sp.bytes('0xBD'): 'BD',
        sp.bytes('0xBE'): 'BE',
        sp.bytes('0xBF'): 'BF',
        sp.bytes('0xC0'): 'C0',
        sp.bytes('0xC1'): 'C1',
        sp.bytes('0xC2'): 'C2',
        sp.bytes('0xC3'): 'C3',
        sp.bytes('0xC4'): 'C4',
        sp.bytes('0xC5'): 'C5',
        sp.bytes('0xC6'): 'C6',
        sp.bytes('0xC7'): 'C7',
        sp.bytes('0xC8'): 'C8',
        sp.bytes('0xC9'): 'C9',
        sp.bytes('0xCA'): 'CA',
        sp.bytes('0xCB'): 'CB',
        sp.bytes('0xCC'): 'CC',
        sp.bytes('0xCD'): 'CD',
        sp.bytes('0xCE'): 'CE',
        sp.bytes('0xCF'): 'CF',
        sp.bytes('0xD0'): 'D0',
        sp.bytes('0xD1'): 'D1',
        sp.bytes('0xD2'): 'D2',
        sp.bytes('0xD3'): 'D3',
        sp.bytes('0xD4'): 'D4',
        sp.bytes('0xD5'): 'D5',
        sp.bytes('0xD6'): 'D6',
        sp.bytes('0xD7'): 'D7',
        sp.bytes('0xD8'): 'D8',
        sp.bytes('0xD9'): 'D9',
        sp.bytes('0xDA'): 'DA',
        sp.bytes('0xDB'): 'DB',
        sp.bytes('0xDC'): 'DC',
        sp.bytes('0xDD'): 'DD',
        sp.bytes('0xDE'): 'DE',
        sp.bytes('0xDF'): 'DF',
        sp.bytes('0xE0'): 'E0',
        sp.bytes('0xE1'): 'E1',
        sp.bytes('0xE2'): 'E2',
        sp.bytes('0xE3'): 'E3',
        sp.bytes('0xE4'): 'E4',
        sp.bytes('0xE5'): 'E5',
        sp.bytes('0xE6'): 'E6',
        sp.bytes('0xE7'): 'E7',
        sp.bytes('0xE8'): 'E8',
        sp.bytes('0xE9'): 'E9',
        sp.bytes('0xEA'): 'EA',
        sp.bytes('0xEB'): 'EB',
        sp.bytes('0xEC'): 'EC',
        sp.bytes('0xED'): 'ED',
        sp.bytes('0xEE'): 'EE',
        sp.bytes('0xEF'): 'EF',
        sp.bytes('0xF0'): 'F0',
        sp.bytes('0xF1'): 'F1',
        sp.bytes('0xF2'): 'F2',
        sp.bytes('0xF3'): 'F3',
        sp.bytes('0xF4'): 'F4',
        sp.bytes('0xF5'): 'F5',
        sp.bytes('0xF6'): 'F6',
        sp.bytes('0xF7'): 'F7',
        sp.bytes('0xF8'): 'F8',
        sp.bytes('0xF9'): 'F9',
        sp.bytes('0xFA'): 'FA',
        sp.bytes('0xFB'): 'FB',
        sp.bytes('0xFC'): 'FC',
        sp.bytes('0xFD'): 'FD',
        sp.bytes('0xFE'): 'FE',
        sp.bytes('0xFF'): 'FF',
      }
    )

  ## Helper functions
  #

  def bytes_to_string(self, hash_bytes):
    sp.set_type(hash_bytes, sp.TBytes)
    _hash = sp.local('_hash', hash_bytes)
    res = sp.local('res', '')
    index = sp.local('index', 0)
    hash_len = sp.local('hash_len', sp.len(_hash.value))
    sp.while index.value < hash_len.value:
      res.value += (self.data.bytes_to_string[sp.slice(_hash.value, index.value, 1).open_some()])
      index.value = index.value + 1
    return res.value

  ## Views
  #

  @sp.onchain_view()
  def string_from_bytes(self, params):
    sp.set_type(params, sp.TBytes)
    res = self.bytes_to_string(params)
    sp.result(res)

