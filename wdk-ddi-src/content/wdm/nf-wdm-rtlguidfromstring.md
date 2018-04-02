---
UID: NF:wdm.RtlGUIDFromString
title: RtlGUIDFromString function
author: windows-driver-content
description: The RtlGUIDFromString routine converts the given Unicode string to a GUID in binary format.
old-location: kernel\rtlguidfromstring.htm
old-project: kernel
ms.assetid: 7bdfc781-93d6-4f49-95f1-46f102908ec5
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: RtlGUIDFromString, RtlGUIDFromString routine [Kernel-Mode Driver Architecture], k109_d6fe22b7-9d81-4024-819c-03bce65d3d14.xml, kernel.rtlguidfromstring, wdm/RtlGUIDFromString
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
req.dll: NtosKrnl.exe (kernel mode); Ntdll.dll (user mode)
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
-	Ntdll.dll
api_name:
-	RtlGUIDFromString
product:
- Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# RtlGUIDFromString function
The <b>RtlGUIDFromString</b> routine converts the given Unicode string to a GUID in binary format.

## Syntax

```
NTSYSAPI NTSTATUS RtlGUIDFromString(
  PCUNICODE_STRING GuidString,
  GUID             *Guid
);
```

## Parameters

`GuidString`

Pointer to the buffered Unicode string to be converted to a GUID.

`Guid`

Pointer to a caller-supplied variable in which the GUID is returned.


## Return Value

If the conversion succeeds, <b>RtlGUIDFromString</b> returns STATUS_SUCCESS. Otherwise, no conversion was done.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 2000.  |
| **Target Platform** | Universal |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe (kernel mode); Ntdll.dll (user mode) |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff562871">RtlStringFromGUID</a>