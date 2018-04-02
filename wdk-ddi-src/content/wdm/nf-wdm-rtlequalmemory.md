---
UID: NF:wdm.RtlEqualMemory
title: RtlEqualMemory macro
author: windows-driver-content
description: The RtlEqualMemory routine compares two blocks of memory to determine whether the specified number of bytes are identical.
old-location: kernel\rtlequalmemory.htm
old-project: kernel
ms.assetid: 43695fa9-32e1-4bd5-b146-88d6d03fe9fb
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: RtlEqualMemory, RtlEqualMemory routine [Kernel-Mode Driver Architecture], k109_a75dfbc8-12af-4f95-9ba0-b7752b796e55.xml, kernel.rtlequalmemory, wdm/RtlEqualMemory
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Desktop
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
req.lib: 
req.dll: 
req.irql: Any level (See Remarks section)
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Wdm.h
api_name:
-	RtlEqualMemory
product:
- Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# RtlEqualMemory function
The <b>RtlEqualMemory</b> routine compares two blocks of memory to determine whether the specified number of bytes are identical.

## Syntax

```
void RtlEqualMemory(
   Destination,
   Source,
   Length
);
```

## Parameters

`Destination`

TBD

`Source`

TBD

`Length`

Specifies the number of bytes to be compared.


## Return Value

None

## Remarks

<b>RtlEqualMemory</b> begins the comparison with byte zero of each block.

Callers of <b>RtlEqualMemory</b> can be running at any IRQL if both blocks of memory are resident.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 2000.  |
| **Target Platform** | Desktop |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **IRQL** | Any level (See Remarks section) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff561778">RtlCompareMemory</a>