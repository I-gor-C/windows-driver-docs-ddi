---
UID: NE.d3d12umddi.D3D12DDI_CRYPTO_SESSION_SUPPORT_FLAGS_0030
title: D3D12DDI_CRYPTO_SESSION_SUPPORT_FLAGS_0030
author: windows-driver-content
description: The crypto session support flags.
old-location: display\d3d12ddi-crypto-session-support-flags-0030.htm
ms.assetid: ffa81a22-3de2-48f8-b753-c296401e0da3
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
req.alt-api: D3D12DDI_CRYPTO_SESSION_SUPPORT_FLAGS_0030
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

# D3D12DDI_CRYPTO_SESSION_SUPPORT_FLAGS_0030 enumeration



## -description
<p>The crypto session support flags.</p>


## -syntax

````
typedef enum _D3D12DDI_CRYPTO_SESSION_SUPPORT_FLAGS_0030 { 
  D3D12DDI_CRYPTO_SESSION_SUPPORT_FLAG_0030_NONE,
  D3D12DDI_CRYPTO_SESSION_SUPPORT_FLAG_0030_SUPPORTED,
  D3D12DDI_CRYPTO_SESSION_SUPPORT_FLAG_0030_HEADER_DECRYPTION_REQUIRED,
  D3D12DDI_CRYPTO_SESSION_SUPPORT_FLAG_0030_INDEPENDENT_DECRYPTION_REQUIRED,
  D3D12DDI_CRYPTO_SESSION_SUPPORT_FLAG_0030_TRANSCRYPTION_REQUIRED
} D3D12DDI_CRYPTO_SESSION_SUPPORT_FLAGS_0030;
````


## -enum-fields
<dl>

### -field <a id="D3D12DDI_CRYPTO_SESSION_SUPPORT_FLAG_0030_NONE"></a><a id="d3d12ddi_crypto_session_support_flag_0030_none"></a><b>D3D12DDI_CRYPTO_SESSION_SUPPORT_FLAG_0030_NONE</b>

<dd>
<p>No flag is defined.</p>
</dd>

### -field <a id="D3D12DDI_CRYPTO_SESSION_SUPPORT_FLAG_0030_SUPPORTED"></a><a id="d3d12ddi_crypto_session_support_flag_0030_supported"></a><b>D3D12DDI_CRYPTO_SESSION_SUPPORT_FLAG_0030_SUPPORTED</b>

<dd>
<p>The crypto session support flag is supported.</p>
</dd>

### -field <a id="D3D12DDI_CRYPTO_SESSION_SUPPORT_FLAG_0030_HEADER_DECRYPTION_REQUIRED"></a><a id="d3d12ddi_crypto_session_support_flag_0030_header_decryption_required"></a><b>D3D12DDI_CRYPTO_SESSION_SUPPORT_FLAG_0030_HEADER_DECRYPTION_REQUIRED</b>

<dd>
<p>The crypto session support flag requires a header decryption.</p>
</dd>

### -field <a id="D3D12DDI_CRYPTO_SESSION_SUPPORT_FLAG_0030_INDEPENDENT_DECRYPTION_REQUIRED"></a><a id="d3d12ddi_crypto_session_support_flag_0030_independent_decryption_required"></a><b>D3D12DDI_CRYPTO_SESSION_SUPPORT_FLAG_0030_INDEPENDENT_DECRYPTION_REQUIRED</b>

<dd>
<p>The crypto session support flag requires an independent decyption.</p>
</dd>

### -field <a id="D3D12DDI_CRYPTO_SESSION_SUPPORT_FLAG_0030_TRANSCRYPTION_REQUIRED"></a><a id="d3d12ddi_crypto_session_support_flag_0030_transcryption_required"></a><b>D3D12DDI_CRYPTO_SESSION_SUPPORT_FLAG_0030_TRANSCRYPTION_REQUIRED</b>

<dd>
<p>The crypto session support flag requires transcryption.</p>
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