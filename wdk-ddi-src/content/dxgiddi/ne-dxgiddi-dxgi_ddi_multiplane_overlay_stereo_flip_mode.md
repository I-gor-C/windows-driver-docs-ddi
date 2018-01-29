---
UID : NE:dxgiddi.DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE
title : DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE
author : windows-driver-content
description : Identifies the overlay plane's stereo flip mode. Only the DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_NONE value is supported.
old-location : display\dxgi_ddi_multiplane_overlay_stereo_flip_mode.htm
old-project : display
ms.assetid : f44317c5-661c-42f6-847b-b325e4c1321a
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_NONE, DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE enumeration [Display Devices], dxgiddi/DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE, dxgiddi/DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_FRAME0, DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_FRAME1, DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE, display.dxgi_ddi_multiplane_overlay_stereo_flip_mode, dxgiddi/DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_NONE, DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_FRAME0, dxgiddi/DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_FRAME1
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : dxgiddi.h
req.include-header : D3d10umddi.h
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
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE
---

# DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE Enumeration
Identifies the overlay plane's stereo flip mode. Only the <b>DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_NONE</b> value is supported.

## Syntax
````
typedef enum DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE { 
  DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_NONE    = 0,
  DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_FRAME0  = 1,
  DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_FRAME1  = 2
} DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE;
````

## Constants

<table>

<tr>
<td>DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_FRAME0</td>
<td>Reserved for system use. Do not use in your driver.</td>
</tr>

<tr>
<td>DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_FRAME1</td>
<td>Reserved for system use. Do not use in your driver.</td>
</tr>

<tr>
<td>DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_NONE</td>
<td>The overplay plane data is not presented in stereo mode.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | dxgiddi.h (include D3d10umddi.h) |