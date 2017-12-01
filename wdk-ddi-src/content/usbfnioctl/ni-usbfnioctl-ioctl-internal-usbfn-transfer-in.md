---
UID: NI.usbfnioctl.IOCTL_INTERNAL_USBFN_TRANSFER_IN
title: IOCTL_INTERNAL_USBFN_TRANSFER_IN
author: windows-driver-content
description: The class driver sends this request to initiate a data transfer to the host on the specified pipe.
old-location: buses\_ioctl_internal_usbfn_transfer_in.htm
old-project: usbref
ms.assetid: 53F895F8-596D-464C-866E-67028CF644E4
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
req.alt-api: IOCTL_INTERNAL_USBFN_TRANSFER_IN
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

# IOCTL_INTERNAL_USBFN_TRANSFER_IN IOCTL



## -description
<p>The class driver sends this request to initiate a data transfer to the host on the specified pipe. </p>


## -ioctlparameters

### -input-buffer
<p>A pointer to a <b>USBFNPIPEID</b> type that specifies the pipe ID.</p>

### -input-buffer-length
<p>The size of a <b>USBFNPIPEID</b> type.</p>

<p>The size of a <b>USBFNPIPEID</b> type.</p>

### -output-buffer
<p>The  output buffer points to a buffer containing the data to be sent. The IN direction is from the host perspective representing an outbound transfer from the device to the host.</p>

<p>The  output buffer points to a buffer containing the data to be sent. The IN direction is from the host perspective representing an outbound transfer from the device to the host.</p>

<p>The  output buffer points to a buffer containing the data to be sent. The IN direction is from the host perspective representing an outbound transfer from the device to the host.</p>

### -output-buffer-length
<p>The length of the data to be sent.</p>

<p>The length of the data to be sent.</p>

<p>The length of the data to be sent.</p>

<p>The length of the data to be sent.</p>

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
<p>This request must be sent after sending the <a href="buses.ioctl_internal_usbfn_activate_usb_bus">IOCTL_INTERNAL_USBFN_ACTIVATE_USB_BUS</a> request.</p>

<p>UFX forwards this IOCTL request to the transfer queue created for the endpoint by <a href="buses.ufxendpointcreate">UfxEndpointCreate</a>.</p>

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