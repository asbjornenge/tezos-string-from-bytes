import smartpy as sp
from datetime import datetime

StringOfBytes = sp.io.import_script_from_url("file:string_of_bytes.py")

allKind = 'all'

def init(scenario):
  sob = StringOfBytes.StringOfBytes(
    metadata = sp.big_map(
      {
        "": sp.utils.bytes_of_string("tezos-storage:content"),
        "content": sp.utils.bytes_of_string('{"name": "String Of Bytes"}')
      }
    )
  )
  scenario += sob 
  return sob 

@sp.add_target(name="All", kind=allKind)
def test():
  scene = sp.test_scenario()
  sob = init(scene)

  ## It can convert bytes to string on-chain
  #

  blake2b = sob.string_from_bytes(sp.sha256(sp.pack('tz1UZZnrre9H7KzAufFVm7ubuJh5cCfjGwam')))
  scene.verify(blake2b == 'B37B52F6D234BFA87D14BE9A4068805BE283F7A4BAD853CDE67A0699204F7E44') 
  sha512 = sob.string_from_bytes(sp.sha512(sp.pack('tz1UZZnrre9H7KzAufFVm7ubuJh5cCfjGwam')))
  scene.verify(sha512 == '96D6A913A18C08168FE2FBE191D4DD8206CBC2D592415D3829B9DE4C145718D40C4D7C7368862AB22DEE2CACFEE66357D4DE068D00599C0D09B3C0C7DBE682A0') 
  sha256 = sob.string_from_bytes(sp.sha256(sp.pack('KT1BfKnSKV6Wx45Cv4yjEYXViwuhmswby8Hp')))
  scene.verify(sha256 == '24EA663496C05A050B5E2151B13602412CB832F6C7B5CE819BE98E54D6FCE8C5') 
  sha3 = sob.string_from_bytes(sp.sha3(sp.pack('KT1BfKnSKV6Wx45Cv4yjEYXViwuhmswby8Hp')))
  scene.verify(sha3 == 'EEE1759307F4F814CC9BCF8BD7A06CCC32999546151D3DCCFBD36BB145D50BF1') 
  keccak = sob.string_from_bytes(sp.keccak(sp.pack('KT1BfKnSKV6Wx45Cv4yjEYXViwuhmswby8Hp')))
  scene.verify(keccak == '304A54AAE33305631DA4C9DE5DD9E10D15518010CA006C65855315881F564995')
  timestamp = sob.string_from_bytes(sp.pack(sp.timestamp(1637752889)))
  scene.verify(timestamp == '0500B980F1990C')
  randomstring = sob.string_from_bytes(sp.pack('applecake'))
  scene.verify(randomstring == '0501000000096170706C6563616B65')
