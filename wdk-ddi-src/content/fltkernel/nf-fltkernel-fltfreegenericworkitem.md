---
UID: NF.fltkernel.FltFreeGenericWorkItem
title: FltFreeGenericWorkItem function
author: windows-driver-content
description: The FltFreeGenericWorkItem routine frees a work item allocated by the FltAllocateGenericWorkItem routine.
old-location: ifsk\fltfreegenericworkitem.htm
old-project: ifsk
ms.assetid: 6675d529-10de-4c39-999c-4c18471ea6e0
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: FltFreeGenericWorkItem
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
req.alt-api: FltFreeGenericWorkItem
req.alt-loc: fltmgr.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: Fltmgr.sys
req.irql: <= DISPATCH_LEVEL
---

# FltFreeGenericWorkItem function



## -description
The <b>FltFreeGenericWorkItem</b> routine frees a work item allocated by the <a href="ifsk.fltallocategenericworkitem">FltAllocateGenericWorkItem</a> routine. 



## -syntax

````
VOID FltFreeGenericWorkItem(
  _In_ PFLT_GENERIC_WORKITEM FltWorkItem
);
````


## -parameters

### -param FltWorkItem [in]

Opaque pointer to the work item to be freed. 


## -returns
None 


## -remarks
<b>FltFreeGenericWorkItem</b> frees an FLT_GENERIC_WORKITEM structure that was allocated by a previous call to <a href="ifsk.fltallocategenericworkitem">FltAllocateGenericWorkItem</a>. The freed memory is returned to nonpaged pool. 


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Fltkernel.h (include Fltkernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>FltMgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>Fltmgr.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= DISPATCH_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.fltallocategenericworkitem">FltAllocateGenericWorkItem</a>
</dt>
<dt>
<a href="ifsk.fltqueuegenericworkitem">FltQueueGenericWorkItem</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltFreeGenericWorkItem routine%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

