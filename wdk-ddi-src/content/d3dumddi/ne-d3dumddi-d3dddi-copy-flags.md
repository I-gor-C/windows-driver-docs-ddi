---
UID: NE.d3dumddi.D3DDDI_COPY_FLAGS
title: D3DDDI_COPY_FLAGS
author: windows-driver-content
description: Specifies how to handle the existing contents of a resource during a copy or update operation of a region within that resource.
old-location: display\d3dddi_copy_flags.htm
old-project: display
ms.assetid: 6186dac4-4797-48f2-bb32-40a0d501bac7
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_COPY_FLAGS
req.alt-loc: D3dumddi.h
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

# D3DDDI_COPY_FLAGS enumeration



## -description
<p>Specifies how to handle the existing contents of a resource during a copy or update operation of a region within that resource.</p>


## -syntax

````
typedef enum D3DDDI_COPY_FLAGS { 
  D3DDDI_COPY_NO_OVERWRITE  = 0x00000001,
  D3DDDI_COPY_DISCARD       = 0x00000002
} D3DDDI_COPY_FLAGS;
````


## -enum-fields
<dl>

### -field <a id="D3DDDI_COPY_NO_OVERWRITE"></a><a id="d3dddi_copy_no_overwrite"></a><b>D3DDDI_COPY_NO_OVERWRITE</b>

<dd>
<p>The caller guarantees that the portion of the surface that is being written to with new data is not currently being referenced or accessed by any previous render operation. The driver can take advantage of this capability to optimize performance and memory usage.</p>
</dd>

### -field <a id="D3DDDI_COPY_DISCARD"></a><a id="d3dddi_copy_discard"></a><b>D3DDDI_COPY_DISCARD</b>

<dd>
<p>The user-mode display driver can discard previous contents of the entire resource. The driver can take advantage of this capability to optimize performance and memory usage.</p>
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
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>