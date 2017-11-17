---
UID: NS.d3d12umddi.D3D12DDI_CRYPTO_SESSION_TRANSFORM_DECRYPT_HEADER_OUTPUT_ARGUMENTS_0030
title: D3D12DDI_CRYPTO_SESSION_TRANSFORM_DECRYPT_HEADER_OUTPUT_ARGUMENTS_0030
author: windows-driver-content
description: Crypto session transform decrypt header output arguments.
old-location: display\d3d12ddi-crypto-session-transform-decrypt-header-output-arguments-0030.htm
ms.assetid: 15f4ea26-3a76-4c81-82cc-1abd5f95c63e
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
req.alt-api: D3D12DDI_CRYPTO_SESSION_TRANSFORM_DECRYPT_HEADER_OUTPUT_ARGUMENTS_0030
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
ms.keywords: D3D12DDI_CRYPTO_SESSION_TRANSFORM_DECRYPT_HEADER_OUTPUT_ARGUMENTS_0030, D3D12DDI_CRYPTO_SESSION_TRANSFORM_DECRYPT_HEADER_OUTPUT_ARGUMENTS_0030
req.iface: 
---

# D3D12DDI_CRYPTO_SESSION_TRANSFORM_DECRYPT_HEADER_OUTPUT_ARGUMENTS_0030 structure



## -description
<p>Crypto session transform decrypt header output arguments.</p>


## -syntax

````
typedef struct _D3D12DDI_CRYPTO_SESSION_TRANSFORM_DECRYPT_HEADER_OUTPUT_ARGUMENTS_0030 {
  BOOL          Enable;
  const void *  pSliceHeaders;
  UINT64        SliceHeadersSize;
  const void *  pContext;
  UINT64        ContextSize;
} D3D12DDI_CRYPTO_SESSION_TRANSFORM_DECRYPT_HEADER_OUTPUT_ARGUMENTS_0030, D3D12DDI_CRYPTO_SESSION_TRANSFORM_DECRYPT_HEADER_OUTPUT_ARGUMENTS_0030;
````


## -struct-fields
<dl>

### -field <b>Enable</b>

<dd>
<p>Enable.</p>
</dd>

### -field <b>pSliceHeaders</b>

<dd>
<p>Slice headers.</p>
</dd>

### -field <b>SliceHeadersSize</b>

<dd>
<p>Slice header size.</p>
</dd>

### -field <b>pContext</b>

<dd>
<p>Context.</p>
</dd>

### -field <b>ContextSize</b>

<dd>
<p>Context size.</p>
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