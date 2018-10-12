package x13bcd_hash

import (
	"encoding/hex"
	"fmt"
	btc "github.com/btcsuite/btcd/blockchain"
	"github.com/btcsuite/btcd/chaincfg/chainhash"
	"math/big"
	"testing"
)

func TestBCD(t *testing.T) {
	blockheader_hex := "00000060b38cb32058b774ea735c0f6cfaf3fb0153a03496be87208219717f4e4ad744ee5dc71fd1295bfe406e03e23877b2b9a64be33f2a2f1e05a238ef6fdf04bb574ca24ec05b6394001b00cfc14c"
	block_header, _ := hex.DecodeString(blockheader_hex)
	// block hash: 995011cd275c40dacd5677f6c2b0a0cee178645cd39e606327d43d8668444861
	// pow hash: "0000000000003ecc852752183cd6a10e32be3dbec4f7e9d45dbfc42cff17b773"
	// hash int: "100913952414760389167500716660663373075201747118999077511477107"
	target, _ := new(big.Int).SetString("100913952414760389167500716660663373075201747118999077511477107", 10)
	b := GetPowHash(block_header)
	powhash, _ := chainhash.NewHash(b)
	hash_int := btc.HashToBig(powhash)
	if hash_int.Cmp(target) != 0 {
		t.Error("error to check bcd powhash")
		return
	}
	fmt.Println("bcd powhash OK")
}
