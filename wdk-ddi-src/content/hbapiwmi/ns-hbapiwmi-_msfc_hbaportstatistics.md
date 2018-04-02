---
UID: NS:hbapiwmi._MSFC_HBAPortStatistics
title: "_MSFC_HBAPortStatistics"
author: windows-driver-content
description: The MSFC_HBAPortStatistics structure contains statistics information about a port.
old-location: storage\msfc_hbaportstatistics.htm
old-project: storage
ms.assetid: 0274b3c7-c17e-45bf-867f-2b0f741b2ecb
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PMSFC_HBAPortStatistics, MSFC_HBAPortStatistics, MSFC_HBAPortStatistics structure [Storage Devices], PMSFC_HBAPortStatistics, PMSFC_HBAPortStatistics structure pointer [Storage Devices], _MSFC_HBAPortStatistics, hbapiwmi/MSFC_HBAPortStatistics, hbapiwmi/PMSFC_HBAPortStatistics, storage.msfc_hbaportstatistics, structs-Fibre_93c56324-f8c5-4d43-815a-40ca9d44350d.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: hbapiwmi.h
req.include-header: Hbapiwmi.h
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
-	hbapiwmi.h
api_name:
-	MSFC_HBAPortStatistics
product: Windows
targetos: Windows
req.typenames: MSFC_HBAPortStatistics, *PMSFC_HBAPortStatistics
---

# _MSFC_HBAPortStatistics structure
The MSFC_HBAPortStatistics structure contains statistics information about a port.

## Syntax
```
typedef struct _MSFC_HBAPortStatistics {
  LONGLONG SecondsSinceLastReset;
  LONGLONG TxFrames;
  LONGLONG TxWords;
  LONGLONG RxFrames;
  LONGLONG RxWords;
  LONGLONG LIPCount;
  LONGLONG NOSCount;
  LONGLONG ErrorFrames;
  LONGLONG DumpedFrames;
  LONGLONG LinkFailureCount;
  LONGLONG LossOfSyncCount;
  LONGLONG LossOfSignalCount;
  LONGLONG PrimitiveSeqProtocolErrCount;
  LONGLONG InvalidTxWordCount;
  LONGLONG InvalidCRCCount;
} *PMSFC_HBAPortStatistics, MSFC_HBAPortStatistics;
```

## Members


`SecondsSinceLastReset`

Contains the number of seconds since the statistics were last reset.

`TxFrames`

Contains the number of total transmitted fibre channel frames across all protocols and classes.

`TxWords`

Contains the number of total transmitted fibre channel words across all protocols and classes.

`RxFrames`

Contains the number of received fibre channel frames across all protocols and classes.

`RxWords`

Contains the number of received fibre channel words across all protocols and classes.

`LIPCount`

Contains the number of loop initialization primitive sequence (LIP) events that have occurred on a arbitrated loop.

`NOSCount`

Contains the number of nonoperational state primitive sequence (NOS) events that have occurred on the switched fabric.

`ErrorFrames`

Contains the number of frames that have been received in error.

`DumpedFrames`

Contains the number of frames that were lost due to a lack of host buffers available.

`LinkFailureCount`

Contains the link failure count.

`LossOfSyncCount`

Contains the loss of synchronization count.

`LossOfSignalCount`

Contains the loss of signal count.

`PrimitiveSeqProtocolErrCount`

Contains the primitive sequence protocol error count.

`InvalidTxWordCount`

Contains a count of the number of invalid transmissions.

`InvalidCRCCount`

Contains a count of the number frames with invalid cyclic redundancy checksums.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | hbapiwmi.h (include Hbapiwmi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff562513">MSFC_HBAPortStatistics WMI Class</a>