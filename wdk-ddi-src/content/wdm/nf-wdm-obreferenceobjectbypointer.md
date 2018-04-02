---
UID: NF:wdm.ObReferenceObjectByPointer
title: ObReferenceObjectByPointer function
author: windows-driver-content
description: The ObReferenceObjectByPointer routine increments the pointer reference count for a given object.
old-location: kernel\obreferenceobjectbypointer.htm
old-project: kernel
ms.assetid: c575bd3f-6790-4815-b7c7-8ee16a9cac17
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: ObReferenceObjectByPointer, ObReferenceObjectByPointer routine [Kernel-Mode Driver Architecture], k107_2846f148-4ad5-472a-aa74-4f03c5251aee.xml, kernel.obreferenceobjectbypointer, wdm/ObReferenceObjectByPointer
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
req.ddi-compliance: TargetRelationNeedsRef, HwStorPortProhibitedDDIs
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
-	ObReferenceObjectByPointer
product: Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# ObReferenceObjectByPointer function
The <b>ObReferenceObjectByPointer</b> routine increments the pointer reference count for a given object.

## Syntax

```
NTKERNELAPI NTSTATUS ObReferenceObjectByPointer(
  PVOID           Object,
  ACCESS_MASK     DesiredAccess,
  POBJECT_TYPE    ObjectType,
  KPROCESSOR_MODE AccessMode
);
```

## Parameters

`Object`

Pointer to the object's body.

`DesiredAccess`

Specifies a mask representing the requested access to the object.

`ObjectType`

Pointer to the object type. <i>ObjectType</i> can be <b>*ExEventObjectType</b>, <b>*ExSemaphoreObjectType</b>, <b>*IoFileObjectType</b>, <b>*PsProcessType</b>, <b>*PsThreadType</b>, <b>*SeTokenObjectType</b>, <b>*TmEnlistmentObjectType</b>, <b>*TmResourceManagerObjectType</b>, <b>*TmTransactionManagerObjectType</b>, or <b>*TmTransactionObjectType</b>. 

<div class="alert"><b>Note</b>    The <b>SeTokenObjectType</b> object type is supported in Windows XP and later versions of Windows.</div>
<div> </div>
This parameter can also be <b>NULL</b> if <i>AccessMode</i> is <b>KernelMode</b>.

`AccessMode`

Indicates the access mode to use for the access check. It must be either <b>UserMode</b> or <b>KernelMode</b>. Lower-level drivers should specify <b>KernelMode</b>.


## Return Value

<b>ObReferenceObjectByPointer</b> returns an NTSTATUS value. Possible return values include:

## Remarks

Calling this routine prevents the object from being deleted, possibly by another component's call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff557724">ObDereferenceObject</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff566417">ZwClose</a>. The caller must decrement the reference count with <b>ObDereferenceObject</b> as soon as it is done with the object.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 2000.  |
| **Target Platform** | Universal |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | "<= DISPATCH_LEVEL" |
| **DDI compliance rules** | TargetRelationNeedsRef, HwStorPortProhibitedDDIs |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff557724">ObDereferenceObject</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff558678">ObReferenceObject</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff558679">ObReferenceObjectByHandle</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff566417">ZwClose</a>