package x13bcd_hash

// #cgo CFLAGS: -I.
// #cgo LDFLAGS: -L. -lx13bcd_hash
// #include "x13.h"
import "C"

import (
	"unsafe"
)

func GetPowHash(blockhash []byte) []byte {
	powhash := make([]byte, 32)
	C.x13bcd_hash((*C.char)(unsafe.Pointer(&blockhash[0])), (*C.char)(unsafe.Pointer(&powhash[0])))
	return powhash
}
