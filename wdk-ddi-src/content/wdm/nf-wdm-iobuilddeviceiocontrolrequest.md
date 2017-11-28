---
UID: NF.wdm.IoBuildDeviceIoControlRequest
title: IoBuildDeviceIoControlRequest
author: windows-driver-content
description: The IoBuildDeviceIoControlRequest routine allocates and sets up an IRP for a synchronously processed device control request.
old-location: kernel\iobuilddeviceiocontrolrequest.htm
old-project: kernel
ms.assetid: dde2a45d-9257-4d94-928a-e25f112b2773
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: IoBuildDeviceIoControlRequest
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoBuildDeviceIoControlRequest
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IoAllocateIrpSignalEventInCompletion, IoAllocateIrpSignalEventInCompletion2, IoAllocateIrpSignalEventInCompletion3, IoBuildDeviceControlNoFree, IoBuildDeviceControlWait, IoBuildDeviceControlWaitTimeout, IoBuildDeviceIoControlSetEvent, IrqlIoPassive1, PowerIrpDDis, SignalEventInCompletion, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# IoBuildDeviceIoControlRequest function



## -description
<p>The <b>IoBuildDeviceIoControlRequest</b> routine allocates and sets up an IRP for a synchronously processed device control request.</p>


## -syntax

````
PIRP IoBuildDeviceIoControlRequest(
  _In_      ULONG            IoControlCode,
  _In_      PDEVICE_OBJECT   DeviceObject,
  _In_opt_  PVOID            InputBuffer,
  _In_      ULONG            InputBufferLength,
  _Out_opt_ PVOID            OutputBuffer,
  _In_      ULONG            OutputBufferLength,
  _In_      BOOLEAN          InternalDeviceIoControl,
  _In_opt_  PKEVENT          Event,
  _Out_     PIO_STATUS_BLOCK IoStatusBlock
);
````


## -parameters
<dl>

### -param <i>IoControlCode</i> [in]

<dd>
<p>Supplies the I/O control code (<a href="wdkgloss.i#wdkgloss.ioctl#wdkgloss.ioctl"><i>IOCTL</i></a>) to be used in the request. For information about device type-specific I/O control codes, see device type-specific sections in the Windows Driver Kit (WDK). </p>
</dd>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Supplies a pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543147">DEVICE_OBJECT</a> structure for the next-lower driver's device object, which represents the target device.</p>
</dd>

### -param <i>InputBuffer</i> [in, optional]

<dd>
<p>Supplies a pointer to an input buffer to be passed to the lower driver, or <b>NULL</b> if the request does not pass input data to lower drivers.</p>
</dd>

### -param <i>InputBufferLength</i> [in]

<dd>
<p>Supplies the length, in bytes, of the input buffer. If <i>InputBuffer</i> is <b>NULL</b>, <i>InputBufferLength</i> must be zero.</p>
</dd>

### -param <i>OutputBuffer</i> [out, optional]

<dd>
<p>Supplies a pointer to an output buffer in which the lower driver is to return data, or <b>NULL</b> if the request does not require lower drivers to return data.</p>
</dd>

### -param <i>OutputBufferLength</i> [in]

<dd>
<p>Supplies the length, in bytes, of the output buffer. If <i>OutputBuffer</i> is <b>NULL</b>, <i>OutputBufferLength</i> must be zero.</p>
</dd>

### -param <i>InternalDeviceIoControl</i> [in]

<dd>
<p>If <b>TRUE</b>, the routine sets the IRP's major function code to <a href="https://msdn.microsoft.com/library/windows/hardware/ff550766">IRP_MJ_INTERNAL_DEVICE_CONTROL</a>. Otherwise, the routine sets the IRP's major function code to <a href="https://msdn.microsoft.com/library/windows/hardware/ff548649">IRP_MJ_DEVICE_CONTROL</a>.</p>
</dd>

### -param <i>Event</i> [in, optional]

<dd>
<p>Supplies a pointer to a caller-allocated and initialized event object. The I/O manager sets the event to the Signaled state when a lower-level driver completes the requested operation. After calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff548336">IoCallDriver</a>, the driver can wait for the event object. The <i>Event</i> parameter is optional and can be set to NULL. However, if <i>Event</i> is NULL, the caller must supply an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548354">IoCompletion</a> routine for the IRP to notify the caller when the operation completes.</p>
</dd>

### -param <i>IoStatusBlock</i> [out]

<dd>
<p>Specifies an I/O status block to be set when the request is completed by lower drivers.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, <b>IoBuildDeviceIoControlRequest</b> returns a pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550694">IRP</a>, with the next-lower driver's I/O stack location set up from the supplied parameters. Otherwise, the routine returns <b>NULL</b>.</p>

## -remarks
<p>A driver can call <b>IoBuildDeviceIoControlRequest</b> to set up IRPs for device control requests that it synchronously sends to lower-level drivers.</p>

<p>After calling <b>IoBuildDeviceIoControlRequest</b> to create a request, the driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548336">IoCallDriver</a> to send the request to the next-lower driver. If <b>IoCallDriver</b> returns STATUS_PENDING, the driver must wait for the completion of the IRP by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff553350">KeWaitForSingleObject</a> on the given <i>Event</i>. Most drivers do not need to set an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548354">IoCompletion</a> routine for the IRP.</p>

<p>IRPs that are created by <b>IoBuildDeviceIoControlRequest</b> must be completed by a driver's call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff548343">IoCompleteRequest</a>. A driver that calls <b>IoBuildDeviceIoControlRequest</b> must not call <a href="https://msdn.microsoft.com/library/windows/hardware/hh454223">IoFreeIrp</a>, because the I/O manager frees these synchronous IRPs after <b>IoCompleteRequest</b> has been called.</p>

<p><b>IoBuildDeviceIoControlRequest</b> queues the IRPs that it creates to an IRP queue that is specific to the current thread. If the thread exits, the I/O manager cancels the IRP.</p>

<p>If the caller supplies an <i>InputBuffer</i> or <i>OutputBuffer</i> parameter, this parameter must point to a buffer that resides in system memory. The caller is responsible for validating any parameter values that it copies into the input buffer from a user-mode buffer. The input buffer might contain parameter values that are interpreted differently depending on whether the originator of the request is a user-mode application or a kernel-mode driver. In the IRP that <b>IoBuildDeviceIoControlRequest</b> returns, the <b>RequestorMode</b> field is always set to <b>KernelMode</b>. This value indicates that the request, and any information contained in the request, is from a trusted, kernel-mode component.</p>

<p>If the caller cannot validate parameter values that it copies from a user-mode buffer to the input buffer, or if these values must not be interpreted as coming from a kernel-mode component, the caller should set the <b>RequestorMode</b> field in the IRP to <b>UserMode</b>. This setting informs the driver that handles the I/O control request that the buffer contains untrusted, user-mode data.</p>

<p>The actual method by which the contents of the <i>InputBuffer</i> and <i>OutputBuffer</i> parameters are stored in the IRP depends on the <i>TransferType</i> value for the IOCTL. For more information about this value, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540663">Buffer Descriptions for I/O Control Codes</a>.</p>

<p>A driver can call <b>IoBuildDeviceIoControlRequest</b> to set up IRPs for device control requests that it synchronously sends to lower-level drivers.</p>

<p>After calling <b>IoBuildDeviceIoControlRequest</b> to create a request, the driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548336">IoCallDriver</a> to send the request to the next-lower driver. If <b>IoCallDriver</b> returns STATUS_PENDING, the driver must wait for the completion of the IRP by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff553350">KeWaitForSingleObject</a> on the given <i>Event</i>. Most drivers do not need to set an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548354">IoCompletion</a> routine for the IRP.</p>

<p>IRPs that are created by <b>IoBuildDeviceIoControlRequest</b> must be completed by a driver's call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff548343">IoCompleteRequest</a>. A driver that calls <b>IoBuildDeviceIoControlRequest</b> must not call <a href="https://msdn.microsoft.com/library/windows/hardware/hh454223">IoFreeIrp</a>, because the I/O manager frees these synchronous IRPs after <b>IoCompleteRequest</b> has been called.</p>

<p><b>IoBuildDeviceIoControlRequest</b> queues the IRPs that it creates to an IRP queue that is specific to the current thread. If the thread exits, the I/O manager cancels the IRP.</p>

<p>If the caller supplies an <i>InputBuffer</i> or <i>OutputBuffer</i> parameter, this parameter must point to a buffer that resides in system memory. The caller is responsible for validating any parameter values that it copies into the input buffer from a user-mode buffer. The input buffer might contain parameter values that are interpreted differently depending on whether the originator of the request is a user-mode application or a kernel-mode driver. In the IRP that <b>IoBuildDeviceIoControlRequest</b> returns, the <b>RequestorMode</b> field is always set to <b>KernelMode</b>. This value indicates that the request, and any information contained in the request, is from a trusted, kernel-mode component.</p>

<p>If the caller cannot validate parameter values that it copies from a user-mode buffer to the input buffer, or if these values must not be interpreted as coming from a kernel-mode component, the caller should set the <b>RequestorMode</b> field in the IRP to <b>UserMode</b>. This setting informs the driver that handles the I/O control request that the buffer contains untrusted, user-mode data.</p>

<p>The actual method by which the contents of the <i>InputBuffer</i> and <i>OutputBuffer</i> parameters are stored in the IRP depends on the <i>TransferType</i> value for the IOCTL. For more information about this value, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540663">Buffer Descriptions for I/O Control Codes</a>.</p>

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
<p>Available starting with Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975155">IoAllocateIrpSignalEventInCompletion</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975156">IoAllocateIrpSignalEventInCompletion2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975157">IoAllocateIrpSignalEventInCompletion3</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975160">IoBuildDeviceControlNoFree</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975161">IoBuildDeviceControlWait</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975162">IoBuildDeviceControlWaitTimeout</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975163">IoBuildDeviceIoControlSetEvent</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547763">IrqlIoPassive1</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975204">PowerIrpDDis</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975249">SignalEventInCompletion</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550659">IO_STACK_LOCATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548257">IoAllocateIrp</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548310">IoBuildAsynchronousFsdRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548330">IoBuildSynchronousFsdRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548336">IoCallDriver</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548343">IoCompleteRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550694">IRP</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552137">KeInitializeEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553350">KeWaitForSingleObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoBuildDeviceIoControlRequest routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
