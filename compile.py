import smartpy as sp
import json
import os
env = os.environ

StringFromBytes = sp.io.import_script_from_url("file:string_from_bytes.py")

metadata = {
  "name": "String From Bytes",
  "description": "Tezos contract that can get a string form some bytes",
  "version": "3.0.0",
  "homepage": "https://github.com/asbjornenge/tezos-string-from-bytes",
  "authors": ["asbjornenge <asbjorn@surflabs.net>"]
}

sp.add_compilation_target("string_from_bytes", StringFromBytes.StringFromBytes(
  metadata = sp.big_map(
    {
      "": sp.utils.bytes_of_string("tezos-storage:content"),
      "content": sp.utils.bytes_of_string(json.dumps(metadata))
    }
  )
))
