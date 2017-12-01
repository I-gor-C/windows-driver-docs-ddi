---
UID: NI.parallel.IOCTL_INTERNAL_GET_PARALLEL_PORT_INFO
title: IOCTL_INTERNAL_GET_PARALLEL_PORT_INFO
author: windows-driver-content
description: The IOCTL_INTERNAL_GET_PARALLEL_PORT_INFO request returns information about a parallel port.
old-location: parports\ioctl_internal_get_parallel_port_info.htm
old-project: parports
ms.assetid: c621e510-1c86-4029-aeb7-e16a38e96f03
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
req.alt-api: IOCTL_INTERNAL_GET_PARALLEL_PORT_INFO
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

# IOCTL_INTERNAL_GET_PARALLEL_PORT_INFO IOCTL



## -description
<p>The <b>IOCTL_INTERNAL_GET_PARALLEL_PORT_INFO</b> request returns information about a parallel port. The information specifies the resources assigned to the parallel port, the capabilities of the port, and pointers to <a href="parports.parallel_port_callback_routines">parallel port callback routines</a>.</p>
<p>For more information, see <a href="https://msdn.microsoft.com/d8ae2296-05b6-419a-93cc-00fcb12d41fe">Obtaining Information About a ParallelPort</a>.</p>


## -ioctlparameters

### -input-buffer
<p>A <a href="..\parallel\ns-parallel--parallel-pnp-information.md">PARALLEL_PNP_INFORMATION</a> structure. </p>

### -input-buffer-length
<p>The <b>Parameters.DeviceIoControl.OutputBufferLength</b> member is set to the size, in bytes, of a <a href="..\parallel\ns-parallel--parallel-port-information.md">PARALLEL_PORT_INFORMATION</a> structure. </p>

<p>The <b>Parameters.DeviceIoControl.OutputBufferLength</b> member is set to the size, in bytes, of a <a href="..\parallel\ns-parallel--parallel-port-information.md">PARALLEL_PORT_INFORMATION</a> structure. </p>

### -output-buffer
<p>The <b>AssociatedIrp.SystemBuffer</b> member points to a <a href="..\parallel\ns-parallel--parallel-pnp-information.md">PARALLEL_PNP_INFORMATION</a> structure that the client allocates to output the parallel port information.</p>

<p>The <b>AssociatedIrp.SystemBuffer</b> member points to a <a href="..\parallel\ns-parallel--parallel-pnp-information.md">PARALLEL_PNP_INFORMATION</a> structure that the client allocates to output the parallel port information.</p>

<p>The <b>AssociatedIrp.SystemBuffer</b> member points to a <a href="..\parallel\ns-parallel--parallel-pnp-information.md">PARALLEL_PNP_INFORMATION</a> structure that the client allocates to output the parallel port information.</p>

### -output-buffer-length
<p>The size of a <a href="..\parallel\ns-parallel--parallel-pnp-information.md">PARALLEL_PNP_INFORMATION</a> structure.</p>

<p>The size of a <a href="..\parallel\ns-parallel--parallel-pnp-information.md">PARALLEL_PNP_INFORMATION</a> structure.</p>

<p>The size of a <a href="..\parallel\ns-parallel--parallel-pnp-information.md">PARALLEL_PNP_INFORMATION</a> structure.</p>

<p>The size of a <a href="..\parallel\ns-parallel--parallel-pnp-information.md">PARALLEL_PNP_INFORMATION</a> structure.</p>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p>If this request succeeds, the <b>Information</b> member is set to the size, in bytes, of a <a href="..\parallel\ns-parallel--parallel-pnp-information.md">PARALLEL_PNP_INFORMATION</a> structure. Otherwise, the <b>Information</b> member is set to zero. </p>

<p>The <b>Status</b> member is set to one of the generic status values returned by internal device control requests for parallel ports or to the following value:</p>

<p></p>

<p>The value of the <b>Parameters.DeviceIoControl.OutputBufferLength</b> member is less than the size, in bytes, of a PARALLEL_PORT_INFORMATION structure.</p>

<p>If this request succeeds, the <b>Information</b> member is set to the size, in bytes, of a <a href="..\parallel\ns-parallel--parallel-pnp-information.md">PARALLEL_PNP_INFORMATION</a> structure. Otherwise, the <b>Information</b> member is set to zero. </p>

<p>The <b>Status</b> member is set to one of the generic status values returned by internal device control requests for parallel ports or to the following value:</p>

<p></p>

<p>The value of the <b>Parameters.DeviceIoControl.OutputBufferLength</b> member is less than the size, in bytes, of a PARALLEL_PORT_INFORMATION structure.</p>

<p>If this request succeeds, the <b>Information</b> member is set to the size, in bytes, of a <a href="..\parallel\ns-parallel--parallel-pnp-information.md">PARALLEL_PNP_INFORMATION</a> structure. Otherwise, the <b>Information</b> member is set to zero. </p>

<p>The <b>Status</b> member is set to one of the generic status values returned by internal device control requests for parallel ports or to the following value:</p>

<p></p>

<p>The value of the <b>Parameters.DeviceIoControl.OutputBufferLength</b> member is less than the size, in bytes, of a PARALLEL_PORT_INFORMATION structure.</p>

<p>If this request succeeds, the <b>Information</b> member is set to the size, in bytes, of a <a href="..\parallel\ns-parallel--parallel-pnp-information.md">PARALLEL_PNP_INFORMATION</a> structure. Otherwise, the <b>Information</b> member is set to zero. </p>

<p>The <b>Status</b> member is set to one of the generic status values returned by internal device control requests for parallel ports or to the following value:</p>

<p></p>

<p>The value of the <b>Parameters.DeviceIoControl.OutputBufferLength</b> member is less than the size, in bytes, of a PARALLEL_PORT_INFORMATION structure.</p>

<p>If this request succeeds, the <b>Information</b> member is set to the size, in bytes, of a <a href="..\parallel\ns-parallel--parallel-pnp-information.md">PARALLEL_PNP_INFORMATION</a> structure. Otherwise, the <b>Information</b> member is set to zero. </p>

<p>The <b>Status</b> member is set to one of the generic status values returned by internal device control requests for parallel ports or to the following value:</p>

<p></p>

<p>The value of the <b>Parameters.DeviceIoControl.OutputBufferLength</b> member is less than the size, in bytes, of a PARALLEL_PORT_INFORMATION structure.</p>

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
<a href="..\parallel\ni-parallel-ioctl-internal-get-more-parallel-port-info.md">IOCTL_INTERNAL_GET_MORE_PARALLEL_PORT_INFO</a>
</dt>
<dt>
<a href="..\parallel\ni-parallel-ioctl-internal-get-parallel-pnp-info.md">IOCTL_INTERNAL_GET_PARALLEL_PNP_INFO</a>
</dt>
<dt>
<a href="..\parallel\ns-parallel--parallel-port-information.md">PARALLEL_PORT_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [parports\parports]:%20IOCTL_INTERNAL_GET_PARALLEL_PORT_INFO control code%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
