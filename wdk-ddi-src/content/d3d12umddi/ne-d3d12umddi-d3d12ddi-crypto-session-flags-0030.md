---
UID: NE.d3d12umddi.D3D12DDI_CRYPTO_SESSION_FLAGS_0030
title: D3D12DDI_CRYPTO_SESSION_FLAGS_0030
author: windows-driver-content
description: The crypto session flags.
old-location: display\d3d12ddi-crypto-session-flags-0030.htm
old-project: display
ms.assetid: 0a799227-9b37-45f6-bded-e56c439e465f
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
req.alt-api: D3D12DDI_CRYPTO_SESSION_FLAGS_0030
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

# D3D12DDI_CRYPTO_SESSION_FLAGS_0030 enumeration



## -description
<p>The crypto session flags.</p>


## -syntax

````
typedef enum _D3D12DDI_CRYPTO_SESSION_FLAGS_0030 { 
  D3D12DDI_CRYPTO_SESSION_FLAG_0030_NONE,
  D3D12DDI_CRYPTO_SESSION_FLAG_0030_HARDWARE
} D3D12DDI_CRYPTO_SESSION_FLAGS_0030;
````


## -enum-fields
<dl>

### -field <a id="D3D12DDI_CRYPTO_SESSION_FLAG_0030_NONE"></a><a id="d3d12ddi_crypto_session_flag_0030_none"></a><b>D3D12DDI_CRYPTO_SESSION_FLAG_0030_NONE</b>

<dd>
<p>No crypto session flag is defined.</p>
</dd>

### -field <a id="D3D12DDI_CRYPTO_SESSION_FLAG_0030_HARDWARE"></a><a id="d3d12ddi_crypto_session_flag_0030_hardware"></a><b>D3D12DDI_CRYPTO_SESSION_FLAG_0030_HARDWARE</b>

<dd>
<p>The crypto session flag is of type hardware.</p>
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