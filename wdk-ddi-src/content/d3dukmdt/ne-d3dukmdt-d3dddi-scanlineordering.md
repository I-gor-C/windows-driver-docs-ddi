---
UID: NE.d3dukmdt.D3DDDI_SCANLINEORDERING
title: D3DDDI_SCANLINEORDERING
author: windows-driver-content
description: The D3DDDI_SCANLINEORDERING enumeration type contains values that identify how the scan lines are drawn on a surface.
old-location: display\d3dddi_scanlineordering.htm
ms.assetid: 6b7b0bbf-79f2-4b0c-a7e6-75dc92bf8a63
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dukmdt.h
req.include-header: D3dumddi.h, D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: D3DDDI_SCANLINEORDERING is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_SCANLINEORDERING
req.alt-loc: d3dukmdt.h
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
ms.keywords: D3DKMT_PRESENT_MULTIPLANE_OVERLAY, D3DKMT_PRESENT_MULTIPLANE_OVERLAY
req.iface: 
---

# D3DDDI_SCANLINEORDERING enumeration



## -description
<p>The D3DDDI_SCANLINEORDERING enumeration type contains values that identify how the scan lines are drawn on a surface. </p>


## -syntax

````
typedef enum D3DDDI_SCANLINEORDERING { 
  D3DDDI_SCANLINEORDERING_UNKNOWN      = 0,
  D3DDDI_SCANLINEORDERING_PROGRESSIVE  = 1,
  D3DDDI_SCANLINEORDERING_INTERLACED   = 2
} D3DDDI_SCANLINEORDERING;
````


## -enum-fields
<dl>

### -field <a id="D3DDDI_SCANLINEORDERING_UNKNOWN"></a><a id="d3dddi_scanlineordering_unknown"></a><b>D3DDDI_SCANLINEORDERING_UNKNOWN</b>

<dd>
<p>The value indicates that scan-line ordering is unknown. </p>
</dd>

### -field <a id="D3DDDI_SCANLINEORDERING_PROGRESSIVE"></a><a id="d3dddi_scanlineordering_progressive"></a><b>D3DDDI_SCANLINEORDERING_PROGRESSIVE</b>

<dd>
<p>The value indicates that scan-line ordering is progressive. </p>
</dd>

### -field <a id="D3DDDI_SCANLINEORDERING_INTERLACED"></a><a id="d3dddi_scanlineordering_interlaced"></a><b>D3DDDI_SCANLINEORDERING_INTERLACED</b>

<dd>
<p>The value indicates that scan-line ordering is interlaced. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>D3DDDI_SCANLINEORDERING is supported beginning with the Windows 7 operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dukmdt.h (include D3dumddi.h or D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>