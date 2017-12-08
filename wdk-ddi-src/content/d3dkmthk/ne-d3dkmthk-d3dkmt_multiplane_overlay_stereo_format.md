---
UID: NE.d3dkmthk.D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT
title: D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmt_multiplane_overlay_stereo_format.htm
old-project: display
ms.assetid: dd26ac4b-ecef-4b4d-a050-d3e429ff0542
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT, D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT
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

# D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT enumeration



## -description
Reserved for system use. Do not use in your driver.


## -syntax

````
typedef enum D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT { 
  DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO                = 0,
  D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_HORIZONTAL          = 1,
  D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_VERTICAL            = 2,
  DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_SEPARATE            = 3,
  DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO_OFFSET         = 4,
  DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_ROW_INTERLEAVED     = 5,
  DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_COLUMN_INTERLEAVED  = 6,
  DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_CHECKERBOARD        = 7
} D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT;
````


## -enum-fields

### -field DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO


### -field D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_HORIZONTAL


### -field D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_VERTICAL


### -field DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_SEPARATE


### -field DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO_OFFSET


### -field DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_ROW_INTERLEAVED


### -field DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_COLUMN_INTERLEAVED


### -field DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_CHECKERBOARD


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
<dt>D3dkmthk.h</dt>
</dl>
</td>
</tr>
</table>