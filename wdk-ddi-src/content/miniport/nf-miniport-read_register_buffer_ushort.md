---
UID: NF:miniport.READ_REGISTER_BUFFER_USHORT
title: READ_REGISTER_BUFFER_USHORT function
author: windows-driver-content
description: The READ_REGISTER_BUFFER_USHORT routine reads a number of USHORT values from the specified register address into a buffer.
old-location: kernel\read_register_buffer_ushort.htm
old-project: kernel
ms.assetid: 30c3fc44-e94a-47ca-a25b-33857b485817
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: READ_REGISTER_BUFFER_USHORT, READ_REGISTER_BUFFER_USHORT routine [Kernel-Mode Driver Architecture], k103_a4ed8007-394e-4090-bcdb-63ad37431377.xml, kernel.read_register_buffer_ushort, wdm/READ_REGISTER_BUFFER_USHORT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: miniport.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h, Miniport.h, Wudfwdm.h
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
-	READ_REGISTER_BUFFER_USHORT
product:
- Windows
targetos: Windows
req.typenames: MEMORY_CACHING_TYPE
---


# READ_REGISTER_BUFFER_USHORT function
The <b>READ_REGISTER_BUFFER_USHORT</b> routine reads a number of USHORT values from the specified register address into a buffer.

## Syntax

```
void READ_REGISTER_BUFFER_USHORT(
  USHORT  *Register,
  PUSHORT Buffer,
  ULONG   Count
);
```

## Parameters

`Register`

Pointer to the register, which must be a mapped range in memory space.

`Buffer`

Pointer to a buffer into which an array of USHORT values is read.

`Count`

Specifies the number of USHORT values to be read into the buffer.


## Return Value

None

## Remarks

The size of the buffer must be large enough to contain at least the specified number of USHORT values.

Callers of <b>READ_REGISTER_BUFFER_USHORT</b> can be running at any IRQL, assuming the <i>Buffer</i> is resident and the <i>Register</i> is resident, mapped device memory.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 2000.  |
| **Target Platform** | Universal |
| **Header** | miniport.h (include Wdm.h, Ntddk.h, Ntifs.h, Miniport.h, Wudfwdm.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | Any level (see Remarks section) |