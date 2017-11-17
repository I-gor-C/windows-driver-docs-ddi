---
UID: NC.parallel.PPARALLEL_DESELECT_ROUTINE
title: PPARALLEL_DESELECT_ROUTINE
author: windows-driver-content
description: The PPARALLEL_DESELECT_ROUTINE-typed callback routine deselects either an IEEE 1284.3 daisy chain device or an IEEE 1284 end-of-chain device that is attached to a parallel port.
old-location: parports\pparallel_deselect_routine.htm
ms.assetid: 91182ed5-e444-41a7-b6fc-f14d0407f089
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: parports
req.header: parallel.h
req.include-header: Parallel.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: (*PPARALLEL_DESELECT_ROUTINE)
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
ms.keywords: RegisterOpRegionHandler
req.iface: 
---

# PPARALLEL_DESELECT_ROUTINE callback



## -description
<p>The <i>PPARALLEL_DESELECT_ROUTINE</i>-typed callback routine deselects either an IEEE 1284.3 daisy chain device or an IEEE 1284 end-of-chain device that is attached to a parallel port. The system-supplied function driver for parallel ports supplies this routine.</p>


## -prototype

````
typedef NTSTATUS (*PPARALLEL_DESELECT_ROUTINE)(
  _In_ PVOID DeselectContext,
  _In_ PVOID DeselectCommand
);
````


## -parameters
<dl>

### -param <i>DeselectContext</i> [in]

<dd>
<p>Pointer to the device extension of a functional device object (<a href="wdkgloss.f#wdkgloss.fdo#wdkgloss.fdo"><i>FDO</i></a>) that represents a parallel port.</p>
</dd>

### -param <i>DeselectCommand</i> [in]

<dd>
<p>Pointer to a PARALLEL_1284_COMMAND structure. The caller specifies the following members:</p>
<p></p>
<dl>

### -param <a id="ID"></a><a id="id"></a><b>ID</b>

<dd>
<p>Specifies the 1284.3 device ID (zero or 1).</p>
</dd>

### -param <a id="CommandFlags"></a><a id="commandflags"></a><a id="COMMANDFLAGS"></a><b>CommandFlags</b>

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
<p>Specifies that the port be kept allocated.</p>
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
</dl><p>The device was deselected.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The specified device ID is invalid.</p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>The system-supplied function driver for parallel ports could not deselect the device.</p>

<p> </p>

## -remarks
<p>To obtain a pointer to the system-supplied <i>PPARALLEL_DESELECT_ROUTINE</i> callback, a kernel-mode driver uses an <a href="https://msdn.microsoft.com/library/windows/hardware/ff543997">IOCTL_INTERNAL_GET_PARALLEL_PNP_INFO</a> request, which returns a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544299">PARALLEL_PNP_INFORMATION</a> structure. The <b>DeselectDevice</b> member of the PARALLEL_PNP_INFORMATION structure is a pointer to this callback.</p>

<p>A kernel-mode driver can use an <a href="https://msdn.microsoft.com/library/windows/hardware/ff543987">IOCTL_INTERNAL_DESELECT_DEVICE</a> request or the <i>PPARALLEL_CLEAR_CHIP_MODE</i> callback to deselect a device on a parallel port represented by a parallel port. To deselect a device, a caller should have the parallel port allocated. If the caller does not set the PAR_HAVE_PORT_KEEP_PORT flag, the system-supplied function driver for parallel ports frees the parallel port after deselecting the device.</p>

<p>For more information, see <a href="https://msdn.microsoft.com/1a3ac1b1-9180-4b71-8740-70c6fbe9a885">Selecting and Deselecting an IEEE 1284 Device Attached to a ParallelPort</a>.</p>

<p>To obtain a pointer to the system-supplied <i>PPARALLEL_DESELECT_ROUTINE</i> callback, a kernel-mode driver uses an <a href="https://msdn.microsoft.com/library/windows/hardware/ff543997">IOCTL_INTERNAL_GET_PARALLEL_PNP_INFO</a> request, which returns a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544299">PARALLEL_PNP_INFORMATION</a> structure. The <b>DeselectDevice</b> member of the PARALLEL_PNP_INFORMATION structure is a pointer to this callback.</p>

<p>A kernel-mode driver can use an <a href="https://msdn.microsoft.com/library/windows/hardware/ff543987">IOCTL_INTERNAL_DESELECT_DEVICE</a> request or the <i>PPARALLEL_CLEAR_CHIP_MODE</i> callback to deselect a device on a parallel port represented by a parallel port. To deselect a device, a caller should have the parallel port allocated. If the caller does not set the PAR_HAVE_PORT_KEEP_PORT flag, the system-supplied function driver for parallel ports frees the parallel port after deselecting the device.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543987">IOCTL_INTERNAL_DESELECT_DEVICE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544052">IOCTL_INTERNAL_SELECT_DEVICE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544299">PARALLEL_PNP_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544767">PPARALLEL_TRY_SELECT_ROUTINE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [parports\parports]:%20PPARALLEL_DESELECT_ROUTINE callback function%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
