---
UID: NS.wdfusb._WDF_USB_REQUEST_COMPLETION_PARAMS
title: WDF_USB_REQUEST_COMPLETION_PARAMS
author: windows-driver-content
description: The WDF_USB_REQUEST_COMPLETION_PARAMS structure contains parameters that are associated with the completion of an I/O request for a USB device.
old-location: wdf\wdf_usb_request_completion_params.htm
old-project: wdf
ms.assetid: cd29d27c-9da2-477f-898e-13ee480aac9e
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WDF_USB_REQUEST_COMPLETION_PARAMS, WDF_USB_REQUEST_COMPLETION_PARAMS, *PWDF_USB_REQUEST_COMPLETION_PARAMS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
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

### -field UsbdStatus

<dd>
<p>The <a href="buses.usbd_status">USBD_STATUS</a>-typed status value that the I/O target returned.</p>
</dd>

### -field Type

<dd>
<p>A <a href="..\wudfusb\ne-wudfusb--wdf-usb-request-type.md">WDF_USB_REQUEST_TYPE</a>-typed values that identifies the request type.</p>
</dd>

### -field Parameters

<dd>
<dl>

### -field DeviceString

<dd>
<dl>

### -field Buffer

<dd>
<p>If the driver has called <a href="..\wdfusb\nf-wdfusb-wdfusbtargetdeviceformatrequestforstring.md">WdfUsbTargetDeviceFormatRequestForString</a>, this member contains the driver-supplied handle to the memory object that receives the Unicode string.</p>
</dd>

### -field LangID

<dd>
<p>If the driver has called <a href="..\wdfusb\nf-wdfusb-wdfusbtargetdeviceformatrequestforstring.md">WdfUsbTargetDeviceFormatRequestForString</a>, this member contains the driver-supplied language identifier.</p>
</dd>

### -field StringIndex

<dd>
<p>If the driver has called <a href="..\wdfusb\nf-wdfusb-wdfusbtargetdeviceformatrequestforstring.md">WdfUsbTargetDeviceFormatRequestForString</a>, this member contains the driver-supplied string index.</p>
</dd>

### -field RequiredSize

<dd>
<p>If the driver has called any method that <a href="wdf.working_with_usb_devices#obtaining_a_device_s_unicode_strings#obtaining_a_device_s_unicode_strings">obtains a device's Unicode strings</a> (except <a href="..\wdfusb\nf-wdfusb-wdfusbtargetdeviceformatrequestforurb.md">WdfUsbTargetDeviceFormatRequestForUrb</a>), this member contains the required size of the buffer that <b>Parameters.DeviceString.Buffer</b> specifies. </p>
<p>If the driver called <a href="..\wdfusb\nf-wdfusb-wdfusbtargetdeviceformatrequestforurb.md">WdfUsbTargetDeviceFormatRequestForUrb</a>, it can obtain the required size value from the URB whose handle is in <b>Parameters.DeviceUrb.Buffer</b>.</p>
</dd>
</dl>
</dd>

### -field DeviceControlTransfer

<dd>
<dl>

### -field Buffer

<dd>
<p>If the driver has called <a href="..\wdfusb\nf-wdfusb-wdfusbtargetdeviceformatrequestforcontroltransfer.md">WdfUsbTargetDeviceFormatRequestForControlTransfer</a>, this member contains the driver-supplied handle to the memory object that receives input or output data.</p>
</dd>

### -field SetupPacket

<dd>
<p>If the driver has called <a href="..\wdfusb\nf-wdfusb-wdfusbtargetdeviceformatrequestforcontroltransfer.md">WdfUsbTargetDeviceFormatRequestForControlTransfer</a>, this member contains the address of the <a href="..\wdfusb\ns-wdfusb--wdf-usb-control-setup-packet.md">WDF_USB_CONTROL_SETUP_PACKET</a> structure that the driver supplied.</p>
</dd>

### -field Length

<dd>
<p>If the driver has called any method that <a href="wdf.working_with_usb_devices#sending_a_control_transfer#sending_a_control_transfer">sends a control transfer</a> (except <a href="..\wdfusb\nf-wdfusb-wdfusbtargetdeviceformatrequestforurb.md">WdfUsbTargetDeviceFormatRequestForUrb</a>), this member contains the number of bytes that were sent or received. </p>
<p>If the driver called <a href="..\wdfusb\nf-wdfusb-wdfusbtargetdeviceformatrequestforurb.md">WdfUsbTargetDeviceFormatRequestForUrb</a>, it can obtain the length value from the URB whose handle is in <b>Parameters.DeviceUrb.Buffer</b>.</p>
</dd>
</dl>
</dd>

### -field DeviceUrb

<dd>
<dl>

### -field Buffer

<dd>
<p>If the driver has called <a href="..\wdfusb\nf-wdfusb-wdfusbtargetdeviceformatrequestforurb.md">WdfUsbTargetDeviceFormatRequestForUrb</a>, this member contains the driver-supplied handle to the memory object that contains a <a href="..\usb\ns-usb--urb.md">URB</a> structure.</p>
</dd>
</dl>
</dd>

### -field PipeWrite

<dd>
<dl>

### -field Buffer

<dd>
<p>If the driver has called <a href="..\wdfusb\nf-wdfusb-wdfusbtargetpipeformatrequestforwrite.md">WdfUsbTargetPipeFormatRequestForWrite</a>, this member contains the driver-supplied handle to the memory object that was written to the pipe.</p>
</dd>

### -field Length

<dd>
<p>If the driver has called any method <a href="wdf.working_with_usb_pipes#writing_to_a_pipe#writing_to_a_pipe">that writes to a pipe</a> (except <a href="..\wdfusb\nf-wdfusb-wdfusbtargetdeviceformatrequestforurb.md">WdfUsbTargetDeviceFormatRequestForUrb</a>), this member contains the number of bytes that were sent. </p>
<p>If the driver called <a href="..\wdfusb\nf-wdfusb-wdfusbtargetdeviceformatrequestforurb.md">WdfUsbTargetDeviceFormatRequestForUrb</a>, it can obtain the length value from the URB whose handle is in <b>Parameters.PipeUrb.Buffer</b>.</p>
</dd>

### -field Offset

<dd>
<p>If the driver has called <a href="..\wdfusb\nf-wdfusb-wdfusbtargetpipeformatrequestforwrite.md">WdfUsbTargetPipeFormatRequestForWrite</a>, this member contains the driver-supplied buffer offset. </p>
</dd>
</dl>
</dd>

### -field PipeRead

<dd>
<dl>

### -field Buffer

<dd>
<p>If the driver has called <a href="..\wdfusb\nf-wdfusb-wdfusbtargetpipeformatrequestforread.md">WdfUsbTargetPipeFormatRequestForRead</a>, this member contains the driver-supplied handle to the memory object that contains data that was read from the pipe.</p>
</dd>

### -field Length

<dd>
<p>If the driver has called any method that <a href="wdf.working_with_usb_pipes#reading_from_a_pipe#reading_from_a_pipe">reads from a pipe</a> sends a control transfer (except <a href="..\wdfusb\nf-wdfusb-wdfusbtargetdeviceformatrequestforurb.md">WdfUsbTargetDeviceFormatRequestForUrb</a>), this member contains the number of bytes that were received. </p>
<p>If the driver called <a href="..\wdfusb\nf-wdfusb-wdfusbtargetdeviceformatrequestforurb.md">WdfUsbTargetDeviceFormatRequestForUrb</a>, it can obtain the length value from the URB whose handle is in <b>Parameters.PipeUrb.Buffer</b>.</p>
</dd>

### -field Offset

<dd>
<p>If the driver has called <a href="..\wdfusb\nf-wdfusb-wdfusbtargetpipeformatrequestforread.md">WdfUsbTargetPipeFormatRequestForRead</a>, this member contains the driver-supplied buffer offset. </p>
</dd>
</dl>
</dd>

### -field PipeUrb

<dd>
<dl>

### -field Buffer

<dd>
<p>If the driver has called <a href="..\wdfusb\nf-wdfusb-wdfusbtargetpipeformatrequestforurb.md">WdfUsbTargetPipeFormatRequestForUrb</a>, this member contains the driver-supplied handle to the memory object that contains a <a href="..\usb\ns-usb--urb.md">URB</a> structure.</p>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The <b>WDF_USB_REQUEST_COMPLETION_PARAMS</b> structure is a member of the <a href="..\wdfrequest\ns-wdfrequest--wdf-request-completion-params.md">WDF_REQUEST_COMPLETION_PARAMS</a> structure.</p>

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
<a href="..\wdfrequest\nc-wdfrequest-evt-wdf-request-completion-routine.md">CompletionRoutine</a>
</dt>
<dt>
<a href="..\wdfrequest\ns-wdfrequest--wdf-request-completion-params.md">WDF_REQUEST_COMPLETION_PARAMS</a>
</dt>
<dt>
<a href="..\wdfrequest\nf-wdfrequest-wdfrequestgetcompletionparams.md">WdfRequestGetCompletionParams</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_USB_REQUEST_COMPLETION_PARAMS structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
