---
UID: NE.d3d10umddi.D3D11_1_DDI_COPY_FLAGS
title: D3D11_1_DDI_COPY_FLAGS
author: windows-driver-content
description: Specifies how to handle the existing contents of a resource during a copy or update operation of a region within that resource. Used by Windows Display Driver Model (WDDM) 1.2 and later user-mode display drivers.
old-location: display\d3d11_1_ddi_copy_flags.htm
old-project: display
ms.assetid: 044dc1cd-426e-4f6c-b14d-8c366834b5ac
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11_1_DDI_COPY_FLAGS
req.alt-loc: D3d10umddi.h
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

# D3D11_1_DDI_COPY_FLAGS enumeration



## -description
<p>Specifies how to handle the existing contents of a resource during a copy or update operation of a region within that resource. Used by Windows Display Driver Model (WDDM) 1.2 and later user-mode display drivers.</p>


## -syntax

````
typedef enum D3D11_1_DDI_COPY_FLAGS { 
  D3D11_1DDI_COPY_NO_OVERWRITE  = 0x00000001,
  D3D11_1DDI_COPY_DISCARD       = 0x00000002,
  D3D11_1DDI_COPY_TILEABLE      = 0x00000004
} D3D11_1_DDI_COPY_FLAGS;
````


## -enum-fields
<dl>

### -field <a id="D3D11_1DDI_COPY_NO_OVERWRITE"></a><a id="d3d11_1ddi_copy_no_overwrite"></a><b>D3D11_1DDI_COPY_NO_OVERWRITE</b>

<dd>
<p>The caller guarantees that the portion of the surface that is being written to with new data is not currently being referenced or accessed by any previous render operation. The driver can take advantage of this capability to optimize performance and memory usage.</p>
</dd>

### -field <a id="D3D11_1DDI_COPY_DISCARD"></a><a id="d3d11_1ddi_copy_discard"></a><b>D3D11_1DDI_COPY_DISCARD</b>

<dd>
<p>The user-mode display driver can discard previous contents of the entire resource. The driver can take advantage of this capability to optimize performance and memory usage.</p>
</dd>

### -field <a id="D3D11_1DDI_COPY_TILEABLE"></a><a id="d3d11_1ddi_copy_tileable"></a><b>D3D11_1DDI_COPY_TILEABLE</b>

<dd>
<p>For tile-based deferred rendering, a copy operation can operate on only the currently processed tile in the source or destination resource, and the scene does not have to be flushed in all tiles.</p>
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
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>