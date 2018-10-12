#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pycoin.block import Block
import io, struct
import x13bcd_hash

def uint256_from_str(s):
    r = 0L
    t = struct.unpack("<IIIIIIII", s[:32])
    for i in xrange(8):
        r += t[i] << (i * 32)
    return r
rawblock = '00000060b38cb32058b774ea735c0f6cfaf3fb0153a03496be87208219717f4e4ad744ee5dc71fd1295bfe406e03e23877b2b9a64be33f2a2f1e05a238ef6fdf04bb574ca24ec05b6394001b00cfc14c02010000000001010000000000000000000000000000000000000000000000000000000000000000ffffffff4c0335350804a24ec05b08fabe6d6d00000000000003600000000000003960000039da4b3161e0000039da4b3161c8010000000000000030d6c52e000000000d2f6e6f64655374726174756d2f00000000020000000000000000266a24aa21a9edd76d419006b113123076afec5868f6b6e3dfde054e82adf4a9693d2a1cc58b256880814a000000001976a914829a4b1a792e9e1514ae902d622aed18a99601b088ac01200000000000000000000000000000000000000000000000000000000000000000000000000c000000d13244a2054b9b33808e72daabd3d9a7c5685b10abd7a4b932f273dd498f131601d4063756d72c0f08af818741b198c97ecf1ae065c464a0ef08ea7c4f0679089d010000006a4730440220243539823fb5fe8fdb8991dda0e5f7e7cf8e3beee36e2dbce6b905e58d142373022058996510c2edf2fbbe77f77016cbfafbe53cc4505e58de05083194af714c50000121021e6a4b6673be9f25e54f4028ebf8459bd2d0726d836dbcee8cecaa856bec458bffffffff0280778e06000000001976a91481b2e127d9c7fec0fbc6b1a1784ba421acf3889d88ac67ccd617000000001976a9145f2bc24285493cafc8ef44b35a5ffe63c5eab5ce88ac00000000'

b = Block.parse_as_header(io.BytesIO(rawblock.decode('hex')))
hash_bin = x13bcd_hash.getPoWHash(b.as_bin())


print uint256_from_str(hash_bin)