---
UID: NS:ntddser._SERIALPERF_STATS
title: "_SERIALPERF_STATS"
author: windows-driver-content
description: The SERIALPERF_STATS structure contains performance statistics for a serial port.
old-location: serports\serialperf_stats.htm
old-project: serports
ms.assetid: 47CAAF39-40C6-4D7F-B8DA-5A60768E4CB0
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: "*PSERIALPERF_STATS, PSERIALPERF_STATS, PSERIALPERF_STATS structure pointer [Serial Ports], SERIALPERF_STATS, SERIALPERF_STATS structure [Serial Ports], _SERIALPERF_STATS, ntddser/PSERIALPERF_STATS, ntddser/SERIALPERF_STATS, serports.serialperf_stats"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddser.h
req.include-header: 
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
-	Ntddser.h
api_name:
-	SERIALPERF_STATS
product: Windows
targetos: Windows
req.typenames: SERIALPERF_STATS, *PSERIALPERF_STATS
---

# _SERIALPERF_STATS structure
The <b>SERIALPERF_STATS</b> structure contains performance statistics for a serial port.

## Syntax
```
typedef struct _SERIALPERF_STATS {
  ULONG ReceivedCount;
  ULONG TransmittedCount;
  ULONG FrameErrorCount;
  ULONG SerialOverrunErrorCount;
  ULONG BufferOverrunErrorCount;
  ULONG ParityErrorCount;
} SERIALPERF_STATS, *PSERIALPERF_STATS;
```

## Members


`ReceivedCount`

The number of characters received since either the serial port was opened or the last <a href="https://msdn.microsoft.com/library/windows/hardware/ff546538">IOCTL_SERIAL_CLEAR_STATS</a> request was processed.

`TransmittedCount`

The number of characters transmitted since either the serial port was opened or the last <b>IOCTL_SERIAL_CLEAR_STATS</b> request was processed.

`FrameErrorCount`

The number of frame errors detected since either the serial port was opened or the last <b>IOCTL_SERIAL_CLEAR_STATS</b> request was processed.

`SerialOverrunErrorCount`

The number of serial overrun errors detected since either the serial port was opened or the last <b>IOCTL_SERIAL_CLEAR_STATS</b> request was processed.

`BufferOverrunErrorCount`

The number of buffer overrun errors detected since either the serial port was opened or the last <b>IOCTL_SERIAL_CLEAR_STATS</b> request was processed.

`ParityErrorCount`

The number of parity errors detected since either the serial port was opened or the last <b>IOCTL_SERIAL_CLEAR_STATS</b> request was processed.

## Remarks
This structure is used by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546600">IOCTL_SERIAL_GET_STATS</a> request.

To reset the performance statistics to zero, send an <a href="https://msdn.microsoft.com/library/windows/hardware/ff546538">IOCTL_SERIAL_CLEAR_STATS</a> request.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddser.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff546538">IOCTL_SERIAL_CLEAR_STATS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff546600">IOCTL_SERIAL_GET_STATS</a>