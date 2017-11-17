---
UID: NF.video.VideoPortMapDmaMemory
title: VideoPortMapDmaMemory
author: windows-driver-content
description: The VideoPortMapDmaMemory function is obsolete in Windows 2000 and later.VideoPortMapDmaMemory maps a range of memory for use in DMA transfers.
old-location: display\videoportmapdmamemory.htm
ms.assetid: 51148c26-c10d-4c57-9e3e-c7d82d6a1c79
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
req.alt-api: VideoPortMapDmaMemory
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
ms.keywords: VideoPortMapDmaMemory
req.iface: 
req.product: Windows 10 or later.
---

# VideoPortMapDmaMemory function



## -description
<p>The <b>VideoPortMapDmaMemory</b> function is <b>obsolete</b> in Windows 2000 and later.</p>
<p><b>VideoPortMapDmaMemory</b> maps a range of memory for use in DMA transfers.</p>


## -syntax

````
PDMA VideoPortMapDmaMemory(
  _In_    PVOID                 HwDeviceExtension,
  _In_    PVIDEO_REQUEST_PACKET pVrp,
  _In_    PHYSICAL_ADDRESS      BoardAddress,
  _In_    PULONG                Length,
  _In_    PULONG                InIoSpace,
  _In_    PVOID                 MappedUserEvent,
  _In_    PVOID                 DisplayDriverEvent,
  _Inout_ PVOID                 *VirtualAddress
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>Pointer to the miniport driver's device extension.</p>
</dd>

### -param <i>pVrp</i> [in]

<dd>
<p>Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff570547">VIDEO_REQUEST_PACKET</a>.</p>
</dd>

### -param <i>BoardAddress</i> [in]

<dd>
<p>Specifies the adapter's beginning address.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>Specifies the length, in bytes, of the range of memory.</p>
</dd>

### -param <i>InIoSpace</i> [in]

<dd>
<p>Indicates the location of the range. This parameter can be one of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>VIDEO_MEMORY_SPACE_DENSE</p>
</td>
<td>
<p>Memory is densely mapped and linear.</p>
</td>
</tr>
<tr>
<td>
<p>VIDEO_MEMORY_SPACE_IO</p>
</td>
<td>
<p>The range is in system I/O space. Should not be set by the display driver.</p>
</td>
</tr>
<tr>
<td>
<p>VIDEO_MEMORY_SPACE_MEMORY</p>
</td>
<td>
<p>The range is in memory space. Should not be set by the display driver.</p>
</td>
</tr>
<tr>
<td>
<p>VIDEO_MEMORY_SPACE_P6CACHE</p>
</td>
<td>
<p>P6 MTRR caching, which is equivalent to write-combine caching. (kernel and user mode).</p>
</td>
</tr>
<tr>
<td>
<p>VIDEO_MEMORY_SPACE_USER_MODE</p>
</td>
<td>
<p>Memory pointer for application use.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>MappedUserEvent</i> [in]

<dd>
<p>Is reserved for system use.</p>
</dd>

### -param <i>DisplayDriverEvent</i> [in]

<dd>
<p>Is reserved for system use.</p>
</dd>

### -param <i>VirtualAddress</i> [in, out]

<dd>
<p>Is reserved for system use.</p>
</dd>
</dl>

## -returns
<p><b>VideoPortMapDmaMemory</b> always returns <b>NULL</b>.</p>

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