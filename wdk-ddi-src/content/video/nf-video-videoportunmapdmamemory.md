---
UID: NF.video.VideoPortUnmapDmaMemory
title: VideoPortUnmapDmaMemory function
author: windows-driver-content
description: The VideoPortUnmapDmaMemory function is obsolete in Windows 2000 and later.VideoPortUnmapDmaMemory unmaps a range of memory previously mapped by VideoPortMapDmaMemory.
old-location: display\videoportunmapdmamemory.htm
old-project: display
ms.assetid: f3d05263-5e6b-4875-afff-1166928778db
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: VideoPortUnmapDmaMemory
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
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
req.product: Windows 10 or later.
---

# VideoPortUnmapDmaMemory function



## -description
The <b>VideoPortUnmapDmaMemory</b> function is <b>obsolete</b> in Windows 2000 and later.

<b>VideoPortUnmapDmaMemory</b> unmaps a range of memory previously mapped by <a href="display.videoportmapdmamemory">VideoPortMapDmaMemory</a>.



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

### -param HwDeviceExtension 

Pointer to the miniport driver's device extension.


### -param VirtualAddress 

Pointer to a virtual address within the mapped range to be released.


### -param ProcessHandle 

Is the handle to the current process.


### -param BoardMemoryHandle 

Is the handle to adapter's memory.


## -returns
<b>VideoPortUnmapDmaMemory</b> always <b>FALSE</b>.


## -remarks
See <a href="https://msdn.microsoft.com/fe6c2e16-d222-4948-b1df-34ed8d57d9d8">Bus-Master DMA in Video Miniport Drivers</a> for information about packet-based and common-buffer DMA transfers.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Windows 2000 and later versions of the Windows operating systems.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Video.h (include Video.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Videoprt.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>Videoprt.sys</dt>
</dl>
</td>
</tr>
</table>