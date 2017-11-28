---
UID: NF.fltkernel.FltClearCancelCompletion
title: FltClearCancelCompletion
author: windows-driver-content
description: FltClearCancelCompletion clears a cancel routine that was specified for an I/O operation.
old-location: ifsk\fltclearcancelcompletion.htm
old-project: ifsk
ms.assetid: 75c66cb7-3378-4951-9180-d1bd9f201a42
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltClearCancelCompletion
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
req.alt-api: FltClearCancelCompletion
req.alt-loc: FltMgr.lib,FltMgr.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: 
req.irql: Any level
req.iface: 
---

# FltClearCancelCompletion function



## -description
<p><b>FltClearCancelCompletion</b> clears a cancel routine that was specified for an I/O operation. </p>


## -syntax

````
NTSTATUS FltClearCancelCompletion(
  _In_ PFLT_CALLBACK_DATA CallbackData
);
````


## -parameters
<dl>

### -param <i>CallbackData</i> [in]

<dd>
<p>Pointer to the callback data (<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>) structure for the I/O operation. </p>
</dd>
</dl>

## -returns
<p>If no cancel routine was previously set or if IRP cancellation is already in progress, <b>FltClearCancelCompletion</b> returns STATUS_CANCELLED. Otherwise, it returns STATUS_SUCCESS. </p>

## -remarks
<p>A minifilter driver calls <b>FltClearCancelCompletion</b> to clear a cancel routine that was specified for an I/O operation by a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff544390">FltSetCancelCompletion</a>. The operation must be an IRP-based I/O operation. To determine whether a given callback data (<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>) structure represents an IRP-based I/O operation, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544654">FLT_IS_IRP_OPERATION</a> macro. </p>

<p>To cancel an I/O operation, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541785">FltCancelIo</a>. </p>

<p>A minifilter driver calls <b>FltClearCancelCompletion</b> to clear a cancel routine that was specified for an I/O operation by a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff544390">FltSetCancelCompletion</a>. The operation must be an IRP-based I/O operation. To determine whether a given callback data (<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>) structure represents an IRP-based I/O operation, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544654">FLT_IS_IRP_OPERATION</a> macro. </p>

<p>To cancel an I/O operation, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541785">FltCancelIo</a>. </p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fltkernel.h (include Fltkernel.h)</dt>
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
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544654">FLT_IS_IRP_OPERATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541785">FltCancelIo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544390">FltSetCancelCompletion</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltClearCancelCompletion routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
