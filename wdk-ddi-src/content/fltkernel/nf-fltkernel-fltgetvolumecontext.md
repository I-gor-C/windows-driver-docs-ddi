---
UID: NF:fltkernel.FltGetVolumeContext
title: FltGetVolumeContext function
author: windows-driver-content
description: The FltGetVolumeContext routine retrieves a context that was set for a volume by a given minifilter driver.
old-location: ifsk\fltgetvolumecontext.htm
old-project: ifsk
ms.assetid: daa7d15f-580a-4668-9159-834e18b28c1f
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: FltApiRef_e_to_o_8cec5d5c-18c3-4ffe-be18-fffcfc8d0c14.xml, FltGetVolumeContext, FltGetVolumeContext routine [Installable File System Drivers], fltkernel/FltGetVolumeContext, ifsk.fltgetvolumecontext
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: 
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
req.lib: FltMgr.lib
req.dll: Fltmgr.sys
req.irql: "<= APC_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	fltmgr.sys
api_name:
-	FltGetVolumeContext
product: Windows
targetos: Windows
req.typenames: EXpsFontRestriction
---


# FltGetVolumeContext function
The <b>FltGetVolumeContext</b> routine retrieves a context that was set for a volume by a given minifilter driver.

## Syntax

```
NTSTATUS FLTAPI FltGetVolumeContext(
  PFLT_FILTER  Filter,
  PFLT_VOLUME  Volume,
  PFLT_CONTEXT *Context
);
```

## Parameters

`Filter`

Opaque filter pointer for the caller. This parameter is required and cannot be <b>NULL</b>.

`Volume`

Opaque pointer for the volume whose context is being retrieved. This parameter is required and cannot be <b>NULL</b>.

`Context`

Pointer to a caller-allocated variable that receives the address of the requested context.


## Return Value

<b>FltGetVolumeContext</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value, such as the following: 

<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_NOT_FOUND</b></dt>
</dl>
</td>
<td width="60%">
No matching context was found. This is an error code. 

</td>
</tr>
</table>

## Remarks

<b>FltGetVolumeContext</b> increments the reference count on the context that the <i>Context </i>parameter points to. When this context pointer is no longer needed, the caller must decrement its reference count by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff544314">FltReleaseContext</a>. Thus every successful call to <b>FltGetVolumeContext</b> must be matched by a subsequent call to <b>FltReleaseContext</b>. 

To set a context for a volume, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544557">FltSetVolumeContext</a>. 

To allocate a new context, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541710">FltAllocateContext</a>. 

To delete a volume context, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff542030">FltDeleteVolumeContext</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff541960">FltDeleteContext</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | fltkernel.h (include Fltkernel.h) |
| **Library** | FltMgr.lib |
| **DLL** | Fltmgr.sys |
| **IRQL** | "<= APC_LEVEL" |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff541710">FltAllocateContext</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541960">FltDeleteContext</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff542030">FltDeleteVolumeContext</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544314">FltReleaseContext</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544557">FltSetVolumeContext</a>