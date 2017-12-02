---
UID: NS.d3dkmthk._D3DKMT_ADDSURFACETOSWAPCHAIN
title: D3DKMT_ADDSURFACETOSWAPCHAIN
author: windows-driver-content
description: Used to add a surface to the swapchain.
old-location: display\d3dkmt-addsurfacetoswapchain.htm
old-project: display
ms.assetid: f1a2390c-0154-4bd7-954f-ca8725710d61
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_ADDSURFACETOSWAPCHAIN, D3DKMT_ADDSURFACETOSWAPCHAIN
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_ADDSURFACETOSWAPCHAIN
req.alt-loc: d3dkmthk.h
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

# D3DKMT_ADDSURFACETOSWAPCHAIN structure



## -description
<p>Used to add a surface to the swapchain.</p>


## -syntax

````
typedef struct _D3DKMT_ADDSURFACETOSWAPCHAIN {
  HANDLE hNtSwapChain;
  BOOL   bProducer;
  HANDLE hNtSurfaceHandle;
  UINT   BufferIdx;
} D3DKMT_ADDSURFACETOSWAPCHAIN;
````


## -struct-fields
<dl>

### -field hNtSwapChain

<dd>
<p>An NT handle for the swapchain in this process.</p>
</dd>

### -field bProducer

<dd>
<p>Indicates if the surface is a producer or consumer.</p>
</dd>

### -field hNtSurfaceHandle

<dd>
<p>An NT handle for the surface to be added.</p>
</dd>

### -field BufferIdx

<dd>
<p>Index of were the texture was placed on the surface table.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h</dt>
</dl>
</td>
</tr>
</table>