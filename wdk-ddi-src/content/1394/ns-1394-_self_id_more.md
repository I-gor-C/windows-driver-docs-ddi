---
UID: NS:1394._SELF_ID_MORE
title: "_SELF_ID_MORE"
author: windows-driver-content
description: The SELF_ID_MORE structure contains a raw packet one, two, or three self-ID packet. See the IEEE 1394 specification for details.
old-location: ieee\self_id_more.htm
old-project: IEEE
ms.assetid: d3c164a6-4830-4f1f-9fa5-5cd61e796e31
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: "*PSELF_ID_MORE, 1394/PSELF_ID_MORE, 1394/SELF_ID_MORE, 1394stct_cbfa017d-065b-45ce-ae08-6a6589c6b477.xml, IEEE.self_id_more, PSELF_ID_MORE, PSELF_ID_MORE structure pointer [Buses], SELF_ID_MORE, SELF_ID_MORE structure [Buses], _SELF_ID_MORE"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: 1394.h
req.include-header: 1394.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	1394.h
api_name:
-	SELF_ID_MORE
product:
- Windows
targetos: Windows
req.typenames: SELF_ID_MORE, *PSELF_ID_MORE
---

# _SELF_ID_MORE structure
The SELF_ID_MORE structure contains a raw packet one, two, or three self-ID packet. See the IEEE 1394 specification for details.

## Syntax
```
typedef struct _SELF_ID_MORE {
  ULONG  : 6 SID_Phys_ID;
  ULONG  : 2 SID_Packet_ID;
  ULONG  : 2 SID_PortA;
  ULONG  : 2 SID_Reserved2;
  ULONG  : 3 SID_Sequence;
  ULONG  : 1 SID_One;
  ULONG  : 2 SID_PortE;
  ULONG  : 2 SID_PortD;
  ULONG  : 2 SID_PortC;
  ULONG  : 2 SID_PortB;
  ULONG  : 1 SID_More_Packets;
  ULONG  : 1 SID_Reserved3;
  ULONG  : 2 SID_PortH;
  ULONG  : 2 SID_PortG;
  ULONG  : 2 SID_PortF;
} *PSELF_ID_MORE, SELF_ID_MORE;
```

## Members


`SID_Phys_ID`

Specifies the device node number. This member specifies bits 0-10 of the node address. This member contains bits 0-5 of byte 0 of the self ID packet.

`SID_Packet_ID`

Must be PHY_PACKET_ID_SELF_ID. This member specifies bits 0-10 of the node address. This member contains bits 6-7 of byte 0 of the self ID packet.

`SID_PortA`

Specifies port status. Possible values are:

SELF_ID_CONNECTED_TO_CHILD

SELF_ID_CONNECTED_TO_PARENT

SELF_ID_NOT_CONNECTED

SELF_ID_NOT_PRESENT

This member contains bits 0-1 of byte 1 of the self ID packet.

`SID_Reserved2`

Reserved. This member contains bits 2-3 of byte 1 of the self ID packet.

`SID_Sequence`

Specifies the packet number in sequence (the first SELF_ID_MORE packet is packet zero). This member contains bits 4-5 of byte 1 of the self ID packet.

`SID_One`

Always a 1. This member contains bit 6 of byte 1 of the self ID packet.

`SID_PortE`

Specifies port status. Possible values are:

SELF_ID_CONNECTED_TO_CHILD

SELF_ID_CONNECTED_TO_PARENT

SELF_ID_NOT_CONNECTED

SELF_ID_NOT_PRESENT

This member specifies bits 0-1 of byte 2 of the self ID packet.

`SID_PortD`

Specifies port status. Possible values are:

SELF_ID_CONNECTED_TO_CHILD

SELF_ID_CONNECTED_TO_PARENT

SELF_ID_NOT_CONNECTED

SELF_ID_NOT_PRESENT

This member specifies bits 2-3 of byte 2 of the self ID packet.

`SID_PortC`

Specifies port status. Possible values are:

SELF_ID_CONNECTED_TO_CHILD

SELF_ID_CONNECTED_TO_PARENT

SELF_ID_NOT_CONNECTED

SELF_ID_NOT_PRESENT

This member contains bits 4-5 of byte 2 of the self ID packet.

`SID_PortB`

Specifies port status. Possible values are:

SELF_ID_CONNECTED_TO_CHILD

SELF_ID_CONNECTED_TO_PARENT

SELF_ID_NOT_CONNECTED

SELF_ID_NOT_PRESENT

This member contains bits 6-7 of byte 2 of the self ID packet.

`SID_More_Packets`

One if this packet will be followed by more SELF_ID_MORE packets, zero otherwise. This member contains bit 0 of byte 3 of the self ID packet.

`SID_Reserved3`

Reserved. This member contains bit 1 of byte 3 of the self ID packet.

`SID_PortH`

Specifies port status. Possible values are:

SELF_ID_CONNECTED_TO_CHILD

SELF_ID_CONNECTED_TO_PARENT

SELF_ID_NOT_CONNECTED

SELF_ID_NOT_PRESENT

This member contains bits 2-3 of byte 3 of the self ID packet.

`SID_PortG`

Specifies port status. Possible values are:

SELF_ID_CONNECTED_TO_CHILD

SELF_ID_CONNECTED_TO_PARENT

SELF_ID_NOT_CONNECTED

SELF_ID_NOT_PRESENT

This member contains bits 4-5 of byte 3 of the self ID packet.

`SID_PortF`

Specifies port status. Possible values are:

SELF_ID_CONNECTED_TO_CHILD

SELF_ID_CONNECTED_TO_PARENT

SELF_ID_NOT_CONNECTED

SELF_ID_NOT_PRESENT

This member contains bits 6-7 of byte 3 of the self ID packet.

## Remarks
This structure corresponds to self ID packet 1, as described in the <i>P1394a</i> specification. Note that type 2 self ID packets are identical to type 1 packets, except that the last five fields are replaced by a reserved area. The SELF_ID_MORE structure can be used to access all of the significant information in both type 1 and type 2 self ID packets.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | 1394.h (include 1394.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff538877">TOPOLOGY_MAP</a>