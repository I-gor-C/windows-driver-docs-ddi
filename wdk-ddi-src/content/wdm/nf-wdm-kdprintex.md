---
UID: NF:wdm.KdPrintEx
title: KdPrintEx macro
author: windows-driver-content
description: The KdPrintEx macro sends a string to the kernel debugger if the conditions you specify are met.A call to KdPrintEx requires double parentheses.
old-location: devtest\kdprintex.htm
old-project: devtest
ms.assetid: 8383e9c8-0058-47bf-9a6e-ed05e61a58f1
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: DebugFns_375418aa-5241-4b2c-9369-c930c3ca1ca6.xml, KdPrintEx, KdPrintEx function [Driver Development Tools], devtest.kdprintex, wdm/KdPrintEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: wdm.h
req.include-header: Wdm.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Microsoft Windows XP and later.
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
req.lib: NtosKrnl.lib (See DbgPrintEx.)
req.dll: NtosKrnl.exe
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	KdPrintEx
product: Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# KdPrintEx function
The <b>KdPrintEx</b> macro sends a string to the kernel debugger if the conditions you specify are met.

A call to <b>KdPrintEx</b> requires double parentheses.

## Syntax

```
void KdPrintEx(
   _x_
);
```

## Parameters

`_x_`

TBD


## Return Value

None

## Remarks

<b>KdPrintEx</b> is identical to the <b>DbgPrintEx</b> routine in code that is compiled for a debug configuration. This routine has no effect in code that is compiled for a release build. Only kernel-mode drivers can call the <b>KdPrintEx</b> routine.<div class="alert"><b>Note</b>  The Windows Driver Kit (WDK) 8 and WDK 7 manage the <b>DBG</b> preprocessor constant define appropriately for debug (check) and release (free) builds. For more information, see <a href="https://msdn.microsoft.com/7879b6c6-4985-4817-a8bc-b287397df721">Conditional Compilation and the Build Environment</a>.</div>
<div> </div>


<b>KdPrintEx</b> either passes the specified string to the kernel debugger or does nothing at all, depending on the values of <i>ComponentId</i>, <i>Level</i>, and the corresponding component filter masks. For details, see <a href="https://msdn.microsoft.com/2ad320f6-596d-4b4c-bfad-d570c856bcc7">Reading and Filtering Debugging Messages</a>.

Unless it is absolutely necessary, you should not obtain a string from user input or another process and pass it to <b>KdPrintEx</b>. If you do use a string that you did not create, you must verify that this is a valid format string, and that the format codes match the argument list in type and quantity. The best coding practice is for all <i>Format</i> strings to be static and defined at compile time.

There is no upper limit to the size of the <i>Format</i> string or the number of arguments. However, any single call to <b>KdPrintEx</b> will only transmit 512 bytes of information. There is also a limit to the size of the DbgPrint buffer. See <a href="https://msdn.microsoft.com/2ad320f6-596d-4b4c-bfad-d570c856bcc7">The DbgPrint Buffer and the Debugger</a> for details.

This routine is defined in ntddk.h and ndis.h; component filter IDs are defined in dpfilter.h, ndis.h, and wdm.h. Include ntddk.h or ndis.h.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Microsoft Windows XP and later.  |
| **Target Platform** | Desktop |
| **Header** | wdm.h (include Wdm.h) |
| **Library** | NtosKrnl.lib (See DbgPrintEx.) |
| **DLL** | NtosKrnl.exe |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff543632">DbgPrint</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff543634">DbgPrintEx</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff548092">KdPrint</a>