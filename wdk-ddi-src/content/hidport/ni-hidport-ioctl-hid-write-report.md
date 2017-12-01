---
UID: NI.hidport.IOCTL_HID_WRITE_REPORT
title: IOCTL_HID_WRITE_REPORT
author: windows-driver-content
description: The IOCTL_HID_WRITE_REPORT request sends a HID report to a HIDClass device.
old-location: hid\ioctl_hid_write_report.htm
old-project: hid
ms.assetid: 30b56c97-f135-4603-a5f0-3ed2105aae59
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: HidRegisterMinidriver
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: hidport.h
req.include-header: Hidport.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_HID_WRITE_REPORT
req.alt-loc: hidport.h
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

# IOCTL_HID_WRITE_REPORT IOCTL



## -description
<p>The IOCTL_HID_WRITE_REPORT request sends a HID report to a HIDClass device.</p>
<p>For general information about HIDClass devices, see <a href="NULL">HID Collections</a>. </p>


## -ioctlparameters

### -input-buffer
<p><b>Irp-&gt;UserBuffer </b> points to a <a href="..\hidclass\ns-hidclass--hid-xfer-packet.md">HID_XFER_PACKET</a> structure the contains the parameters and report to be transmitted to the device. The following members are used:</p>

<p></p>

<p>A pointer to a resident buffer containing the data to be sent to the device.</p>

<p>Specifies the length of the buffer provided at <b>reportBuffer</b>.</p>

<p>Specifies the report identifier, for this collection, of the report data to be written to the device.</p>

### -input-buffer-length
<p>The size of a <a href="..\hidclass\ns-hidclass--hid-xfer-packet.md">HID_XFER_PACKET</a> structure.</p>

<p>The size of a <a href="..\hidclass\ns-hidclass--hid-xfer-packet.md">HID_XFER_PACKET</a> structure.</p>

### -output-buffer
<p>None.</p>

<p>None.</p>

<p>None.</p>

### -output-buffer-length
<p>None.</p>

<p>None.</p>

<p>None.</p>

<p>None.</p>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p>
       HID minidrivers that carry out the I/O to the device set the following fields of <b>Irp-&gt;IoStatus</b>:</p>

<p><b>Information</b> is set to the number of bytes transferred to the device.</p>

<p><b>Status</b> is set to STATUS_SUCCESS if the transfer completed without error. Otherwise, it is set to an appropriate NTSTATUS error code.</p>

<p>HID minidrivers that call other drivers with this IOCTL to carry out the I/O to their device, should ensure that the <b>Information</b> field of the status block is correct and not change the contents of the <b>Status</b> field.</p>

<p>
       HID minidrivers that carry out the I/O to the device set the following fields of <b>Irp-&gt;IoStatus</b>:</p>

<p><b>Information</b> is set to the number of bytes transferred to the device.</p>

<p><b>Status</b> is set to STATUS_SUCCESS if the transfer completed without error. Otherwise, it is set to an appropriate NTSTATUS error code.</p>

<p>HID minidrivers that call other drivers with this IOCTL to carry out the I/O to their device, should ensure that the <b>Information</b> field of the status block is correct and not change the contents of the <b>Status</b> field.</p>

<p>
       HID minidrivers that carry out the I/O to the device set the following fields of <b>Irp-&gt;IoStatus</b>:</p>

<p><b>Information</b> is set to the number of bytes transferred to the device.</p>

<p><b>Status</b> is set to STATUS_SUCCESS if the transfer completed without error. Otherwise, it is set to an appropriate NTSTATUS error code.</p>

<p>HID minidrivers that call other drivers with this IOCTL to carry out the I/O to their device, should ensure that the <b>Information</b> field of the status block is correct and not change the contents of the <b>Status</b> field.</p>

<p>
       HID minidrivers that carry out the I/O to the device set the following fields of <b>Irp-&gt;IoStatus</b>:</p>

<p><b>Information</b> is set to the number of bytes transferred to the device.</p>

<p><b>Status</b> is set to STATUS_SUCCESS if the transfer completed without error. Otherwise, it is set to an appropriate NTSTATUS error code.</p>

<p>HID minidrivers that call other drivers with this IOCTL to carry out the I/O to their device, should ensure that the <b>Information</b> field of the status block is correct and not change the contents of the <b>Status</b> field.</p>

<p>
       HID minidrivers that carry out the I/O to the device set the following fields of <b>Irp-&gt;IoStatus</b>:</p>

<p><b>Information</b> is set to the number of bytes transferred to the device.</p>

<p><b>Status</b> is set to STATUS_SUCCESS if the transfer completed without error. Otherwise, it is set to an appropriate NTSTATUS error code.</p>

<p>HID minidrivers that call other drivers with this IOCTL to carry out the I/O to their device, should ensure that the <b>Information</b> field of the status block is correct and not change the contents of the <b>Status</b> field.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hidport.h (include Hidport.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\hidsdi\nf-hidsdi-hidd-getfeature.md">HidD_GetFeature</a>
</dt>
<dt>
<a href="..\hidsdi\nf-hidsdi-hidd-getinputreport.md">HidD_GetInputReport</a>
</dt>
<dt>
<a href="..\hidsdi\nf-hidsdi-hidd-setfeature.md">HidD_SetFeature</a>
</dt>
<dt>
<a href="..\hidsdi\nf-hidsdi-hidd-setoutputreport.md">HidD_SetOutputReport</a>
</dt>
<dt>
<a href="..\hidclass\ns-hidclass--hid-xfer-packet.md">HID_XFER_PACKET</a>
</dt>
<dt>
<a href="..\hidclass\ni-hidclass-ioctl-hid-get-feature.md">IOCTL_HID_GET_FEATURE</a>
</dt>
<dt>
<a href="..\hidclass\ni-hidclass-ioctl-hid-get-input-report.md">IOCTL_HID_GET_INPUT_REPORT</a>
</dt>
<dt>
<a href="..\hidport\ni-hidport-ioctl-hid-read-report.md">IOCTL_HID_READ_REPORT</a>
</dt>
<dt>
<a href="..\hidclass\ni-hidclass-ioctl-hid-set-feature.md">IOCTL_HID_SET_FEATURE</a>
</dt>
<dt>
<a href="..\hidclass\ni-hidclass-ioctl-hid-set-output-report.md">IOCTL_HID_SET_OUTPUT_REPORT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20IOCTL_HID_WRITE_REPORT control code%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
