---
UID: NC.fltkernel.PFLT_INSTANCE_TEARDOWN_CALLBACK
title: PFLT_INSTANCE_TEARDOWN_CALLBACK
author: windows-driver-content
description: A minifilter driver can register two routines of type PFLT_INSTANCE_TEARDOWN_CALLBACK as the minifilter driver's InstanceTeardownStartCallback and InstanceTeardownCompleteCallback routines.
old-location: ifsk\pflt_instance_teardown_callback.htm
ms.assetid: d2f87c47-7f26-4c22-a5b8-2be8f309d1ba
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: ifsk
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PFLT_INSTANCE_TEARDOWN_CALLBACK
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
ms.keywords: IXpsPartIterator, Reset, IXpsPartIterator::Reset
req.iface: IXpsPartIterator
---

# PFLT_INSTANCE_TEARDOWN_CALLBACK callback



## -description
<p>A minifilter driver can register two routines of type PFLT_INSTANCE_TEARDOWN_CALLBACK as the minifilter driver's <i>InstanceTeardownStartCallback</i> and <i>InstanceTeardownCompleteCallback</i> routines. </p>


## -prototype

````
typedef VOID ( *PFLT_INSTANCE_TEARDOWN_CALLBACK)(
  _In_ PCFLT_RELATED_OBJECTS       FltObjects,
  _In_ FLT_INSTANCE_TEARDOWN_FLAGS Reason
);
````


## -parameters
<dl>

### -param <i>FltObjects</i> [in]

<dd>
<p>Pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff544816">FLT_RELATED_OBJECTS</a> structure that contains opaque pointers for the objects related to the current I/O operation. </p>
</dd>

### -param <i>Reason</i> [in]

<dd>
<p>Flag that indicates why the minifilter driver instance is being torn down. One of the following: </p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>FLTFL_INSTANCE_TEARDOWN_FILTER_UNLOAD</p>
</td>
<td>
<p>The minifilter driver is being unloaded. </p>
</td>
</tr>
<tr>
<td>
<p>FLTFL_INSTANCE_TEARDOWN_INTERNAL_ERROR</p>
</td>
<td>
<p>An error, such as a memory allocation failure, occurred during instance setup. </p>
</td>
</tr>
<tr>
<td>
<p>FLTFL_INSTANCE_TEARDOWN_MANDATORY_FILTER_UNLOAD</p>
</td>
<td>
<p>The minifilter driver is being unloaded. </p>
</td>
</tr>
<tr>
<td>
<p>FLTFL_INSTANCE_TEARDOWN_MANUAL</p>
</td>
<td>
<p>The instance is being detached because a user-mode application has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff540475">FilterDetach</a> or a kernel-mode component has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff542041">FltDetachVolume</a>. </p>
</td>
</tr>
<tr>
<td>
<p>FLTFL_INSTANCE_TEARDOWN_VOLUME_DISMOUNT</p>
</td>
<td>
<p>If set, the volume is being dismounted. (Or the volume has already been dismounted. Or the volume mount operation failed. Or the minifilter driver instance or the volume is being torn down. Or the file system unregistered itself as an active file system.) </p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>None </p>

## -remarks
<p>When a minifilter driver registers itself by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff544305">FltRegisterFilter</a> from its <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine, it can register two routines of type PFLT_INSTANCE_TEARDOWN_CALLBACK as the minifilter driver's <i>InstanceTeardownStartCallback</i> and <i>InstanceTeardownCompleteCallback</i> routines. </p>

<p>To register these callback routines, the minifilter driver stores the addresses of the two routines of type PFLT_INSTANCE_TEARDOWN_CALLBACK in the <b>InstanceTeardownStartCallback</b> and <b>InstanceTeardownCompleteCallback</b> members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544811">FLT_REGISTRATION</a> structure that the minifilter driver passes as the <i>Registration</i> parameter of <b>FltRegisterFilter</b>. </p>

<p>The <i>InstanceTeardownStartCallback</i> and <i>InstanceTeardownCompleteCallback</i> routines are optional and can be <b>NULL</b>. If the minifilter driver specifies <b>NULL</b> for the <i>InstanceTeardownStartCallback</i> or <i>InstanceTeardownCompleteCallback</i> routine, the instance is still torn down. </p>

<p>The <i>InstanceTeardownStartCallback</i> routine is called when the filter manager starts tearing down a minifilter driver instance to allow the minifilter driver to complete any pended I/O operations and save state information. </p>

<p>The <i>InstanceTeardownStartCallback</i> routine must: </p>

<p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541913">FltCompletePendedPreOperation</a> for each I/O operation that was pended in the minifilter driver's preoperation callback routine to complete the operation or return control of the operation to the filter manager. </p>

<p>Not pend any new I/O operations. If the minifilter driver uses a callback data queue, it must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541796">FltCbdqDisable</a> to disable it. </p>

<p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541897">FltCompletePendedPostOperation</a> for each I/O operation that was pended in the minifilter driver's postoperation callback routine to return control of the operation to the filter manager. </p>

<p>The <i>InstanceTeardownStartCallback</i> routine can optionally do the following to allow the minifilter driver to unload as quickly as possible: </p>

<p>Close any opened files. </p>

<p>Ensure that worker threads perform only the minimum necessary to complete processing of outstanding work items. </p>

<p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541785">FltCancelIo</a> to cancel any I/O operations that were initiated by the minifilter driver. </p>

<p>Stop queuing new work items. </p>

<p>Once the minifilter driver's <i>InstanceTeardownStartCallback</i> routine is called, the minifilter driver's preoperation and postoperation callback routines are not called for any new I/O operations. However, they may be called for I/O operations that were started before instance teardown was initiated. </p>

<p>The <i>InstanceTeardownCompleteCallback</i> routine is called when the teardown process is complete to allow the minifilter driver to close open files and perform any other necessary cleanup processing. </p>

<p>The <i>InstanceTeardownCompleteCallback</i> routine must close any files that were opened by the minifilter driver. </p>

<p>The filter manager calls the minifilter driver's <i>InstanceTeardownCompleteCallback</i> routine only after all outstanding I/O operations have been completed or drained. </p>

<p><b>Warning</b>: The <i>InstanceTeardownCompleteCallback</i> routine will not be called if any of the following conditions are true: </p>

<p>There are outstanding pended I/O operations. </p>

<p>There are any outstanding I/O operations that were initiated by the minifilter driver. </p>

<p>If the minifilter driver instance is being torn down because the minifilter driver is being unloaded, the unload operation appears to hang until the <i>InstanceTeardownCompleteCallback</i> routine returns. To debug these kinds of problems, you should enable the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557262">Driver Verifier</a> on your minifilter driver. The Filter Verifier <a href="NULL">I/O Verification</a> option can help identify possible causes, such as unreleased references, that would prevent the minifilter driver from unloading. For more information, see <a href="ifsk.development_and_testing_tools#filter_verifier#filter_verifier">Filter Verifier</a>. </p>

<p>Note that referencing the instance (by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff543382">FltObjectReference</a>) does not prevent the <i>InstanceTeardownCompleteCallback</i> routine from being called. </p>

<p>The filter manager calls the <i>InstanceTeardownStartCallback</i> and <i>InstanceTeardownCompleteCallback</i> routines at IRQL PASSIVE_LEVEL. </p>

<p>When a minifilter driver registers itself by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff544305">FltRegisterFilter</a> from its <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine, it can register two routines of type PFLT_INSTANCE_TEARDOWN_CALLBACK as the minifilter driver's <i>InstanceTeardownStartCallback</i> and <i>InstanceTeardownCompleteCallback</i> routines. </p>

<p>To register these callback routines, the minifilter driver stores the addresses of the two routines of type PFLT_INSTANCE_TEARDOWN_CALLBACK in the <b>InstanceTeardownStartCallback</b> and <b>InstanceTeardownCompleteCallback</b> members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544811">FLT_REGISTRATION</a> structure that the minifilter driver passes as the <i>Registration</i> parameter of <b>FltRegisterFilter</b>. </p>

<p>The <i>InstanceTeardownStartCallback</i> and <i>InstanceTeardownCompleteCallback</i> routines are optional and can be <b>NULL</b>. If the minifilter driver specifies <b>NULL</b> for the <i>InstanceTeardownStartCallback</i> or <i>InstanceTeardownCompleteCallback</i> routine, the instance is still torn down. </p>

<p>The <i>InstanceTeardownStartCallback</i> routine is called when the filter manager starts tearing down a minifilter driver instance to allow the minifilter driver to complete any pended I/O operations and save state information. </p>

<p>The <i>InstanceTeardownStartCallback</i> routine must: </p>

<p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541913">FltCompletePendedPreOperation</a> for each I/O operation that was pended in the minifilter driver's preoperation callback routine to complete the operation or return control of the operation to the filter manager. </p>

<p>Not pend any new I/O operations. If the minifilter driver uses a callback data queue, it must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541796">FltCbdqDisable</a> to disable it. </p>

<p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541897">FltCompletePendedPostOperation</a> for each I/O operation that was pended in the minifilter driver's postoperation callback routine to return control of the operation to the filter manager. </p>

<p>The <i>InstanceTeardownStartCallback</i> routine can optionally do the following to allow the minifilter driver to unload as quickly as possible: </p>

<p>Close any opened files. </p>

<p>Ensure that worker threads perform only the minimum necessary to complete processing of outstanding work items. </p>

<p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541785">FltCancelIo</a> to cancel any I/O operations that were initiated by the minifilter driver. </p>

<p>Stop queuing new work items. </p>

<p>Once the minifilter driver's <i>InstanceTeardownStartCallback</i> routine is called, the minifilter driver's preoperation and postoperation callback routines are not called for any new I/O operations. However, they may be called for I/O operations that were started before instance teardown was initiated. </p>

<p>The <i>InstanceTeardownCompleteCallback</i> routine is called when the teardown process is complete to allow the minifilter driver to close open files and perform any other necessary cleanup processing. </p>

<p>The <i>InstanceTeardownCompleteCallback</i> routine must close any files that were opened by the minifilter driver. </p>

<p>The filter manager calls the minifilter driver's <i>InstanceTeardownCompleteCallback</i> routine only after all outstanding I/O operations have been completed or drained. </p>

<p><b>Warning</b>: The <i>InstanceTeardownCompleteCallback</i> routine will not be called if any of the following conditions are true: </p>

<p>There are outstanding pended I/O operations. </p>

<p>There are any outstanding I/O operations that were initiated by the minifilter driver. </p>

<p>If the minifilter driver instance is being torn down because the minifilter driver is being unloaded, the unload operation appears to hang until the <i>InstanceTeardownCompleteCallback</i> routine returns. To debug these kinds of problems, you should enable the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557262">Driver Verifier</a> on your minifilter driver. The Filter Verifier <a href="NULL">I/O Verification</a> option can help identify possible causes, such as unreleased references, that would prevent the minifilter driver from unloading. For more information, see <a href="ifsk.development_and_testing_tools#filter_verifier#filter_verifier">Filter Verifier</a>. </p>

<p>Note that referencing the instance (by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff543382">FltObjectReference</a>) does not prevent the <i>InstanceTeardownCompleteCallback</i> routine from being called. </p>

<p>The filter manager calls the <i>InstanceTeardownStartCallback</i> and <i>InstanceTeardownCompleteCallback</i> routines at IRQL PASSIVE_LEVEL. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540475">FilterDetach</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544811">FLT_REGISTRATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544816">FLT_RELATED_OBJECTS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541785">FltCancelIo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541796">FltCbdqDisable</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541897">FltCompletePendedPostOperation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541913">FltCompletePendedPreOperation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542041">FltDetachVolume</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544305">FltRegisterFilter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551095">PFLT_INSTANCE_QUERY_TEARDOWN_CALLBACK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551096">PFLT_INSTANCE_SETUP_CALLBACK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20PFLT_INSTANCE_TEARDOWN_CALLBACK function pointer%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
