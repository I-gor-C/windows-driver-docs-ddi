---
UID: NE.d3d12umddi.D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030
title: D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030
author: windows-driver-content
description: The crypto session transform operations.
old-location: display\d3d12ddi-crypto-session-transform-operation-0030.htm
old-project: display
ms.assetid: 20d49b34-436a-4bc3-9b32-25f03478c90a
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC, D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d12umddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030
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
req.iface: 
---

# D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030 enumeration



## -description
<p>The crypto session transform operations.</p>


## -syntax

````
typedef enum _D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030 { 
  D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_NONE,
  D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_DECRYPT,
  D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_DECRYPT_WITH_HEADER,
  D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_TRANSCRYPT,
  D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_TRANSCRYPT_WITH_HEADER,
  D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_DECRYPT_HEADER
} D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030;
````


## -enum-fields
<dl>

### -field D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_NONE

<dd>
<p>The crypto session transform operation type is not available.</p>
</dd>

### -field D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_DECRYPT

<dd>
<p>The crypto session transform operation is decrypt.</p>
</dd>

### -field D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_DECRYPT_WITH_HEADER

<dd>
<p>The crypto session transform operation is decrypt with header.</p>
</dd>

### -field D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_TRANSCRYPT

<dd>
<p>The crypto session transform operation is transcrypt.</p>
</dd>

### -field D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_TRANSCRYPT_WITH_HEADER

<dd>
<p>The crypto session transform operation is transcrypt with header.</p>
</dd>

### -field D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_DECRYPT_HEADER

<dd>
<p>The crypto session transform operation is decrypt header.</p>
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