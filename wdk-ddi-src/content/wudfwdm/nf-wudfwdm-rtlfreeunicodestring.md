---
UID: NF:wudfwdm.RtlFreeUnicodeString
title: RtlFreeUnicodeString function
author: windows-driver-content
description: The RtlFreeUnicodeString routine releases storage that was allocated by RtlAnsiStringToUnicodeString or RtlUpcaseUnicodeString.
old-location: kernel\rtlfreeunicodestring.htm
old-project: kernel
ms.assetid: 505e2ab7-13c3-4cdd-90ba-a37bb38fe160
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: RtlFreeUnicodeString, RtlFreeUnicodeString routine [Kernel-Mode Driver Architecture], k109_c23e6c5e-d2dd-4b88-8249-5f88ad8482ad.xml, kernel.rtlfreeunicodestring, wdm/RtlFreeUnicodeString
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfwdm.h
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
-	RtlFreeUnicodeString
product:
- Windows
targetos: Windows
req.typenames: PO_FX_PERF_STATE_UNIT, *PPO_FX_PERF_STATE_UNIT
req.product: Windows 10 or later.
---


# RtlFreeUnicodeString function
The <b>RtlFreeUnicodeString</b> routine releases storage that was allocated by <b>RtlAnsiStringToUnicodeString</b> or <b>RtlUpcaseUnicodeString</b>.

## Syntax

````
VOID RtlFreeUnicodeString(
  _Inout_ PUNICODE_STRING UnicodeString
);
````

## Parameters

`UnicodeString`

Pointer to the Unicode string buffer previously allocated by <b>RtlAnsiStringToUnicodeString</b> or <b>RtlUpcaseUnicodeString</b>.


## Return Value

None

## Remarks

This routine does not release the ANSI string buffer passed to <b>RtlAnsiStringToUnicodeString</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 2000.  |
| **Target Platform** | Universal |
| **Header** | wudfwdm.h (include Wdm.h, Ntddk.h, Ntifs.h, Wudfwdm.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | "<=APC_LEVEL" |

## See Also

<a href="..\ntddk\nf-ntddk-rtlupcaseunicodestring.md">RtlUpcaseUnicodeString</a>



<a href="..\wdm\nf-wdm-rtlansistringtounicodestring.md">RtlAnsiStringToUnicodeString</a>