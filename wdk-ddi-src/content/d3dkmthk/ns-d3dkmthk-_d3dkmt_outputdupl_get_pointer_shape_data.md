---
UID: NS.D3DKMTHK._D3DKMT_OUTPUTDUPL_GET_POINTER_SHAPE_DATA
title: _D3DKMT_OUTPUTDUPL_GET_POINTER_SHAPE_DATA
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmt_outputdupl_get_pointer_shape_data.htm
old-project: display
ms.assetid: 31502888-88b0-49c2-8f03-63bb31886931
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _D3DKMT_OUTPUTDUPL_GET_POINTER_SHAPE_DATA, D3DKMT_OUTPUTDUPL_GET_POINTER_SHAPE_DATA
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
---

# _D3DKMT_OUTPUTDUPL_GET_POINTER_SHAPE_DATA structure



## -description
Reserved for system use. Do not use in your driver.


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

### -field hAdapter


### -field VidPnSourceId


### -field BufferSizeSupplied


### -field pShapeBuffer


### -field BufferSizeRequired


### -field ShapeInfo


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
Windows 8
</td>
</tr>
<tr>
<th width="30%">
Minimum supported server
</th>
<td width="70%">
Windows Server 2012
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>