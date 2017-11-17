---
UID: NS.d3d12umddi.D3D12DDI_VIDEO_DECODE_DECRYPTION_ARGUMENTS_0030
title: D3D12DDI_VIDEO_DECODE_DECRYPTION_ARGUMENTS_0030
author: windows-driver-content
description: Video decode decryption arguments.
old-location: display\d3d12ddi-video-decode-decryption-arguments-0030.htm
ms.assetid: cdd89f48-1b27-4362-81b3-ed3b89b80b6e
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
req.alt-api: D3D12DDI_VIDEO_DECODE_DECRYPTION_ARGUMENTS_0030
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
ms.keywords: D3D12DDI_VIDEO_DECODE_DECRYPTION_ARGUMENTS_0030, D3D12DDI_VIDEO_DECODE_DECRYPTION_ARGUMENTS_0030
req.iface: 
---

# D3D12DDI_VIDEO_DECODE_DECRYPTION_ARGUMENTS_0030 structure



## -description
<p>Video decode decryption arguments.</p>


## -syntax

````
typedef struct _D3D12DDI_VIDEO_DECODE_DECRYPTION_ARGUMENTS_0030 {
  D3D12DDI_HCRYPTOSESSIONPOLICY_0030  hDrvCryptoSessionPolicy;
  CONST VOID *                        pIV;
  UINT                                IVSize;
  CONST VOID *                        pSubSampleMappingBlock;
  UINT                                SubSampleMappingCount;
} D3D12DDI_VIDEO_DECODE_DECRYPTION_ARGUMENTS_0030, D3D12DDI_VIDEO_DECODE_DECRYPTION_ARGUMENTS_0030;
````


## -struct-fields
<dl>

### -field <b>hDrvCryptoSessionPolicy</b>

<dd>
<p>Crypto session policy.</p>
</dd>

### -field <b>pIV</b>

<dd>
<p>Initialization vector.</p>
</dd>

### -field <b>IVSize</b>

<dd>
<p>Initialization vector size.</p>
</dd>

### -field <b>pSubSampleMappingBlock</b>

<dd>
<p>Sub sample mapping block.</p>
</dd>

### -field <b>SubSampleMappingCount</b>

<dd>
<p>Sub sample mapping count.</p>
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