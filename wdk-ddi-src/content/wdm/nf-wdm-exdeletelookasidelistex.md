---
UID: NF:wdm.ExDeleteLookasideListEx
title: ExDeleteLookasideListEx function
author: windows-driver-content
description: The ExDeleteLookasideListEx routine deletes a lookaside list.
old-location: kernel\exdeletelookasidelistex.htm
old-project: kernel
ms.assetid: b72187de-a2ac-446f-bb06-9ca380454122
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: ExDeleteLookasideListEx, ExDeleteLookasideListEx routine [Kernel-Mode Driver Architecture], k102_35b6c2b4-58a3-4900-b8dc-63ed0a53b80f.xml, kernel.exdeletelookasidelistex, wdm/ExDeleteLookasideListEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of Windows.
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
req.irql: "<= DISPATCH_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	ExDeleteLookasideListEx
product: Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# ExDeleteLookasideListEx function
The <b>ExDeleteLookasideListEx</b> routine deletes a lookaside list.

## Syntax

```
NTKERNELAPI VOID ExDeleteLookasideListEx(
  PLOOKASIDE_LIST_EX Lookaside
);
```

## Parameters

`Lookaside`

A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff554329">LOOKASIDE_LIST_EX</a> structure that describes a lookaside list. This structure was previously initialized by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545298">ExInitializeLookasideListEx</a> routine.


## Return Value

None

## Remarks

<b>ExDeleteLookasideListEx</b> is the reciprocal of the <b>ExInitializeLookasideListEx</b> routine. It frees any remaining entries in the specified lookaside list and then removes the list from the system-wide set of active lookaside lists.

On return from <b>ExDeleteLookasideListEx</b>, the caller is responsible for releasing, if necessary, the caller-supplied storage for the <b>LOOKASIDE_LIST_EX</b> structure.

For more information about lookaside lists, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565416">Using Lookaside Lists</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of Windows.  |
| **Target Platform** | Universal |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | "<= DISPATCH_LEVEL" |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff545298">ExInitializeLookasideListEx</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff554329">LOOKASIDE_LIST_EX</a>