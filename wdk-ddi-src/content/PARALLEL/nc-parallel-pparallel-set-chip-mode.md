---
UID: NC.parallel.PPARALLEL_SET_CHIP_MODE
title: PPARALLEL_SET_CHIP_MODE
author: windows-driver-content
description: The PPARALLEL_SET_CHIP_MODE-typed callback routine sets the operating mode of a parallel port. The system-supplied function driver for parallel ports supplies this routine.
old-location: parports\pparallel_set_chip_mode.htm
ms.assetid: 7c80f3ee-cbb2-400d-9dfb-36ccef93d80f
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
req.alt-api: (*PPARALLEL_SET_CHIP_MODE)
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

# PPARALLEL_SET_CHIP_MODE callback



## -description
<p>The <i>PPARALLEL_SET_CHIP_MODE</i>-typed callback routine sets the operating mode of a parallel port. The system-supplied function driver for parallel ports supplies this routine.</p>


## -prototype

````
typedef NTSTATUS (*PPARALLEL_SET_CHIP_MODE)(
  _In_ PVOID SetChipContext,
  _In_ UCHAR ChipMode
);
````


## -parameters
<dl>

### -param <i>SetChipContext</i> [in]

<dd>
<p>Pointer to the device extension of a parallel port's functional device object (<a href="wdkgloss.f#wdkgloss.fdo#wdkgloss.fdo"><i>FDO</i></a>).</p>
</dd>

### -param <i>ChipMode</i> [in]

<dd>
<p>Specifies the operating mode of a parallel port. (For more information about operating modes, see the modes that are defined for the enhanced capabilities register (ECR) in the <i>parallel.h</i> file that is included in the Microsoft Windows Driver Kit [WDK].)</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The specified operating mode was set.</p><dl>
<dt><b>STATUS_INVALID_DEVICE_STATE</b></dt>
</dl><p>The mode is not cleared.</p><dl>
<dt><b>STATUS_NO_SUCH_DEVICE</b></dt>
</dl><p>The specified operating mode is not valid.</p>

<p> </p>

## -remarks
<p>To obtain a pointer to the system-supplied <i>PPARALLEL_SET_CHIP_MODE</i> callback, a kernel-mode driver uses an <a href="https://msdn.microsoft.com/library/windows/hardware/ff543997">IOCTL_INTERNAL_GET_PARALLEL_PNP_INFO</a> request, which returns a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544299">PARALLEL_PNP_INFORMATION</a> structure. The <b>TrySetChipMode</b> member of the PARALLEL_PNP_INFORMATION structure is a pointer to this callback.</p>

<p>A caller uses the <i>PPARALLEL_SET_CHIP_MODE</i> callback in conjunction with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544398">PPARALLEL_CLEAR_CHIP_MODE</a> callback.</p>

<p>To set a new mode, a caller must first clear the current mode. </p>

<p>For more information, see <a href="https://msdn.microsoft.com/a22cdeef-4ae7-49f8-b0b5-a4d68feb4235">Setting and Clearing the Communication Mode on a ParallelPort</a>.</p>

<p>To obtain a pointer to the system-supplied <i>PPARALLEL_SET_CHIP_MODE</i> callback, a kernel-mode driver uses an <a href="https://msdn.microsoft.com/library/windows/hardware/ff543997">IOCTL_INTERNAL_GET_PARALLEL_PNP_INFO</a> request, which returns a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544299">PARALLEL_PNP_INFORMATION</a> structure. The <b>TrySetChipMode</b> member of the PARALLEL_PNP_INFORMATION structure is a pointer to this callback.</p>

<p>A caller uses the <i>PPARALLEL_SET_CHIP_MODE</i> callback in conjunction with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544398">PPARALLEL_CLEAR_CHIP_MODE</a> callback.</p>

<p>To set a new mode, a caller must first clear the current mode. </p>

<p>For more information, see <a href="https://msdn.microsoft.com/a22cdeef-4ae7-49f8-b0b5-a4d68feb4235">Setting and Clearing the Communication Mode on a ParallelPort</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544002">IOCTL_INTERNAL_GET_PARALLEL_PORT_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544017">IOCTL_INTERNAL_PARALLEL_CLEAR_CHIP_MODE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544031">IOCTL_INTERNAL_PARALLEL_SET_CHIP_MODE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544299">PARALLEL_PNP_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544398">PPARALLEL_CLEAR_CHIP_MODE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [parports\parports]:%20PPARALLEL_SET_CHIP_MODE callback function%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
