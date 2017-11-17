---
UID: NC.fltkernel.PFLT_PRE_OPERATION_CALLBACK
title: PFLT_PRE_OPERATION_CALLBACK
author: windows-driver-content
description: A minifilter driver's PFLT_PRE_OPERATION_CALLBACK routine performs pre-operation processing for I/O operations.
old-location: ifsk\pflt_pre_operation_callback.htm
ms.assetid: 758a480a-b52c-45e4-8c78-74c805c61e07
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: ifsk
req.header: fltkernel.h
req.include-header: FltKernel.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Microsoft Windows 2000 Update Rollup 1 for SP4, Windows XP SP2, Windows Server 2003 SP1, and later Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PFLT_PRE_OPERATION_CALLBACK
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
req.irql: See Remarks section
ms.keywords: IXpsPartIterator, Reset, IXpsPartIterator::Reset
req.iface: IXpsPartIterator
---

# PFLT_PRE_OPERATION_CALLBACK callback



## -description
<p>A minifilter driver's PFLT_PRE_OPERATION_CALLBACK routine performs pre-operation processing for I/O operations. </p>


## -prototype

````
typedef FLT_PREOP_CALLBACK_STATUS ( *PFLT_PRE_OPERATION_CALLBACK)(
  _Inout_ PFLT_CALLBACK_DATA    Data,
  _In_    PCFLT_RELATED_OBJECTS FltObjects,
  _Out_   PVOID                 *CompletionContext
);
````


## -parameters
<dl>

### -param <i>Data</i> [in, out]

<dd>
<p>A pointer to the callback data (<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>) structure for the I/O operation. </p>
</dd>

### -param <i>FltObjects</i> [in]

<dd>
<p>A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff544816">FLT_RELATED_OBJECTS</a> structure that contains opaque pointers for the objects related to the current I/O request. </p>
</dd>

### -param <i>CompletionContext</i> [out]

<dd>
<p>If this callback routine returns FLT_PREOP_SUCCESS_WITH_CALLBACK or FLT_PREOP_SYNCHRONIZE, this parameter is an optional context pointer to be passed to the corresponding post-operation callback routine. Otherwise, it must be <b>NULL</b>. </p>
</dd>
</dl>

## -returns
<p>This callback routine returns one of the following FLT_PREOP_CALLBACK_STATUS values: </p><dl>
<dt><b>FLT_PREOP_COMPLETE</b></dt>
</dl><p>The minifilter driver is completing the I/O operation. The filter manager does not send the I/O operation to any minifilter drivers below the caller in the driver stack or to the file system. In this case, the filter manager only calls the post-operation callback routines of the minifilter drivers above the caller in the driver stack. </p><dl>
<dt><b>FLT_PREOP_DISALLOW_FASTIO</b></dt>
</dl><p>The operation is a fast I/O operation, and the minifilter driver is not allowing the fast I/O path to be used for this operation. The filter manager does not send the fast I/O operation to any minifilter drivers below the caller in the driver stack or to the file system. In this case, the filter manager only calls the post-operation callback routines of the minifilter drivers above the caller in the driver stack. </p><dl>
<dt><b>FLT_PREOP_PENDING</b></dt>
</dl><p>The minifilter driver has pended the I/O operation, and the operation is still pending. The filter manager does not process the I/O operation further until the minifilter driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff541913">FltCompletePendedPreOperation</a>. </p><dl>
<dt><b>FLT_PREOP_SUCCESS_NO_CALLBACK</b></dt>
</dl><p>The minifilter driver is returning the I/O operation to the filter manager for further processing. In this case, the filter manager does not call the minifilter driver's post-operation callback, if one exists, during I/O completion. </p><dl>
<dt><b>FLT_PREOP_SUCCESS_WITH_CALLBACK</b></dt>
</dl><p>The minifilter driver is returning the I/O operation to the filter manager for further processing. In this case, the filter manager calls the minifilter driver's post-operation callback during I/O completion. </p><dl>
<dt><b>FLT_PREOP_SYNCHRONIZE</b></dt>
</dl><p>The minifilter driver is returning the I/O operation to the filter manager for further processing, but it is not completing the operation. In this case, the filter manager calls the minifilter's post-operation callback in the context of the current thread at IRQL &lt;= APC_LEVEL. </p>

<p> </p>

## -remarks
<p>A minifilter driver's pre-operation callback routine processes one or more types of I/O operations. This callback routine is similar to a dispatch routine in the legacy filter model. </p>

<p>A minifilter driver registers a pre-operation callback routine for a particular type of I/O operation by storing the callback routine's entry point in the <b>OperationRegistration</b> array of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544811">FLT_REGISTRATION</a> structure. The minifilter driver passes this structure as a parameter to <a href="https://msdn.microsoft.com/library/windows/hardware/ff544305">FltRegisterFilter</a> in its <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine. A minifilter driver can register a pre-operation callback routine for a given type of I/O operation without registering a post-operation callback (<a href="https://msdn.microsoft.com/library/windows/hardware/ff551107">PFLT_POST_OPERATION_CALLBACK</a>) routine and vice versa. </p>

<p>If this routine returns FLT_PREOP_COMPLETE, it must set the callback data structure's <b>IoStatus.Status</b> field to the final NTSTATUS value for the I/O operation. This NTSTATUS value cannot be STATUS_PENDING. For a cleanup or close operation, it must be a success NTSTATUS value other than STATUS_PENDING because cleanup and close operations cannot fail. </p>

<p>If this routine returns FLT_PREOP_DISALLOW_FASTIO, it should not set the callback data structure's <b>IoStatus.Status</b> field because the filter manager automatically sets this field to STATUS_FLT_DISALLOW_FAST_IO. </p>

<p>FLT_PREOP_DISALLOW_FASTIO can only be returned for a fast I/O operation. To determine whether a given callback data structure represents a fast I/O operation, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544645">FLT_IS_FASTIO_OPERATION</a> macro. </p>

<p>FLT_PREOP_PENDING can only be returned for IRP-based I/O operations because only IRP-based I/O operations can be pended. To determine whether a given callback data structure represents an IRP-based I/O operation, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544654">FLT_IS_IRP_OPERATION</a> macro. </p>

<p>If a minifilter driver's pre-operation callback routine returns FLT_PREOP_SYNCHRONIZE, the minifilter driver must have registered a corresponding post-operation callback for the operation. </p>

<p>FLT_PREOP_SYNCHRONIZE should only be returned for IRP-based I/O operations. If it is returned for an I/O operation that is not an IRP-based operation, the filter manager treats this return value as if it were FLT_PREOP_SUCCESS_WITH_CALLBACK. </p>

<p>Minifilter drivers should not return FLT_PREOP_SYNCHRONIZE for create operations, because these operations are already synchronized by the filter manager. </p>

<p>Minifilter drivers must never return FLT_PREOP_SYNCHRONIZE for asynchronous read and write operations. Doing so can severely degrade both minifilter driver and system performance. </p>

<p>A minifilter driver's pre-operation or post-operation callback routine can modify the contents of the callback data structure for the operation. If it does, it must then call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544383">FltSetCallbackDataDirty</a>, unless it has changed the contents of the callback data structure's <b>IoStatus</b> field. </p>

<p>The IRQL for this generic callback routine depends on its specific IO paths.</p>

<p>File systems round write and read operations at end of file up to a multiple of the sector size of the underlying file storage device. When processing pre-read or pre-write operations, filters that allocate and swap buffers need to round the size of an allocated buffer up to a multiple of the sector size of the associated device. If they do not, the length of data transferred from the underlying file system will exceed the allocated length of the buffer. For more information about swapping buffers, see <a href="http://go.microsoft.com/fwlink/p/?linkid=256055">swapBuffers Minifilter Sample</a>.</p>

<p>Starting with Windows 8, <i>CompletionContext</i> uses the <a href="https://msdn.microsoft.com/C3B285EA-0DAB-48D4-AE2F-CB4FBB30EF15">_Flt_CompletionContext_Outptr_</a> annotation which defines valid context values based on the operation result. The following is a usage example for the callback with the annotation for <i>CompletionContext</i>.</p>

<p>A minifilter driver's pre-operation callback routine processes one or more types of I/O operations. This callback routine is similar to a dispatch routine in the legacy filter model. </p>

<p>A minifilter driver registers a pre-operation callback routine for a particular type of I/O operation by storing the callback routine's entry point in the <b>OperationRegistration</b> array of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544811">FLT_REGISTRATION</a> structure. The minifilter driver passes this structure as a parameter to <a href="https://msdn.microsoft.com/library/windows/hardware/ff544305">FltRegisterFilter</a> in its <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine. A minifilter driver can register a pre-operation callback routine for a given type of I/O operation without registering a post-operation callback (<a href="https://msdn.microsoft.com/library/windows/hardware/ff551107">PFLT_POST_OPERATION_CALLBACK</a>) routine and vice versa. </p>

<p>If this routine returns FLT_PREOP_COMPLETE, it must set the callback data structure's <b>IoStatus.Status</b> field to the final NTSTATUS value for the I/O operation. This NTSTATUS value cannot be STATUS_PENDING. For a cleanup or close operation, it must be a success NTSTATUS value other than STATUS_PENDING because cleanup and close operations cannot fail. </p>

<p>If this routine returns FLT_PREOP_DISALLOW_FASTIO, it should not set the callback data structure's <b>IoStatus.Status</b> field because the filter manager automatically sets this field to STATUS_FLT_DISALLOW_FAST_IO. </p>

<p>FLT_PREOP_DISALLOW_FASTIO can only be returned for a fast I/O operation. To determine whether a given callback data structure represents a fast I/O operation, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544645">FLT_IS_FASTIO_OPERATION</a> macro. </p>

<p>FLT_PREOP_PENDING can only be returned for IRP-based I/O operations because only IRP-based I/O operations can be pended. To determine whether a given callback data structure represents an IRP-based I/O operation, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544654">FLT_IS_IRP_OPERATION</a> macro. </p>

<p>If a minifilter driver's pre-operation callback routine returns FLT_PREOP_SYNCHRONIZE, the minifilter driver must have registered a corresponding post-operation callback for the operation. </p>

<p>FLT_PREOP_SYNCHRONIZE should only be returned for IRP-based I/O operations. If it is returned for an I/O operation that is not an IRP-based operation, the filter manager treats this return value as if it were FLT_PREOP_SUCCESS_WITH_CALLBACK. </p>

<p>Minifilter drivers should not return FLT_PREOP_SYNCHRONIZE for create operations, because these operations are already synchronized by the filter manager. </p>

<p>Minifilter drivers must never return FLT_PREOP_SYNCHRONIZE for asynchronous read and write operations. Doing so can severely degrade both minifilter driver and system performance. </p>

<p>A minifilter driver's pre-operation or post-operation callback routine can modify the contents of the callback data structure for the operation. If it does, it must then call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544383">FltSetCallbackDataDirty</a>, unless it has changed the contents of the callback data structure's <b>IoStatus</b> field. </p>

<p>The IRQL for this generic callback routine depends on its specific IO paths.</p>

<p>File systems round write and read operations at end of file up to a multiple of the sector size of the underlying file storage device. When processing pre-read or pre-write operations, filters that allocate and swap buffers need to round the size of an allocated buffer up to a multiple of the sector size of the associated device. If they do not, the length of data transferred from the underlying file system will exceed the allocated length of the buffer. For more information about swapping buffers, see <a href="http://go.microsoft.com/fwlink/p/?linkid=256055">swapBuffers Minifilter Sample</a>.</p>

<p>Starting with Windows 8, <i>CompletionContext</i> uses the <a href="https://msdn.microsoft.com/C3B285EA-0DAB-48D4-AE2F-CB4FBB30EF15">_Flt_CompletionContext_Outptr_</a> annotation which defines valid context values based on the operation result. The following is a usage example for the callback with the annotation for <i>CompletionContext</i>.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Microsoft Windows 2000 Update Rollup 1 for SP4, Windows XP SP2, Windows Server 2003 SP1, and later Windows operating systems.</p>
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
<p>IRQL</p>
</th>
<td width="70%">
<p>See Remarks section</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/C3B285EA-0DAB-48D4-AE2F-CB4FBB30EF15">_Flt_CompletionContext_Outptr_</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544638">FLT_IO_PARAMETER_BLOCK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544645">FLT_IS_FASTIO_OPERATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544654">FLT_IS_IRP_OPERATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544660">FLT_IS_REISSUED_IO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544663">FLT_IS_SYSTEM_BUFFER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544811">FLT_REGISTRATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544816">FLT_RELATED_OBJECTS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541897">FltCompletePendedPostOperation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541913">FltCompletePendedPreOperation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543449">FltQueueDeferredIoWorkItem</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544305">FltRegisterFilter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544383">FltSetCallbackDataDirty</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551107">PFLT_POST_OPERATION_CALLBACK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20PFLT_PRE_OPERATION_CALLBACK function pointer%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
