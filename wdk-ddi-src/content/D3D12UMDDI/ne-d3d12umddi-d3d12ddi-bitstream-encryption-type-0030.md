---
UID: NE.d3d12umddi.D3D12DDI_BITSTREAM_ENCRYPTION_TYPE_0030
title: D3D12DDI_BITSTREAM_ENCRYPTION_TYPE_0030
author: windows-driver-content
description: The bitstream encryption type.
old-location: display\d3d12ddi-bitstream-encryption-type-0030.htm
ms.assetid: 99eab339-d93c-4afa-95f2-899ceb2e7828
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3d12umddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDI_BITSTREAM_ENCRYPTION_TYPE_0030
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
ms.keywords: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC, D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
req.iface: 
---

# D3D12DDI_BITSTREAM_ENCRYPTION_TYPE_0030 enumeration



## -description
<p>The bitstream encryption type.</p>


## -syntax

````
typedef enum _D3D12DDI_BITSTREAM_ENCRYPTION_TYPE_0030 { 
  D3D12DDI_BITSTREAM_ENCRYPTION_TYPE_0030_NONE,
  D3D12DDI_BITSTREAM_ENCRYPTION_TYPE_0030_CENC_AES_CTR_128
} D3D12DDI_BITSTREAM_ENCRYPTION_TYPE_0030;
````


## -enum-fields
<dl>

### -field <a id="D3D12DDI_BITSTREAM_ENCRYPTION_TYPE_0030_NONE"></a><a id="d3d12ddi_bitstream_encryption_type_0030_none"></a><b>D3D12DDI_BITSTREAM_ENCRYPTION_TYPE_0030_NONE</b>

<dd>
<p>Indicates that the bitstream encryption type is undefined.</p>
</dd>

### -field <a id="D3D12DDI_BITSTREAM_ENCRYPTION_TYPE_0030_CENC_AES_CTR_128"></a><a id="d3d12ddi_bitstream_encryption_type_0030_cenc_aes_ctr_128"></a><b>D3D12DDI_BITSTREAM_ENCRYPTION_TYPE_0030_CENC_AES_CTR_128</b>

<dd>
<p>Indicates that the bitstream encryption type is the CENC (Common Encryption Standard) with an AES-CTR 128 bit key.</p>
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