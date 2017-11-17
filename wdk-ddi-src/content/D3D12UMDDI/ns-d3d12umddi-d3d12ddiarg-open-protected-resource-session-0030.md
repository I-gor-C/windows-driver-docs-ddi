---
UID: NS.d3d12umddi.D3D12DDIARG_OPEN_PROTECTED_RESOURCE_SESSION_0030
title: D3D12DDIARG_OPEN_PROTECTED_RESOURCE_SESSION_0030
author: windows-driver-content
description: Opens a protected resource session.
old-location: display\d3d12ddiarg-open-protected-resource-session-0030.htm
ms.assetid: d5f0a089-c6cb-444d-a959-ee8a5a024ea7
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3d12umddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDIARG_OPEN_PROTECTED_RESOURCE_SESSION_0030
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
ms.keywords: D3D12DDIARG_OPEN_PROTECTED_RESOURCE_SESSION_0030, D3D12DDIARG_OPEN_PROTECTED_RESOURCE_SESSION_0030
req.iface: 
---

# D3D12DDIARG_OPEN_PROTECTED_RESOURCE_SESSION_0030 structure



## -description
<p>Opens a protected resource session.</p>


## -syntax

````
typedef struct _D3D12DDIARG_OPEN_PROTECTED_RESOURCE_SESSION_0030 {
  CONST VOID *  pPrivateDriverData;
  UINT          PrivateDriverDataSize;
} D3D12DDIARG_OPEN_PROTECTED_RESOURCE_SESSION_0030, D3D12DDIARG_OPEN_PROTECTED_RESOURCE_SESSION_0030;
````


## -struct-fields
<dl>

### -field <b>pPrivateDriverData</b>

<dd>
<p>The private driver data.</p>
</dd>

### -field <b>PrivateDriverDataSize</b>

<dd>
<p>The private driver data size.</p>
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
<dt>D3d12umddi.h</dt>
</dl>
</td>
</tr>
</table>