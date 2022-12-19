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

  scene.show(sob.get_string_from_bytes(sp.sha256(sp.pack('eplekakejonas'))))
