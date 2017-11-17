---
UID: NS.d3dkmthk._D3DKMT_OUTDUPL_POINTER_SHAPE_INFO
title: D3DKMT_OUTDUPL_POINTER_SHAPE_INFO
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmt_outdupl_pointer_shape_info.htm
ms.assetid: fc72fe82-8807-44ac-b9da-8f84d38c45bf
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_OUTDUPL_POINTER_SHAPE_INFO
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
ms.keywords: D3DKMT_OUTDUPL_POINTER_SHAPE_INFO, D3DKMT_OUTDUPL_POINTER_SHAPE_INFO
req.iface: 
---

# D3DKMT_OUTDUPL_POINTER_SHAPE_INFO structure



## -description
<p>Reserved for system use. Do not use in your driver.</p>


## -syntax

````
typedef struct _D3DKMT_OUTDUPL_POINTER_SHAPE_INFO {
  D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE Type;
  UINT                              Width;
  UINT                              Height;
  UINT                              Pitch;
  POINT                             HotSpot;
} D3DKMT_OUTDUPL_POINTER_SHAPE_INFO;
````


## -struct-fields
<dl>

### -field <b>Type</b>

<dd></dd>

### -field <b>Width</b>

<dd></dd>

### -field <b>Height</b>

<dd></dd>

### -field <b>Pitch</b>

<dd></dd>

### -field <b>HotSpot</b>

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