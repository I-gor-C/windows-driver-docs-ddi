---
UID: NF:wdm.RtlFindLongestRunClear
title: RtlFindLongestRunClear function
author: windows-driver-content
description: The RtlFindLongestRunClear routine searches for the largest contiguous range of clear bits within a given bitmap.
old-location: kernel\rtlfindlongestrunclear.htm
old-project: kernel
ms.assetid: 6d68cb0f-d0b8-4468-8def-60a65780480e
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: RtlFindLongestRunClear, RtlFindLongestRunClear routine [Kernel-Mode Driver Architecture], k109_a6295996-9e2c-4d19-9ee9-1dc7802bd145.xml, kernel.rtlfindlongestrunclear, wdm/RtlFindLongestRunClear
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
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
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: "<= APC_LEVEL (See Remarks section)"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	RtlFindLongestRunClear
product: Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# RtlFindLongestRunClear function
The <b>RtlFindLongestRunClear</b> routine searches for the largest contiguous range of clear bits within a given bitmap.

## Syntax

```
NTSYSAPI ULONG RtlFindLongestRunClear(
  PRTL_BITMAP BitMapHeader,
  PULONG      StartingIndex
);
```

## Parameters

`BitMapHeader`

A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563614">RTL_BITMAP</a> structure that describes the bitmap. This structure must have been initialized by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561925">RtlInitializeBitMap</a> routine.

`StartingIndex`

Pointer to a variable in which the starting index of the longest clear run in the bitmap is returned. This is a zero-based value indicating the bit position of the first clear bit in the returned range.


## Return Value

<b>RtlFindLongestRunClear</b> returns either the number of bits in the run beginning at <i>StartingIndex</i>, or zero if it cannot find a run of clear bits within the bitmap.

## Remarks

A returned run can have a single clear bit.

Callers of <b>RtlFindLongestRunClear</b> must be running at IRQL &lt;= APC_LEVEL if the memory that contains the bitmap variable is pageable or the memory at <i>BitMapHeader</i> is pageable. Otherwise, <b>RtlFindLongestRunClear</b> can be called at any IRQL.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 2000.  |
| **Target Platform** | Universal |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | "<= APC_LEVEL (See Remarks section)" |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff563614">RTL_BITMAP</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561742">RtlAreBitsClear</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561873">RtlFindClearBits</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561875">RtlFindClearRuns</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561877">RtlFindFirstRunClear</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561879">RtlFindLastBackwardRunClear</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561881">RtlFindLongestRunClear</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561885">RtlFindNextForwardRunClear</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561925">RtlInitializeBitMap</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff562034">RtlNumberOfClearBits</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff562775">RtlSetBits</a>