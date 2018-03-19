---
UID: NF:wdm.IoGetInitialStack
title: IoGetInitialStack function
author: windows-driver-content
description: The IoGetInitialStack routine returns the base address of the current thread's stack.
old-location: kernel\iogetinitialstack.htm
old-project: kernel
ms.assetid: 0d0d793f-c2c1-48ff-9e7f-ef2697255bfa
ms.author: windowsdriverdev
ms.date: 3/1/2018
ms.keywords: IoGetInitialStack, IoGetInitialStack routine [Kernel-Mode Driver Architecture], k104_5e1ac4e5-b51e-4840-86e3-2ce67c634489.xml, kernel.iogetinitialstack, wdm/IoGetInitialStack
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: IrqlIoApcLte, HwStorPortProhibitedDDIs
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
-	IoGetInitialStack
product: Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# IoGetInitialStack function
The <b>IoGetInitialStack</b> routine returns the base address of the current thread's stack.

## Syntax

````
PVOID IoGetInitialStack(void);
````

## Parameters

This function has no parameters.

## Return Value

<b>IoGetInitialStack</b> returns the initial base address of the current thread's stack.

## Remarks

Highest-level drivers can call this routine, particularly file systems attempting to determine whether they've been passed a pointer to a location on the current thread's stack.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 2000.  |
| **Target Platform** | Universal |
| **Header** | wdm.h (include Ntddk.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | "<=APC_LEVEL" |
| **DDI compliance rules** | IrqlIoApcLte, HwStorPortProhibitedDDIs |

## See Also

<a href="..\wdm\nf-wdm-iogetstacklimits.md">IoGetStackLimits</a>



<a href="..\wdm\nf-wdm-iogetremainingstacksize.md">IoGetRemainingStackSize</a>