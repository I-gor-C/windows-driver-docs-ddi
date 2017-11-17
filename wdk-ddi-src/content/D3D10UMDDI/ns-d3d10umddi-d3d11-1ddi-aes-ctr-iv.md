---
UID: NS.d3d10umddi.D3D11_1DDI_AES_CTR_IV
title: D3D11_1DDI_AES_CTR_IV
author: windows-driver-content
description: Contains an initialization vector (IV) for 128-bit Advanced Encryption Standard CTR mode (AES-CTR) block cipher encryption.
old-location: display\d3d11_1ddi_aes_ctr_iv.htm
ms.assetid: 56228a1d-ca3b-4bd4-850c-af736e91494c
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11_1DDI_AES_CTR_IV
req.alt-loc: d3d10umddi.h
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
ms.keywords: D3D11_1DDI_AES_CTR_IV, D3D11_1DDI_AES_CTR_IV
req.iface: 
---

# D3D11_1DDI_AES_CTR_IV structure



## -description
<p>Contains an initialization vector (IV) for 128-bit Advanced Encryption Standard CTR mode (AES-CTR) block cipher encryption.</p>


## -syntax

````
typedef struct D3D11_1DDI_AES_CTR_IV {
  UINT64 IV;
  UINT64 Count;
} D3D11_1DDI_AES_CTR_IV;
````


## -struct-fields
<dl>

### -field <b>IV</b>

<dd>
<p>The IV, in big-endian format.</p>
</dd>

### -field <b>Count</b>

<dd>
<p>The block count, in big-endian format.</p>
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