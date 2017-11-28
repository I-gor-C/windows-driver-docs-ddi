---
UID: NF.fltkernel.FltGetIoPriorityHintFromFileObject
title: FltGetIoPriorityHintFromFileObject
author: windows-driver-content
description: The FltGetIoPriorityHintFromFileObject routine is used by a minifilter driver to get IO priority information from a file object.
old-location: ifsk\fltgetiopriorityhintfromfileobject.htm
old-project: ifsk
ms.assetid: ca854716-8f6e-42bd-ae03-e31f951b0874
ms.author: windowsdriverdev
ms.date: 11/14/2017
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
req.iface: 
---

# FltGetIoPriorityHintFromFileObject function



## -description
<p>The <b>FltGetIoPriorityHintFromFileObject</b> routine is used by a minifilter driver to get IO priority information from a file object.</p>


## -syntax

````
IO_PRIORITY_HINT FltGetIoPriorityHintFromFileObject(
  _In_ PFILE_OBJECT FileObject
);
````


## -parameters
<dl>

### -param <i>FileObject</i> [in]

<dd>
<p>A pointer to a file object. This parameter is required and cannot be <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p>The <b>FltGetIoPriorityHintFromFileObject</b> routine returns an IO priority hint retrieved from a file object.</p>

<p>If the <i>FileObject</i> does not have a priority, the routine returns IoPriorityNormal.</p>

<p>If an error occurs retrieving the priority, the routine returns IoPriorityNormal.</p>

## -remarks
<p>This routine is NONPAGED and can be called from paging IO paths.</p>

<p>This routine is NONPAGED and can be called from paging IO paths.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fltkernel.h (include FltKernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>FltMgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Fltmgr.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541766">FltApplyPriorityInfoThread</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543065">FltGetIoPriorityHint</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543068">FltGetIoPriorityHintFromCallbackData</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543080">FltGetIoPriorityHintFromThread</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544354">FltRetrieveIoPriorityInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544526">FltSetIoPriorityHintIntoCallbackData</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544530">FltSetIoPriorityHintIntoFileObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544534">FltSetIoPriorityHintIntoThread</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548568">IO_PRIORITY_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltGetIoPriorityHintFromFileObject routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
