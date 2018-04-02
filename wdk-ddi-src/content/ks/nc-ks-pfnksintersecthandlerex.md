---
UID: NC:ks.PFNKSINTERSECTHANDLEREX
title: PFNKSINTERSECTHANDLEREX
author: windows-driver-content
description: AVStream calls a minidriver's AVStrMiniIntersectHandlerEx routine to determine the highest quality intersection of two data ranges.
old-location: stream\avstrminiintersecthandlerex.htm
old-project: stream
ms.assetid: d80f8bc6-29dc-4cb0-87f5-414ec6418156
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: AVStrMiniIntersectHandlerEx, AVStrMiniIntersectHandlerEx routine [Streaming Media Devices], PFNKSINTERSECTHANDLEREX, avstclbk_7a9be78c-3ca2-4fe2-961c-37dbd122a4b8.xml, ks/AVStrMiniIntersectHandlerEx, stream.avstrminiintersecthandlerex
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ks.h
req.include-header: 
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	ks.h
api_name:
-	AVStrMiniIntersectHandlerEx
product: Windows
targetos: Windows
req.typenames: SOUNDDETECTOR_PATTERNHEADER
---


# PFNKSINTERSECTHANDLEREX callback function
AVStream calls a minidriver's <i>AVStrMiniIntersectHandlerEx</i> routine to determine the highest quality intersection of two data ranges.

## Syntax

```
PFNKSINTERSECTHANDLEREX Pfnksintersecthandlerex;

NTSTATUS Pfnksintersecthandlerex(
  PVOID Context,
  PIRP Irp,
  PKSP_PIN Pin,
  PKSDATARANGE DataRange,
  PKSDATARANGE MatchingDataRange,
  ULONG DataBufferSize,
  PVOID Data,
  PULONG DataSize
)
{...}
```

## Parameters

`Context`

Pointer to the <b>Context</b> member of the corresponding <a href="https://msdn.microsoft.com/library/windows/hardware/ff562522">KSFILTER</a> structure.

`Irp`

Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550694">IRP</a> containing the intersection request.

`Pin`

Pointer to a structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff566722">KSP_PIN</a> that was passed in the intersection property request.

`DataRange`

Pointer to an array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff561658">KSDATARANGE</a> structures.

`MatchingDataRange`

Pointer to an array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff561658">KSDATARANGE</a> structures to match to <i>DataRange</i>.

`DataBufferSize`

Specifies a value of type ULONG that contains the size of the data buffer.

`Data`

Pointer to an optional data buffer in which the minidriver outputs the intersection.

`DataSize`

Pointer to a value of type ULONG specifying the size of the data buffer.


## Return Value

If the callback finds a match, return STATUS_SUCCESS. Otherwise return STATUS_NO_MATCH.

## Remarks

The minidriver specifies this routine's address in the <b>IntersectHandler</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563534">KSPIN_DESCRIPTOR_EX</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | ks.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff561658">KSDATARANGE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff562522">KSFILTER</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff563534">KSPIN_DESCRIPTOR_EX</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff565198">KSPROPERTY_PIN_DATAINTERSECTION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff566722">KSP_PIN</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff563499">KsPinDataIntersectionEx</a>