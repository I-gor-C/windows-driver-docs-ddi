---
UID: NI.ntdd8042.IOCTL_INTERNAL_I8042_KEYBOARD_WRITE_BUFFER
title: IOCTL_INTERNAL_I8042_KEYBOARD_WRITE_BUFFER
author: windows-driver-content
description: The IOCTL_INTERNAL_I8042_KEYBOARD_WRITE_BUFFER request writes data to the i8042 port controller to control operation of a keyboard device.
old-location: hid\ioctl_internal_i8042_keyboard_write_buffer.htm
old-project: hid
ms.assetid: 583263fc-8b95-47d9-9f20-306b2200b573
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: MSFC_VirtualFibrePortAttributes, MSFC_VirtualFibrePortAttributes, *PMSFC_VirtualFibrePortAttributes
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: ntdd8042.h
req.include-header: Ntdd8042.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_INTERNAL_I8042_KEYBOARD_WRITE_BUFFER
req.alt-loc: ntdd8042.h
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

# IOCTL_INTERNAL_I8042_KEYBOARD_WRITE_BUFFER IOCTL



## -description
<p>
<p>The IOCTL_INTERNAL_I8042_KEYBOARD_WRITE_BUFFER request writes data to the i8042 port controller to control operation of a keyboard device. A filter driver can use this request to control the operation of a keyboard.</p>
<p>I8042prt synchronizes write buffer requests and other keyboard requests that write to the i8042 port controller, including <a href="hid.ioctl_keyboard_set_indicators">IOCTL_KEYBOARD_SET_INDICATORS</a> and <a href="hid.ioctl_keyboard_set_typematic">IOCTL_KEYBOARD_SET_TYPEMATIC</a>. I8042prt synchronizes the actual write of data with the keyboard ISR.</p>
</p>
<p>The IOCTL_INTERNAL_I8042_KEYBOARD_WRITE_BUFFER request writes data to the i8042 port controller to control operation of a keyboard device. A filter driver can use this request to control the operation of a keyboard.</p>
<p>I8042prt synchronizes write buffer requests and other keyboard requests that write to the i8042 port controller, including <a href="hid.ioctl_keyboard_set_indicators">IOCTL_KEYBOARD_SET_INDICATORS</a> and <a href="hid.ioctl_keyboard_set_typematic">IOCTL_KEYBOARD_SET_TYPEMATIC</a>. I8042prt synchronizes the actual write of data with the keyboard ISR.</p>


## -ioctlparameters

### -input-buffer
<p><b>Parameters.DeviceIoControl.Type3InputBuffer</b> points to a client-allocated buffer which inputs the data to write to an i8042 port controller.</p>

### -input-buffer-length
<p><b>Parameters.DeviceIoControl.InputBufferLength</b> is set to the number of bytes in the input buffer, which must be greater than one.</p>

<p><b>Parameters.DeviceIoControl.InputBufferLength</b> is set to the number of bytes in the input buffer, which must be greater than one.</p>

### -output-buffer
<p>None</p>

<p>None</p>

<p>None</p>

### -output-buffer-length
<p>None</p>

<p>None</p>

<p>None</p>

<p>None</p>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p>The <b>Status</b> member is set to one of the following values:</p>

<p></p>

<p>The request completed successfully.</p>

<p>The keyboard interrupt is not initialized.</p>

<p>The input parameters are not valid.</p>

<p>The request timed out.</p>

<p>The <b>Status</b> member is set to one of the following values:</p>

<p></p>

<p>The request completed successfully.</p>

<p>The keyboard interrupt is not initialized.</p>

<p>The input parameters are not valid.</p>

<p>The request timed out.</p>

<p>The <b>Status</b> member is set to one of the following values:</p>

<p></p>

<p>The request completed successfully.</p>

<p>The keyboard interrupt is not initialized.</p>

<p>The input parameters are not valid.</p>

<p>The request timed out.</p>

<p>The <b>Status</b> member is set to one of the following values:</p>

<p></p>

<p>The request completed successfully.</p>

<p>The keyboard interrupt is not initialized.</p>

<p>The input parameters are not valid.</p>

<p>The request timed out.</p>

<p>The <b>Status</b> member is set to one of the following values:</p>

<p></p>

<p>The request completed successfully.</p>

<p>The keyboard interrupt is not initialized.</p>

<p>The input parameters are not valid.</p>

<p>The request timed out.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntdd8042.h (include Ntdd8042.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="hid.ioctl_keyboard_set_indicators">IOCTL_KEYBOARD_SET_INDICATORS</a>
</dt>
<dt>
<a href="hid.ioctl_keyboard_set_typematic">IOCTL_KEYBOARD_SET_TYPEMATIC</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20IOCTL_INTERNAL_I8042_KEYBOARD_WRITE_BUFFER control code%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
