---
UID: NS.d3dkmthk._D3DKMT_ADAPTERTYPE
title: D3DKMT_ADAPTERTYPE
author: windows-driver-content
description: Specifies the type of display device that the graphics adapter supports.
old-location: display\d3dkmt_adaptertype.htm
old-project: display
ms.assetid: a92865bc-620f-434d-a185-b837924599fc
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_ADAPTERTYPE, D3DKMT_ADAPTERTYPE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_ADAPTERTYPE
req.alt-loc: D3dkmthk.h
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

# D3DKMT_ADAPTERTYPE structure



## -description
<p>Specifies the type of display device that the graphics adapter supports.</p>


## -syntax

````
typedef struct _D3DKMT_ADAPTERTYPE {
  UINT RenderSupported  :1;
  UINT DisplaySupported  :1;
  UINT SoftwareDevice  :1;
  UINT PostDevice  :1;
  UINT Reserved  :28;
} D3DKMT_ADAPTERTYPE;
````


## -struct-fields
<dl>

### -field RenderSupported

<dd>
<p>The adapter supports a render device.</p>
</dd>

### -field DisplaySupported

<dd>
<p>The adapter supports a display device.</p>
</dd>

### -field SoftwareDevice

<dd>
<p>The adapter supports a non-plug and play (PnP) device that is implemented in software.</p>
</dd>

### -field PostDevice

<dd>
<p>The adapter supports a power-on self-test (POST) device.</p>
</dd>

### -field Reserved

<dd>
<p>Reserved for system use.</p>
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
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>