---
UID: NI.ntddser.IOCTL_SERIAL_SET_LINE_CONTROL
title: IOCTL_SERIAL_SET_LINE_CONTROL
author: windows-driver-content
description: The IOCTL_SERIAL_SET_LINE_CONTROL request sets the line control register (LCR). The line control register controls the data size, the number of stop bits, and the parity.
old-location: serports\ioctl_serial_set_line_control.htm
old-project: serports
ms.assetid: 0883b10c-1900-42b1-afc9-1e61effed111
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: SdBusSubmitRequestAsync
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: ntddser.h
req.include-header: Ntddser.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_SERIAL_SET_LINE_CONTROL
req.alt-loc: Ntddser.h
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
---

# IOCTL_SERIAL_SET_LINE_CONTROL IOCTL



## -description
The <b>IOCTL_SERIAL_SET_LINE_CONTROL</b> request sets the line control register (LCR). The line control register controls the data size, the number of stop bits, and the parity.

To obtain the value of the line control register, a client can use an <a href="..\ntddser\ni-ntddser-ioctl_serial_get_line_control.md">IOCTL_SERIAL_GET_LINE_CONTROL</a> request.



## -ioctlparameters

### -input-buffer
The <b>AssociatedIrp.SystemBuffer</b> points to a client-allocated <a href="serports.serial_line_control">SERIAL_LINE_CONTROL</a> structure that is used to input line control information.


### -input-buffer-length
The <b>Parameters.DeviceIoControl.InputBufferLength</b> is set to the size, in bytes, of a <b>SERIAL_LINE_CONTROL</b> structure.


### -output-buffer
None.


### -output-buffer-length
None.


### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
The <b>Information</b> member is set to zero.

The <b>Status</b> member is set to one of the <a href="serial_device_control_requests.htm#generic_status_values_for_serial_device_control_requests">Generic Status Values for Serial Device Control Requests</a>. A status of STATUS_INVALID_PARAMETER indicates that the specified line control information is not valid.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntddser.h (include Ntddser.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddser\ni-ntddser-ioctl_serial_get_line_control.md">IOCTL_SERIAL_GET_LINE_CONTROL</a>
</dt>
<dt>
<a href="serports.serial_line_control">SERIAL_LINE_CONTROL</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [serports\serports]:%20IOCTL_SERIAL_SET_LINE_CONTROL control code%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
