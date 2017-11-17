---
UID: NI.hidclass.IOCTL_HID_GET_MS_GENRE_DESCRIPTOR
title: IOCTL_HID_GET_MS_GENRE_DESCRIPTOR
author: windows-driver-content
description: The IOCTL_HID_GET_MS_GENRE_DESCRIPTOR request is used for retrieving the genre descriptor for the device.
old-location: hid\ioctl_hid_get_ms_genre_descriptor.htm
ms.assetid: C83C6086-369D-41DB-BEB5-33B3A0C1C0AE
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
req.alt-api: IOCTL_HID_GET_MS_GENRE_DESCRIPTOR
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

# IOCTL_HID_GET_MS_GENRE_DESCRIPTOR IOCTL



## -description
<p>The <b>IOCTL_HID_GET_MS_GENRE_DESCRIPTOR</b> 
   request is used for retrieving the genre descriptor for the device.</p>


## -ioctlparameters

### -input-buffer
<p>
       The <b>Parameters.DeviceIoControl.OutputBufferLength</b> member specifies the size, in bytes, of a requester-allocated output buffer. </p>

### -input-buffer-length
<p></p>

<p></p>

### -output-buffer
<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, Status to the appropriate error condition as a <a href="kernel.ntstatus_value">NTSTATUS</a> code.</p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, Status to the appropriate error condition as a <a href="kernel.ntstatus_value">NTSTATUS</a> code.</p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, Status to the appropriate error condition as a <a href="kernel.ntstatus_value">NTSTATUS</a> code.</p>

### -output-buffer-length
<p>The size of a status code.</p>

<p>The size of a status code.</p>

<p>The size of a status code.</p>

<p>The size of a status code.</p>

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