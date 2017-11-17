---
UID: NI.parallel.IOCTL_INTERNAL_PARCLASS_CONNECT
title: IOCTL_INTERNAL_PARCLASS_CONNECT
author: windows-driver-content
description: The IOCTL_INTERNAL_PARCLASS_CONNECT request returns information about a parallel port and the callback routines that the system-supplied bus driver for parallel ports provides to operate the parallel port.
old-location: parports\ioctl_internal_parclass_connect.htm
ms.assetid: 77dc31a1-a50c-4727-b730-1785e5d4a355
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: ioctl
ms.prod: windows-hardware
ms.technology: parports
req.header: parallel.h
req.include-header: Parallel.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_INTERNAL_PARCLASS_CONNECT
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
ms.keywords: RegisterOpRegionHandler
req.iface: 
---

# IOCTL_INTERNAL_PARCLASS_CONNECT IOCTL



## -description
<p>The <b>IOCTL_INTERNAL_PARCLASS_CONNECT</b> request returns information about a parallel port and the callback routines that the system-supplied bus driver for parallel ports provides to operate the parallel port.</p>
<p>For more information, see <a href="NULL">Connecting to a Parallel Device</a>.</p>


## -ioctlparameters

### -input-buffer
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544334">PARCLASS_INFORMATION</a> structure. </p>

### -input-buffer-length
<p>The value of the <b>Parameters.DeviceIoControl.OutputBufferLength</b> member is set to the size, in bytes, of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544334">PARCLASS_INFORMATION</a> structure. </p>

<p>The value of the <b>Parameters.DeviceIoControl.OutputBufferLength</b> member is set to the size, in bytes, of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544334">PARCLASS_INFORMATION</a> structure. </p>

### -output-buffer
<p>The <b>AssociatedIrp.SystemBuffer</b> member points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544334">PARCLASS_INFORMATION</a> structure that the client allocates to output information.</p>

<p>The <b>AssociatedIrp.SystemBuffer</b> member points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544334">PARCLASS_INFORMATION</a> structure that the client allocates to output information.</p>

<p>The <b>AssociatedIrp.SystemBuffer</b> member points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544334">PARCLASS_INFORMATION</a> structure that the client allocates to output information.</p>

### -output-buffer-length
<p>The size of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544334">PARCLASS_INFORMATION</a> structure.</p>

<p>The size of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544334">PARCLASS_INFORMATION</a> structure.</p>

<p>The size of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544334">PARCLASS_INFORMATION</a> structure.</p>

<p>The size of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544334">PARCLASS_INFORMATION</a> structure.</p>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p>If the request is successful, the <b>Information</b> member is set to the size, in bytes, of a PARCLASS_INFORMATION structure. Otherwise, the <b>Information</b> member is set to zero. </p>

<p>The <b>Status</b> member is set to one of the generic status values returned by internal device control requests for parallel devices or to the following value:</p>

<p></p>

<p>The value of the <b>Parameters.DeviceIoControl.OutputBufferLength</b> member is less than the size, in bytes, of a PARCLASS_INFORMATION structure.</p>

<p>If the request is successful, the <b>Information</b> member is set to the size, in bytes, of a PARCLASS_INFORMATION structure. Otherwise, the <b>Information</b> member is set to zero. </p>

<p>The <b>Status</b> member is set to one of the generic status values returned by internal device control requests for parallel devices or to the following value:</p>

<p></p>

<p>The value of the <b>Parameters.DeviceIoControl.OutputBufferLength</b> member is less than the size, in bytes, of a PARCLASS_INFORMATION structure.</p>

<p>If the request is successful, the <b>Information</b> member is set to the size, in bytes, of a PARCLASS_INFORMATION structure. Otherwise, the <b>Information</b> member is set to zero. </p>

<p>The <b>Status</b> member is set to one of the generic status values returned by internal device control requests for parallel devices or to the following value:</p>

<p></p>

<p>The value of the <b>Parameters.DeviceIoControl.OutputBufferLength</b> member is less than the size, in bytes, of a PARCLASS_INFORMATION structure.</p>

<p>If the request is successful, the <b>Information</b> member is set to the size, in bytes, of a PARCLASS_INFORMATION structure. Otherwise, the <b>Information</b> member is set to zero. </p>

<p>The <b>Status</b> member is set to one of the generic status values returned by internal device control requests for parallel devices or to the following value:</p>

<p></p>

<p>The value of the <b>Parameters.DeviceIoControl.OutputBufferLength</b> member is less than the size, in bytes, of a PARCLASS_INFORMATION structure.</p>

<p>If the request is successful, the <b>Information</b> member is set to the size, in bytes, of a PARCLASS_INFORMATION structure. Otherwise, the <b>Information</b> member is set to zero. </p>

<p>The <b>Status</b> member is set to one of the generic status values returned by internal device control requests for parallel devices or to the following value:</p>

<p></p>

<p>The value of the <b>Parameters.DeviceIoControl.OutputBufferLength</b> member is less than the size, in bytes, of a PARCLASS_INFORMATION structure.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544046">IOCTL_INTERNAL_PARCLASS_DISCONNECT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544334">PARCLASS_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [parports\parports]:%20IOCTL_INTERNAL_PARCLASS_CONNECT control code%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
