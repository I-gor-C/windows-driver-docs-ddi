---
UID: NF:wdm.RtlEqualUnicodeString
title: RtlEqualUnicodeString function
author: windows-driver-content
description: The RtlEqualUnicodeString routine compares two Unicode strings to determine whether they are equal.
old-location: kernel\rtlequalunicodestring.htm
old-project: kernel
ms.assetid: ba50fcac-acb1-43de-aacc-b47845f19f44
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: RtlEqualUnicodeString, RtlEqualUnicodeString routine [Kernel-Mode Driver Architecture], k109_59d7c507-968a-4cf5-b1f0-91c8cd7ccb64.xml, kernel.rtlequalunicodestring, wdm/RtlEqualUnicodeString
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h, Wudfwdm.h
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
-	RtlEqualUnicodeString
product: Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# RtlEqualUnicodeString function
The <b>RtlEqualUnicodeString</b> routine compares two Unicode strings to determine whether they are equal.

## Syntax

```
NTSYSAPI BOOLEAN RtlEqualUnicodeString(
  PCUNICODE_STRING String1,
  PCUNICODE_STRING String2,
  BOOLEAN          CaseInSensitive
);
```

## Parameters

`String1`

Pointer to the first Unicode string.

`String2`

Pointer to the second Unicode string.

`CaseInSensitive`

If <b>TRUE</b>, case should be ignored when doing the comparison.


## Return Value

<b>RtlEqualUnicodeString</b> returns <b>TRUE</b> if the two Unicode strings are equal; otherwise, it returns <b>FALSE</b>.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 2000.  |
| **Target Platform** | Universal |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h, Wudfwdm.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe (kernel mode); Ntdll.dll (user mode) |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff561852">RtlEqualString</a>