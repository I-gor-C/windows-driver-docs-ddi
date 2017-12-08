---
UID: NC.parallel.PPARALLEL_TRY_SELECT_ROUTINE
title: PPARALLEL_TRY_SELECT_ROUTINE
author: windows-driver-content
description: The PPARALLEL_TRY_SELECT_ROUTINE-typed callback routine selects an IEEE 1284.3 daisy chain device or an IEEE 1284 end-of-chain device that is attached to a parallel port. The system-supplied function driver for parallel ports supplies this routine.
old-location: parports\pparallel_try_select_routine.htm
old-project: parports
ms.assetid: e7ecc2ac-fb86-40fe-829b-ee5851c6ae5f
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RegisterOpRegionHandler
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: parallel.h
req.include-header: Parallel.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: (*PPARALLEL_TRY_SELECT_ROUTINE)
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
req.irql: <=DISPATCH_LEVEL
req.iface: 
---

# PPARALLEL_TRY_SELECT_ROUTINE callback



## -description
<p>The <i>PPARALLEL_TRY_SELECT_ROUTINE</i>-typed callback routine selects an IEEE 1284.3 daisy chain device or an IEEE 1284 end-of-chain device that is attached to a parallel port. The system-supplied function driver for parallel ports supplies this routine.</p>


## -prototype

````
typedef NTSTATUS (*PPARALLEL_TRY_SELECT_ROUTINE)(
  _In_ PVOID TrySelectContext,
  _In_ PVOID TrySelectCommand
);
````


## -parameters
<dl>

### -param TrySelectContext [in]

<dd>
<p>Pointer to the device extension of a parallel port's functional device object (<a href="wdkgloss.f#wdkgloss.fdo#wdkgloss.fdo"><i>FDO</i></a>).</p>
</dd>

### -param TrySelectCommand [in]

<dd>
<p>Pointer to a <a href="..\parallel\ns-parallel--parallel-1284-command.md">PARALLEL_1284_COMMAND</a> structure. The caller specifies the following members:</p>
<p></p>
<dl>

### -param ID

<dd>
<p>Specifies the 1284.3 device ID. </p>
</dd>

### -param CommandFlags

<dd>
<p>Specifies a bitwise OR of zero or more of the following flags:</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>PAR_END_OF_CHAIN_DEVICE</p>
</td>
<td>
<p>Specifies an end-of-chain device.</p>
</td>
</tr>
<tr>
<td>
<p>PAR_HAVE_PORT_KEEP_PORT</p>
</td>
<td>
<p>Specifies that the caller has the port allocated and to keep the port allocated.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>
</dd>
</dl>

## -returns
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The device was selected.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The device ID is not valid.</p><dl>
<dt><b>STATUS_PENDING</b></dt>
</dl><p>The caller did not specify PAR_HAVE_PORT_KEEP_PORT, and the parallel port is already allocated.</p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>The caller has allocated the parallel port, but the system-supplied function driver for parallel ports could not select the specified parallel device.</p>

<p> </p>

## -remarks
<p>To obtain a pointer to the system-supplied <i>PPARALLEL_TRY_SELECT_ROUTINE</i> callback, a kernel-mode driver uses an <a href="..\parallel\ni-parallel-ioctl-internal-get-parallel-pnp-info.md">IOCTL_INTERNAL_GET_PARALLEL_PNP_INFO</a> request, which returns a <a href="..\parallel\ns-parallel--parallel-pnp-information.md">PARALLEL_PNP_INFORMATION</a> structure. The <b>TrySelectDevice</b> member of the PARALLEL_PNP_INFORMATION structure is a pointer to this callback.</p>

<p>A kernel-mode driver can use an <a href="..\parallel\ni-parallel-ioctl-internal-select-device.md">IOCTL_INTERNAL_SELECT_DEVICE</a> request or the <i>PPARALLEL_TRY_SELECT_ROUTINE</i> callback to select a parallel device on a parallel port. The parallel port function driver queues a select request if the parallel port is already allocated. However, the <i>PPARALLEL_TRY_SELECT_ROUTINE</i> callback does not queue a select request, and the routine returns immediately if the port cannot be allocated.</p>

<p>For more information, see <a href="https://msdn.microsoft.com/1a3ac1b1-9180-4b71-8740-70c6fbe9a885">Selecting and Deselecting an IEEE 1284 Device Attached to a ParallelPort</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
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
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\parallel\ni-parallel-ioctl-internal-deselect-device.md">IOCTL_INTERNAL_DESELECT_DEVICE</a>
</dt>
<dt>
<a href="..\parallel\ni-parallel-ioctl-internal-get-parallel-port-info.md">IOCTL_INTERNAL_GET_PARALLEL_PORT_INFO</a>
</dt>
<dt>
<a href="..\parallel\ni-parallel-ioctl-internal-select-device.md">IOCTL_INTERNAL_SELECT_DEVICE</a>
</dt>
<dt>
<a href="..\parallel\ns-parallel--parallel-1284-command.md">PARALLEL_1284_COMMAND</a>
</dt>
<dt>
<a href="..\parallel\ns-parallel--parallel-pnp-information.md">PARALLEL_PNP_INFORMATION</a>
</dt>
<dt>
<a href="..\parallel\nc-parallel-pparallel-deselect-routine.md">PPARALLEL_DESELECT_ROUTINE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [parports\parports]:%20PPARALLEL_TRY_SELECT_ROUTINE callback function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
