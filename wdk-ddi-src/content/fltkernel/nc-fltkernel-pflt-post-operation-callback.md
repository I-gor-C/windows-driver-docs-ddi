---
UID: NC.fltkernel.PFLT_POST_OPERATION_CALLBACK
title: PFLT_POST_OPERATION_CALLBACK
author: windows-driver-content
description: A minifilter driver can register one or more routines of type PFLT_POST_OPERATION_CALLBACK to perform completion processing for I/O operations.
old-location: ifsk\pflt_post_operation_callback.htm
old-project: ifsk
ms.assetid: 5bf2a533-e06b-4834-9075-62cb62fa5b06
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IXpsPartIterator, Reset, IXpsPartIterator::Reset
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: fltkernel.h
req.include-header: FltKernel.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Microsoft Windows 2000 Update Rollup 1 for SP4, Windows XP SP2, Windows Server 2003 SP1, and later Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PFLT_POST_OPERATION_CALLBACK
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
req.iface: IXpsPartIterator
---

# PFLT_POST_OPERATION_CALLBACK callback



## -description
<p>A minifilter driver can register one or more routines of type PFLT_POST_OPERATION_CALLBACK to perform completion processing for I/O operations. </p>


## -prototype

````
typedef FLT_POSTOP_CALLBACK_STATUS ( *PFLT_POST_OPERATION_CALLBACK)(
  _Inout_  PFLT_CALLBACK_DATA       Data,
  _In_     PCFLT_RELATED_OBJECTS    FltObjects,
  _In_opt_ PVOID                    CompletionContext,
  _In_     FLT_POST_OPERATION_FLAGS Flags
);
````


## -parameters
<dl>

### -param Data [in, out]

<dd>
<p>A pointer to the callback data (<a href="..\fltkernel\ns-fltkernel--flt-callback-data.md">FLT_CALLBACK_DATA</a>) structure for the I/O operation. </p>
</dd>

### -param FltObjects [in]

<dd>
<p>A pointer to a filter manager maintained <a href="..\fltkernel\ns-fltkernel--flt-related-objects.md">FLT_RELATED_OBJECTS</a> structure that contains opaque pointers for the objects related to the current I/O request. </p>
</dd>

### -param CompletionContext [in, optional]

<dd>
<p>A context pointer that was returned by the minifilter driver's pre-operation callback (<a href="..\fltkernel\nc-fltkernel-pflt-pre-operation-callback.md">PFLT_PRE_OPERATION_CALLBACK</a>) routine.  The <i>CompletionContext</i> pointer provides a way to communicate information from the pre-operation callback routine to the post-operation callback routine.</p>
</dd>

### -param Flags [in]

<dd>
<p>A bitmask of flags that specifies how the post-operation callback is to be performed. </p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>FLTFL_POST_OPERATION_DRAINING</p>
</td>
<td>
<p>The filter manager sets this flag to indicate that the minifilter driver instance is being detached and that this post-operation callback routine is being called to clean up the minifilter driver's completion context. The post-operation callback should return FLT_POSTOP_FINISHED_PROCESSING. If this flag is set, the <i>Data</i> parameter points to a copy of the original callback data structure for the operation, not the original callback data structure. Additionally, when this flag is set, the post-operation callback routine is called at IRQL &lt;= APC_LEVEL.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>This callback routine returns one of the following status values: </p><dl>
<dt><b>FLT_POSTOP_FINISHED_PROCESSING</b></dt>
</dl><p>The minifilter driver has finished completion processing for the I/O operation and is returning control of the operation to the filter manager. </p>

<p>After the post-operation callback returns this status value, the filter manager continues completion processing of the I/O operation. </p><dl>
<dt><b>FLT_POSTOP_MORE_PROCESSING_REQUIRED</b></dt>
</dl><p>The minifilter driver has halted completion processing for the I/O operation, but it is not returning control of the operation to the filter manager. </p>

<p>A minifilter driver's post-operation callback can return this status value only if the minifilter driver's post-operation callback has posted the I/O operation to a work queue. The minifilter driver must eventually resume completion processing of the I/O operation. </p>

<p>After the post-operation callback returns FLT_POSTOP_MORE_PROCESSING_REQUIRED, the filter manager performs no further completion processing of the I/O operation, unless both of the following conditions are true: </p>

<p>The post-operation callback has posted the I/O operation to a work queue. </p>

<p>After the work routine performs completion processing for the operation, it calls <a href="..\fltkernel\nf-fltkernel-fltcompletependedpostoperation.md">FltCompletePendedPostOperation</a> to return control of the operation to the filter manager. </p>

<p>This status value can only be returned for IRP-based I/O operations. To determine whether a given callback data structure represents an IRP-based I/O operation, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544654">FLT_IS_IRP_OPERATION</a> macro. </p>

<p> </p>

## -remarks
<p>A minifilter driver's post-operation callback routine performs completion processing for one or more types of I/O operations. </p>

<p>Post-operation callback routines are similar to the completion routines used by legacy file system filter drivers. </p>

<p>Post-operation callback routines are called in an arbitrary thread context, at IRQL &lt;= DISPATCH_LEVEL. </p>

<p>Because this callback routine can be called at IRQL DISPATCH_LEVEL, it is subject to the following constraints: </p>

<p>It cannot safely call any kernel-mode routine that must run at a lower IRQL. </p>

<p>Any data structures used in this routine must be allocated from nonpaged pool. </p>

<p>It cannot be made pageable. </p>

<p>It cannot acquire resources, mutexes, or fast mutexes. However, it can acquire spin locks. </p>

<p>It cannot get, set, or delete contexts, but it can release contexts. </p>

<p>Any I/O completion processing that needs to be performed at IRQL &lt; DISPATCH_LEVEL cannot be performed directly in the postoperation callback routine. Instead, it must be posted to a work queue by calling a routine such as <a href="..\fltkernel\nf-fltkernel-fltdocompletionprocessingwhensafe.md">FltDoCompletionProcessingWhenSafe</a> or <a href="..\fltkernel\nf-fltkernel-fltqueuedeferredioworkitem.md">FltQueueDeferredIoWorkItem</a>. </p>

<p>Be aware that <b>FltDoCompletionProcessingWhenSafe</b> should never be called if the <i>Flags</i> parameter of the post-operation callback has the FLTFL_POST_OPERATION_DRAINING bit set.  The following are exceptions to this rule: </p>

<p>If a minifilter driver's pre-operation callback routine returns FLT_PREOP_SYNCHRONIZE for an IRP-based I/O operation, the corresponding post-operation callback routine is guaranteed to be called at IRQL &lt;= APC_LEVEL, in the same thread context as the pre-operation callback. </p>

<p>Post-create callback routines are guaranteed to be called at IRQL PASSIVE_LEVEL, in the context of the thread that originated the IRP_MJ_CREATE operation. </p>

<p>A minifilter driver registers a post-operation callback routine for a particular type of I/O operation by storing the callback routine's entry point in the <b>OperationRegistration</b> array of the <a href="..\fltkernel\ns-fltkernel--flt-registration.md">FLT_REGISTRATION</a> structure.  The minifilter driver passes this structure as a parameter to <a href="..\fltkernel\nf-fltkernel-fltregisterfilter.md">FltRegisterFilter</a> in its <a href="..\wdm\nc-wdm-driver-initialize.md">DriverEntry</a> routine. </p>

<p>A minifilter driver can register a post-operation callback routine for a particular type of I/O operation without registering a pre-operation callback (<a href="..\fltkernel\nc-fltkernel-pflt-pre-operation-callback.md">PFLT_PRE_OPERATION_CALLBACK</a>) routine, and vice versa. </p>

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
<p>Available in Microsoft Windows 2000 Update Rollup 1 for SP4, Windows XP SP2, Windows Server 2003 SP1, and later Windows operating systems. </p>
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
<a href="..\fltkernel\ns-fltkernel--flt-callback-data.md">FLT_CALLBACK_DATA</a>
</dt>
<dt>
<a href="..\fltkernel\ns-fltkernel--flt-io-parameter-block.md">FLT_IO_PARAMETER_BLOCK</a>
</dt>
<dt>
<a href="ifsk.flt_is_fastio_operation">FLT_IS_FASTIO_OPERATION</a>
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
<a href="..\fltkernel\ns-fltkernel--flt-registration.md">FLT_REGISTRATION</a>
</dt>
<dt>
<a href="..\fltkernel\ns-fltkernel--flt-related-objects.md">FLT_RELATED_OBJECTS</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltcancelfileopen.md">FltCancelFileOpen</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltcompletependedpostoperation.md">FltCompletePendedPostOperation</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltdocompletionprocessingwhensafe.md">FltDoCompletionProcessingWhenSafe</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltqueuedeferredioworkitem.md">FltQueueDeferredIoWorkItem</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltregisterfilter.md">FltRegisterFilter</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltsetcallbackdatadirty.md">FltSetCallbackDataDirty</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt-pre-operation-callback.md">PFLT_PRE_OPERATION_CALLBACK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20PFLT_POST_OPERATION_CALLBACK function pointer%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
