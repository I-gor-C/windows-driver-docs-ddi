---
UID: NF:wdm.KeGetCurrentThread
title: KeGetCurrentThread function
author: windows-driver-content
description: The KeGetCurrentThread routine identifies the current thread.
old-location: kernel\kegetcurrentthread.htm
old-project: kernel
ms.assetid: 0fbc9f6d-698b-4fa5-86c4-3f6ef0cc50fb
ms.author: windowsdriverdev
ms.date: 3/1/2018
ms.keywords: KeGetCurrentThread, KeGetCurrentThread routine [Kernel-Mode Driver Architecture], k105_fa2d3ae9-9ac8-4c50-bf51-5d6751a2b81e.xml, kernel.kegetcurrentthread, wdm/KeGetCurrentThread
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
-	KeGetCurrentThread
product: Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# KeGetCurrentThread function
The <b>KeGetCurrentThread</b> routine identifies the current thread.

## Syntax

````
PKTHREAD KeGetCurrentThread(void);
````

## Parameters

This function has no parameters.

## Return Value

<b>KeGetCurrentThread</b> returns a pointer to an opaque thread object.

## Remarks

This routine is identical to <a href="..\wdm\nf-wdm-psgetcurrentthread.md">PsGetCurrentThread</a>.

A caller of <b>KeGetCurrentThread</b> can use the returned pointer as an input parameter to <a href="..\wdm\nf-wdm-kequeryprioritythread.md">KeQueryPriorityThread</a>, <a href="..\ntddk\nf-ntddk-kesetbaseprioritythread.md">KeSetBasePriorityThread</a>, or <a href="..\wdm\nf-wdm-kesetprioritythread.md">KeSetPriorityThread</a>. However, the memory containing the thread object is opaque; that is, it is reserved for exclusive use by the operating system.

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

<a href="..\ntddk\nf-ntddk-kesetbaseprioritythread.md">KeSetBasePriorityThread</a>



<a href="..\wdm\nf-wdm-kesetprioritythread.md">KeSetPriorityThread</a>



<a href="..\wdm\nf-wdm-psgetcurrentthread.md">PsGetCurrentThread</a>



<a href="..\wdm\nf-wdm-kequeryprioritythread.md">KeQueryPriorityThread</a>