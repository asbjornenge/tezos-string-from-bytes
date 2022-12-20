# String From Bytes

A small helper contract to get a `string` from a `bytes` type.

## Contracts

```
Ghostnet: KT1V6rPYSGghLEgCW2wkcbq4uGAPf4aMTWzZ
Mainnet: TBA
```

## Usage

SmartPy example.

```py
@sp.private_lambda(with_storage='read-only', with_operations=True, wrap_call=True)
def sob(self, _bytes):
  sp.set_type(_bytes, sp.TBytes)
  _string = sp.view('string_from_bytes', self.data.config.string_from_bytes_address, _bytes, sp.TString).open_some('Invalid view string_from_bytes')
  sp.result(_string)
```

enjoy.
