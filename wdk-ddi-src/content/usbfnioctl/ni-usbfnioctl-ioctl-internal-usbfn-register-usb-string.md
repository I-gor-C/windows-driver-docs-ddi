---
UID: NI.usbfnioctl.IOCTL_INTERNAL_USBFN_REGISTER_USB_STRING
title: IOCTL_INTERNAL_USBFN_REGISTER_USB_STRING
author: windows-driver-content
description: The class driver sends this request to register a USB string descriptor.
old-location: buses\ioctl_internal_usbfn_register_usb_string.htm
old-project: usbref
ms.assetid: 80CB670A-4E64-4E53-815C-12580BE982B5
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
req.alt-api: IOCTL_INTERNAL_USBFN_REGISTER_USB_STRING
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

# IOCTL_INTERNAL_USBFN_REGISTER_USB_STRING IOCTL



## -description
<p>The class driver sends this request to register a USB string descriptor.</p>


## -ioctlparameters

### -input-buffer
<p>A pointer to a buffer that contains a  <a href="..\usbfnbase\ns-usbfnbase--usbfn-usb-string.md">USBFN_USB_STRING</a> structure with the USB string descriptor. </p>

### -input-buffer-length
<p>The length of the input buffer must be at least <code>sizeof(USBFN_USB_STRING)</code>.</p>

<p>The length of the input buffer must be at least <code>sizeof(USBFN_USB_STRING)</code>.</p>

### -output-buffer
<p>NULL.</p>

<p>NULL.</p>

<p>NULL.</p>

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
<p>If the request is successful, the USB function class extension (UFX) returns STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE. Otherwise it returns a status value for which NT_SUCCESS(status) equals FALSE. </p>

<p>If the request is successful, the USB function class extension (UFX) returns STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE. Otherwise it returns a status value for which NT_SUCCESS(status) equals FALSE. </p>

<p>If the request is successful, the USB function class extension (UFX) returns STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE. Otherwise it returns a status value for which NT_SUCCESS(status) equals FALSE. </p>

<p>If the request is successful, the USB function class extension (UFX) returns STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE. Otherwise it returns a status value for which NT_SUCCESS(status) equals FALSE. </p>

<p>If the request is successful, the USB function class extension (UFX) returns STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE. Otherwise it returns a status value for which NT_SUCCESS(status) equals FALSE. </p>

## -remarks
<p>This request must be sent after sending the <a href="..\usbfnioctl\ni-usbfnioctl-ioctl-internal-usbfn-activate-usb-bus.md">IOCTL_INTERNAL_USBFN_ACTIVATE_USB_BUS</a> request.</p>

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

## -see-also
<dl>
<dt>
<a href="..\usbfnbase\ns-usbfnbase--usbfn-usb-string.md">USBFN_USB_STRING</a>
</dt>
<dt>
<a href="..\usbfnioctl\ni-usbfnioctl-ioctl-internal-usbfn-activate-usb-bus.md">IOCTL_INTERNAL_USBFN_ACTIVATE_USB_BUS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20IOCTL_INTERNAL_USBFN_REGISTER_USB_STRING control code%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
