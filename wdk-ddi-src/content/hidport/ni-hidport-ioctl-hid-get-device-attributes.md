---
UID: NI.hidport.IOCTL_HID_GET_DEVICE_ATTRIBUTES
title: IOCTL_HID_GET_DEVICE_ATTRIBUTES
author: windows-driver-content
description: The IOCTL_HID_GET_DEVICE_ATTRIBUTES request obtains a HIDClass device's attributes in a HID_DEVICE_ATTRIBUTES structure.
old-location: hid\ioctl_hid_get_device_attributes.htm
old-project: hid
ms.assetid: ee68c045-e99a-471d-ae22-396673d68168
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
req.alt-api: IOCTL_HID_GET_DEVICE_ATTRIBUTES
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

# IOCTL_HID_GET_DEVICE_ATTRIBUTES IOCTL



## -description
<p>The IOCTL_HID_GET_DEVICE_ATTRIBUTES request obtains a HIDClass device's attributes in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff539893">HID_DEVICE_ATTRIBUTES</a> structure.</p>
<p>For general information about HIDClass devices, see <a href="NULL">HID Collections</a>. </p>


## -ioctlparameters

### -input-buffer
<p><b>Parameters.DeviceIoControl.OutputBufferLength</b> contains the length, in bytes, of the HID class driver's buffer located at <b>Irp-&gt;UserBuffer</b>. </p>

### -input-buffer-length
<p>The size, in bytes, of the buffer must be greater than or equal to the size, in bytes, of a HID_DEVICE_ATTRIBUTES structure.</p>

<p>The size, in bytes, of the buffer must be greater than or equal to the size, in bytes, of a HID_DEVICE_ATTRIBUTES structure.</p>

### -output-buffer
<p>The HID minidriver returns the device attributes in a HID_DEVICE_ATTRIBUTES structure at <b>Irp-&gt;UserBuffer</b>.</p>

<p>The HID minidriver returns the device attributes in a HID_DEVICE_ATTRIBUTES structure at <b>Irp-&gt;UserBuffer</b>.</p>

<p>The HID minidriver returns the device attributes in a HID_DEVICE_ATTRIBUTES structure at <b>Irp-&gt;UserBuffer</b>.</p>

### -output-buffer-length
<p>The size of a HID_DEVICE_ATTRIBUTES structure.</p>

<p>The size of a HID_DEVICE_ATTRIBUTES structure.</p>

<p>The size of a HID_DEVICE_ATTRIBUTES structure.</p>

<p>The size of a HID_DEVICE_ATTRIBUTES structure.</p>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p>The HID minidriver sets the following fields of <b>Irp-&gt;IoStatus</b>:</p>

<p><b>Information</b> is set to the number of bytes transferred from the device.</p>

<p><b>Status</b> is set to STATUS_SUCCESS if the transfer completed without error. Otherwise, it is set to an appropriate NTSTATUS error code.</p>

<p>The HID minidriver sets the following fields of <b>Irp-&gt;IoStatus</b>:</p>

<p><b>Information</b> is set to the number of bytes transferred from the device.</p>

<p><b>Status</b> is set to STATUS_SUCCESS if the transfer completed without error. Otherwise, it is set to an appropriate NTSTATUS error code.</p>

<p>The HID minidriver sets the following fields of <b>Irp-&gt;IoStatus</b>:</p>

<p><b>Information</b> is set to the number of bytes transferred from the device.</p>

<p><b>Status</b> is set to STATUS_SUCCESS if the transfer completed without error. Otherwise, it is set to an appropriate NTSTATUS error code.</p>

<p>The HID minidriver sets the following fields of <b>Irp-&gt;IoStatus</b>:</p>

<p><b>Information</b> is set to the number of bytes transferred from the device.</p>

<p><b>Status</b> is set to STATUS_SUCCESS if the transfer completed without error. Otherwise, it is set to an appropriate NTSTATUS error code.</p>

<p>The HID minidriver sets the following fields of <b>Irp-&gt;IoStatus</b>:</p>

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
<dt>Hidport.h (include Hidport.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539893">HID_DEVICE_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439622">IOCTL_HID_GET_DEVICE_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20IOCTL_HID_GET_DEVICE_ATTRIBUTES control code%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
