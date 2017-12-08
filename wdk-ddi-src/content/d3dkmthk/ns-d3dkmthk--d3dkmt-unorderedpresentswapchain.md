---
UID: NS.d3dkmthk._D3DKMT_UNORDEREDPRESENTSWAPCHAIN
title: D3DKMT_UNORDEREDPRESENTSWAPCHAIN
author: windows-driver-content
description: Used to store information about the swapchain being presented.
old-location: display\d3dkmt-unorderedpresentswapchain.htm
old-project: display
ms.assetid: c8b13348-71a6-4981-8c99-6368fa0f01ff
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_UNORDEREDPRESENTSWAPCHAIN, D3DKMT_UNORDEREDPRESENTSWAPCHAIN
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
req.alt-api: D3DKMT_UNORDEREDPRESENTSWAPCHAIN
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

# D3DKMT_UNORDEREDPRESENTSWAPCHAIN structure



## -description
<p>Used to store information about the swapchain being presented.</p>


## -syntax

````
typedef struct _D3DKMT_UNORDEREDPRESENTSWAPCHAIN {
  HANDLE hNtSwapChain;
  BOOL   bProducer;
  UINT   PresentBufferIdx;
  UINT   MetaDataSize;
  PVOID  pMetaData;
} D3DKMT_UNORDEREDPRESENTSWAPCHAIN;
````


## -struct-fields
<dl>

### -field hNtSwapChain

<dd>
<p>NT handle for the swapchain in this process.</p>
</dd>

### -field bProducer

<dd>
<p>Indicates if producer or consumer.</p>
</dd>

### -field PresentBufferIdx

<dd>
<p>Index of the buffer to present.</p>
</dd>

### -field MetaDataSize

<dd>
<p>Size of the metadata.</p>
</dd>

### -field pMetaData

<dd>
<p>A pointer to the metadata for the frame.</p>
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