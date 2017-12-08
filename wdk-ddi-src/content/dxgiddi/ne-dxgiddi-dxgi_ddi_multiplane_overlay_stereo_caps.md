---
UID: NE.dxgiddi.DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS
title: DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS
author: windows-driver-content
description: Reserved for system use. Do not use it in your driver.
old-location: display\dxgi_ddi_multiplane_overlay_stereo_caps.htm
old-project: display
ms.assetid: 28017595-06d5-48ff-91d7-0e084d1e92de
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS, DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: dxgiddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS
req.alt-loc: Dxgiddi.h
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

# DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS enumeration



## -description
Reserved for system use. Do not use it in your driver.


## -syntax

````
typedef enum DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS { 
  DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS_SEPARATE            = 0x1,
  DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS_ROW_INTERLEAVED     = 0x4,
  DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS_COLUMN_INTERLEAVED  = 0x8,
  DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS_CHECKERBOARD        = 0x10,
  DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS_FLIP_MODE           = 0x20
} DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS;
````


## -enum-fields

### -field DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS_SEPARATE


### -field DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS_ROW_INTERLEAVED


### -field DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS_COLUMN_INTERLEAVED


### -field DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS_CHECKERBOARD


### -field DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS_FLIP_MODE


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
<dt>Dxgiddi.h</dt>
</dl>
</td>
</tr>
</table>