---
UID: NI.parallel.IOCTL_INTERNAL_PARALLEL_DISCONNECT_INTERRUPT
title: IOCTL_INTERNAL_PARALLEL_DISCONNECT_INTERRUPT
author: windows-driver-content
description: The IOCTL_INTERNAL_PARALLEL_DISCONNECT_INTERRUPT request disconnects an interrupt service routine (and an optional deferred port check service routine) that was connected by using an IOCTL_INTERNAL_PARALLEL_CONNECT_INTERRUPT request.
old-location: parports\ioctl_internal_parallel_disconnect_interrupt.htm
old-project: parports
ms.assetid: 9ca488b1-30d3-44dc-acb3-87d97e439393
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
req.alt-api: IOCTL_INTERNAL_PARALLEL_DISCONNECT_INTERRUPT
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

# IOCTL_INTERNAL_PARALLEL_DISCONNECT_INTERRUPT IOCTL



## -description
<p>The <b>IOCTL_INTERNAL_PARALLEL_DISCONNECT_INTERRUPT</b> request disconnects an interrupt service routine (and an optional deferred port check service routine) that was connected by using an <a href="https://msdn.microsoft.com/library/windows/hardware/ff544020">IOCTL_INTERNAL_PARALLEL_CONNECT_INTERRUPT</a> request. Only kernel-mode drivers can connect and disconnect an interrupt routine.</p>


## -ioctlparameters

### -input-buffer
<p>The <b>AssociatedIrp.SystemBuffer</b> member points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544295">PARALLEL_INTERRUPT_SERVICE_ROUTINE</a> structure that the client allocates for the input of interrupt service information.</p>

### -input-buffer-length
<p>The <b>Parameters.DeviceIoControl.InputBufferLength</b> member is set to the size, in bytes, of a PARALLEL_INTERRUPT_SERVICE_ROUTINE structure. </p>

<p>The <b>Parameters.DeviceIoControl.InputBufferLength</b> member is set to the size, in bytes, of a PARALLEL_INTERRUPT_SERVICE_ROUTINE structure. </p>

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
<p>The <b>Information</b> member is set to zero. </p>

<p>The <b>Status</b> member is set to one of the generic status values returned by internal device control requests for parallel ports or to one of the following values:</p>

<p></p>

<p>The value of the <b>Parameters.DeviceIoControl.InputBufferLength</b> member is less than the size, in bytes, of a PARALLEL_INTERRUPT_SERVICE_ROUTINE structure.</p>

<p>The specified interrupt service routine is not connected.</p>

<p>The <b>Information</b> member is set to zero. </p>

<p>The <b>Status</b> member is set to one of the generic status values returned by internal device control requests for parallel ports or to one of the following values:</p>

<p></p>

<p>The value of the <b>Parameters.DeviceIoControl.InputBufferLength</b> member is less than the size, in bytes, of a PARALLEL_INTERRUPT_SERVICE_ROUTINE structure.</p>

<p>The specified interrupt service routine is not connected.</p>

<p>The <b>Information</b> member is set to zero. </p>

<p>The <b>Status</b> member is set to one of the generic status values returned by internal device control requests for parallel ports or to one of the following values:</p>

<p></p>

<p>The value of the <b>Parameters.DeviceIoControl.InputBufferLength</b> member is less than the size, in bytes, of a PARALLEL_INTERRUPT_SERVICE_ROUTINE structure.</p>

<p>The specified interrupt service routine is not connected.</p>

<p>The <b>Information</b> member is set to zero. </p>

<p>The <b>Status</b> member is set to one of the generic status values returned by internal device control requests for parallel ports or to one of the following values:</p>

<p></p>

<p>The value of the <b>Parameters.DeviceIoControl.InputBufferLength</b> member is less than the size, in bytes, of a PARALLEL_INTERRUPT_SERVICE_ROUTINE structure.</p>

<p>The specified interrupt service routine is not connected.</p>

<p>The <b>Information</b> member is set to zero. </p>

<p>The <b>Status</b> member is set to one of the generic status values returned by internal device control requests for parallel ports or to one of the following values:</p>

<p></p>

<p>The value of the <b>Parameters.DeviceIoControl.InputBufferLength</b> member is less than the size, in bytes, of a PARALLEL_INTERRUPT_SERVICE_ROUTINE structure.</p>

<p>The specified interrupt service routine is not connected.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544020">IOCTL_INTERNAL_PARALLEL_CONNECT_INTERRUPT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544290">PARALLEL_INTERRUPT_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544295">PARALLEL_INTERRUPT_SERVICE_ROUTINE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [parports\parports]:%20IOCTL_INTERNAL_PARALLEL_DISCONNECT_INTERRUPT control code%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
