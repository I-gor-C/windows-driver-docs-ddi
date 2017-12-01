---
UID: NI.hidclass.IOCTL_HID_GET_SERIALNUMBER_STRING
title: IOCTL_HID_GET_SERIALNUMBER_STRING
author: windows-driver-content
description: The IOCTL_HID_GET_SERIALNUMBER_STRING request obtains a top-level collection's embedded string that identifies the device's serial number.
old-location: hid\ioctl_hid_get_serialnumber_string.htm
old-project: hid
ms.assetid: 81adb295-a4b3-46de-8b46-15fe89c5f7a5
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: HDAUDIO_STREAM_FORMAT, HDAUDIO_STREAM_FORMAT, *PHDAUDIO_STREAM_FORMAT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: hidclass.h
req.include-header: Hidclass.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_HID_GET_SERIALNUMBER_STRING
req.alt-loc: hidclass.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# IOCTL_HID_GET_SERIALNUMBER_STRING IOCTL



## -description
<p>The IOCTL_HID_GET_SERIALNUMBER_STRING request obtains a <a href="https://msdn.microsoft.com/dcbee8e3-d03a-45c8-92e4-0897b9f55177">top-level collection's</a> embedded string that identifies the device's serial number. The retrieved string is a NULL-terminated wide character string in a human-readable format.</p>
<p>For general information about HIDClass devices, see <a href="NULL">HID Collections</a>. </p>


## -ioctlparameters

### -input-buffer
<p><b>Parameters.DeviceIoControl.OutputBufferLength</b> in the I/O stack location of the IRP indicates the size, in bytes, of the output buffer. If the output buffer is not large enough to hold the entire NULL-terminated embedded string, the request returns nothing in the output buffer. </p>

### -input-buffer-length
<p>The maximum possible number of characters in an embedded string is device specific. For USB devices, the maximum string length is 126 wide characters (not including the terminating NULL character). </p>

<p>The maximum possible number of characters in an embedded string is device specific. For USB devices, the maximum string length is 126 wide characters (not including the terminating NULL character). </p>

### -output-buffer
<p><b>Irp-&gt;MdlAddress</b> points to a buffer to receive the serial number string (a NULL-terminated wide character string).</p>

<p><b>Irp-&gt;MdlAddress</b> points to a buffer to receive the serial number string (a NULL-terminated wide character string).</p>

<p><b>Irp-&gt;MdlAddress</b> points to a buffer to receive the serial number string (a NULL-terminated wide character string).</p>

### -output-buffer-length
<p>The length of a NULL-terminated wide character string.</p>

<p>The length of a NULL-terminated wide character string.</p>

<p>The length of a NULL-terminated wide character string.</p>

<p>The length of a NULL-terminated wide character string.</p>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p>The HID class driver sets the following fields of <b>Irp-&gt;IoStatus</b>:</p>

<p><b>Information</b> is set to the number of bytes transferred from the device.</p>

<p><b>Status</b> is set to STATUS_SUCCESS if the transfer completed without error. Otherwise, it is set to an appropriate NTSTATUS error code.</p>

<p>The HID class driver sets the following fields of <b>Irp-&gt;IoStatus</b>:</p>

<p><b>Information</b> is set to the number of bytes transferred from the device.</p>

<p><b>Status</b> is set to STATUS_SUCCESS if the transfer completed without error. Otherwise, it is set to an appropriate NTSTATUS error code.</p>

<p>The HID class driver sets the following fields of <b>Irp-&gt;IoStatus</b>:</p>

<p><b>Information</b> is set to the number of bytes transferred from the device.</p>

<p><b>Status</b> is set to STATUS_SUCCESS if the transfer completed without error. Otherwise, it is set to an appropriate NTSTATUS error code.</p>

<p>The HID class driver sets the following fields of <b>Irp-&gt;IoStatus</b>:</p>

<p><b>Information</b> is set to the number of bytes transferred from the device.</p>

<p><b>Status</b> is set to STATUS_SUCCESS if the transfer completed without error. Otherwise, it is set to an appropriate NTSTATUS error code.</p>

<p>The HID class driver sets the following fields of <b>Irp-&gt;IoStatus</b>:</p>

<p><b>Information</b> is set to the number of bytes transferred from the device.</p>

<p><b>Status</b> is set to STATUS_SUCCESS if the transfer completed without error. Otherwise, it is set to an appropriate NTSTATUS error code.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hidclass.h (include Hidclass.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\hidsdi\nf-hidsdi-hidd-getindexedstring.md">HidD_GetIndexedString</a>
</dt>
<dt>
<a href="..\hidsdi\nf-hidsdi-hidd-getmanufacturerstring.md">HidD_GetManufacturerString</a>
</dt>
<dt>
<a href="..\hidsdi\nf-hidsdi-hidd-getphysicaldescriptor.md">HidD_GetPhysicalDescriptor</a>
</dt>
<dt>
<a href="..\hidsdi\nf-hidsdi-hidd-getproductstring.md">HidD_GetProductString</a>
</dt>
<dt>
<a href="..\hidsdi\nf-hidsdi-hidd-getserialnumberstring.md">HidD_GetSerialNumberString</a>
</dt>
<dt>
<a href="..\hidclass\ni-hidclass-ioctl-hid-get-indexed-string.md">IOCTL_HID_GET_INDEXED_STRING</a>
</dt>
<dt>
<a href="..\hidclass\ni-hidclass-ioctl-hid-get-manufacturer-string.md">IOCTL_HID_GET_MANUFACTURER_STRING</a>
</dt>
<dt>
<a href="..\hidclass\ni-hidclass-ioctl-hid-get-product-string.md">IOCTL_HID_GET_PRODUCT_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20IOCTL_HID_GET_SERIALNUMBER_STRING control code%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
