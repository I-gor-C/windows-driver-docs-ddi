---
UID: NS:61883._IPCR
title: "_IPCR"
author: windows-driver-content
description: The IPCR structure contains initialization values for an input plug.
old-location: ieee\ipcr.htm
old-project: IEEE
ms.assetid: 81c89fbc-5d58-4983-b591-765a7818b932
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: "*PIPCR, 61883/IPCR, 61883/PIPCR, 61883_structures_e7226c37-f3b1-4e57-977a-6fb25c853f19.xml, IEEE.ipcr, IPCR, IPCR structure [Buses], PIPCR, PIPCR structure pointer [Buses], _IPCR"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: 61883.h
req.include-header: 61883.h
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
-	61883.h
api_name:
-	IPCR
product:
- Windows
targetos: Windows
req.typenames: IPCR, *PIPCR
---

# _IPCR structure
The IPCR structure contains initialization values for an input plug.

## Syntax
```
typedef struct _IPCR {
  ULONG  : 16 Reserved0;
  ULONG  : 6  Channel;
  ULONG  : 2  Reserved1;
  ULONG  : 6  PPCCounter;
  ULONG  : 1  BCCCounter;
  ULONG  : 1  OnLine;
} IPCR, *PIPCR;
```

## Members


`Reserved0`

Reserved.

`Channel`

Indicates the channel number that the input plug shall use to transmit the isochronous data flow, for a suspended input plug. For an active input plug it indicates the actual channel number that the input plug uses to transmit the isochronous data flow. For an unconnected input plug it has no meaning.

`Reserved1`

Reserved.

`PPCCounter`

Indicates the number of point-to-point connections to the input plug.

`BCCCounter`

Indicates, when one, that there is a broadcast-in connection to the input plug. When zero it indicates that there is no connection.

`OnLine`

Indicates, when one, that the corresponding input plug is on-line. When zero it indicates that the input plug is off-line.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | 61883.h (include 61883.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff537010">AV_PCR</a>