---
UID: NS.d3dkmthk._D3DKMT_REMOVESURFACEFROMSWAPCHAIN
title: D3DKMT_REMOVESURFACEFROMSWAPCHAIN
author: windows-driver-content
description: Used to remove a surface from the swap chain.
old-location: display\d3dkmt-removesurfacefromswapchain.htm
old-project: display
ms.assetid: 249a2bfc-7326-480f-bcc0-8d5104a9c890
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_REMOVESURFACEFROMSWAPCHAIN, D3DKMT_REMOVESURFACEFROMSWAPCHAIN
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
req.alt-api: D3DKMT_REMOVESURFACEFROMSWAPCHAIN
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

# D3DKMT_REMOVESURFACEFROMSWAPCHAIN structure



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>Used to remove a surface from the swap chain.</p>


## -syntax

````
typedef struct _D3DKMT_REMOVESURFACEFROMSWAPCHAIN {
  HANDLE hNtSwapChain;
  BOOL   bProducer;
  HANDLE hNtSurfaceHandle;
  UINT   BufferIdx;
} D3DKMT_REMOVESURFACEFROMSWAPCHAIN;
````


## -struct-fields
<dl>

### -field hNtSwapChain

<dd>
<p>The NT handle for the swapchain in this process.</p>
</dd>

### -field bProducer

<dd>
<p>Indicates if the handle is a producer or consumer.</p>
</dd>

### -field hNtSurfaceHandle

<dd>
<p>The NT handle of the surface to remove.</p>
</dd>

### -field BufferIdx

<dd>
<p>The buffer index of the surface to remove.</p>
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