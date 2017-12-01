---
UID: NF.video.VideoPortGetMdl
title: VideoPortGetMdl
author: windows-driver-content
description: The VideoPortGetMdl function is obsolete in Windows 2000 and later.VideoPortGetMdl retrieves the memory descriptor list (MDL) that represents the page table of the locked buffer.
old-location: display\videoportgetmdl.htm
old-project: display
ms.assetid: 03ec6323-a3f9-485d-80c8-92ac99d8e73a
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VideoPortGetMdl
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
req.alt-api: VideoPortGetMdl
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

# VideoPortGetMdl function



## -description
<p>The <b>VideoPortGetMdl</b> function is <b>obsolete</b> in Windows 2000 and later.</p>
<p><b>VideoPortGetMdl</b> retrieves the memory descriptor list (<a href="wdkgloss.m#wdkgloss.mdl#wdkgloss.mdl"><i>MDL</i></a>) that represents the page table of the locked buffer.</p>


## -syntax

````
PVOID VideoPortGetMdl(
  _In_ PVOID HwDeviceExtension,
  _In_ PDMA  pDma
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>Pointer to the miniport driver's device extension.</p>
</dd>

### -param <i>pDma</i> [in]

<dd>
<p>Is a handle to the DMA context being queried. This handle was obtained from <a href="..\video\nf-video-videoportlockpages.md">VideoPortLockPages</a> or <a href="..\video\nf-video-videoportdodma.md">VideoPortDoDma</a>.</p>
</dd>
</dl>

## -returns
<p><b>VideoPortGetMdl</b> returns <i>pDma</i>, for compatibility reasons. </p>

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