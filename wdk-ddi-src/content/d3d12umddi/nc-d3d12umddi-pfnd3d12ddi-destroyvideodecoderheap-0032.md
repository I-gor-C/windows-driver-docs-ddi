---
UID: NC.d3d12umddi.PFND3D12DDI_DESTROYVIDEODECODERHEAP_0032
title: PFND3D12DDI_DESTROYVIDEODECODERHEAP_0032
author: windows-driver-content
description: Used to destroy a video decoder heap.
old-location: display\pfnd3d12ddi_destroyvideodecoderheap_0032.htm
old-project: display
ms.assetid: EFB7D67D-1900-4182-B604-8C0A183B118D
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC, D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d12umddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PFND3D12DDI_DESTROYVIDEODECODERHEAP_0032
req.alt-loc: d3d12umddi.h
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
---

# PFND3D12DDI_DESTROYVIDEODECODERHEAP_0032 callback



## -description
<p>Used to destroy a video decoder heap.</p>


## -prototype

````
VOID APIENTRY* PFND3D12DDI_DESTROYVIDEODECODERHEAP_0032(
   D3D12DDI_HDEVICE                hDrvDevice,
   D3D12DDI_HVIDEODECODERHEAP_0032 hDrvVideoDecoderHeap
);
````


## -parameters
<dl>

### -param <i>hDrvDevice</i> 

<dd>
<p>The hardware device being processed.</p>
</dd>

### -param <i>hDrvVideoDecoderHeap</i> 

<dd>
<p>The video decoder heap.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d12umddi.h</dt>
</dl>
</td>
</tr>
</table>