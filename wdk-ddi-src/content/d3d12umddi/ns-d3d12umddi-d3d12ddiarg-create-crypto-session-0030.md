---
UID: NS.d3d12umddi.D3D12DDIARG_CREATE_CRYPTO_SESSION_0030
title: D3D12DDIARG_CREATE_CRYPTO_SESSION_0030
author: windows-driver-content
description: Creates a crypto session.
old-location: display\d3d12ddiarg-create-crypto-session-0030.htm
old-project: display
ms.assetid: 71d65f25-ef9c-4a3d-ad1d-1d55e73bc0cb
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D12DDIARG_CREATE_CRYPTO_SESSION_0030, D3D12DDIARG_CREATE_CRYPTO_SESSION_0030
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d12umddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDIARG_CREATE_CRYPTO_SESSION_0030
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

# D3D12DDIARG_CREATE_CRYPTO_SESSION_0030 structure



## -description
<p>Creates a crypto session.</p>


## -syntax

````
typedef struct _D3D12DDIARG_CREATE_CRYPTO_SESSION_0030 {
  UINT                                     NodeMask;
  GUID                                     DecodeProfile;
  GUID                                     ContentProtectionSystem;
  D3D12DDI_BITSTREAM_ENCRYPTION_TYPE_0030  BitstreamEncryption;
  D3D12DDI_CRYPTO_SESSION_FLAGS_0030       Flags;
} D3D12DDIARG_CREATE_CRYPTO_SESSION_0030, D3D12DDIARG_CREATE_CRYPTO_SESSION_0030;
````


## -struct-fields
<dl>

### -field NodeMask

<dd>
<p>Represents the set of nodes.</p>
</dd>

### -field DecodeProfile

<dd>
<p>The decode profile.</p>
</dd>

### -field ContentProtectionSystem

<dd>
<p>The content protection system.</p>
</dd>

### -field BitstreamEncryption

<dd>
<p>The bitstream encryption.</p>
</dd>

### -field Flags

<dd>
<p>The crypto session flags.</p>
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