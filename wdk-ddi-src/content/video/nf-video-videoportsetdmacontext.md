---
UID: NF.video.VideoPortSetDmaContext
title: VideoPortSetDmaContext
author: windows-driver-content
description: The VideoPortSetDmaContext function is obsolete in Windows 2000 and later.
old-location: display\videoportsetdmacontext.htm
old-project: display
ms.assetid: 4f357612-c07d-42fe-a49f-59acec80a8bc
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VideoPortSetDmaContext
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
req.alt-api: VideoPortSetDmaContext
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
req.iface: 
req.product: Windows 10 or later.
---

# VideoPortSetDmaContext function



## -description
<p>The <b>VideoPortSetDmaContext</b> function is <b>obsolete</b> in Windows 2000 and later. </p>


## -syntax

````
VOID VideoPortSetDmaContext(
  _In_  PVOID HwDeviceExtension,
  _Out_ PDMA  pDma,
  _In_  PVOID InstanceContext
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>Pointer to the miniport driver's device extension.</p>
</dd>

### -param <i>pDma</i> [out]

<dd>
<p>Pointer to a DMA handle. </p>
</dd>

### -param <i>InstanceContext</i> [in]

<dd>
<p>Pointer to the DMA context to set.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
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