---
UID: NF.fltkernel.FltGetIoPriorityHintFromFileObject
title: FltGetIoPriorityHintFromFileObject function
author: windows-driver-content
description: The FltGetIoPriorityHintFromFileObject routine is used by a minifilter driver to get IO priority information from a file object.
old-location: ifsk\fltgetiopriorityhintfromfileobject.htm
old-project: ifsk
ms.assetid: ca854716-8f6e-42bd-ae03-e31f951b0874
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: FltGetIoPriorityHintFromFileObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: FltKernel.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltGetIoPriorityHintFromFileObject
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

# FltGetIoPriorityHintFromFileObject function



## -description
The <b>FltGetIoPriorityHintFromFileObject</b> routine is used by a minifilter driver to get IO priority information from a file object.



## -syntax

````
IO_PRIORITY_HINT FltGetIoPriorityHintFromFileObject(
  _In_ PFILE_OBJECT FileObject
);
````


## -parameters

### -param FileObject [in]

A pointer to a file object. This parameter is required and cannot be <b>NULL</b>.


## -returns
The <b>FltGetIoPriorityHintFromFileObject</b> routine returns an IO priority hint retrieved from a file object.

If the <i>FileObject</i> does not have a priority, the routine returns IoPriorityNormal.

If an error occurs retrieving the priority, the routine returns IoPriorityNormal.


## -remarks
This routine is NONPAGED and can be called from paging IO paths.


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
Version

</th>
<td width="70%">
Available in Windows Vista and later Windows operating systems.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Fltkernel.h (include FltKernel.h)</dt>
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
<a href="ifsk.flt_callback_data">FLT_CALLBACK_DATA</a>
</dt>
<dt>
<a href="ifsk.fltapplypriorityinfothread">FltApplyPriorityInfoThread</a>
</dt>
<dt>
<a href="ifsk.fltgetiopriorityhint">FltGetIoPriorityHint</a>
</dt>
<dt>
<a href="ifsk.fltgetiopriorityhintfromcallbackdata">FltGetIoPriorityHintFromCallbackData</a>
</dt>
<dt>
<a href="ifsk.fltgetiopriorityhintfromthread">FltGetIoPriorityHintFromThread</a>
</dt>
<dt>
<a href="ifsk.fltretrieveiopriorityinfo">FltRetrieveIoPriorityInfo</a>
</dt>
<dt>
<a href="ifsk.fltsetiopriorityhintintocallbackdata">FltSetIoPriorityHintIntoCallbackData</a>
</dt>
<dt>
<a href="ifsk.fltsetiopriorityhintintofileobject">FltSetIoPriorityHintIntoFileObject</a>
</dt>
<dt>
<a href="ifsk.fltsetiopriorityhintintothread">FltSetIoPriorityHintIntoThread</a>
</dt>
<dt>
<a href="ifsk.io_priority_info">IO_PRIORITY_INFO</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltGetIoPriorityHintFromFileObject routine%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

