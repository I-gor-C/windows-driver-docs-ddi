---
UID: NS.d3dkmthk._D3DKMT_SCATTERBLT
title: D3DKMT_SCATTERBLT
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmt_scatterblt.htm
ms.assetid: 94463e11-8a18-4d23-b7b6-d2486dc7dc9d
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_SCATTERBLT
req.alt-loc: D3dkmthk.h
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
ms.keywords: D3DKMT_SCATTERBLT, D3DKMT_SCATTERBLT
req.iface: 
---

# D3DKMT_SCATTERBLT structure



## -description
<p>Reserved for system use. Do not use in your driver.</p>


## -syntax

````
typedef struct _D3DKMT_SCATTERBLT {
  ULONG64 hLogicalSurfaceDestination;
  LONG64  hDestinationCompSurfDWM;
  UINT64  DestinationCompositionBindingId;
  RECT    SourceRect;
  POINT   DestinationOffset;
} D3DKMT_SCATTERBLT;
````


## -struct-fields
<dl>

### -field <b>hLogicalSurfaceDestination</b>

<dd></dd>

### -field <b>hDestinationCompSurfDWM</b>

<dd></dd>

### -field <b>DestinationCompositionBindingId</b>

<dd></dd>

### -field <b>SourceRect</b>

<dd></dd>

### -field <b>DestinationOffset</b>

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>