---
UID: NC.video.PEXECUTE_DMA
title: PEXECUTE_DMA
author: windows-driver-content
description: HwVidExecuteDma is a miniport driver-implemented callback routine that is responsible for retrieving physical address/length pairs from a scatter/gather list, and for programming the hardware to start the actual DMA transfer.
old-location: display\hwvidexecutedma.htm
old-project: display
ms.assetid: 262c4b9b-fdca-4899-a635-fb273bbf4cc8
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VHF_CONFIG, VHF_CONFIG, *PVHF_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: video.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HwVidExecuteDma
req.alt-loc: video.h
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
req.product: Windows 10 or later.
---

# PEXECUTE_DMA callback



## -description
<p><i>HwVidExecuteDma</i> is a miniport driver-implemented callback routine that is responsible for retrieving physical address/length pairs from a scatter/gather list, and for programming the hardware to start the actual DMA transfer.</p>


## -prototype

````
PEXECUTE_DMA HwVidExecuteDma;

VOID HwVidExecuteDma(
   PVOID                   HwDeviceExtension,
   PVP_DMA_ADAPTER         VpDmaAdapter,
   PVP_SCATTER_GATHER_LIST SGList,
   PVOID                   Context
)
{ ... }
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> 

<dd>
<p>Pointer to the miniport driver's per-adapter storage area. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff543119">Device Extensions</a>.</p>
</dd>

### -param <i>VpDmaAdapter</i> 

<dd>
<p>Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff570570">VP_DMA_ADAPTER</a> structure that represents the bus-master adapter. This structure was returned by a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff570312">VideoPortGetDmaAdapter</a>.</p>
</dd>

### -param <i>SGList</i> 

<dd>
<p>Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff570572">VP_SCATTER_GATHER_LIST</a> structure. The video port driver fills in the information in this structure, and passes this structure to the miniport driver.</p>
</dd>

### -param <i>Context</i> 

<dd>
<p>Pointer to the driver-determined context passed in from <b>VideoPortStartDma</b>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>This function is available in Windows XP and later.</p>

<p>If the miniport driver reports that the device does not support scatter/gather, there will be only a single element in the scatter/gather list passed to this routine. The scatter/gather list is valid until <a href="https://msdn.microsoft.com/library/windows/hardware/ff570286">VideoPortCompleteDma</a> is called.</p>

<p>The last task that the video port driver's <b>VideoPortStartDma</b> function performs is to call the miniport driver's <i>HwVidExecuteDma</i> callback routine. It is this callback that actually carries out the DMA transfer operation.</p>

<p><i>HwVidExecuteDma</i> must be in nonpaged memory and must not access any pageable code or data.</p>

<p>This function is available in Windows XP and later.</p>

<p>If the miniport driver reports that the device does not support scatter/gather, there will be only a single element in the scatter/gather list passed to this routine. The scatter/gather list is valid until <a href="https://msdn.microsoft.com/library/windows/hardware/ff570286">VideoPortCompleteDma</a> is called.</p>

<p>The last task that the video port driver's <b>VideoPortStartDma</b> function performs is to call the miniport driver's <i>HwVidExecuteDma</i> callback routine. It is this callback that actually carries out the DMA transfer operation.</p>

<p><i>HwVidExecuteDma</i> must be in nonpaged memory and must not access any pageable code or data.</p>

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
<dt>Video.h (include Video.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570312">VideoPortGetDmaAdapter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570369">VideoPortStartDma</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570286">VideoPortCompleteDma</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570570">VP_DMA_ADAPTER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570572">VP_SCATTER_GATHER_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PEXECUTE_DMA callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
