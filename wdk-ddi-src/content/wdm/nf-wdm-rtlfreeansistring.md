---
UID: NF:wdm.RtlFreeAnsiString
title: RtlFreeAnsiString function
author: windows-driver-content
description: The RtlFreeAnsiString routine releases storage that was allocated by RtlUnicodeStringToAnsiString.
old-location: kernel\rtlfreeansistring.htm
old-project: kernel
ms.assetid: ca46be9e-31f6-4118-8958-4eb2c8450e8c
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: RtlFreeAnsiString, RtlFreeAnsiString routine [Kernel-Mode Driver Architecture], k109_0213924f-caca-4411-b5cc-d93282f01948.xml, kernel.rtlfreeansistring, wdm/RtlFreeAnsiString
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
req.irql: "<=APC_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	RtlFreeAnsiString
product: Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# RtlFreeAnsiString function
The <b>RtlFreeAnsiString</b> routine releases storage that was allocated by <b>RtlUnicodeStringToAnsiString</b>.

## Syntax

```
NTSYSAPI VOID RtlFreeAnsiString(
  PANSI_STRING AnsiString
);
```

## Parameters

`AnsiString`

Pointer to the ANSI string buffer previously allocated by <b>RtlUnicodeStringToAnsiString</b>.


## Return Value

None

## Remarks

This routine does not release the Unicode string buffer passed to <b>RtlUnicodeStringToAnsiString</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 2000.  |
| **Target Platform** | Universal |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | "<=APC_LEVEL" |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff562969">RtlUnicodeStringToAnsiString</a>