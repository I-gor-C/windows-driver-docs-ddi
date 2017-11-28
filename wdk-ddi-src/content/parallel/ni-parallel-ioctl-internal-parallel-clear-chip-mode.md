---
UID: NI.parallel.IOCTL_INTERNAL_PARALLEL_CLEAR_CHIP_MODE
title: IOCTL_INTERNAL_PARALLEL_CLEAR_CHIP_MODE
author: windows-driver-content
description: The IOCTL_INTERNAL_PARALLEL_CLEAR_CHIP_MODE request clears the operating mode of a parallel port.
old-location: parports\ioctl_internal_parallel_clear_chip_mode.htm
old-project: parports
ms.assetid: bca93bca-96f6-46bb-ba24-9f39b5ad1ab4
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
req.alt-api: IOCTL_INTERNAL_PARALLEL_CLEAR_CHIP_MODE
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

# IOCTL_INTERNAL_PARALLEL_CLEAR_CHIP_MODE IOCTL



## -description
<p>The <b>IOCTL_INTERNAL_PARALLEL_CLEAR_CHIP_MODE</b> request clears the operating mode of a parallel port.</p>
<p>For more information see, <a href="https://msdn.microsoft.com/a22cdeef-4ae7-49f8-b0b5-a4d68feb4235">Setting and Clearing the Communication Mode on a ParallelPort</a>.</p>


## -ioctlparameters

### -input-buffer
<p>The <b>AssociatedIrp.SystemBuffer</b> member points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544252">PARALLEL_CHIP_MODE</a> structure that the client allocates to input chip mode information. The client sets the <b>ModeFlags</b> member to the current operating mode.</p>

### -input-buffer-length
<p>The request sets the <b>Parameters.DeviceIoControl.InputBufferLength</b> member to the size, in bytes, of a PARALLEL_CHIP_MODE structure.</p>

<p>The request sets the <b>Parameters.DeviceIoControl.InputBufferLength</b> member to the size, in bytes, of a PARALLEL_CHIP_MODE structure.</p>

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

<p>The value of the <b>Parameters.DeviceIoControl.InputBufferLength</b> member is less than the size, in bytes, of a PARALLEL_CHIP_MODE structure.</p>

<p>The specified operating mode is not the same as the current operating mode of the parallel port.</p>

<p>The <b>Information</b> member is set to zero. </p>

<p>The <b>Status</b> member is set to one of the generic status values returned by internal device control requests for parallel ports or to one of the following values:</p>

<p></p>

<p>The value of the <b>Parameters.DeviceIoControl.InputBufferLength</b> member is less than the size, in bytes, of a PARALLEL_CHIP_MODE structure.</p>

<p>The specified operating mode is not the same as the current operating mode of the parallel port.</p>

<p>The <b>Information</b> member is set to zero. </p>

<p>The <b>Status</b> member is set to one of the generic status values returned by internal device control requests for parallel ports or to one of the following values:</p>

<p></p>

<p>The value of the <b>Parameters.DeviceIoControl.InputBufferLength</b> member is less than the size, in bytes, of a PARALLEL_CHIP_MODE structure.</p>

<p>The specified operating mode is not the same as the current operating mode of the parallel port.</p>

<p>The <b>Information</b> member is set to zero. </p>

<p>The <b>Status</b> member is set to one of the generic status values returned by internal device control requests for parallel ports or to one of the following values:</p>

<p></p>

<p>The value of the <b>Parameters.DeviceIoControl.InputBufferLength</b> member is less than the size, in bytes, of a PARALLEL_CHIP_MODE structure.</p>

<p>The specified operating mode is not the same as the current operating mode of the parallel port.</p>

<p>The <b>Information</b> member is set to zero. </p>

<p>The <b>Status</b> member is set to one of the generic status values returned by internal device control requests for parallel ports or to one of the following values:</p>

<p></p>

<p>The value of the <b>Parameters.DeviceIoControl.InputBufferLength</b> member is less than the size, in bytes, of a PARALLEL_CHIP_MODE structure.</p>

<p>The specified operating mode is not the same as the current operating mode of the parallel port.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544031">IOCTL_INTERNAL_PARALLEL_SET_CHIP_MODE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544252">PARALLEL_CHIP_MODE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [parports\parports]:%20IOCTL_INTERNAL_PARALLEL_CLEAR_CHIP_MODE control code%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
