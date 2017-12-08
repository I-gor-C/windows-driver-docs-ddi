---
UID: NE.d3dkmthk._D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE
title: _D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmt_outdupl_pointer_shape_type.htm
old-project: display
ms.assetid: 50a6cc24-2ac8-435c-8e82-9cd0c02f57e9
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE, D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
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
---

# _D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE enumeration



## -description
Reserved for system use. Do not use in your driver.


## -syntax

````
typedef enum _D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE { 
  D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE_MONOCHROME    = 0x00000001,
  D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE_COLOR         = 0x00000002,
  D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE_MASKED_COLOR  = 0x00000004
} D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE;
````


## -enum-fields

### -field D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE_MONOCHROME


### -field D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE_COLOR


### -field D3DKMT_OUTDUPL_POINTER_SHAPE_TYPE_MASKED_COLOR


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