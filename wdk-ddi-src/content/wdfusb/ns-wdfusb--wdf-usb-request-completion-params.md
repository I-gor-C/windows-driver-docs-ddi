---
UID: NS.wdfusb._WDF_USB_REQUEST_COMPLETION_PARAMS
title: WDF_USB_REQUEST_COMPLETION_PARAMS
author: windows-driver-content
description: The WDF_USB_REQUEST_COMPLETION_PARAMS structure contains parameters that are associated with the completion of an I/O request for a USB device.
old-location: wdf\wdf_usb_request_completion_params.htm
ms.assetid: cd29d27c-9da2-477f-898e-13ee480aac9e
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfusb.h
req.include-header: Wdfusb.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_USB_REQUEST_COMPLETION_PARAMS
req.alt-loc: wdfusb.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: WDF_USB_REQUEST_COMPLETION_PARAMS, WDF_USB_REQUEST_COMPLETION_PARAMS, *PWDF_USB_REQUEST_COMPLETION_PARAMS
req.iface: 
req.product: Windows 10 or later.
---

# WDF_USB_REQUEST_COMPLETION_PARAMS structure



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_USB_REQUEST_COMPLETION_PARAMS</b> structure contains parameters that are associated with the completion of an I/O request for a USB device.</p>


## -syntax

````
typedef struct _WDF_USB_REQUEST_COMPLETION_PARAMS {
  USBD_STATUS          UsbdStatus;
  WDF_USB_REQUEST_TYPE Type;
  union {
    struct {
      WDFMEMORY Buffer;
      USHORT    LangID;
      UCHAR     StringIndex;
      UCHAR     RequiredSize;
    } DeviceString;
    struct {
      WDFMEMORY                    Buffer;
      WDF_USB_CONTROL_SETUP_PACKET SetupPacket;
      ULONG                        Length;
    } DeviceControlTransfer;
    struct {
      WDFMEMORY Buffer;
    } DeviceUrb;
    struct {
      WDFMEMORY Buffer;
      size_t    Length;
      size_t    Offset;
    } PipeWrite;
    struct {
      WDFMEMORY Buffer;
      size_t    Length;
      size_t    Offset;
    } PipeRead;
    struct {
      WDFMEMORY Buffer;
    } PipeUrb;
  } Parameters;
} WDF_USB_REQUEST_COMPLETION_PARAMS, *PWDF_USB_REQUEST_COMPLETION_PARAMS;
````


## -struct-fields
<dl>

### -field <b>UsbdStatus</b>

<dd>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff539136">USBD_STATUS</a>-typed status value that the I/O target returned.</p>
</dd>

### -field <b>Type</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff553055">WDF_USB_REQUEST_TYPE</a>-typed values that identifies the request type.</p>
</dd>

### -field <b>Parameters</b>

<dd>
<dl>

### -field <b>DeviceString</b>

<dd>
<dl>

### -field <b>Buffer</b>

<dd>
<p>If the driver has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff550086">WdfUsbTargetDeviceFormatRequestForString</a>, this member contains the driver-supplied handle to the memory object that receives the Unicode string.</p>
</dd>

### -field <b>LangID</b>

<dd>
<p>If the driver has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff550086">WdfUsbTargetDeviceFormatRequestForString</a>, this member contains the driver-supplied language identifier.</p>
</dd>

### -field <b>StringIndex</b>

<dd>
<p>If the driver has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff550086">WdfUsbTargetDeviceFormatRequestForString</a>, this member contains the driver-supplied string index.</p>
</dd>

### -field <b>RequiredSize</b>

<dd>
<p>If the driver has called any method that <a href="wdf.working_with_usb_devices#obtaining_a_device_s_unicode_strings#obtaining_a_device_s_unicode_strings">obtains a device's Unicode strings</a> (except <a href="https://msdn.microsoft.com/library/windows/hardware/ff550088">WdfUsbTargetDeviceFormatRequestForUrb</a>), this member contains the required size of the buffer that <b>Parameters.DeviceString.Buffer</b> specifies. </p>
<p>If the driver called <a href="https://msdn.microsoft.com/library/windows/hardware/ff550088">WdfUsbTargetDeviceFormatRequestForUrb</a>, it can obtain the required size value from the URB whose handle is in <b>Parameters.DeviceUrb.Buffer</b>.</p>
</dd>
</dl>
</dd>

### -field <b>DeviceControlTransfer</b>

<dd>
<dl>

### -field <b>Buffer</b>

<dd>
<p>If the driver has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff550082">WdfUsbTargetDeviceFormatRequestForControlTransfer</a>, this member contains the driver-supplied handle to the memory object that receives input or output data.</p>
</dd>

### -field <b>SetupPacket</b>

<dd>
<p>If the driver has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff550082">WdfUsbTargetDeviceFormatRequestForControlTransfer</a>, this member contains the address of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552568">WDF_USB_CONTROL_SETUP_PACKET</a> structure that the driver supplied.</p>
</dd>

### -field <b>Length</b>

<dd>
<p>If the driver has called any method that <a href="wdf.working_with_usb_devices#sending_a_control_transfer#sending_a_control_transfer">sends a control transfer</a> (except <a href="https://msdn.microsoft.com/library/windows/hardware/ff550088">WdfUsbTargetDeviceFormatRequestForUrb</a>), this member contains the number of bytes that were sent or received. </p>
<p>If the driver called <a href="https://msdn.microsoft.com/library/windows/hardware/ff550088">WdfUsbTargetDeviceFormatRequestForUrb</a>, it can obtain the length value from the URB whose handle is in <b>Parameters.DeviceUrb.Buffer</b>.</p>
</dd>
</dl>
</dd>

### -field <b>DeviceUrb</b>

<dd>
<dl>

### -field <b>Buffer</b>

<dd>
<p>If the driver has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff550088">WdfUsbTargetDeviceFormatRequestForUrb</a>, this member contains the driver-supplied handle to the memory object that contains a <a href="https://msdn.microsoft.com/library/windows/hardware/ff538923">URB</a> structure.</p>
</dd>
</dl>
</dd>

### -field <b>PipeWrite</b>

<dd>
<dl>

### -field <b>Buffer</b>

<dd>
<p>If the driver has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff551141">WdfUsbTargetPipeFormatRequestForWrite</a>, this member contains the driver-supplied handle to the memory object that was written to the pipe.</p>
</dd>

### -field <b>Length</b>

<dd>
<p>If the driver has called any method <a href="wdf.working_with_usb_pipes#writing_to_a_pipe#writing_to_a_pipe">that writes to a pipe</a> (except <a href="https://msdn.microsoft.com/library/windows/hardware/ff550088">WdfUsbTargetDeviceFormatRequestForUrb</a>), this member contains the number of bytes that were sent. </p>
<p>If the driver called <a href="https://msdn.microsoft.com/library/windows/hardware/ff550088">WdfUsbTargetDeviceFormatRequestForUrb</a>, it can obtain the length value from the URB whose handle is in <b>Parameters.PipeUrb.Buffer</b>.</p>
</dd>

### -field <b>Offset</b>

<dd>
<p>If the driver has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff551141">WdfUsbTargetPipeFormatRequestForWrite</a>, this member contains the driver-supplied buffer offset. </p>
</dd>
</dl>
</dd>

### -field <b>PipeRead</b>

<dd>
<dl>

### -field <b>Buffer</b>

<dd>
<p>If the driver has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff551136">WdfUsbTargetPipeFormatRequestForRead</a>, this member contains the driver-supplied handle to the memory object that contains data that was read from the pipe.</p>
</dd>

### -field <b>Length</b>

<dd>
<p>If the driver has called any method that <a href="wdf.working_with_usb_pipes#reading_from_a_pipe#reading_from_a_pipe">reads from a pipe</a> sends a control transfer (except <a href="https://msdn.microsoft.com/library/windows/hardware/ff550088">WdfUsbTargetDeviceFormatRequestForUrb</a>), this member contains the number of bytes that were received. </p>
<p>If the driver called <a href="https://msdn.microsoft.com/library/windows/hardware/ff550088">WdfUsbTargetDeviceFormatRequestForUrb</a>, it can obtain the length value from the URB whose handle is in <b>Parameters.PipeUrb.Buffer</b>.</p>
</dd>

### -field <b>Offset</b>

<dd>
<p>If the driver has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff551136">WdfUsbTargetPipeFormatRequestForRead</a>, this member contains the driver-supplied buffer offset. </p>
</dd>
</dl>
</dd>

### -field <b>PipeUrb</b>

<dd>
<dl>

### -field <b>Buffer</b>

<dd>
<p>If the driver has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff551139">WdfUsbTargetPipeFormatRequestForUrb</a>, this member contains the driver-supplied handle to the memory object that contains a <a href="https://msdn.microsoft.com/library/windows/hardware/ff538923">URB</a> structure.</p>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The <b>WDF_USB_REQUEST_COMPLETION_PARAMS</b> structure is a member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552454">WDF_REQUEST_COMPLETION_PARAMS</a> structure.</p>

## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/7d3eb4d6-9fc7-4924-9b95-f5824713049b">CompletionRoutine</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552454">WDF_REQUEST_COMPLETION_PARAMS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549961">WdfRequestGetCompletionParams</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_USB_REQUEST_COMPLETION_PARAMS structure%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
