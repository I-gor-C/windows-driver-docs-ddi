---
UID: NF.wdfusb.WdfUsbTargetPipeWriteSynchronously
title: WdfUsbTargetPipeWriteSynchronously
author: windows-driver-content
description: The WdfUsbTargetPipeWriteSynchronously method builds a write request and sends it synchronously to a specified USB output pipe.
old-location: wdf\wdfusbtargetpipewritesynchronously.htm
old-project: wdf
ms.assetid: 5513a245-0417-42f7-9c01-99b8bd5745eb
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfUsbTargetPipeWriteSynchronously
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfusb.h
req.include-header: Wdfusb.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfUsbTargetPipeWriteSynchronously
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, InternalIoctlReqs, IoctlReqs, KmdfIrql, KmdfIrql2, ReadReqs, SyncReqSend, UsbKmdfIrql, UsbKmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); 
WUDFx02000.dll (UMDF)
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfUsbTargetPipeWriteSynchronously function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfUsbTargetPipeWriteSynchronously</b> method builds a write request and sends it synchronously to a specified USB output pipe.</p>


## -syntax

````
NTSTATUS WdfUsbTargetPipeWriteSynchronously(
  _In_      WDFUSBPIPE                Pipe,
  _In_opt_  WDFREQUEST                Request,
  _In_opt_  PWDF_REQUEST_SEND_OPTIONS RequestOptions,
  _In_opt_  PWDF_MEMORY_DESCRIPTOR    MemoryDescriptor,
  _Out_opt_ PULONG                    BytesWritten
);
````


## -parameters
<dl>

### -param <i>Pipe</i> [in]

<dd>
<p>A handle to a framework pipe object that was obtained by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff550057">WdfUsbInterfaceGetConfiguredPipe</a>.</p>
</dd>

### -param <i>Request</i> [in, optional]

<dd>
<p>A handle to a framework request object. This parameter is optional and can be <b>NULL</b>. For more information, see the following Remarks section.</p>
</dd>

### -param <i>RequestOptions</i> [in, optional]

<dd>
<p>A pointer to a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff552491">WDF_REQUEST_SEND_OPTIONS</a> structure that specifies options for the request. This pointer is optional and can be <b>NULL</b>. For more information, see the following Remarks section.</p>
</dd>

### -param <i>MemoryDescriptor</i> [in, optional]

<dd>
<p>A pointer to a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff552392">WDF_MEMORY_DESCRIPTOR</a> structure that describes the buffer that contains data that will be written to the device. For more information about this buffer, see the following Remarks section. </p>
</dd>

### -param <i>BytesWritten</i> [out, optional]

<dd>
<p>A pointer to a location that receives the number of bytes written, if the operation succeeds. This parameter is optional and can be <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p><b>WdfUsbTargetPipeWriteSynchronously</b> returns the I/O target's completion status value if the operation succeeds. Otherwise, this method might return one of the following values:</p><dl>
<dt><b>STATUS_INFO_LENGTH_MISMATCH</b></dt>
</dl><p>The size of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552491">WDF_REQUEST_SEND_OPTIONS</a> structure that the <i>RequestOptions</i> parameter points to was incorrect.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid parameter was detected.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>Insufficient memory was available.</p><dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>The caller's IRQL was not PASSIVE_LEVEL, an invalid memory descriptor was specified, the pipe's type was not valid, the transfer direction was invalid, or the specified I/O request was already queued to an I/O target.</p><dl>
<dt><b>STATUS_IO_TIMEOUT</b></dt>
</dl><p>The driver supplied a time-out value and the request did not complete within the allotted time.</p><dl>
<dt><b>STATUS_REQUEST_NOT_ACCEPTED</b></dt>
</dl><p>The I/O request packet (<a href="https://msdn.microsoft.com/library/windows/hardware/ff550694">IRP</a>) that the <i>Request</i> parameter represents does not provide enough <a href="https://msdn.microsoft.com/library/windows/hardware/ff550659">IO_STACK_LOCATION</a> structures to allow the driver to forward the request.</p>

<p> </p>

<p>This method also might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>Use the <b>WdfUsbTargetPipeWriteSynchronously</b> method to send write requests synchronously. To send write requests asynchronously, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff551141">WdfUsbTargetPipeFormatRequestForWrite</a>, followed by <a href="https://msdn.microsoft.com/library/windows/hardware/ff550027">WdfRequestSend</a>.</p>

<p>The specified pipe must be an output pipe, and the pipe's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439450">type</a> must be <b>WdfUsbPipeTypeBulk</b> or <b>WdfUsbPipeTypeInterrupt</b>.</p>

<p>The <b>WdfUsbTargetPipeWriteSynchronously</b> method does not return until the request has completed, unless the driver supplies a time-out value in the <i>RequestOptions</i> parameter's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552491">WDF_REQUEST_SEND_OPTIONS</a> structure, or unless an error is detected.</p>

<p>You can forward an I/O request that your driver received in an I/O queue, or you can create and send a new request. In either case, the framework requires a request object and some buffer space.</p>

<p>To forward an I/O request that your driver received in an I/O queue:</p>

<p>Specify the received request's handle for the <i>Request</i> parameter.</p>

<p>Use the received request's input buffer for the <i>MemoryDescriptor</i> parameter.</p>

<p>The driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff550015">WdfRequestRetrieveInputMemory</a> to obtain a handle to a framework memory object that represents the request's input buffer and then place that handle in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552392">WDF_MEMORY_DESCRIPTOR</a> structure that <i>MemoryDescriptor</i> points to.</p>

<p>For more information about forwarding an I/O request, see <a href="wdf.forwarding_i_o_requests">Forwarding I/O Requests</a>.</p>

<p>Drivers often divide received I/O requests into smaller requests that they send to an I/O target, so your driver might create new requests.</p>

<p>To create a new I/O request:</p>

<p>Supply a <b>NULL</b> request handle for the <b>WdfUsbTargetPipeWriteSynchronously</b> method's <i>Request</i> parameter, or create a new request object and supply its handle:<ul>
<li>If you supply a <b>NULL</b> request handle, the framework uses an internal request object. This technique is simple to use, but the driver cannot cancel the request.</li>
<li>If you call <a href="https://msdn.microsoft.com/library/windows/hardware/ff549951">WdfRequestCreate</a> to create one or more request objects, you can reuse these request objects by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff550026">WdfRequestReuse</a>. This technique enables your driver's <a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a> callback function to preallocate request objects for a device. Additionally, another driver thread can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff549941">WdfRequestCancelSentRequest</a> to cancel the request, if necessary.</li>
</ul>
</p>

<p>Your driver can specify a non-<b>NULL</b> <i>RequestOptions</i> parameter, whether the driver provides a non-<b>NULL</b> or a <b>NULL</b> <i>Request</i> parameter. You can, for example, use the <i>RequestOptions</i> parameter to specify a time-out value. </p>

<p>Provide buffer space for the <b>WdfUsbTargetPipeWriteSynchronously</b> method's <i>MemoryDescriptor</i> parameter.</p>

<p>Your driver can specify this buffer space as a locally allocated buffer, as a WDFMEMORY handle, or as a MDL. You can use whichever method is most convenient. </p>

<p>If necessary, the framework converts the buffer description to one that is correct for the I/O target's <a href="https://msdn.microsoft.com/f95a0aec-65f9-44c9-8ae5-11bb4d832752">method for accessing data buffers</a>. </p>

<p>The following techniques are available:</p>

<p>Supply a local buffer</p>

<p>Because <b>WdfUsbTargetPipeWriteSynchronously</b> handles I/O requests synchronously, the driver can create request buffers that are local to the calling routine, as the following code example shows.</p>

<p>Supply a WDFMEMORY handle</p>

<p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548706">WdfMemoryCreate</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff548712">WdfMemoryCreatePreallocated</a> to obtain a handle to framework-managed memory, as the following code example shows. </p>

<p>Alternatively, the driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff550015">WdfRequestRetrieveInputMemory</a> to obtain a handle to a framework memory object that represents a received I/O request's input buffer, if you want the driver to pass that buffer's contents to the I/O target. The driver must not complete the received I/O request until the new request that <b>WdfUsbTargetPipeWriteSynchronously</b> sends to the I/O target has been deleted, reused, or reformatted. (<b>WdfUsbTargetPipeWriteSynchronously</b> increments the memory object's reference count. Deleting, reusing, or reformatting a request object decrements the memory object's reference count.)</p>

<p>Supply a MDL</p>

<p>Drivers can obtain the MDL that is associated with a received I/O request by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff550016">WdfRequestRetrieveInputWdmMdl</a>.</p>

<p>For information about obtaining status information after an I/O request completes, see <a href="wdf.completing_i_o_requests#obtaining_completion_information#obtaining_completion_information">Obtaining Completion Information</a>.</p>

<p>For more information about the <b>WdfUsbTargetPipeWriteSynchronously</b> method and USB I/O targets, see <a href="wdf.usb_i_o_targets">USB I/O Targets</a>.</p>

<p>The following code example creates a memory object, obtains a pointer to the object's buffer, fills the buffer, and uses the buffer as input to <b>WdfUsbTargetPipeWriteSynchronously</b>.</p>

<p>Use the <b>WdfUsbTargetPipeWriteSynchronously</b> method to send write requests synchronously. To send write requests asynchronously, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff551141">WdfUsbTargetPipeFormatRequestForWrite</a>, followed by <a href="https://msdn.microsoft.com/library/windows/hardware/ff550027">WdfRequestSend</a>.</p>

<p>The specified pipe must be an output pipe, and the pipe's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439450">type</a> must be <b>WdfUsbPipeTypeBulk</b> or <b>WdfUsbPipeTypeInterrupt</b>.</p>

<p>The <b>WdfUsbTargetPipeWriteSynchronously</b> method does not return until the request has completed, unless the driver supplies a time-out value in the <i>RequestOptions</i> parameter's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552491">WDF_REQUEST_SEND_OPTIONS</a> structure, or unless an error is detected.</p>

<p>You can forward an I/O request that your driver received in an I/O queue, or you can create and send a new request. In either case, the framework requires a request object and some buffer space.</p>

<p>To forward an I/O request that your driver received in an I/O queue:</p>

<p>Specify the received request's handle for the <i>Request</i> parameter.</p>

<p>Use the received request's input buffer for the <i>MemoryDescriptor</i> parameter.</p>

<p>The driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff550015">WdfRequestRetrieveInputMemory</a> to obtain a handle to a framework memory object that represents the request's input buffer and then place that handle in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552392">WDF_MEMORY_DESCRIPTOR</a> structure that <i>MemoryDescriptor</i> points to.</p>

<p>For more information about forwarding an I/O request, see <a href="wdf.forwarding_i_o_requests">Forwarding I/O Requests</a>.</p>

<p>Drivers often divide received I/O requests into smaller requests that they send to an I/O target, so your driver might create new requests.</p>

<p>To create a new I/O request:</p>

<p>Supply a <b>NULL</b> request handle for the <b>WdfUsbTargetPipeWriteSynchronously</b> method's <i>Request</i> parameter, or create a new request object and supply its handle:<ul>
<li>If you supply a <b>NULL</b> request handle, the framework uses an internal request object. This technique is simple to use, but the driver cannot cancel the request.</li>
<li>If you call <a href="https://msdn.microsoft.com/library/windows/hardware/ff549951">WdfRequestCreate</a> to create one or more request objects, you can reuse these request objects by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff550026">WdfRequestReuse</a>. This technique enables your driver's <a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a> callback function to preallocate request objects for a device. Additionally, another driver thread can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff549941">WdfRequestCancelSentRequest</a> to cancel the request, if necessary.</li>
</ul>
</p>

<p>Your driver can specify a non-<b>NULL</b> <i>RequestOptions</i> parameter, whether the driver provides a non-<b>NULL</b> or a <b>NULL</b> <i>Request</i> parameter. You can, for example, use the <i>RequestOptions</i> parameter to specify a time-out value. </p>

<p>Provide buffer space for the <b>WdfUsbTargetPipeWriteSynchronously</b> method's <i>MemoryDescriptor</i> parameter.</p>

<p>Your driver can specify this buffer space as a locally allocated buffer, as a WDFMEMORY handle, or as a MDL. You can use whichever method is most convenient. </p>

<p>If necessary, the framework converts the buffer description to one that is correct for the I/O target's <a href="https://msdn.microsoft.com/f95a0aec-65f9-44c9-8ae5-11bb4d832752">method for accessing data buffers</a>. </p>

<p>The following techniques are available:</p>

<p>Supply a local buffer</p>

<p>Because <b>WdfUsbTargetPipeWriteSynchronously</b> handles I/O requests synchronously, the driver can create request buffers that are local to the calling routine, as the following code example shows.</p>

<p>Supply a WDFMEMORY handle</p>

<p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548706">WdfMemoryCreate</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff548712">WdfMemoryCreatePreallocated</a> to obtain a handle to framework-managed memory, as the following code example shows. </p>

<p>Alternatively, the driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff550015">WdfRequestRetrieveInputMemory</a> to obtain a handle to a framework memory object that represents a received I/O request's input buffer, if you want the driver to pass that buffer's contents to the I/O target. The driver must not complete the received I/O request until the new request that <b>WdfUsbTargetPipeWriteSynchronously</b> sends to the I/O target has been deleted, reused, or reformatted. (<b>WdfUsbTargetPipeWriteSynchronously</b> increments the memory object's reference count. Deleting, reusing, or reformatting a request object decrements the memory object's reference count.)</p>

<p>Supply a MDL</p>

<p>Drivers can obtain the MDL that is associated with a received I/O request by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff550016">WdfRequestRetrieveInputWdmMdl</a>.</p>

<p>For information about obtaining status information after an I/O request completes, see <a href="wdf.completing_i_o_requests#obtaining_completion_information#obtaining_completion_information">Obtaining Completion Information</a>.</p>

<p>For more information about the <b>WdfUsbTargetPipeWriteSynchronously</b> method and USB I/O targets, see <a href="wdf.usb_i_o_targets">USB I/O Targets</a>.</p>

<p>The following code example creates a memory object, obtains a pointer to the object's buffer, fills the buffer, and uses the buffer as input to <b>WdfUsbTargetPipeWriteSynchronously</b>.</p>

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
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfusb.h (include Wdfusb.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547217">InternalIoctlReqs</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547288">IoctlReqs</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff551525">ReadReqs</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff552890">SyncReqSend</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff554042">UsbKmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh995019">UsbKmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552393">WDF_MEMORY_DESCRIPTOR_INIT_BUFFER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548706">WdfMemoryCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548715">WdfMemoryGetBuffer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549941">WdfRequestCancelSentRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551155">WdfUsbTargetPipeReadSynchronously</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfUsbTargetPipeWriteSynchronously method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
