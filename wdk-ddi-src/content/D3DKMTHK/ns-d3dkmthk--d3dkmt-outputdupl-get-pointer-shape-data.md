---
UID: NS.d3dkmthk._D3DKMT_OUTPUTDUPL_GET_POINTER_SHAPE_DATA
title: D3DKMT_OUTPUTDUPL_GET_POINTER_SHAPE_DATA
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmt_outputdupl_get_pointer_shape_data.htm
ms.assetid: 31502888-88b0-49c2-8f03-63bb31886931
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
req.alt-api: D3DKMT_OUTPUTDUPL_GET_POINTER_SHAPE_DATA
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
ms.keywords: D3DKMT_OUTPUTDUPL_GET_POINTER_SHAPE_DATA, D3DKMT_OUTPUTDUPL_GET_POINTER_SHAPE_DATA
req.iface: 
---

# D3DKMT_OUTPUTDUPL_GET_POINTER_SHAPE_DATA structure



## -description
<p>Reserved for system use. Do not use in your driver.</p>


## -syntax

````
typedef struct _D3DKMT_OUTPUTDUPL_GET_POINTER_SHAPE_DATA {
  D3DKMT_HANDLE                     hAdapter;
  D3DDDI_VIDEO_PRESENT_SOURCE_ID    VidPnSourceId;
  UINT                              BufferSizeSupplied;
  PVOID                             pShapeBuffer;
  UINT                              BufferSizeRequired;
  D3DKMT_OUTDUPL_POINTER_SHAPE_INFO ShapeInfo;
} D3DKMT_OUTPUTDUPL_GET_POINTER_SHAPE_DATA;
````


## -struct-fields
<dl>

### -field <b>hAdapter</b>

<dd></dd>

### -field <b>VidPnSourceId</b>

<dd></dd>

### -field <b>BufferSizeSupplied</b>

<dd></dd>

### -field <b>pShapeBuffer</b>

<dd></dd>

### -field <b>BufferSizeRequired</b>

<dd></dd>

### -field <b>ShapeInfo</b>

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