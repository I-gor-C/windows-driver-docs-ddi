---
UID: NS.d3dkmthk._D3DKMT_QUERY_PHYSICAL_ADAPTER_PNP_KEY
title: D3DKMT_QUERY_PHYSICAL_ADAPTER_PNP_KEY
author: windows-driver-content
description: A structure that holds information to query the physical adapter PNP key.
old-location: display\d3dkmt_query_physical_adapter_pnp_key.htm
ms.assetid: 58E5D200-56C3-48BA-A7C9-C9DC01592554
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
req.alt-api: D3DKMT_QUERY_PHYSICAL_ADAPTER_PNP_KEY
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
ms.keywords: D3DKMT_QUERY_PHYSICAL_ADAPTER_PNP_KEY, D3DKMT_QUERY_PHYSICAL_ADAPTER_PNP_KEY
req.iface: 
---

# D3DKMT_QUERY_PHYSICAL_ADAPTER_PNP_KEY structure



## -description
<p>A structure that holds information to query the physical adapter PNP key.</p>


## -syntax

````
typedef struct _D3DKMT_QUERY_PHYSICAL_ADAPTER_PNP_KEY {
  UINT                PhysicalAdapterIndex;
  D3DKMT_PNP_KEY_TYPE PnPKeyType;
  WCHAR               *pDest;
   UINT               *pCchDest;
} D3DKMT_QUERY_PHYSICAL_ADAPTER_PNP_KEY;
````


## -struct-fields
<dl>

### -field <b>PhysicalAdapterIndex</b>

<dd>
<p>The physical adapter index.</p>
</dd>

### -field <b>PnPKeyType</b>

<dd>
<p>The type of the PNP key being queried.</p>
</dd>

### -field <b>pDest</b>

<dd>
<p>A WCHAR value respresenting the pDest.</p>
</dd>

### -field <b>pCchDest</b>

<dd>
<p>A UINT value representing the pCchDest.</p>
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