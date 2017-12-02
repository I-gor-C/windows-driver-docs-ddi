---
UID: NE.d3dkmdt._D3DKMDT_COLOR_BASIS
title: D3DKMDT_COLOR_BASIS
author: windows-driver-content
description: The D3DKMDT_COLOR_BASIS enumeration contains constants that indicate the color basis used to encode the content of a video present source or the signal on a video present target.
old-location: display\d3dkmdt_color_basis.htm
old-project: display
ms.assetid: c2a8973d-bdab-44a6-b88b-482355ada1e5
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO, DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMDT_COLOR_BASIS
req.alt-loc: d3dkmdt.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# D3DKMDT_COLOR_BASIS enumeration



## -description
<p>The D3DKMDT_COLOR_BASIS enumeration contains constants that indicate the color basis used to encode the content of a video present source or the signal on a video present target.</p>


## -syntax

````
typedef enum _D3DKMDT_COLOR_BASIS { 
  D3DKMDT_CB_UNINITIALIZED  = 0,
  D3DKMDT_CB_INTENSITY      = 1,
  D3DKMDT_CB_SRGB           = 2,
  D3DKMDT_CB_SCRGB          = 3,
  D3DKMDT_CB_YCBCR          = 4,
  D3DKMDT_CB_YPBPR          = 5
} D3DKMDT_COLOR_BASIS;
````


## -enum-fields
<dl>

### -field D3DKMDT_CB_UNINITIALIZED

<dd>
<p>Indicates that a variable of type D3DKMDT_COLOR_BASIS has not yet been assigned a meaningful value.</p>
</dd>

### -field D3DKMDT_CB_INTENSITY

<dd>
<p>Indicates an encoding scheme that relies only on intensity. This basis is used for monochrome images.</p>
</dd>

### -field D3DKMDT_CB_SRGB

<dd>
<p>Indicates the SRGB color basis.</p>
</dd>

### -field D3DKMDT_CB_SCRGB

<dd>
<p>Indicates the SCRGB color basis.</p>
</dd>

### -field D3DKMDT_CB_YCBCR

<dd>
<p>Indicates the YCBCR color basis.</p>
</dd>

### -field D3DKMDT_CB_YPBPR

<dd>
<p>Indicates the YPBPR color basis.</p>
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
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmdt.h (include D3dkmdt.h)</dt>
</dl>
</td>
</tr>
</table>