---
UID: NF:ntifs.RtlCompareMemoryUlong
title: RtlCompareMemoryUlong function
author: windows-driver-content
description: The RtlCompareMemoryUlong routine returns how many bytes in a block of memory match a specified pattern.
old-location: ifsk\rtlcomparememoryulong.htm
old-project: ifsk
ms.assetid: 78ff21da-be0f-4b57-9162-1052a6c12b5c
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: RtlCompareMemoryUlong, RtlCompareMemoryUlong routine [Installable File System Drivers], ifsk.rtlcomparememoryulong, ntifs/RtlCompareMemoryUlong, rtlref_a220e168-945b-46d1-9aa7-7750bdfc39bd.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
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
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe (kernel mode); Ntdll.dll (user mode)
req.irql: Any level (see Remarks section)
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
-	Ntdll.dll
api_name:
-	RtlCompareMemoryUlong
product:
- Windows
targetos: Windows
req.typenames: TOKEN_TYPE
---


# RtlCompareMemoryUlong function
The <b>RtlCompareMemoryUlong</b> routine returns how many bytes in a block of memory match a specified pattern.

## Syntax

```
NTSYSAPI SIZE_T RtlCompareMemoryUlong(
  PVOID  Source,
  SIZE_T Length,
  ULONG  Pattern
);
```

## Parameters

`Source`

Pointer to a block of memory. Must be aligned on a ULONG boundary.

`Length`

Number of bytes over which the comparison should be done. Must be a multiple of <b>sizeof(</b>ULONG<b>)</b>.

`Pattern`

Pattern to be compared byte by byte, repeatedly, through the specified memory range.


## Return Value

<b>RtlCompareMemoryUlong</b> returns the number of bytes that were compared and found to be equal. If all bytes compare as equal, the input <i>Length</i> is returned. <b>RtlCompareMemoryUlong</b> returns zero if <i>Source</i> is not ULONG-aligned or if <i>Length</i> is not a multiple of <b>sizeof(</b>ULONG<b>)</b>.

## Remarks

If the block of memory at <i>Source</i> is nonpaged, the caller can be running at any IRQL. Otherwise, callers of <b>RtlCompareMemoryUlong</b> must be running at IRQL &lt; DISPATCH_LEVEL. 

For more information about managing buffered data and initializing driver-allocated buffers, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540656">Buffered Data and Buffer Initialization</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | ntifs.h (include Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe (kernel mode); Ntdll.dll (user mode) |
| **IRQL** | Any level (see Remarks section) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff561778">RtlCompareMemory</a>