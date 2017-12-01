---
UID: NI.kbdmou.IOCTL_INTERNAL_MOUSE_CONNECT
title: IOCTL_INTERNAL_MOUSE_CONNECT
author: windows-driver-content
description: The IOCTL_INTERNAL_MOUSE_CONNECT request connects Mouclass service to a mouse device.
old-location: hid\ioctl_internal_mouse_connect.htm
old-project: hid
ms.assetid: f20e424a-60d3-4bfa-9cc3-d2541c927b22
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: MSiSCSI_SessionStatistics, MSiSCSI_SessionStatistics, *PMSiSCSI_SessionStatistics
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: kbdmou.h
req.include-header: Kbdmou.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_INTERNAL_MOUSE_CONNECT
req.alt-loc: kbdmou.h
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

# IOCTL_INTERNAL_MOUSE_CONNECT IOCTL



## -description
<p>The IOCTL_INTERNAL_MOUSE_CONNECT request connects Mouclass service to a mouse device. Mouclass sends this request down the device stack before it opens a mouse device. </p>
<p>After Moufiltr receives the mouse connect request, it filters the request in the following way:</p>
<p>Saves a copy of the <a href="https://msdn.microsoft.com/c6c2ebe5-eb88-4dc6-a85a-b297ecdc85d3">CONNECT_DATA (Mouclass)</a> structure that was passed to Moufiltr</p>
<p>Substitutes its own connect information for the class driver connect information</p>
<p>Sends the IOCTL_INTERNAL_MOUSE_CONNECT request down the device stack</p>
<p>If the request is not successful, Moufiltr completes the request with an appropriate error status.</p>
<p>Moufiltr provides a template for a filter service callback routine that can supplement the operation of <a href="https://msdn.microsoft.com/949955c1-a1c7-4b0b-a74e-593dd7885135">MouseClassServiceCallback</a>, the Mouclass service callback routine. The filter service callback can filter the input data that is transferred from the device input buffer to the class driver data queue. </p>
<p>For more information about the connection of the Mouclass service, see the following topics:</p>
<p>
<a href="hid.i8042prt_callback_routines">I8042prt Callback Routines</a>
</p>
<p>
<a href="https://msdn.microsoft.com/c6b60905-edd0-496e-a4e7-5ca271a51bce">Moufiltr Callback Routines</a>
</p>


## -ioctlparameters

### -input-buffer
<p>The <b>Parameters.DeviceIoControl.Type3InputBuffer</b> member points to a CONNECT_DATA structure that is allocated and set by Mouclass.</p>

### -input-buffer-length
<p>The <b>Parameters.DeviceIoControl.InputBufferLength</b> member is set to a value greater than or equal to the size, in bytes, of a CONNECT_DATA structure.</p>

<p>The <b>Parameters.DeviceIoControl.InputBufferLength</b> member is set to a value greater than or equal to the size, in bytes, of a CONNECT_DATA structure.</p>

### -output-buffer
<p>The <b>Parameters.DeviceIoControl.Type3InputBuffer</b> member points to a CONNECT_DATA structure that is set by Moufiltr.</p>

<p>The <b>Parameters.DeviceIoControl.Type3InputBuffer</b> member points to a CONNECT_DATA structure that is set by Moufiltr.</p>

<p>The <b>Parameters.DeviceIoControl.Type3InputBuffer</b> member points to a CONNECT_DATA structure that is set by Moufiltr.</p>

### -output-buffer-length
<p>The size of a CONNECT_DATA structure.</p>

<p>The size of a CONNECT_DATA structure.</p>

<p>The size of a CONNECT_DATA structure.</p>

<p>The size of a CONNECT_DATA structure.</p>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p>The <b>Information</b> member is set to zero.</p>

<p>The <b>Status</b> member is set to one of the following values:</p>

<p></p>

<p><b>Parameters.DeviceIoControl.InputBufferLength</b> is less than the size, in bytes, of a CONNECT_DATA structure.</p>

<p>Moufiltr is already connected (a filter driver supports only one connect request).</p>

<p>The <b>Information</b> member is set to zero.</p>

<p>The <b>Status</b> member is set to one of the following values:</p>

<p></p>

<p><b>Parameters.DeviceIoControl.InputBufferLength</b> is less than the size, in bytes, of a CONNECT_DATA structure.</p>

<p>Moufiltr is already connected (a filter driver supports only one connect request).</p>

<p>The <b>Information</b> member is set to zero.</p>

<p>The <b>Status</b> member is set to one of the following values:</p>

<p></p>

<p><b>Parameters.DeviceIoControl.InputBufferLength</b> is less than the size, in bytes, of a CONNECT_DATA structure.</p>

<p>Moufiltr is already connected (a filter driver supports only one connect request).</p>

<p>The <b>Information</b> member is set to zero.</p>

<p>The <b>Status</b> member is set to one of the following values:</p>

<p></p>

<p><b>Parameters.DeviceIoControl.InputBufferLength</b> is less than the size, in bytes, of a CONNECT_DATA structure.</p>

<p>Moufiltr is already connected (a filter driver supports only one connect request).</p>

<p>The <b>Information</b> member is set to zero.</p>

<p>The <b>Status</b> member is set to one of the following values:</p>

<p></p>

<p><b>Parameters.DeviceIoControl.InputBufferLength</b> is less than the size, in bytes, of a CONNECT_DATA structure.</p>

<p>Moufiltr is already connected (a filter driver supports only one connect request).</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Kbdmou.h (include Kbdmou.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/c6c2ebe5-eb88-4dc6-a85a-b297ecdc85d3">CONNECT_DATA (Mouclass)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/949955c1-a1c7-4b0b-a74e-593dd7885135">MouseClassServiceCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20IOCTL_INTERNAL_MOUSE_CONNECT control code%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
