---
UID: NF.wdfiotarget.WdfIoTargetSendIoctlSynchronously
title: WdfIoTargetSendIoctlSynchronously function
author: windows-driver-content
description: The WdfIoTargetSendIoctlSynchronously method builds a device control request and sends it synchronously to an I/O target.
old-location: wdf\wdfiotargetsendioctlsynchronously.htm
old-project: wdf
ms.assetid: 1c43f6cd-0026-4654-b3ce-71fd51b3821d
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfIoTargetSendIoctlSynchronously
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfiotarget.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfIoTargetSendIoctlSynchronously
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DeferredRequestCompleted, DriverCreate, InternalIoctlReqs, KmdfIrql, KmdfIrql2, ReadReqs, RequestCompleted, RequestCompletedLocal, SyncReqSend, WriteReqs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# WdfIoTargetSendIoctlSynchronously function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfIoTargetSendIoctlSynchronously</b> method builds a device control request and sends it synchronously to an I/O target.



## -syntax

````
NTSTATUS WdfIoTargetSendIoctlSynchronously(
  _In_      WDFIOTARGET               IoTarget,
  _In_opt_  WDFREQUEST                Request,
  _In_      ULONG                     IoctlCode,
  _In_opt_  PWDF_MEMORY_DESCRIPTOR    InputBuffer,
  _In_opt_  PWDF_MEMORY_DESCRIPTOR    OutputBuffer,
  _In_opt_  PWDF_REQUEST_SEND_OPTIONS RequestOptions,
  _Out_opt_ PULONG_PTR                BytesReturned
);
````


## -parameters

### -param IoTarget [in]

A handle to a local or remote I/O target object that was obtained from a previous call to <a href="wdf.wdfdevicegetiotarget">WdfDeviceGetIoTarget</a> or <a href="wdf.wdfiotargetcreate">WdfIoTargetCreate</a>, or from a method that a specialized I/O target supplies.


### -param Request [in, optional]

A handle to a framework request object. This parameter is optional and can be <b>NULL</b>. For more information, see the following Remarks section.


### -param IoctlCode [in]

An I/O control code (IOCTL) that the I/O target supports. 


### -param InputBuffer [in, optional]

A pointer to a caller-allocated <a href="wdf.wdf_memory_descriptor">WDF_MEMORY_DESCRIPTOR</a> structure that describes a buffer that will be written to the I/O target. For more information, see the following Remarks section. This parameter is optional and can be <b>NULL</b> if the request does not send data.


### -param OutputBuffer [in, optional]

A pointer to a caller-allocated <a href="wdf.wdf_memory_descriptor">WDF_MEMORY_DESCRIPTOR</a> structure that describes a buffer that will receive data from the I/O target. For more information, see the following Remarks section. This parameter is optional and can be <b>NULL</b> if the request does not receive data.


### -param RequestOptions [in, optional]

A pointer to a caller-allocated <a href="wdf.wdf_request_send_options">WDF_REQUEST_SEND_OPTIONS</a> structure that specifies options for the request. This pointer is optional and can be <b>NULL</b>. For more information, see the following Remarks section.


### -param BytesReturned [out, optional]

A pointer to a location that receives information (such as the number of bytes that were transferred) that another driver supplies when it completes the request by calling <a href="wdf.wdfrequestcompletewithinformation">WdfRequestCompleteWithInformation</a>. This pointer is optional and can be <b>NULL</b>.


## -returns
If the operation succeeds, <b>WdfIoTargetSendIoctlSynchronously</b> returns after the device control request completes, and the return value is the request's completion status value. Otherwise, this method might return one of the following values:
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>An invalid parameter was detected.
<dl>
<dt><b>STATUS_INFO_LENGTH_MISMATCH</b></dt>
</dl>The size of the <a href="wdf.wdf_request_send_options">WDF_REQUEST_SEND_OPTIONS</a> structure that the <i>RequestOptions</i> parameter pointed to was incorrect.
<dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl>The request was already queued to an I/O target.
<dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl>The framework cannot allocate system resources (typically memory).
<dl>
<dt><b>STATUS_REQUEST_NOT_ACCEPTED</b></dt>
</dl>The I/O request packet (<a href="kernel.irp">IRP</a>) that the <i>Request</i> parameter represents does not provide enough <a href="kernel.io_stack_location">IO_STACK_LOCATION</a> structures to allow the driver to forward the request.

 

This method also might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.

A bug check occurs if the driver supplies an invalid object handle.




## -remarks
Use the <b>WdfIoTargetSendIoctlSynchronously</b> method to send device control requests synchronously. To send device control requests asynchronously, use the <a href="wdf.wdfiotargetformatrequestforioctl">WdfIoTargetFormatRequestForIoctl</a> method, followed by the <a href="wdf.wdfrequestsend">WdfRequestSend</a> method.

For more information about device control requests, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565406">Using I/O Control Codes</a>.

The <b>WdfIoTargetSendIoctlSynchronously</b> method does not return until the request has completed, unless the driver supplies a time-out value in the <i>RequestOptions</i> parameter's <a href="wdf.wdf_request_send_options">WDF_REQUEST_SEND_OPTIONS</a> structure, or unless an error is detected.

You can forward a device control request that your driver received in an I/O queue, or you can create and send a new request. In either case, the framework requires a request object and some buffer space.

To forward a device control request that your driver received in an I/O queue:

Specify the received request's handle for the <b>WdfIoTargetSendIoctlSynchronously</b> method's <i>Request</i> parameter.

Use the received request's input buffer for the <b>WdfIoTargetSendIoctlSynchronously</b> method's <i>InputBuffer</i> parameter.

The driver must call <a href="wdf.wdfrequestretrieveinputmemory">WdfRequestRetrieveInputMemory</a> to obtain a handle to a framework memory object that represents the request's input buffer. Then the driver must place that handle in the <a href="wdf.wdf_memory_descriptor">WDF_MEMORY_DESCRIPTOR</a> structure that the driver supplies for the <i>InputBuffer</i> parameter of <b>WdfIoTargetSendIoctlSynchronously</b>.

Use the received request's output buffer for the <b>WdfIoTargetSendIoctlSynchronously</b> method's <i>OutputBuffer</i> parameter.

The driver must call <a href="wdf.wdfrequestretrieveoutputmemory">WdfRequestRetrieveOutputMemory</a> to obtain a handle to a framework memory object that represents the request's output buffer. Then the driver must place that handle in the <a href="wdf.wdf_memory_descriptor">WDF_MEMORY_DESCRIPTOR</a> structure that the driver supplies for the <i>OutputBuffer</i> parameter of <b>WdfIoTargetSendIoctlSynchronously</b>.

For more information about forwarding an I/O request, see <a href="wdf.forwarding_i_o_requests">Forwarding I/O Requests</a>.

Drivers often divide received I/O requests into smaller requests that they send to an I/O target, so your driver might create new requests.

To create a new I/O request:

Supply a <b>NULL</b> request handle for the <b>WdfIoTargetSendIoctlSynchronously</b> method's <i>Request</i> parameter, or create a new request object and supply its handle:<ul>
<li>If you supply a <b>NULL</b> request handle, the framework uses an internal request object. This technique is simple to use, but the driver cannot cancel the request.</li>
<li>If you call <a href="wdf.wdfrequestcreate">WdfRequestCreate</a> to create one or more request objects, you can reuse these request objects by calling <a href="wdf.wdfrequestreuse">WdfRequestReuse</a>. This technique enables your driver's <a href="..\wdfdriver\nc-wdfdriver-evt_wdf_driver_device_add.md">EvtDriverDeviceAdd</a> callback function to preallocate request objects for a device. Additionally, another driver thread can call <a href="wdf.wdfrequestcancelsentrequest">WdfRequestCancelSentRequest</a> to cancel the request, if necessary.</li>
</ul>


Your driver can specify a non-<b>NULL</b> <i>RequestOptions</i> parameter, whether the driver provides a non-<b>NULL</b> or a <b>NULL</b> <i>Request</i> parameter. You can, for example, use the <i>RequestOptions</i> parameter to specify a time-out value. 

Provide buffer space for the <b>WdfIoTargetSendIoctlSynchronously</b> method's <i>InputBuffer</i> and <i>OutputBuffer</i> parameters, if the request requires them.

Your driver can specify this buffer space as locally allocated buffers, as WDFMEMORY handles, or as memory descriptor lists (MDLs). You can use whichever method is most convenient. 

If necessary, the framework converts the buffer descriptions so that they are correct for the IOCTL's transfer type. For more information about IOCTL transfer types, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff543023">Defining I/O Control Codes</a>. 

The following techniques to specify buffer space are available:

Supply local buffers.

Because <b>WdfIoTargetSendIoctlSynchronously</b> handles I/O requests synchronously, the driver can create request buffers that are local to the calling routine, as the following code example shows.

Supply WDFMEMORY handles.

Call <a href="wdf.wdfmemorycreate">WdfMemoryCreate</a> or <a href="wdf.wdfmemorycreatepreallocated">WdfMemoryCreatePreallocated</a> to obtain a handle to framework-managed memory, as the following code example shows. 

Alternatively, the driver can call <a href="wdf.wdfrequestretrieveinputmemory">WdfRequestRetrieveInputMemory</a> or <a href="wdf.wdfrequestretrieveoutputmemory">WdfRequestRetrieveOutputMemory</a> to obtain a handle to a framework memory object that represents a received I/O request's buffer, if you want the driver to pass that buffer's contents to the I/O target. The driver must not complete the received I/O request until the new request that <b>WdfIoTargetSendIoctlSynchronously</b> sends to the I/O target has been deleted, reused, or reformatted. (<b>WdfIoTargetSendIoctlSynchronously</b> increments the memory object's reference count. Deleting, reusing, or reformatting a request object decrements the memory object's reference count.)

Supply MDLs.

Drivers can obtain MDLs that are associated with a received I/O request by calling <a href="wdf.wdfrequestretrieveinputwdmmdl">WdfRequestRetrieveInputWdmMdl</a> and <a href="wdf.wdfrequestretrieveoutputwdmmdl">WdfRequestRetrieveOutputWdmMdl</a>.

For information about obtaining status information after an I/O request completes, see <a href="wdf.completing_i_o_requests#obtaining_completion_information#obtaining_completion_information">Obtaining Completion Information</a>.

For more information about <b>WdfIoTargetSendIoctlSynchronously</b>, see <a href="wdf.sending_i_o_requests_to_general_i_o_targets">Sending I/O Requests to General I/O Targets</a>.

For more information about I/O targets, see <a href="wdf.using_i_o_targets">Using I/O Targets</a>.

The following code example defines a local buffer, initializes a <a href="wdf.wdf_memory_descriptor">WDF_MEMORY_DESCRIPTOR</a> structure, and calls <b>WdfIoTargetSendIoctlSynchronously</b>. This example specifies <b>NULL</b> for the request object handle, so the framework will create a new request object for the I/O target.


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
Minimum KMDF version

</th>
<td width="70%">
1.0

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
2.0

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdfiotarget.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

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
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.kmdf_deferredrequestcompleted">DeferredRequestCompleted</a>, <a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_internalioctlreqs">InternalIoctlReqs</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>, <a href="devtest.kmdf_readreqs">ReadReqs</a>, <a href="devtest.kmdf_requestcompleted">RequestCompleted</a>, <a href="devtest.kmdf_requestcompletedlocal">RequestCompletedLocal</a>, <a href="devtest.kmdf_syncreqsend">SyncReqSend</a>, <a href="devtest.kmdf_writereqs">WriteReqs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfdriver\nc-wdfdriver-evt_wdf_driver_device_add.md">EvtDriverDeviceAdd</a>
</dt>
<dt>
<a href="wdf.wdf_memory_descriptor">WDF_MEMORY_DESCRIPTOR</a>
</dt>
<dt>
<a href="wdf.wdf_memory_descriptor_init_buffer">WDF_MEMORY_DESCRIPTOR_INIT_BUFFER</a>
</dt>
<dt>
<a href="wdf.wdf_request_send_options">WDF_REQUEST_SEND_OPTIONS</a>
</dt>
<dt>
<a href="wdf.wdfdevicegetiotarget">WdfDeviceGetIoTarget</a>
</dt>
<dt>
<a href="wdf.wdfiotargetcreate">WdfIoTargetCreate</a>
</dt>
<dt>
<a href="wdf.wdfiotargetformatrequestforioctl">WdfIoTargetFormatRequestForIoctl</a>
</dt>
<dt>
<a href="wdf.wdfiotargetsendinternalioctlsynchronously">WdfIoTargetSendInternalIoctlSynchronously</a>
</dt>
<dt>
<a href="wdf.wdfmemorycreate">WdfMemoryCreate</a>
</dt>
<dt>
<a href="wdf.wdfmemorycreatepreallocated">WdfMemoryCreatePreallocated</a>
</dt>
<dt>
<a href="wdf.wdfrequestcancelsentrequest">WdfRequestCancelSentRequest</a>
</dt>
<dt>
<a href="wdf.wdfrequestcompletewithinformation">WdfRequestCompleteWithInformation</a>
</dt>
<dt>
<a href="wdf.wdfrequestcreate">WdfRequestCreate</a>
</dt>
<dt>
<a href="wdf.wdfrequestretrieveinputmemory">WdfRequestRetrieveInputMemory</a>
</dt>
<dt>
<a href="wdf.wdfrequestretrieveinputwdmmdl">WdfRequestRetrieveInputWdmMdl</a>
</dt>
<dt>
<a href="wdf.wdfrequestretrieveoutputmemory">WdfRequestRetrieveOutputMemory</a>
</dt>
<dt>
<a href="wdf.wdfrequestretrieveoutputwdmmdl">WdfRequestRetrieveOutputWdmMdl</a>
</dt>
<dt>
<a href="wdf.wdfrequestreuse">WdfRequestReuse</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfIoTargetSendIoctlSynchronously method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

