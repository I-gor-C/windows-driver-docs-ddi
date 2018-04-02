---
UID: NF:wdm.ExInterlockedCompareExchange64
title: ExInterlockedCompareExchange64 macro
author: windows-driver-content
description: The ExInterlockedCompareExchange64 routine compares one integer variable to another and, if they are equal, sets the first variable to a caller-supplied value.
old-location: kernel\exinterlockedcompareexchange64.htm
old-project: kernel
ms.assetid: 7d13ca70-e05a-49e0-8dd8-5ab47b4d8169
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: ExInterlockedCompareExchange64, ExInterlockedCompareExchange64 routine [Kernel-Mode Driver Architecture], k102_424c24f9-3965-40fd-b02b-f9bf1f7df4ec.xml, kernel.exinterlockedcompareexchange64, wdm/ExInterlockedCompareExchange64
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
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
req.irql: Any level (see Remarks section)
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	ExInterlockedCompareExchange64
product:
- Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# ExInterlockedCompareExchange64 function
The <b>ExInterlockedCompareExchange64</b> routine compares one integer variable to another and, if they are equal, sets the first variable to a caller-supplied value.

## Syntax

```
void ExInterlockedCompareExchange64(
   Destination,
   Exchange,
   Comperand,
   Lock
);
```

## Parameters

`Destination`

A pointer to an integer that will be compared and possibly replaced.

`Exchange`

A pointer to an integer that will replace the one at <i>Destination</i> if the comparison results in equality.

`Comperand`

TBD

`Lock`

A pointer to a caller-allocated spin-lock that is used if the host system does not support an 8-byte atomic compare-and-exchange operation.


## Return Value

None

## Remarks

<b>ExInterlockedCompareExchange64</b> tests and, possibly, replaces the value of a given variable. For most underlying microprocessors, this routine is implemented inline by the compiler to execute as an atomic operation. If a spin lock is used, this routine can only be safely used on nonpaged parameters.

If the <i>Destination</i> and <i>Comparand</i> are unequal, <b>ExInterlockedCompareExchange64</b> simply returns the value of <i>Destination</i>.

<b>ExInterlockedCompareExchange64</b> is atomic only with respect to other <b>(Ex)Interlocked<i>Xxx</i></b> calls. 

Callers of <b>ExInterlockedCompareExchange64</b> can be running at any IRQL. The storage for the <i>Destination</i>, Comparand, and <i>Exchange</i> parameter and the list entries must be resident at all IRQLs.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 2000.  |
| **Target Platform** | Universal |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | Any level (see Remarks section) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff547853">InterlockedCompareExchange</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff547892">InterlockedExchange</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff547903">InterlockedExchangeAdd</a>