---
UID: NS.d3d10umddi.D3D11_1DDI_OMAC
title: D3D11_1DDI_OMAC
author: windows-driver-content
description: Contains a Message Authentication Code (MAC).
old-location: display\d3d11_1ddi_omac.htm
old-project: display
ms.assetid: 6807f32a-0e63-4603-abfb-b35d0d0d5f8c
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D11_1DDI_OMAC, D3D11_1DDI_OMAC
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11_1DDI_OMAC
req.alt-loc: D3d10umddi.h
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

# D3D11_1DDI_OMAC structure



## -description
<p>Contains a Message Authentication Code (MAC).</p>


## -syntax

````
typedef struct D3D11_1DDI_OMAC {
  BYTE Omac[D3D_OMAC_SIZE];
} D3D11_1DDI_OMAC;
````


## -struct-fields
<dl>

### -field <b>Omac</b>

<dd>
<p>A byte array that contains the cryptographic MAC value of the message.</p>
</dd>
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
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>