---
UID: NI.hidclass.IOCTL_HID_SET_S0_IDLE_TIMEOUT
title: IOCTL_HID_SET_S0_IDLE_TIMEOUT
author: windows-driver-content
description: The IOCTL_HID_SET_S0_IDLE_TIMEOUT request is used by a client to inform the HID class driver about the client's preferred idle timeout value.
old-location: hid\ioctl_hid_set_s0_idle_timeout.htm
ms.assetid: 9372E6D5-0E0B-4916-929D-73532FB6A5D6
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: ioctl
ms.prod: windows-hardware
ms.technology: hid
req.header: hidclass.h
req.include-header: Hidclass.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_HID_SET_S0_IDLE_TIMEOUT
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
ms.keywords: HDAUDIO_STREAM_FORMAT, HDAUDIO_STREAM_FORMAT, *PHDAUDIO_STREAM_FORMAT
req.iface: 
---

# IOCTL_HID_SET_S0_IDLE_TIMEOUT IOCTL



## -description
<p>The <b>IOCTL_HID_SET_S0_IDLE_TIMEOUT</b> 
   request is used by a client to inform the HID class driver about the client's preferred idle timeout value.</p>
<p>When the client sets this value to zero (0), it informs the HID class driver that the preferred idle timeout value is no longer valid. In this case, the HID class driver will start to use the default idle timeout value.</p>


## -ioctlparameters

### -input-buffer
<p>
       The <b>Parameters.DeviceIoControl.OutputBufferLength</b> member specifies the size, in bytes, of a requester-allocated output buffer. </p>

### -input-buffer-length
<p>This is a buffer of size ULONG.</p>

<p>This is a buffer of size ULONG.</p>

### -output-buffer
<p>The <b>Irp-&gt;AssociatedIrp.SystemBuffer</b> member is a pointer to the requestor-allocated buffer that the client uses to return the idle timeout value.</p>

<p>The <b>Irp-&gt;AssociatedIrp.SystemBuffer</b> member is a pointer to the requestor-allocated buffer that the client uses to return the idle timeout value.</p>

<p>The <b>Irp-&gt;AssociatedIrp.SystemBuffer</b> member is a pointer to the requestor-allocated buffer that the client uses to return the idle timeout value.</p>

### -output-buffer-length
<p></p>

<p></p>

<p></p>

<p></p>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, Status to the appropriate error condition as a <a href="kernel.ntstatus_value">NTSTATUS</a> code.</p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, Status to the appropriate error condition as a <a href="kernel.ntstatus_value">NTSTATUS</a> code.</p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, Status to the appropriate error condition as a <a href="kernel.ntstatus_value">NTSTATUS</a> code.</p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, Status to the appropriate error condition as a <a href="kernel.ntstatus_value">NTSTATUS</a> code.</p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, Status to the appropriate error condition as a <a href="kernel.ntstatus_value">NTSTATUS</a> code.</p>

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