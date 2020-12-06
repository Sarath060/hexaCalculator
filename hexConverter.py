import struct


# rawHexHex = input("Enter The Hex 32 Bit \n")


def hexTOBytes(rawHex):
    bins = []
    print(rawHex)
    for x in range(0, len(rawHex), 2):
        bins.insert(x, rawHex[x:x + 2])
    return bins


def bytes1(rawHex):

    result = ["Base:"]
    rawHex = str(format(int(rawHex, 16), '#04x'))[2:]
    print("byte1 Conversion Started", rawHex)

    rawInt = int(rawHex, 16)

    #'''''''''''''''''''''''''''''''''''''''''''''''''''
    # base
    # Binary
    bin_A = bin(int(rawHex, 16))[2:].zfill(8)
    result.append(f"Binary  8 bit : {' '.join(bin_A[i:i + 4] for i in range(0, 8, 4))}")
    # Octa
    result.append(f"Octa Decimal 8 bit : {rawInt:03o}")
    # Decimal
    result.append(f"Decimal 8 bit : {rawInt:#03d}")
    # Hex
    result.append(f"Hexa Decimal 8 bit : {rawHex}")


    # ASCII
    # rawHex_byte = bytes.fromhex(rawHex_ABCD)
    result.append(f"ASCII : {bytes.fromhex(rawHex).decode('iso-8859-1')}")

    # UINT8
    result.append(f"\nUnsigned Integer 8 bit : {struct.unpack('>B', bytes.fromhex(rawHex))[0]}")
    # INT8
    result.append(f"\nSigned Integer 8 bit : {struct.unpack('>b', bytes.fromhex(rawHex))[0]}")

    return result


def bytes2(rawHex):

    result = []
    rawHex = str(format(int(rawHex, 16), '#06x'))[2:]
    print("byte2 Conversion Started", rawHex)

    rawInt = int(rawHex, 16)

    #'''''''''''''''''''''''''''''''''''''''''''''''''''
    # base
    # Binary
    bin_A = bin(int(rawHex, 16))[2:].zfill(16)
    result.append(f"Binary  16 bit : {' '.join(bin_A[i:i + 4] for i in range(0, 16, 4))}")
    # Octa
    result.append(f"Octa Decimal 16 bit : {rawInt:06o}")
    # Decimal
    result.append(f"Decimal 16 bit : {rawInt:#05d}")
    # Hex
    result.append(f"Hexa Decimal 16 bit : {rawHex}")

    #'''''''''''''''''''''''''''''''''''''''''''''''''''
    # UINT16
    result.append(f"\nUnsigned Integer 16 bit : 0x{rawHex}")
    result.append(f"Big Endian (AB)    : {struct.unpack('>H', bytes.fromhex(rawHex))[0]}")
    result.append(f"Little Endian (BA) : {struct.unpack('<H', bytes.fromhex(rawHex))[0]}")

    # INT16
    result.append(f"\nSigned Integer 16 bit : 0x{rawHex}")
    result.append(f"Big Endian (AB)     : {struct.unpack('>h', bytes.fromhex(rawHex))[0]}")
    result.append(f"Little Endian (BA)  : {struct.unpack('<h', bytes.fromhex(rawHex))[0]}")

    # UINT8
    result.append(f"\nSigned Integer 8 bit : 0x{rawHex}")
    result.append(f"(A) 8 bit : {struct.unpack('>B', bytes.fromhex(rawHex[:2]))[0]}")
    result.append(f"(B) 8 bit : {struct.unpack('>B', bytes.fromhex(rawHex[2:]))[0]}")
    # INT8
    result.append(f"\nSigned Integer 8 bit : 0x{rawHex}")
    result.append(f"(A) 8 bit : {struct.unpack('>b', bytes.fromhex(rawHex[:2]))[0]}")
    result.append(f"(B) 8 bit : {struct.unpack('>b', bytes.fromhex(rawHex[2:]))[0]}")

    return result


def bytes4(rawHex):

    result = []
    rawHex = str(format(int(rawHex, 16), '#010x'))[2:]
    print("byte4 Conversion Started", rawHex)
    rawHex_bytes = hexTOBytes(rawHex)
    # print(rawHex_bytes)
    rawHex_ABCD = ''.join([rawHex_bytes[i] for i in[0, 1, 2, 3]])
    rawHex_DCBA = ''.join([rawHex_bytes[i] for i in[3, 2, 1, 0]])
    rawHex_BADC = ''.join([rawHex_bytes[i] for i in[1, 0, 3, 2]])
    rawHex_CDAB = ''.join([rawHex_bytes[i] for i in[2, 3, 0, 1]])
    rawHex_AB = ''.join([rawHex_bytes[i] for i in [0, 1]])
    rawHex_CD = ''.join([rawHex_bytes[i] for i in [2, 3]])

    rawInt = int(rawHex, 16)

    #'''''''''''''''''''''''''''''''''''''''''''''''''''
    # base
    # Binary
    bin_A = bin(int(rawHex, 16))[2:].zfill(32)
    result.append(f"Binary  32 bit : {' '.join(bin_A[i:i + 4] for i in range(0, 32, 4))}")
    # Octa
    result.append(f"Octa Decimal 32 bit : {rawInt:013o}")
    # Decimal
    result.append(f"Decimal 32 bit : {rawInt:#010d}")
    # Hex
    result.append(f"Hexa Decimal 32 bit : {rawHex}")

    # Float
    result.append(f"\nFolating Point 32 bit : 0x{rawHex}")
    result.append(f"Big Endian (ABCD)       : {struct.unpack('>f', bytes.fromhex(rawHex_ABCD))[0]}")
    result.append(f"Little Endian (DCBA)    : {struct.unpack('>f', bytes.fromhex(rawHex_DCBA))[0]}")
    result.append(f"Mid-Big Endian (BADC)   : {struct.unpack('>f', bytes.fromhex(rawHex_BADC))[0]}")
    result.append(f"Mid-Little Endian (CDAB): {struct.unpack('>f', bytes.fromhex(rawHex_CDAB))[0]}")

    # UINT32

    result.append(f"\nUnsigned Integer 32 bit : 0x{rawHex}")
    result.append(f"Big Endian (ABCD)       : {struct.unpack('>I', bytes.fromhex(rawHex_ABCD))[0]}")
    result.append(f"Little Endian (DCBA)    : {struct.unpack('>I', bytes.fromhex(rawHex_DCBA))[0]}")
    result.append(f"Mid-Big Endian (BADC)   : {struct.unpack('>I', bytes.fromhex(rawHex_BADC))[0]}")
    result.append(f"Mid-Little Endian (CDAB): {struct.unpack('>I', bytes.fromhex(rawHex_CDAB))[0]}")


    # INT32

    result.append(f"\nSigned Integer 32 bit : 0x{rawHex}")
    result.append(f"Big Endian (ABCD)       : {struct.unpack('>i', bytes.fromhex(rawHex_ABCD))[0]}")
    result.append(f"Little Endian (DCBA)    : {struct.unpack('>i', bytes.fromhex(rawHex_DCBA))[0]}")
    result.append(f"Mid-Big Endian (BADC)   : {struct.unpack('>i', bytes.fromhex(rawHex_BADC))[0]}")
    result.append(f"Mid-Little Endian (CDAB): {struct.unpack('>i', bytes.fromhex(rawHex_CDAB))[0]}")

    # UINT16
    result.append(f"\nUnsigned Integer 16 bit : 0x{rawHex}")
    result.append(f"Big Endian (AB)    : {struct.unpack('>H', bytes.fromhex(rawHex_AB))[0]}")
    result.append(f"Little Endian (BA) : {struct.unpack('<H', bytes.fromhex(rawHex_AB))[0]}")
    result.append(f"Big Endian (CD)    : {struct.unpack('>H', bytes.fromhex(rawHex_CD))[0]}")
    result.append(f"Little Endian (DC) : {struct.unpack('<H', bytes.fromhex(rawHex_CD))[0]}")

    # INT16
    result.append(f"\nSigned Integer 16 bit : 0x{rawHex}")
    result.append(f"Big Endian (AB)     : {struct.unpack('>h', bytes.fromhex(rawHex_AB))[0]}")
    result.append(f"Little Endian (BA)  : {struct.unpack('<h', bytes.fromhex(rawHex_AB))[0]}")
    result.append(f"Big Endian (CD)     : {struct.unpack('>h', bytes.fromhex(rawHex_CD))[0]}")
    result.append(f"Little Endian (DC)  : {struct.unpack('<h', bytes.fromhex(rawHex_CD))[0]}")

    # UINT8
    result.append(f"\nSigned Integer 8 bit : 0x{rawHex}")
    result.append(f"(A) 8 bit : {struct.unpack('>B', bytes.fromhex(rawHex_bytes[0]))[0]}")
    result.append(f"(B) 8 bit : {struct.unpack('>B', bytes.fromhex(rawHex_bytes[1]))[0]}")
    result.append(f"(C) 8 bit : {struct.unpack('>B', bytes.fromhex(rawHex_bytes[2]))[0]}")
    result.append(f"(D) 8 bit : {struct.unpack('>B', bytes.fromhex(rawHex_bytes[3]))[0]}")
    # INT8
    result.append(f"\nSigned Integer 8 bit : 0x{rawHex}")
    result.append(f"(A) 8 bit : {struct.unpack('>b', bytes.fromhex(rawHex_bytes[0]))[0]}")
    result.append(f"(B) 8 bit : {struct.unpack('>b', bytes.fromhex(rawHex_bytes[1]))[0]}")
    result.append(f"(C) 8 bit : {struct.unpack('>b', bytes.fromhex(rawHex_bytes[2]))[0]}")
    result.append(f"(D) 8 bit : {struct.unpack('>b', bytes.fromhex(rawHex_bytes[3]))[0]}")

    return result


def bytes8(rawHex):

    result = []
    rawHex = str(format(int(rawHex, 16), '#018x'))[2:]
    print("byte8 Conversion Started", rawHex)
    rawHex_bytes = hexTOBytes(rawHex)
    # print(rawHex_bytes)
    rawHex_ABCD = ''.join([rawHex_bytes[i] for i in[0, 1, 2, 3]])
    rawHex_DCBA = ''.join([rawHex_bytes[i] for i in[3, 2, 1, 0]])
    rawHex_BADC = ''.join([rawHex_bytes[i] for i in[1, 0, 3, 2]])
    rawHex_CDAB = ''.join([rawHex_bytes[i] for i in[2, 3, 0, 1]])
    rawHex_EFGH = ''.join([rawHex_bytes[i] for i in[4, 5, 6, 7]])
    rawHex_HGEF = ''.join([rawHex_bytes[i] for i in[7, 6, 5, 4]])
    rawHex_FEHG = ''.join([rawHex_bytes[i] for i in[5, 4, 7, 6]])
    rawHex_GHFE = ''.join([rawHex_bytes[i] for i in[6, 7, 4, 5]])

    rawHex_AB = ''.join([rawHex_bytes[i] for i in [0, 1]])
    rawHex_CD = ''.join([rawHex_bytes[i] for i in [2, 3]])
    rawHex_EF = ''.join([rawHex_bytes[i] for i in [4, 5]])
    rawHex_GH = ''.join([rawHex_bytes[i] for i in [6, 7]])

    rawInt = int(rawHex, 16)

    # '''''''''''''''''''''''''''''''''''''''''''''''''''
    # base
    # Binary
    bin_ABCD = bin(int(rawHex_ABCD, 16))[2:].zfill(64)
    result.append(f"Binary  (ABCD) 32bit : {' '.join(bin_ABCD[i:i + 4] for i in range(0, 64, 4))}")
    bin_EFGH = bin(int(rawHex_EFGH, 16))[2:].zfill(64)
    result.append(f"Binary  (EFGH) 32 bit : {' '.join(bin_EFGH[i:i + 4] for i in range(0, 64, 4))}")
    # Octa
    result.append(f"Octa Decimal 64 bit : {rawInt:013o}")
    # Decimal
    result.append(f"Decimal 64 bit : {rawInt:#010d}")
    # Hex
    result.append(f"Hexa Decimal 64 bit : {rawHex}")

    # Float
    result.append(f"\nFolating Point 64 bit : 0x{rawHex}")
    result.append(f"Big Endian (ABCDEFGH)\t\t: {struct.unpack('>d', bytes.fromhex(rawHex_ABCD+rawHex_EFGH))[0]}")
    result.append(f"Little Endian (HGFEDCBA)\t: {struct.unpack('>d', bytes.fromhex(rawHex_HGEF+rawHex_DCBA))[0]}")
    result.append(f"Mid-Big Endian (BADCFEHG)\t: {struct.unpack('>d', bytes.fromhex(rawHex_BADC+rawHex_FEHG))[0]}")
    result.append(f"Mid-Little Endian (GHEFCDAB): {struct.unpack('>d', bytes.fromhex(rawHex_GHFE+rawHex_CDAB))[0]}")

    # UINT64
    result.append(f"\nFolating Point 64 bit : 0x{rawHex}")
    result.append(f"Big Endian (ABCDEFGH)\t\t: {struct.unpack('>Q', bytes.fromhex(rawHex_ABCD+rawHex_EFGH))[0]}")
    result.append(f"Little Endian (HGFEDCBA)\t: {struct.unpack('>Q', bytes.fromhex(rawHex_HGEF+rawHex_DCBA))[0]}")
    result.append(f"Mid-Big Endian (BADCFEHG)\t: {struct.unpack('>Q', bytes.fromhex(rawHex_BADC+rawHex_FEHG))[0]}")
    result.append(f"Mid-Little Endian (GHEFCDAB): {struct.unpack('>Q', bytes.fromhex(rawHex_GHFE+rawHex_CDAB))[0]}")

    # INT64
    result.append(f"\nFolating Point 64 bit : 0x{rawHex}")
    result.append(f"Big Endian (ABCDEFGH)\t\t: {struct.unpack('>q', bytes.fromhex(rawHex_ABCD+rawHex_EFGH))[0]}")
    result.append(f"Little Endian (HGFEDCBA)\t: {struct.unpack('>q', bytes.fromhex(rawHex_HGEF+rawHex_DCBA))[0]}")
    result.append(f"Mid-Big Endian (BADCFEHG)\t: {struct.unpack('>q', bytes.fromhex(rawHex_BADC+rawHex_FEHG))[0]}")
    result.append(f"Mid-Little Endian (GHEFCDAB): {struct.unpack('>q', bytes.fromhex(rawHex_GHFE+rawHex_CDAB))[0]}")

    # Float
    result.append(f"\nFolating Point 32 bit : 0x{rawHex}")
    result.append(f"Big Endian (ABCD)       : {struct.unpack('>f', bytes.fromhex(rawHex_ABCD))[0]}")
    result.append(f"Little Endian (DCBA)    : {struct.unpack('>f', bytes.fromhex(rawHex_DCBA))[0]}")
    result.append(f"Mid-Big Endian (BADC)   : {struct.unpack('>f', bytes.fromhex(rawHex_BADC))[0]}")
    result.append(f"Mid-Little Endian (CDAB): {struct.unpack('>f', bytes.fromhex(rawHex_CDAB))[0]}")
    result.append(f"Big Endian (EFGH)       : {struct.unpack('>f', bytes.fromhex(rawHex_EFGH))[0]}")
    result.append(f"Little Endian (HGFE)    : {struct.unpack('>f', bytes.fromhex(rawHex_HGEF))[0]}")
    result.append(f"Mid-Big Endian (FEHG)   : {struct.unpack('>f', bytes.fromhex(rawHex_FEHG))[0]}")
    result.append(f"Mid-Little Endian (GHEF): {struct.unpack('>f', bytes.fromhex(rawHex_GHFE))[0]}")

    # UINT32

    result.append(f"\nUnsigned Integer 32 bit : 0x{rawHex}")
    result.append(f"Big Endian (ABCD)       : {struct.unpack('>I', bytes.fromhex(rawHex_ABCD))[0]}")
    result.append(f"Little Endian (DCBA)    : {struct.unpack('>I', bytes.fromhex(rawHex_DCBA))[0]}")
    result.append(f"Mid-Big Endian (BADC)   : {struct.unpack('>I', bytes.fromhex(rawHex_BADC))[0]}")
    result.append(f"Mid-Little Endian (CDAB): {struct.unpack('>I', bytes.fromhex(rawHex_CDAB))[0]}")
    result.append(f"Big Endian (EFGH)       : {struct.unpack('>I', bytes.fromhex(rawHex_EFGH))[0]}")
    result.append(f"Little Endian (HGFE)    : {struct.unpack('>I', bytes.fromhex(rawHex_HGEF))[0]}")
    result.append(f"Mid-Big Endian (FEHG)   : {struct.unpack('>I', bytes.fromhex(rawHex_FEHG))[0]}")
    result.append(f"Mid-Little Endian (GHEF): {struct.unpack('>I', bytes.fromhex(rawHex_GHFE))[0]}")


    # INT32

    result.append(f"\nSigned Integer 32 bit : 0x{rawHex}")
    result.append(f"Big Endian (ABCD)       : {struct.unpack('>i', bytes.fromhex(rawHex_ABCD))[0]}")
    result.append(f"Little Endian (DCBA)    : {struct.unpack('>i', bytes.fromhex(rawHex_DCBA))[0]}")
    result.append(f"Mid-Big Endian (BADC)   : {struct.unpack('>i', bytes.fromhex(rawHex_BADC))[0]}")
    result.append(f"Mid-Little Endian (CDAB): {struct.unpack('>i', bytes.fromhex(rawHex_CDAB))[0]}")
    result.append(f"Big Endian (EFGH)       : {struct.unpack('>i', bytes.fromhex(rawHex_EFGH))[0]}")
    result.append(f"Little Endian (HGFE)    : {struct.unpack('>i', bytes.fromhex(rawHex_HGEF))[0]}")
    result.append(f"Mid-Big Endian (FEHG)   : {struct.unpack('>i', bytes.fromhex(rawHex_FEHG))[0]}")
    result.append(f"Mid-Little Endian (GHEF): {struct.unpack('>i', bytes.fromhex(rawHex_GHFE))[0]}")

    # UINT16
    result.append(f"\nUnsigned Integer 16 bit : 0x{rawHex}")
    result.append(f"Big Endian (AB)    : {struct.unpack('>H', bytes.fromhex(rawHex_AB))[0]}")
    result.append(f"Little Endian (BA) : {struct.unpack('<H', bytes.fromhex(rawHex_AB))[0]}")
    result.append(f"Big Endian (CD)    : {struct.unpack('>H', bytes.fromhex(rawHex_CD))[0]}")
    result.append(f"Little Endian (DC) : {struct.unpack('<H', bytes.fromhex(rawHex_CD))[0]}")
    result.append(f"Big Endian (EF)    : {struct.unpack('>H', bytes.fromhex(rawHex_EF))[0]}")
    result.append(f"Little Endian (FE) : {struct.unpack('<H', bytes.fromhex(rawHex_EF))[0]}")
    result.append(f"Big Endian (GH)    : {struct.unpack('>H', bytes.fromhex(rawHex_GH))[0]}")
    result.append(f"Little Endian (HG) : {struct.unpack('<H', bytes.fromhex(rawHex_GH))[0]}")

    # INT16
    result.append(f"\nSigned Integer 16 bit : 0x{rawHex}")
    result.append(f"Big Endian (AB)     : {struct.unpack('>h', bytes.fromhex(rawHex_AB))[0]}")
    result.append(f"Little Endian (BA)  : {struct.unpack('<h', bytes.fromhex(rawHex_AB))[0]}")
    result.append(f"Big Endian (CD)     : {struct.unpack('>h', bytes.fromhex(rawHex_CD))[0]}")
    result.append(f"Little Endian (DC)  : {struct.unpack('<h', bytes.fromhex(rawHex_CD))[0]}")
    result.append(f"Big Endian (EF)    : {struct.unpack('>h', bytes.fromhex(rawHex_EF))[0]}")
    result.append(f"Little Endian (FE) : {struct.unpack('<h', bytes.fromhex(rawHex_EF))[0]}")
    result.append(f"Big Endian (GH)    : {struct.unpack('>h', bytes.fromhex(rawHex_GH))[0]}")
    result.append(f"Little Endian (HG) : {struct.unpack('<h', bytes.fromhex(rawHex_GH))[0]}")

    # UINT8
    result.append(f"\nSigned Integer 8 bit : 0x{rawHex}")
    result.append(f"(A) 8 bit : {struct.unpack('>B', bytes.fromhex(rawHex_bytes[0]))[0]}")
    result.append(f"(B) 8 bit : {struct.unpack('>B', bytes.fromhex(rawHex_bytes[1]))[0]}")
    result.append(f"(C) 8 bit : {struct.unpack('>B', bytes.fromhex(rawHex_bytes[2]))[0]}")
    result.append(f"(D) 8 bit : {struct.unpack('>B', bytes.fromhex(rawHex_bytes[3]))[0]}")
    result.append(f"(E) 8 bit : {struct.unpack('>B', bytes.fromhex(rawHex_bytes[4]))[0]}")
    result.append(f"(F) 8 bit : {struct.unpack('>B', bytes.fromhex(rawHex_bytes[5]))[0]}")
    result.append(f"(G) 8 bit : {struct.unpack('>B', bytes.fromhex(rawHex_bytes[6]))[0]}")
    result.append(f"(H) 8 bit : {struct.unpack('>B', bytes.fromhex(rawHex_bytes[7]))[0]}")

    # INT8
    result.append(f"\nSigned Integer 8 bit : 0x{rawHex}")
    result.append(f"(A) 8 bit : {struct.unpack('>b', bytes.fromhex(rawHex_bytes[0]))[0]}")
    result.append(f"(B) 8 bit : {struct.unpack('>b', bytes.fromhex(rawHex_bytes[1]))[0]}")
    result.append(f"(C) 8 bit : {struct.unpack('>b', bytes.fromhex(rawHex_bytes[2]))[0]}")
    result.append(f"(D) 8 bit : {struct.unpack('>b', bytes.fromhex(rawHex_bytes[3]))[0]}")
    result.append(f"(E) 8 bit : {struct.unpack('>b', bytes.fromhex(rawHex_bytes[4]))[0]}")
    result.append(f"(F) 8 bit : {struct.unpack('>b', bytes.fromhex(rawHex_bytes[5]))[0]}")
    result.append(f"(G) 8 bit : {struct.unpack('>b', bytes.fromhex(rawHex_bytes[6]))[0]}")
    result.append(f"(H) 8 bit : {struct.unpack('>b', bytes.fromhex(rawHex_bytes[7]))[0]}")

    return result


def conversion(rawHex, byte):
    result = ["Output:\n"]
    print(rawHex, byte, len(rawHex))
    if byte == 1 and len(rawHex) <= 2:
        result = bytes1(rawHex)
    elif byte == 2 and len(rawHex) <= 4 :
        result = bytes2(rawHex)
    elif byte == 4 and len(rawHex) <= 8:
        result = bytes4(rawHex)
    elif byte == 8 and len(rawHex) <= 16:
        result = bytes8(rawHex)
    else:
        result.append(f"Value is greater than {byte} bytes Hex:{rawHex} Len:{len(rawHex)}")

    result.insert(0, "Output:\n")
    return result


if __name__ == '__main__':
    byt = input("Enter Number of Bytes\n")
    raw = input("Enter The Hexdecimal \n")
    # print(format(rawHexHex, '#010x'))
    out = conversion(raw, int(byt , 10))
    print('\n'.join(out))
