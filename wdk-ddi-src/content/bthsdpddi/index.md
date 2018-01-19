---
UID : NA:bthsdpddi
ms.assetid : 88ababa4-ac09-3370-b639-94a67fbff2d8
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# bthsdpddi.h header



bthsdpddi.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [PBYTESWAPUINT128](nc-bthsdpddi-pbyteswapuint128.md) | The Bluetooth SdpByteSwapUint128 function is used to reverse the byte order of an unsigned 128-bit integer. |
| [PBYTESWAPUINT64](nc-bthsdpddi-pbyteswapuint64.md) | The Bluetooth SdpByteSwapUint64 function is used to reverse the byte order of an unsigned 64-bit integer. |
| [PBYTESWAPUUID128](nc-bthsdpddi-pbyteswapuuid128.md) | The Bluetooth SdpByteSwapUuid128 function is used to reverse the byte order of a 128-bit universally unique identifier (UUID). |
| [PCONVERTSTREAMTOTREE](nc-bthsdpddi-pconvertstreamtotree.md) | The Bluetooth SdpConvertStreamToTree function is used to create a Microsoft proprietary tree-based representation of an SDP record, while leaving the original stream-based representation unmodified. |
| [PCONVERTTREETOSTREAM](nc-bthsdpddi-pconverttreetostream.md) | The Bluetooth SdpConvertTreeToStream function is used to produce a raw bytestream representation of an SDP record from a tree representation. The raw bytestream version is suitable for publication on a local SDP server. |
| [PGETNEXTELEMENT](nc-bthsdpddi-pgetnextelement.md) | The Bluetooth SdpGetNextElement function is used to iterate through the entries found in an SDP record stream. |
| [PRETRIEVEUINT64](nc-bthsdpddi-pretrieveuint64.md) | The Bluetooth SdpRetrieveUint128 function is used to copy an unaligned 128-bit integer from an SDP stream. |
| [PRETRIEVEUUID128](nc-bthsdpddi-pretrieveuuid128.md) | The Bluetooth SdpRetrieveUuid128 function is used to copy an unaligned 128-bit universally unique identifier (UUID) from an SDP stream. |
| [PVALIDATESTREAM](nc-bthsdpddi-pvalidatestream.md) | The Bluetooth SdpValidateStream function is used to parse a raw SDP record and determine if it contains errors. |



## Structures
| Title | Description |
| ---- |:---- |
| [_BTHDDI_SDP_NODE_INTERFACE](ns-bthsdpddi-_bthddi_sdp_node_interface.md) | The BTHDDI_SDP_NODE_INTERFACE structure provides functions for manipulating SDP records, including converting them to and from a tree representation that profile drivers can more easily parse. |
| [_BTHDDI_SDP_PARSE_INTERFACE](ns-bthsdpddi-_bthddi_sdp_parse_interface.md) | The BTHDDI_SDP_PARSE_INTERFACE structure provides functions for parsing SDP records. |