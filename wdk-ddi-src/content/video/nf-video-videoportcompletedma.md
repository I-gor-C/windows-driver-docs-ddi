---
UID: NF.video.VideoPortCompleteDma
title: VideoPortCompleteDma
author: windows-driver-content
description: The VideoPortCompleteDma function flushes any data remaining in a bus-master adapter's internal cache at the end of a DMA transfer operation, and then frees the previously allocated map registers and scatter/gather list used in scatter/gather DMA operations.
old-location: display\videoportcompletedma.htm
old-project: display
ms.assetid: 8af5a397-7945-4f72-a253-04d227bf3ca1
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VideoPortCompleteDma
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: video.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows XP and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VideoPortCompleteDma
req.alt-loc: Videoprt.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Videoprt.lib
req.dll: Videoprt.sys
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# VideoPortCompleteDma function



## -description
<p>The <b>VideoPortCompleteDma</b> function flushes any data remaining in a bus-master adapter's internal cache at the end of a DMA transfer operation, and then frees the previously allocated map registers and scatter/gather list used in scatter/gather DMA operations.</p>


## -syntax

````
VP_STATUS VideoPortCompleteDma(
  _In_ PVOID                   HwDeviceExtension,
  _In_ PVP_DMA_ADAPTER         VpDmaAdapter,
  _In_ PVP_SCATTER_GATHER_LIST VpScatterGather,
  _In_ BOOLEAN                 WriteToDevice
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>Pointer to the miniport driver's device extension.</p>
</dd>

### -param <i>VpDmaAdapter</i> [in]

<dd>
<p>Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff570570">VP_DMA_ADAPTER</a> structure that represents the bus-master adapter. This structure was returned by a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff570312">VideoPortGetDmaAdapter</a>.</p>
</dd>

### -param <i>VpScatterGather</i> [in]

<dd>
<p>Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff570572">VP_SCATTER_GATHER_LIST</a> structure previously passed to the miniport driver callback routine, <a href="..\video\nc-video-pexecute-dma.md">HwVidExecuteDma</a>.</p>
</dd>

### -param <i>WriteToDevice</i> [in]

<dd>
<p>Specifies the direction of the DMA transfer. A value of <b>TRUE</b> denotes a transfer from the buffer to the device, and a value of <b>FALSE</b> denotes a transfer from the device to the buffer.</p>
</dd>
</dl>

## -returns
<p><b>VideoPortCompleteDma</b> returns NO_ERROR.</p>

## -remarks
<p>The video miniport driver should call <b>VideoPortCompleteDma</b> immediately to free up system resources after a DMA transfer has been completed. </p>

<p>It is important to note that the scatter/gather list built by <b>VideoPortStartDma</b> becomes invalid when <b>VideoPortCompleteDma</b> is called..</p>

<p>The video miniport driver should call <b>VideoPortCompleteDma</b> immediately to free up system resources after a DMA transfer has been completed. </p>

<p>It is important to note that the scatter/gather list built by <b>VideoPortStartDma</b> becomes invalid when <b>VideoPortCompleteDma</b> is called..</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows XP and later versions of the Windows operating systems.</p>
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
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Videoprt.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Videoprt.sys</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570312">VideoPortGetDmaAdapter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570369">VideoPortStartDma</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortCompleteDma function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
