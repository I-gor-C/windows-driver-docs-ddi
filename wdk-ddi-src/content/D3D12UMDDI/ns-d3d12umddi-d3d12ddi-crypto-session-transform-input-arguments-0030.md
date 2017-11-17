---
UID: NS.d3d12umddi.D3D12DDI_CRYPTO_SESSION_TRANSFORM_INPUT_ARGUMENTS_0030
title: D3D12DDI_CRYPTO_SESSION_TRANSFORM_INPUT_ARGUMENTS_0030
author: windows-driver-content
description: Crypto session transform input arguments.
old-location: display\d3d12ddi-crypto-session-transform-input-arguments-0030.htm
ms.assetid: 2c7e1218-63d3-4fa5-8b02-7bee5920146c
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
req.alt-api: D3D12DDI_CRYPTO_SESSION_TRANSFORM_INPUT_ARGUMENTS_0030
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
ms.keywords: D3D12DDI_CRYPTO_SESSION_TRANSFORM_INPUT_ARGUMENTS_0030, D3D12DDI_CRYPTO_SESSION_TRANSFORM_INPUT_ARGUMENTS_0030
req.iface: 
---

# D3D12DDI_CRYPTO_SESSION_TRANSFORM_INPUT_ARGUMENTS_0030 structure



## -description
<p>Crypto session transform input arguments.</p>


## -syntax

````
typedef struct _D3D12DDI_CRYPTO_SESSION_TRANSFORM_INPUT_ARGUMENTS_0030 {
  D3D12DDI_HCRYPTOSESSIONPOLICY_0030                                     hDrvCryptoSessionPolicy;
  D3D12DDI_HRESOURCE                                                     hDrvBuffer;
  UINT64                                                                 Size;
  UINT64                                                                 Offset;
  const void *                                                           pIV;
  UINT                                                                   IVSize;
  const void *                                                           pSubSampleMappingBlock;
  UINT                                                                   SubSampleMappingCount;
  const void *                                                           pContext;
  UINT64                                                                 ContextSize;
  D3D12DDI_CRYPTO_SESSION_TRANSFORM_DECRYPT_HEADER_INPUT_ARGUMENTS_0030  EncryptedHeader;
} D3D12DDI_CRYPTO_SESSION_TRANSFORM_INPUT_ARGUMENTS_0030, D3D12DDI_CRYPTO_SESSION_TRANSFORM_INPUT_ARGUMENTS_0030;
````


## -struct-fields
<dl>

### -field <b>hDrvCryptoSessionPolicy</b>

<dd>
<p>Crypto session policy.</p>
</dd>

### -field <b>hDrvBuffer</b>

<dd>
<p>Resource.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>Size.</p>
</dd>

### -field <b>Offset</b>

<dd>
<p>Offset.</p>
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

### -field <b>pContext</b>

<dd>
<p>Context.</p>
</dd>

### -field <b>ContextSize</b>

<dd>
<p>Context size.</p>
</dd>

### -field <b>EncryptedHeader</b>

<dd>
<p>Encrypted header.</p>
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