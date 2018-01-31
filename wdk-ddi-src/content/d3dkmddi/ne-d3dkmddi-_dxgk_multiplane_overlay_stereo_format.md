---
UID : NE:d3dkmddi._DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT
title : "_DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT"
author : windows-driver-content
description : Identifies the overlay plane's stereo presentation format. Only the DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO value is supported.
old-location : display\dxgk_multiplane_overlay_stereo_format.htm
old-project : display
ms.assetid : ce9ad02d-645a-4333-9208-27f0805508a5
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : d3dkmddi/DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO_OFFSET, DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_SEPARATE, DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_HORIZONTAL, DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT, DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_ROW_INTERLEAVED, _DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT, DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_CHECKERBOARD, DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO, d3dkmddi/DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT, d3dkmddi/DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO, DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_VERTICAL, DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_COLUMN_INTERLEAVED, d3dkmddi/DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_COLUMN_INTERLEAVED, d3dkmddi/DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_SEPARATE, d3dkmddi/DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_VERTICAL, d3dkmddi/DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_CHECKERBOARD, display.dxgk_multiplane_overlay_stereo_format, DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO_OFFSET, d3dkmddi/DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_ROW_INTERLEAVED, DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT enumeration [Display Devices], d3dkmddi/DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_HORIZONTAL
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : d3dkmddi.h
req.include-header : D3dkmddi.h
req.target-type : Windows
req.target-min-winverclnt : Windows 8.1
req.target-min-winversvr : Windows Server 2012 R2
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT
---

# _DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT Enumeration
Identifies the overlay plane's stereo presentation format. Only the <b>DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO</b> value is supported.

## Syntax
````
typedef enum _DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT { 
  DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO                = 0,
  DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_HORIZONTAL          = 1,
  DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_VERTICAL            = 2,
  DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_SEPARATE            = 3,
  DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO_OFFSET         = 4,
  DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_ROW_INTERLEAVED     = 5,
  DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_COLUMN_INTERLEAVED  = 6,
  DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_CHECKERBOARD        = 7
} DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT;
````

## Constants

<table>

<tr>
<td>DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_CHECKERBOARD</td>
<td>Reserved for system use. Do not use in your driver.</td>
</tr>

<tr>
<td>DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_COLUMN_INTERLEAVED</td>
<td>Reserved for system use. Do not use in your driver.</td>
</tr>

<tr>
<td>DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_HORIZONTAL</td>
<td>Reserved for system use. Do not use in your driver.</td>
</tr>

<tr>
<td>DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO</td>
<td>The overplay plane data is presented in mono (non-stereo) format.</td>
</tr>

<tr>
<td>DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO_OFFSET</td>
<td>Reserved for system use. Do not use in your driver.</td>
</tr>

<tr>
<td>DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_ROW_INTERLEAVED</td>
<td>Reserved for system use. Do not use in your driver.</td>
</tr>

<tr>
<td>DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_SEPARATE</td>
<td>Reserved for system use. Do not use in your driver.</td>
</tr>

<tr>
<td>DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_VERTICAL</td>
<td>Reserved for system use. Do not use in your driver.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |