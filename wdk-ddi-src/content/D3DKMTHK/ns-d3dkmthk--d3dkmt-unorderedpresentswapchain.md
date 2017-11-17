---
UID: NS.d3dkmthk._D3DKMT_UNORDEREDPRESENTSWAPCHAIN
title: D3DKMT_UNORDEREDPRESENTSWAPCHAIN
author: windows-driver-content
description: Used to store information about the swapchain being presented.
old-location: display\d3dkmt-unorderedpresentswapchain.htm
ms.assetid: c8b13348-71a6-4981-8c99-6368fa0f01ff
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
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
ms.keywords: D3DKMT_UNORDEREDPRESENTSWAPCHAIN, D3DKMT_UNORDEREDPRESENTSWAPCHAIN
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

### -field <b>hNtSwapChain</b>

<dd>
<p>NT handle for the swapchain in this process.</p>
</dd>

### -field <b>bProducer</b>

<dd>
<p>Indicates if producer or consumer.</p>
</dd>

### -field <b>PresentBufferIdx</b>

<dd>
<p>Index of the buffer to present.</p>
</dd>

### -field <b>MetaDataSize</b>

<dd>
<p>Size of the metadata.</p>
</dd>

### -field <b>pMetaData</b>

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