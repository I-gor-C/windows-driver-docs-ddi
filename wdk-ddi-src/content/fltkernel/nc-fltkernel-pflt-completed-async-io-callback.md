---
UID: NC.fltkernel.PFLT_COMPLETED_ASYNC_IO_CALLBACK
title: PFLT_COMPLETED_ASYNC_IO_CALLBACK
author: windows-driver-content
description: A minifilter driver that initiates an asynchronous I/O operation can specify a routine of type PFLT_COMPLETED_ASYNC_IO_CALLBACK routine to be called when the operation is completed.
old-location: ifsk\pflt_completed_async_io_callback.htm
old-project: ifsk
ms.assetid: 920e4236-9078-41c6-befb-9e82accbfa59
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IXpsPartIterator, Reset, IXpsPartIterator::Reset
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PFLT_COMPLETED_ASYNC_IO_CALLBACK
req.alt-loc: fltkernel.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section.
req.iface: IXpsPartIterator
---

# PFLT_COMPLETED_ASYNC_IO_CALLBACK callback



## -description
<p>A minifilter driver that initiates an asynchronous I/O operation can specify a routine of type PFLT_COMPLETED_ASYNC_IO_CALLBACK routine to be called when the operation is completed. </p>


## -prototype

````
typedef VOID ( *PFLT_COMPLETED_ASYNC_IO_CALLBACK)(
  _In_ PFLT_CALLBACK_DATA CallbackData,
  _In_ PFLT_CONTEXT       Context
);
````


## -parameters
<dl>

### -param <i>CallbackData</i> [in]

<dd>
<p>Pointer to the callback data structure for the I/O operation. </p>
</dd>

### -param <i>Context</i> [in]

<dd>
<p>Context pointer that the minifilter driver passed as a parameter to <a href="https://msdn.microsoft.com/library/windows/hardware/ff543420">FltPerformAsynchronousIo</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544286">FltReadFile</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff544610">FltWriteFile</a>. </p>
</dd>
</dl>

## -returns
<p>None </p>

## -remarks
<p>When a minifilter driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff543420">FltPerformAsynchronousIo</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544286">FltReadFile</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff544610">FltWriteFile</a> to initiate an asynchronous I/O operation, the minifilter driver can optionally specify a callback routine to be called when the I/O operation is completed. This is done by specifying a routine of type PFLT_COMPLETED_ASYNC_IO_CALLBACK for the <i>CallbackRoutine</i> parameter. </p>

<p>When the I/O operation is completed, this callback routine is called in an arbitrary thread context, at IRQL &lt;= DISPATCH_LEVEL. </p>

<p>Because the PFLT_COMPLETED_ASYNC_IO_CALLBACK routine can be called at IRQL DISPATCH_LEVEL, it is subject to the following constraints: </p>

<p>It cannot safely call any kernel-mode routines that require a lower IRQL. </p>

<p>Any data structures used in this routine must be allocated from nonpaged pool. </p>

<p>It cannot be made pageable. </p>

<p>It cannot acquire resources, mutexes, or fast mutexes. However, it can acquire spin locks. </p>

<p>When a minifilter driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff543420">FltPerformAsynchronousIo</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544286">FltReadFile</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff544610">FltWriteFile</a> to initiate an asynchronous I/O operation, the minifilter driver can optionally specify a callback routine to be called when the I/O operation is completed. This is done by specifying a routine of type PFLT_COMPLETED_ASYNC_IO_CALLBACK for the <i>CallbackRoutine</i> parameter. </p>

<p>When the I/O operation is completed, this callback routine is called in an arbitrary thread context, at IRQL &lt;= DISPATCH_LEVEL. </p>

<p>Because the PFLT_COMPLETED_ASYNC_IO_CALLBACK routine can be called at IRQL DISPATCH_LEVEL, it is subject to the following constraints: </p>

<p>It cannot safely call any kernel-mode routines that require a lower IRQL. </p>

<p>Any data structures used in this routine must be allocated from nonpaged pool. </p>

<p>It cannot be made pageable. </p>

<p>It cannot acquire resources, mutexes, or fast mutexes. However, it can acquire spin locks. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
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
<p>IRQL</p>
</th>
<td width="70%">
<p>See Remarks section.</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543420">FltPerformAsynchronousIo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544286">FltReadFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544610">FltWriteFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20PFLT_COMPLETED_ASYNC_IO_CALLBACK function pointer%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
