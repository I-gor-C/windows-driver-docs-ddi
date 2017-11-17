---
UID: NF.video.VideoPortUnmapDmaMemory
title: VideoPortUnmapDmaMemory
author: windows-driver-content
description: The VideoPortUnmapDmaMemory function is obsolete in Windows 2000 and later.VideoPortUnmapDmaMemory unmaps a range of memory previously mapped by VideoPortMapDmaMemory.
old-location: display\videoportunmapdmamemory.htm
ms.assetid: f3d05263-5e6b-4875-afff-1166928778db
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: display
req.header: video.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows 2000 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VideoPortUnmapDmaMemory
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
req.irql: 
ms.keywords: VideoPortUnmapDmaMemory
req.iface: 
req.product: Windows 10 or later.
---

# VideoPortUnmapDmaMemory function



## -description
<p>The <b>VideoPortUnmapDmaMemory</b> function is <b>obsolete</b> in Windows 2000 and later.</p>
<p><b>VideoPortUnmapDmaMemory</b> unmaps a range of memory previously mapped by <a href="https://msdn.microsoft.com/library/windows/hardware/ff570330">VideoPortMapDmaMemory</a>.</p>


## -syntax

````
BOOLEAN VideoPortUnmapDmaMemory(
   PVOID  HwDeviceExtension,
   PVOID  VirtualAddress,
   HANDLE ProcessHandle,
   PDMA   BoardMemoryHandle
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> 

<dd>
<p>Pointer to the miniport driver's device extension.</p>
</dd>

### -param <i>VirtualAddress</i> 

<dd>
<p>Pointer to a virtual address within the mapped range to be released.</p>
</dd>

### -param <i>ProcessHandle</i> 

<dd>
<p>Is the handle to the current process.</p>
</dd>

### -param <i>BoardMemoryHandle</i> 

<dd>
<p>Is the handle to adapter's memory.</p>
</dd>
</dl>

## -returns
<p><b>VideoPortUnmapDmaMemory</b> always <b>FALSE</b>.</p>

## -remarks
<p>See <a href="https://msdn.microsoft.com/fe6c2e16-d222-4948-b1df-34ed8d57d9d8">Bus-Master DMA in Video Miniport Drivers</a> for information about packet-based and common-buffer DMA transfers.</p>

<p>See <a href="https://msdn.microsoft.com/fe6c2e16-d222-4948-b1df-34ed8d57d9d8">Bus-Master DMA in Video Miniport Drivers</a> for information about packet-based and common-buffer DMA transfers.</p>

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
<p>Available in Windows 2000 and later versions of the Windows operating systems.</p>
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
</table>