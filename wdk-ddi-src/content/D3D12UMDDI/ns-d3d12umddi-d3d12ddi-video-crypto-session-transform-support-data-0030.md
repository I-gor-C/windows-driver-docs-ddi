---
UID: NS.d3d12umddi.D3D12DDI_VIDEO_CRYPTO_SESSION_TRANSFORM_SUPPORT_DATA_0030
title: D3D12DDI_VIDEO_CRYPTO_SESSION_TRANSFORM_SUPPORT_DATA_0030
author: windows-driver-content
description: Video crypto session transform support data.
old-location: display\d3d12ddi-video-crypto-session-transform-support-data-0030.htm
ms.assetid: fb83a03e-56d9-4daf-93c1-407744ad134a
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
req.alt-api: D3D12DDI_VIDEO_CRYPTO_SESSION_TRANSFORM_SUPPORT_DATA_0030
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
ms.keywords: D3D12DDI_VIDEO_CRYPTO_SESSION_TRANSFORM_SUPPORT_DATA_0030, D3D12DDI_VIDEO_CRYPTO_SESSION_TRANSFORM_SUPPORT_DATA_0030
req.iface: 
---

# D3D12DDI_VIDEO_CRYPTO_SESSION_TRANSFORM_SUPPORT_DATA_0030 structure



## -description
<p>Video crypto session transform support data.</p>


## -syntax

````
typedef struct _D3D12DDI_VIDEO_CRYPTO_SESSION_TRANSFORM_SUPPORT_DATA_0030 {
  UINT                                                  NodeIndex;
  GUID                                                  DecodeProfile;
  GUID                                                  ContentProtectionSystem;
  D3D12DDI_CRYPTO_SESSION_FLAGS_0030                    Flags;
  D3D12DDI_BITSTREAM_ENCRYPTION_TYPE_0030               BitstreamEncryption;
  D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030      Operation;
  BOOL                                                  ProtectedOutputRequired;
  UINT64                                                InputAlignment;
  UINT64                                                InputPreambleSize;
  UINT64                                                OutputAlignment;
  UINT64                                                OutputPreambleSize;
  D3D12DDI_CRYPTO_SESSION_TRANSFORM_SUPPORT_FLAGS_0030  Support;
} D3D12DDI_VIDEO_CRYPTO_SESSION_TRANSFORM_SUPPORT_DATA_0030, D3D12DDI_VIDEO_CRYPTO_SESSION_TRANSFORM_SUPPORT_DATA_0030;
````


## -struct-fields
<dl>

### -field <b>NodeIndex</b>

<dd>
<p>Node index.</p>
</dd>

### -field <b>DecodeProfile</b>

<dd>
<p>Decode profile.</p>
</dd>

### -field <b>ContentProtectionSystem</b>

<dd>
<p>Content protection system.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Flags.</p>
</dd>

### -field <b>BitstreamEncryption</b>

<dd>
<p>Bitstream encryption.</p>
</dd>

### -field <b>Operation</b>

<dd>
<p>Operation.</p>
</dd>

### -field <b>ProtectedOutputRequired</b>

<dd>
<p>Protected output required.</p>
</dd>

### -field <b>InputAlignment</b>

<dd>
<p>Input alignment.</p>
</dd>

### -field <b>InputPreambleSize</b>

<dd>
<p>Input preamble size.</p>
</dd>

### -field <b>OutputAlignment</b>

<dd>
<p>Output alignment.</p>
</dd>

### -field <b>OutputPreambleSize</b>

<dd>
<p>Output preamble size.</p>
</dd>

### -field <b>Support</b>

<dd>
<p>Support.</p>
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