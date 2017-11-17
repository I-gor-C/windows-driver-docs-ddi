---
UID: NE.d3dkmthk._D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE
title: D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmt_outdupl_pointer_shape_type.htm
ms.assetid: 50a6cc24-2ac8-435c-8e82-9cd0c02f57e9
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE
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
ms.keywords: DXGKMDT_OPM_STANDARD_INFORMATION, DXGKMDT_OPM_STANDARD_INFORMATION
req.iface: 
---

# D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE enumeration



## -description
<p>Reserved for system use. Do not use in your driver.</p>


## -syntax

````
typedef enum _D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE { 
  D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE_MONOCHROME    = 0x00000001,
  D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE_COLOR         = 0x00000002,
  D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE_MASKED_COLOR  = 0x00000004
} D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE;
````


## -enum-fields
<dl>

### -field <a id="D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE_MONOCHROME"></a><a id="d3dkmt_outdupl_pointer_shape_type_monochrome"></a><b>D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE_MONOCHROME</b>

<dd></dd>

### -field <a id="D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE_COLOR"></a><a id="d3dkmt_outdupl_pointer_shape_type_color"></a><b>D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE_COLOR</b>

<dd></dd>

### -field <a id="D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE_MASKED_COLOR"></a><a id="d3dkmt_outdupl_pointer_shape_type_masked_color"></a><b>D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE_MASKED_COLOR</b>

<dd></dd>
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