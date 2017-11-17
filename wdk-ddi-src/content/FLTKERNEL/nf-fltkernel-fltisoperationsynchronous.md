---
UID: NF.fltkernel.FltIsOperationSynchronous
title: FltIsOperationSynchronous
author: windows-driver-content
description: The FltIsOperationSynchronous routine determines whether a given callback data structure (FLT_CALLBACK_DATA) represents a synchronous or asynchronous I/O operation.
old-location: ifsk\fltisoperationsynchronous.htm
ms.assetid: 44594383-9f07-4b6a-8ea3-eaf84c9fefda
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltIsOperationSynchronous
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
req.irql: Any level
ms.keywords: FltIsOperationSynchronous
req.iface: 
---

# FltIsOperationSynchronous function



## -description
<p>The <b>FltIsOperationSynchronous</b> routine determines whether a given callback data structure (<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>) represents a synchronous or asynchronous I/O operation. </p>


## -syntax

````
BOOLEAN FltIsOperationSynchronous(
  _In_ PFLT_CALLBACK_DATA CallbackData
);
````


## -parameters
<dl>

### -param <i>CallbackData</i> [in]

<dd>
<p>Pointer to the callback data structure for the operation (<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>). </p>
</dd>
</dl>

## -returns
<p><b>FltIsOperationSynchronous</b> returns <b>TRUE</b> if the operation is synchronous, and <b>FALSE</b> if the operation is asynchronous. </p>

## -remarks
<p><b>FltIsOperationSynchronous</b> determines whether a given callback data structure (<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>) represents a synchronous or asynchronous I/O operation, according to the following conditions: </p>

<p>If the operation is not an IRP-based I/O operation, the operation is synchronous. To determine whether an operation is IRP-based, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544654">FLT_IS_IRP_OPERATION</a> macro. </p>

<p>If the operation is an asynchronous paging I/O operation, the operation is asynchronous, even if one of the other conditions in this list is true. </p>

<p>If the operation is a synchronous paging I/O operation, the operation is synchronous. </p>

<p>If the file object for the operation was opened for synchronous I/O, the operation is synchronous. </p>

<p>If the IRP_SYNCHRONOUS_API flag is set in the IRP for the operation, the operation is synchronous. This flag is set for operations, such as IRP_MJ_QUERY_INFORMATION and IRP_MJ_SET_INFORMATION, that are always synchronous, even when performed on a file object that was opened for asynchronous I/O. </p>

<p>If none of the above conditions is true, the operation is asynchronous. </p>

<p><b>FltIsOperationSynchronous</b> can be called for all classes of operations: fast I/O, file system filter (FSFilter) callbacks, and IRP-based operations. </p>

<p><b>FltIsOperationSynchronous</b> determines whether a given callback data structure (<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>) represents a synchronous or asynchronous I/O operation, according to the following conditions: </p>

<p>If the operation is not an IRP-based I/O operation, the operation is synchronous. To determine whether an operation is IRP-based, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544654">FLT_IS_IRP_OPERATION</a> macro. </p>

<p>If the operation is an asynchronous paging I/O operation, the operation is asynchronous, even if one of the other conditions in this list is true. </p>

<p>If the operation is a synchronous paging I/O operation, the operation is synchronous. </p>

<p>If the file object for the operation was opened for synchronous I/O, the operation is synchronous. </p>

<p>If the IRP_SYNCHRONOUS_API flag is set in the IRP for the operation, the operation is synchronous. This flag is set for operations, such as IRP_MJ_QUERY_INFORMATION and IRP_MJ_SET_INFORMATION, that are always synchronous, even when performed on a file object that was opened for asynchronous I/O. </p>

<p>If none of the above conditions is true, the operation is asynchronous. </p>

<p><b>FltIsOperationSynchronous</b> can be called for all classes of operations: fast I/O, file system filter (FSFilter) callbacks, and IRP-based operations. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544645">FLT_IS_FASTIO_OPERATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544648">FLT_IS_FS_FILTER_OPERATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544654">FLT_IS_IRP_OPERATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548443">IoIsOperationSynchronous</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltIsOperationSynchronous routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
