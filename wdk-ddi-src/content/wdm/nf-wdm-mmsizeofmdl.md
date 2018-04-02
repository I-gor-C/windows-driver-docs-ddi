---
UID: NF:wdm.MmSizeOfMdl
title: MmSizeOfMdl function
author: windows-driver-content
description: The MmSizeOfMdl routine returns the number of bytes to allocate for an MDL describing a given address range.
old-location: kernel\mmsizeofmdl.htm
old-project: kernel
ms.assetid: 83e7d4be-df76-4dc8-a8e2-91d279127ef1
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: MmSizeOfMdl, MmSizeOfMdl routine [Kernel-Mode Driver Architecture], k106_7cddc848-8b01-4a6a-b5b1-977f2386fc21.xml, kernel.mmsizeofmdl, wdm/MmSizeOfMdl
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
req.irql: Any level
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	MmSizeOfMdl
product:
- Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# MmSizeOfMdl function
The <b>MmSizeOfMdl</b> routine returns the number of bytes to allocate for an MDL describing a given address range.

## Syntax

```
NTKERNELAPI SIZE_T MmSizeOfMdl(
  PVOID  Base,
  SIZE_T Length
);
```

## Parameters

`Base`

Pointer to the base virtual address for the range.

`Length`

Supplies the size, in bytes, of the range.


## Return Value

<b>MmSizeOfMdl</b> returns the number of bytes required to contain the MDL.

## Remarks

Memory for the MDL itself must be allocated from nonpaged pool.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 2000.  |
| **Target Platform** | Universal |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | Any level |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff554500">MmCreateMdl</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff554568">MmInitializeMdl</a>