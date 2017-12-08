---
UID: NI.usbfnioctl.IOCTL_INTERNAL_USBFN_TRANSFER_IN_APPEND_ZERO_PKT
title: IOCTL_INTERNAL_USBFN_TRANSFER_IN_APPEND_ZERO_PKT
author: windows-driver-content
description: The class driver sends this request to initiate an IN transfer to the specified pipe and appends a zero-length packet to indicate the end of the transfer.
old-location: buses\ioctl_internal_usbfn_transfer_in_append_zero_pkt.htm
old-project: usbref
ms.assetid: 3912A632-E9D0-42D5-B7B7-766A92EE8C95
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USBFN_USB_STRING, USBFN_USB_STRING, *PUSBFN_USB_STRING
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: usbfnioctl.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_INTERNAL_USBFN_TRANSFER_IN_APPEND_ZERO_PKT
req.alt-loc: usbfnioctl.h
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
req.product: Windows 10 or later.
---

# IOCTL_INTERNAL_USBFN_TRANSFER_IN_APPEND_ZERO_PKT IOCTL



## -description
<p>The class driver sends this request to initiate an IN transfer to the specified pipe and appends a zero-length packet to indicate the end of the transfer. </p>


## -ioctlparameters

### -input-buffer
<p>A pointer to a <b>USBFNPIPEID</b> type that specifies the pipe ID.</p>

### -input-buffer-length
<p>The size of a <b>USBFNPIPEID</b> type.</p>

<p>The size of a <b>USBFNPIPEID</b> type.</p>

### -output-buffer
<p>The  output buffer points to a data buffer containing the data to be sent. The IN direction is from the host perspective representing an outbound transfer from the device to the host.</p>

<p>The  output buffer points to a data buffer containing the data to be sent. The IN direction is from the host perspective representing an outbound transfer from the device to the host.</p>

<p>The  output buffer points to a data buffer containing the data to be sent. The IN direction is from the host perspective representing an outbound transfer from the device to the host.</p>

### -output-buffer-length
<p>The size of the data to be sent.</p>

<p>The size of the data to be sent.</p>

<p>The size of the data to be sent.</p>

<p>The size of the data to be sent.</p>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p>If the request is successful, the USB function class extension (UFX) returns STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE. Otherwise it returns a status value for which NT_SUCCESS(status) equals FALSE. </p>

<p>If the request is successful, the USB function class extension (UFX) returns STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE. Otherwise it returns a status value for which NT_SUCCESS(status) equals FALSE. </p>

<p>If the request is successful, the USB function class extension (UFX) returns STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE. Otherwise it returns a status value for which NT_SUCCESS(status) equals FALSE. </p>

<p>If the request is successful, the USB function class extension (UFX) returns STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE. Otherwise it returns a status value for which NT_SUCCESS(status) equals FALSE. </p>

<p>If the request is successful, the USB function class extension (UFX) returns STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE. Otherwise it returns a status value for which NT_SUCCESS(status) equals FALSE. </p>

## -remarks
<p>This request must be sent after sending the <a href="..\usbfnioctl\ni-usbfnioctl-ioctl-internal-usbfn-activate-usb-bus.md">IOCTL_INTERNAL_USBFN_ACTIVATE_USB_BUS</a> request.</p>

<p>UFX forwards this IOCTL request to the transfer queue created for the endpoint by <a href="..\ufxclient\nf-ufxclient-ufxendpointcreate.md">UfxEndpointCreate</a>.</p>

<p>The function controller initiates a transfer in the IN direction on the endpoint and automatically appends a zero-length packet transfer after the data provided in the data buffer is successfully sent. A zero-length packet is only appended by the controller if the size of the transfer payload is a multiple of the endpoint’s maximum packet size.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usbfnioctl.h</dt>
</dl>
</td>
</tr>
</table>