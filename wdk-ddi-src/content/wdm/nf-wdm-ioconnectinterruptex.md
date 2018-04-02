---
UID: NF:wdm.IoConnectInterruptEx
title: IoConnectInterruptEx function
author: windows-driver-content
description: For more information, see the WdmlibIoConnectInterruptEx function.#define IoConnectInterruptEx WdmlibIoConnectInterruptEx
old-location: kernel\ioconnectinterruptex.htm
old-project: kernel
ms.assetid: f77a2701-bde2-42c2-8393-88a7e4576f1b
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: IoConnectInterruptEx, IoConnectInterruptEx routine [Kernel-Mode Driver Architecture], WdmlibIoConnectInterruptEx, k104_17833453-ee13-4346-9c58-a1c47dccf636.xml, kernel.ioconnectinterruptex, wdm/IoConnectInterruptEx, wdm/WdmlibIoConnectInterruptEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available on Windows Vista and later versions of the Windows operating system. Drivers that must also work on Windows 2000, Windows XP, or Windows Server 2003 can instead link to Iointex.lib to use the routine.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	IoConnectInterruptEx
-	WdmlibIoConnectInterruptEx
product: Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# IoConnectInterruptEx function
For more information, see the <a href="https://msdn.microsoft.com/172598B1-C486-489F-98F0-382EB8139A08">WdmlibIoConnectInterruptEx</a> function.

<code>#define IoConnectInterruptEx WdmlibIoConnectInterruptEx</code>

## Syntax

```
NTKERNELAPI NTSTATUS IoConnectInterruptEx(
  PIO_CONNECT_INTERRUPT_PARAMETERS Parameters
);
```

## Parameters

`Parameters`

For more information, see the <a href="https://msdn.microsoft.com/172598B1-C486-489F-98F0-382EB8139A08">WdmlibIoConnectInterruptEx</a> function.


## Return Value

For more information, see the <a href="https://msdn.microsoft.com/172598B1-C486-489F-98F0-382EB8139A08">WdmlibIoConnectInterruptEx</a> function.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available on Windows Vista and later versions of the Windows operating system. Drivers that must also work on Windows 2000, Windows XP, or Windows Server 2003 can instead link to Iointex.lib to use the routine.  |
| **Target Platform** | Universal |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | PASSIVE_LEVEL |
| **DDI compliance rules** | HwStorPortProhibitedDDIs |

## See Also

<a href="https://msdn.microsoft.com/172598B1-C486-489F-98F0-382EB8139A08">WdmlibIoConnectInterruptEx</a>