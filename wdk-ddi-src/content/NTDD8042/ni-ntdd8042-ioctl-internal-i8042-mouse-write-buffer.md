---
UID: NI.ntdd8042.IOCTL_INTERNAL_I8042_MOUSE_WRITE_BUFFER
title: IOCTL_INTERNAL_I8042_MOUSE_WRITE_BUFFER
author: windows-driver-content
description: The IOCTL_INTERNAL_I8042_MOUSE_WRITE_BUFFER request writes data to the i8042 port controller to control operation of a mouse device.
old-location: hid\ioctl_internal_i8042_mouse_write_buffer.htm
ms.assetid: 40f6fd0b-8c18-408b-b1f7-5b280b9aa67d
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: ioctl
ms.prod: windows-hardware
ms.technology: hid
req.header: ntdd8042.h
req.include-header: Ntdd8042.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_INTERNAL_I8042_MOUSE_WRITE_BUFFER
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
ms.keywords: MSFC_VirtualFibrePortAttributes, MSFC_VirtualFibrePortAttributes, *PMSFC_VirtualFibrePortAttributes
req.iface: 
---

# IOCTL_INTERNAL_I8042_MOUSE_WRITE_BUFFER IOCTL



## -description
<p>
<p>The IOCTL_INTERNAL_I8042_MOUSE_WRITE_BUFFER request writes data to the i8042 port controller to control operation of a mouse device. An upper-level filter driver can use this request to control the operation of a mouse.</p>
<p>I8042prt synchronizes write buffer requests with one another. I8042prt synchronizes the actual write of data with the mouse ISR.</p>
</p>
<p>The IOCTL_INTERNAL_I8042_MOUSE_WRITE_BUFFER request writes data to the i8042 port controller to control operation of a mouse device. An upper-level filter driver can use this request to control the operation of a mouse.</p>
<p>I8042prt synchronizes write buffer requests with one another. I8042prt synchronizes the actual write of data with the mouse ISR.</p>


## -ioctlparameters

### -input-buffer
<p><b>Parameters.DeviceIoControl.Type3InputBuffer</b> points to a client-allocated buffer that supplies the data to write to an i8042 port controller.</p>

### -input-buffer-length
<p><b>Parameters.DeviceIoControl.InputBufferLength</b> is set to the number of bytes in the input buffer, which must be greater than 1.</p>

<p><b>Parameters.DeviceIoControl.InputBufferLength</b> is set to the number of bytes in the input buffer, which must be greater than 1.</p>

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

<p>The mouse interrupt is not initialized.</p>

<p>The input parameters are not valid.</p>

<p>The request timed out.</p>

<p>The <b>Status</b> member is set to one of the following values:</p>

<p></p>

<p>The request completed successfully.</p>

<p>The mouse interrupt is not initialized.</p>

<p>The input parameters are not valid.</p>

<p>The request timed out.</p>

<p>The <b>Status</b> member is set to one of the following values:</p>

<p></p>

<p>The request completed successfully.</p>

<p>The mouse interrupt is not initialized.</p>

<p>The input parameters are not valid.</p>

<p>The request timed out.</p>

<p>The <b>Status</b> member is set to one of the following values:</p>

<p></p>

<p>The request completed successfully.</p>

<p>The mouse interrupt is not initialized.</p>

<p>The input parameters are not valid.</p>

<p>The request timed out.</p>

<p>The <b>Status</b> member is set to one of the following values:</p>

<p></p>

<p>The request completed successfully.</p>

<p>The mouse interrupt is not initialized.</p>

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