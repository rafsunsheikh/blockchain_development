# Verification

import nacl.encoding
import nacl.signing

# From the previous example
bobs_public_key = b'2f16af54266edaf8114547357f11a043ef6f19603bd21382d078cd5391c076bb'

# We generate the verify_key
verify_key = nacl.signing.VerifyKey(bobs_public_key, encoder=nacl.encoding.HexEncoder)

signed_message = b'a\x10iC;T_\xeb\xdb\xdb\x95I8F\x87\xbd\x91\xe3g\xa2\x81{}\xafK?\xb1\xf4h\x1e\xc6Kk\xa2o)\xa5t\xbd,\x84:mh\x19\xd6\\\xc2\xa6^\xa1\x8f\xe8\xc0E\xde\x13\xd6{%=\r\xf1\rSend $37 to Alice'

# Now we attempt to verify the message
# Any invalidation will result in an Exception being thrown 
verification = verify_key.verify(signed_message)
print(verification)