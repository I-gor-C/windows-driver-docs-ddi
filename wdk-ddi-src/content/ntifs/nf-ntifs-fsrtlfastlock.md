---
UID: NF:ntifs.FsRtlFastLock
title: FsRtlFastLock macro
author: windows-driver-content
description: The FsRtlFastLock macro is used by file systems and filter drivers to request a byte-range lock for a file stream.
old-location: ifsk\fsrtlfastlock.htm
old-project: ifsk
ms.assetid: c3e209b5-9925-4911-8c42-0f15c1c710be
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: FsRtlFastLock, FsRtlFastLock function [Installable File System Drivers], fsrtlref_c60db87b-ac5a-4c60-83f2-7381e0156806.xml, ifsk.fsrtlfastlock, ntifs/FsRtlFastLock
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: ntifs.h
req.include-header: Ntifs.h
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
-	ntifs.h
api_name:
-	FsRtlFastLock
product: Windows
targetos: Windows
req.typenames: TOKEN_TYPE
---


# FsRtlFastLock function
The <b>FsRtlFastLock</b> macro is used by file systems and filter drivers to request a byte-range lock for a file stream.

## Syntax

```
void FsRtlFastLock(
   A1,
   A2,
   A3,
   A4,
   A5,
   A6,
   A7,
   A8,
   A9,
   A10,
   A11
);
```

## Parameters

`A1`

TBD

`A2`

TBD

`A3`

TBD

`A4`

TBD

`A5`

TBD

`A6`

TBD

`A7`

TBD

`A8`

TBD

`A9`

TBD

`A10`

TBD

`A11`

TBD


## Return Value

None

## Remarks

The <b>FsRtlFastLock</b> macro causes the caller to acquire a byte-range lock on a region of the specified file.

A return value of <b>TRUE</b> indicates that the IO_STATUS_BLOCK structure pointed to by <i>Iosb</i> received status information about the lock operation. To examine the contents of this structure, use the NT_STATUS macro.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | ntifs.h (include Ntifs.h) |
| **IRQL** | "<= APC_LEVEL" |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff545640">FsRtlAllocateFileLock</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff546122">FsRtlInitializeFileLock</a>