---
UID: NF.wdfusb.WdfUsbTargetPipeConfigContinuousReader
title: WdfUsbTargetPipeConfigContinuousReader
author: windows-driver-content
description: The WdfUsbTargetPipeConfigContinuousReader method configures the framework to continuously read from a specified USB pipe.
old-location: wdf\wdfusbtargetpipeconfigcontinuousreader.htm
old-project: wdf
ms.assetid: 56ed3c4f-bcfa-417d-a276-9934e3bc1666
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfUsbTargetPipeConfigContinuousReader
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
req.alt-api: WdfUsbTargetPipeConfigContinuousReader
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, FailD0EntryIoTargetState, KmdfIrql, KmdfIrql2, UsbContReader, UsbKmdfIrql, UsbKmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); 
WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfUsbTargetPipeConfigContinuousReader function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfUsbTargetPipeConfigContinuousReader</b> method configures the framework to continuously read from a specified USB pipe.</p>


## -syntax

````
NTSTATUS WdfUsbTargetPipeConfigContinuousReader(
  _In_ WDFUSBPIPE                        Pipe,
  _In_ PWDF_USB_CONTINUOUS_READER_CONFIG Config
);
````


## -parameters
<dl>

### -param <i>Pipe</i> [in]

<dd>
<p>A handle to a framework pipe object that was obtained by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff550057">WdfUsbInterfaceGetConfiguredPipe</a>. </p>
</dd>

### -param <i>Config</i> [in]

<dd>
<p>A pointer to a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff552561">WDF_USB_CONTINUOUS_READER_CONFIG</a> structure.</p>
</dd>
</dl>

## -returns
<p><b>WdfUsbTargetPipeConfigContinuousReader</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method can return one of the following values:</p><dl>
<dt><b>STATUS_INFO_LENGTH_MISMATCH</b></dt>
</dl><p>The size of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552561">WDF_USB_CONTINUOUS_READER_CONFIG</a> structure that the <i>Config</i> parameter specified was incorrect.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid parameter was detected.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>Insufficient memory was available.</p><dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>The pipe's type was not valid.</p><dl>
<dt><b>STATUS_INTEGER_OVERFLOW</b></dt>
</dl><p>The <b>HeaderLength</b>, <b>TransferLength</b>, or <b>TrailerLength</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552561">WDF_USB_CONTINUOUS_READER_CONFIG</a> structure that the <i>Config</i> parameter specified a size what was too large or otherwise invalid.</p><dl>
<dt><b>STATUS_INVALID_BUFFER_SIZE</b></dt>
</dl><p>The size of the read buffer was not a multiple of the pipe's maximum packet size.</p>

<p> </p>

<p>For a list of other return values that the <b>WdfUsbTargetPipeConfigContinuousReader</b> method might return, see <a href="wdf.framework_object_creation_errors">Framework Object Creation Errors</a>.</p>

<p>This method also might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>You can configure a continuous reader for a bulk pipe or an interrupt pipe. The pipe must have an input endpoint.</p>

<p>After calling <b>WdfUsbTargetPipeConfigContinuousReader</b> to configure a continuous reader, your driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548677">WdfIoTargetStart</a> to start the reader. To stop the reader, the driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548680">WdfIoTargetStop</a>.</p>

<p>Typically, a driver calls <b>WdfUsbTargetPipeConfigContinuousReader</b> from within its <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-prepare-hardware.md">EvtDevicePrepareHardware</a> callback function. The driver should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548677">WdfIoTargetStart</a> from within its <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-d0-entry.md">EvtDeviceD0Entry</a> callback function and should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548680">WdfIoTargetStop</a> from within its <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-d0-exit.md">EvtDeviceD0Exit</a> callback function.</p>

<p>Each time the pipe's I/O target successfully completes a read request, the framework calls the driver's <a href="..\wdfusb\nc-wdfusb-evt-wdf-usb-reader-completion-routine.md">EvtUsbTargetPipeReadComplete</a> callback function. If the I/O target reports a failure while processing a request, the framework calls the driver's <a href="..\wdfusb\nc-wdfusb-evt-wdf-usb-readers-failed.md">EvtUsbTargetPipeReadersFailed</a> callback function after all read requests have been completed. (Therefore, the <i>EvtUsbTargetPipeReadComplete</i> callback function will not be called while the <i>EvtUsbTargetPipeReadersFailed</i> callback function is executing).</p>

<p>If you do not supply the optional <a href="..\wdfusb\nc-wdfusb-evt-wdf-usb-readers-failed.md">EvtUsbTargetPipeReadersFailed</a> callback, the framework responds to a failed read attempt by sending another read request. Therefore if the bus is in a state where it is not accepting reads, the framework continually sends new requests to recover from a failed read.</p>

<p>After a driver has called <b>WdfUsbTargetPipeConfigContinuousReader</b>, the driver cannot use <a href="https://msdn.microsoft.com/library/windows/hardware/ff551155">WdfUsbTargetPipeReadSynchronously</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff550027">WdfRequestSend</a> to send I/O requests to the pipe unless the continuous reader has been stopped. To stop the reader, the driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548680">WdfIoTargetStop</a> or return <b>FALSE</b> from its <a href="..\wdfusb\nc-wdfusb-evt-wdf-usb-readers-failed.md">EvtUsbTargetPipeReadersFailed</a> callback function.  If the driver calls <b>WdfUsbTargetPipeReadSynchronously</b> while the reader is stopped, it must set the WDF_REQUEST_SEND_OPTION_IGNORE_TARGET_STATE flag in the <b>Flags</b> member of the <i>RequestOptions</i> parameter. Otherwise the request will be pended until the target is restarted.</p>

<p>The framework sets the USBD_SHORT_TRANSFER_OK flag in its internal <a href="https://msdn.microsoft.com/library/windows/hardware/ff538923">URB</a>. Setting this flag allows the last packet of a data transfer to be less than the maximum packet size.</p>

<p>For more information about the <b>WdfUsbTargetPipeConfigContinuousReader</b> method and USB I/O targets, see <a href="wdf.working_with_usb_pipes">Reading from a Pipe</a>.</p>

<p>The following code example initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552561">WDF_USB_CONTINUOUS_READER_CONFIG</a> structure and calls <b>WdfUsbTargetPipeConfigContinuousReader</b>.</p>

<p>You can configure a continuous reader for a bulk pipe or an interrupt pipe. The pipe must have an input endpoint.</p>

<p>After calling <b>WdfUsbTargetPipeConfigContinuousReader</b> to configure a continuous reader, your driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548677">WdfIoTargetStart</a> to start the reader. To stop the reader, the driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548680">WdfIoTargetStop</a>.</p>

<p>Typically, a driver calls <b>WdfUsbTargetPipeConfigContinuousReader</b> from within its <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-prepare-hardware.md">EvtDevicePrepareHardware</a> callback function. The driver should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548677">WdfIoTargetStart</a> from within its <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-d0-entry.md">EvtDeviceD0Entry</a> callback function and should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548680">WdfIoTargetStop</a> from within its <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-d0-exit.md">EvtDeviceD0Exit</a> callback function.</p>

<p>Each time the pipe's I/O target successfully completes a read request, the framework calls the driver's <a href="..\wdfusb\nc-wdfusb-evt-wdf-usb-reader-completion-routine.md">EvtUsbTargetPipeReadComplete</a> callback function. If the I/O target reports a failure while processing a request, the framework calls the driver's <a href="..\wdfusb\nc-wdfusb-evt-wdf-usb-readers-failed.md">EvtUsbTargetPipeReadersFailed</a> callback function after all read requests have been completed. (Therefore, the <i>EvtUsbTargetPipeReadComplete</i> callback function will not be called while the <i>EvtUsbTargetPipeReadersFailed</i> callback function is executing).</p>

<p>If you do not supply the optional <a href="..\wdfusb\nc-wdfusb-evt-wdf-usb-readers-failed.md">EvtUsbTargetPipeReadersFailed</a> callback, the framework responds to a failed read attempt by sending another read request. Therefore if the bus is in a state where it is not accepting reads, the framework continually sends new requests to recover from a failed read.</p>

<p>After a driver has called <b>WdfUsbTargetPipeConfigContinuousReader</b>, the driver cannot use <a href="https://msdn.microsoft.com/library/windows/hardware/ff551155">WdfUsbTargetPipeReadSynchronously</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff550027">WdfRequestSend</a> to send I/O requests to the pipe unless the continuous reader has been stopped. To stop the reader, the driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548680">WdfIoTargetStop</a> or return <b>FALSE</b> from its <a href="..\wdfusb\nc-wdfusb-evt-wdf-usb-readers-failed.md">EvtUsbTargetPipeReadersFailed</a> callback function.  If the driver calls <b>WdfUsbTargetPipeReadSynchronously</b> while the reader is stopped, it must set the WDF_REQUEST_SEND_OPTION_IGNORE_TARGET_STATE flag in the <b>Flags</b> member of the <i>RequestOptions</i> parameter. Otherwise the request will be pended until the target is restarted.</p>

<p>The framework sets the USBD_SHORT_TRANSFER_OK flag in its internal <a href="https://msdn.microsoft.com/library/windows/hardware/ff538923">URB</a>. Setting this flag allows the last packet of a data transfer to be less than the maximum packet size.</p>

<p>For more information about the <b>WdfUsbTargetPipeConfigContinuousReader</b> method and USB I/O targets, see <a href="wdf.working_with_usb_pipes">Reading from a Pipe</a>.</p>

<p>The following code example initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552561">WDF_USB_CONTINUOUS_READER_CONFIG</a> structure and calls <b>WdfUsbTargetPipeConfigContinuousReader</b>.</p>

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
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975077">FailD0EntryIoTargetState</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff554034">UsbContReader</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff554042">UsbKmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh995019">UsbKmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-d0-entry.md">EvtDeviceD0Entry</a>
</dt>
<dt>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-d0-exit.md">EvtDeviceD0Exit</a>
</dt>
<dt>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-prepare-hardware.md">EvtDevicePrepareHardware</a>
</dt>
<dt>
<a href="..\wdfusb\nc-wdfusb-evt-wdf-usb-reader-completion-routine.md">EvtUsbTargetPipeReadComplete</a>
</dt>
<dt>
<a href="..\wdfusb\nc-wdfusb-evt-wdf-usb-readers-failed.md">EvtUsbTargetPipeReadersFailed</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538923">URB</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552561">WDF_USB_CONTINUOUS_READER_CONFIG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552566">WDF_USB_CONTINUOUS_READER_CONFIG_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548677">WdfIoTargetStart</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548680">WdfIoTargetStop</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550057">WdfUsbInterfaceGetConfiguredPipe</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfUsbTargetPipeConfigContinuousReader method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
