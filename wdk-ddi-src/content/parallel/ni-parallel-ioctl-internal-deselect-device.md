---
UID: NI.parallel.IOCTL_INTERNAL_DESELECT_DEVICE
title: IOCTL_INTERNAL_DESELECT_DEVICE
author: windows-driver-content
description: The IOCTL_INTERNAL_DESELECT_DEVICE request deselects an IEEE 1284.3 daisy-chain device or an IEEE 1284 end-of-chain device attached to a parallel port.
old-location: parports\ioctl_internal_deselect_device.htm
old-project: parports
ms.assetid: 39cb818e-6219-4d7e-8114-8c0dfdfff76e
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: RegisterOpRegionHandler
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: parallel.h
req.include-header: Parallel.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_INTERNAL_DESELECT_DEVICE
req.alt-loc: parallel.h
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

# IOCTL_INTERNAL_DESELECT_DEVICE IOCTL



## -description
<p>The <b>IOCTL_INTERNAL_DESELECT_DEVICE</b> request deselects an IEEE 1284.3 daisy-chain device or an IEEE 1284 end-of-chain device attached to a parallel port.</p>
<p>For more information, see <a href="https://msdn.microsoft.com/1a3ac1b1-9180-4b71-8740-70c6fbe9a885">Selecting and Deselecting an IEEE 1284 Device Attached to a ParallelPort</a>.</p>


## -ioctlparameters

### -input-buffer
<p>The <b>AssociatedIrp.SystemBuffer</b> member points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544243">PARALLEL_1284_COMMAND</a> structure that the client allocates to input IEEE 1284.3 command information. The client can free the parallel port by not setting the PAR_HAVE_PORT_KEEP_PORT flag in the <b>CommandFlags</b> member.</p>

### -input-buffer-length
<p>The <b>Parameters.DeviceIoControl.InputBufferLength</b> member specifies the size, in bytes, of the PARALLEL_1284_COMMAND structure.</p>

<p>The <b>Parameters.DeviceIoControl.InputBufferLength</b> member specifies the size, in bytes, of the PARALLEL_1284_COMMAND structure.</p>

### -output-buffer
<p>None.</p>

<p>None.</p>

<p>None.</p>

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
<p>The <b>Information</b> member is set to zero.</p>

<p>The <b>Status</b> member is set to one of the generic status values returned by internal device control requests for parallel ports or to one of the following values:</p>

<p></p>

<p>The value of the <b>Parameters.DeviceIoControl.InputBufferLength</b> member is less than the size, in bytes, of a PARALLEL_1284_COMMAND structure.</p>

<p>The specified device is not flagged internally as an end-of-chain device, and the specified ID value is greater than the number of existing daisy-chain devices.</p>

<p>The <b>Information</b> member is set to zero.</p>

<p>The <b>Status</b> member is set to one of the generic status values returned by internal device control requests for parallel ports or to one of the following values:</p>

<p></p>

<p>The value of the <b>Parameters.DeviceIoControl.InputBufferLength</b> member is less than the size, in bytes, of a PARALLEL_1284_COMMAND structure.</p>

<p>The specified device is not flagged internally as an end-of-chain device, and the specified ID value is greater than the number of existing daisy-chain devices.</p>

<p>The <b>Information</b> member is set to zero.</p>

<p>The <b>Status</b> member is set to one of the generic status values returned by internal device control requests for parallel ports or to one of the following values:</p>

<p></p>

<p>The value of the <b>Parameters.DeviceIoControl.InputBufferLength</b> member is less than the size, in bytes, of a PARALLEL_1284_COMMAND structure.</p>

<p>The specified device is not flagged internally as an end-of-chain device, and the specified ID value is greater than the number of existing daisy-chain devices.</p>

<p>The <b>Information</b> member is set to zero.</p>

<p>The <b>Status</b> member is set to one of the generic status values returned by internal device control requests for parallel ports or to one of the following values:</p>

<p></p>

<p>The value of the <b>Parameters.DeviceIoControl.InputBufferLength</b> member is less than the size, in bytes, of a PARALLEL_1284_COMMAND structure.</p>

<p>The specified device is not flagged internally as an end-of-chain device, and the specified ID value is greater than the number of existing daisy-chain devices.</p>

<p>The <b>Information</b> member is set to zero.</p>

<p>The <b>Status</b> member is set to one of the generic status values returned by internal device control requests for parallel ports or to one of the following values:</p>

<p></p>

<p>The value of the <b>Parameters.DeviceIoControl.InputBufferLength</b> member is less than the size, in bytes, of a PARALLEL_1284_COMMAND structure.</p>

<p>The specified device is not flagged internally as an end-of-chain device, and the specified ID value is greater than the number of existing daisy-chain devices.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Parallel.h (include Parallel.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544052">IOCTL_INTERNAL_SELECT_DEVICE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544243">PARALLEL_1284_COMMAND</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [parports\parports]:%20IOCTL_INTERNAL_DESELECT_DEVICE control code%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
