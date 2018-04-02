---
UID: NF:rxprocs.RxLogEventWithAnnotation
title: RxLogEventWithAnnotation function
author: windows-driver-content
description: RxLogEventWithAnnotation allocates an I/O error log structure, fills it in with information, and writes the entry to the I/O error log.
old-location: ifsk\rxlogeventwithannotation.htm
old-project: ifsk
ms.assetid: cb8b757a-cff5-41cf-8155-2c45a8a35f00
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: RxLogEventWithAnnotation, RxLogEventWithAnnotation function [Installable File System Drivers], ifsk.rxlogeventwithannotation, rxprocs/RxLogEventWithAnnotation, rxref_9c7d3613-cf3b-4de9-bfcb-a1dbe9213834.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: rxprocs.h
req.include-header: Rxprocs.h, Rxstruc.h
req.target-type: Desktop
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
req.irql: "<= APC_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	rxprocs.h
api_name:
-	RxLogEventWithAnnotation
product:
- Windows
targetos: Windows
req.typenames: RX_CONTEXT, *PRX_CONTEXT
req.product: Windows 10 or later.
---


# RxLogEventWithAnnotation function
<b>RxLogEventWithAnnotation</b> allocates an I/O error log structure, fills it in with information, and writes the entry to the I/O error log.

## Syntax

```
void RxLogEventWithAnnotation(
  IN PRDBSS_DEVICE_OBJECT DeviceObject,
  IN ULONG                EventId,
  IN NTSTATUS             Status,
  IN PVOID                DataBuffer,
  IN USHORT               DataBufferLength,
  IN PUNICODE_STRING      Annotation,
  IN ULONG                AnnotationCount
);
```

## Parameters

`DeviceObject`

A pointer to the RDBSS device object.

`EventId`

TBD

`Status`

TBD

`DataBuffer`

TBD

`DataBufferLength`

TBD

`Annotation`

TBD

`AnnotationCount`

The count of the number of annotation strings to add to the I/O error log structure.


## Return Value

None

## Remarks

A network mini-redirector would call <b>RxLogEventWithAnnotation</b> to log an I/O error.

The I/O error log entry size is limited to a length of 255 characters. So if the combined length of the <i>Id</i>, <i>RawDataBuffer</i>, and <i>Annotations</i> parameters plus the size of the fixed part of the I/O error log entry exceeds 255, then <b>RxLogEventWithAnnotation</b> will silently fail and no I/O error log entry will be created.

The <b>RxLogEventWithAnnotation</b> routine needs to allocate memory in order to create the I/O error log entry . Consequently, <b>RxLogEventWithAnnotation</b> can silently fail if the memory allocation fails.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | rxprocs.h (include Rxprocs.h, Rxstruc.h) |
| **IRQL** | "<= APC_LEVEL" |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff554515">RxLogEventDirect</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff554524">RxLogEventWithBufferDirect</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff557368">_RxLog</a>