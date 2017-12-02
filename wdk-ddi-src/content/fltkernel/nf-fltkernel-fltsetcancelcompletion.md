---
UID: NF.fltkernel.FltSetCancelCompletion
title: FltSetCancelCompletion
author: windows-driver-content
description: A minifilter driver calls FltSetCancelCompletion to specify a cancel routine to be called if a given I/O operation is canceled.
old-location: ifsk\fltsetcancelcompletion.htm
old-project: ifsk
ms.assetid: 3f15d3b2-321d-45ca-8fe4-d8706fe61d48
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltSetCancelCompletion
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
req.alt-api: FltSetCancelCompletion
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

# FltSetCancelCompletion function



## -description
<p>A minifilter driver calls <b>FltSetCancelCompletion</b> to specify a cancel routine to be called if a given I/O operation is canceled. </p>


## -syntax

````
NTSTATUS FltSetCancelCompletion(
  _In_ PFLT_CALLBACK_DATA              CallbackData,
  _In_ PFLT_COMPLETE_CANCELED_CALLBACK CanceledCallback
);
````


## -parameters
<dl>

### -param CallbackData [in]

<dd>
<p>Pointer to the callback data (<a href="..\fltkernel\ns-fltkernel--flt-callback-data.md">FLT_CALLBACK_DATA</a>) structure for the I/O operation. The operation must be an IRP-based I/O operation and must not be a paging I/O operation. To determine whether a given callback data structure represents an IRP-based I/O operation, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544654">FLT_IS_IRP_OPERATION</a> macro. This parameter is required and cannot be <b>NULL</b>. </p>
</dd>

### -param CanceledCallback [in]

<dd>
<p>Pointer to a caller-supplied cancel routine. The Filter Manager calls this routine if the I/O operation represented by <i>CallbackData</i> is canceled. </p>
<p>This routine is declared as follows: </p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef VOID
(*PFLT_COMPLETE_CANCELED_CALLBACK) (
      IN PFLT_CALLBACK_DATA CallbackData
      );</pre>
</td>
</tr>
</table></span></div>
<p></p>
<dl>

### -param CallbackData

<dd>
<p>Pointer to the FLT_CALLBACK_DATA structure for the I/O operation. </p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p><b>FltSetCancelCompletion</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value. </p>

## -remarks
<p><b>FltSetCancelCompletion</b> specifies a cancel routine for an IRP-based I/O operation that is to be posted to a work queue. </p>

<p>Minifilter drivers usually call <b>FltSetCancelCompletion</b> for an I/O operation immediately before calling <a href="..\fltkernel\nf-fltkernel-fltqueuedeferredioworkitem.md">FltQueueDeferredIoWorkItem</a> to post the operation to a work queue. </p>

<p>Do not call <b>FltSetCancelCompletion</b> for any I/O operation that is to be posted to a cancel-safe callback data queue using the <b>FltCbdq</b><i>Xxx</i> routines. </p>

<p>The Filter Manager calls the <i>CanceledCallback</i> routine without holding the system cancel spin lock or performing any other synchronization. Any required synchronization must be supplied by the minifilter driver itself. </p>

<p>To cancel an I/O operation, call <a href="..\fltkernel\nf-fltkernel-fltcancelio.md">FltCancelIo</a>. </p>

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
<a href="..\fltkernel\ns-fltkernel--flt-callback-data.md">FLT_CALLBACK_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544654">FLT_IS_IRP_OPERATION</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltcancelio.md">FltCancelIo</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltclearcancelcompletion.md">FltClearCancelCompletion</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltqueuedeferredioworkitem.md">FltQueueDeferredIoWorkItem</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltSetCancelCompletion routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
