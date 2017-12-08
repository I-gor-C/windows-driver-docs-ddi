---
UID: NS.d3dkmddi._DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES3
title: DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES3
author: windows-driver-content
description: A structure containing the attributes used for the image in a multiplane overlay.
old-location: display\dxgk_multiplane_overlay_attributes3.htm
old-project: display
ms.assetid: 0491AF42-53DF-4538-BE8A-AA5AA7B2C65E
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES3, DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES3
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES3
req.alt-loc: d3dkmddi.h
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

# DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES3 structure



## -description
<p>A structure containing the attributes used for the image in a multiplane overlay.</p>


## -syntax

````
typedef struct _DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES3 {
  DXGK_MULTIPLANE_OVERLAY_FLAGS                 Flags;
  RECT                                          SrcRect;
  RECT                                          DstRect;
  RECT                                          ClipRect;
  D3DDDI_ROTATION                               Rotation;
  DXGK_MULTIPLANE_OVERLAY_BLEND                 Blend;
  D3DDDI_COLOR_SPACE_TYPE                       ColorSpaceType;
  DXGK_MULTIPLANE_OVERLAY_STRETCH_QUALITY       StretchQuality;
} DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES3;
````


## -struct-fields
<dl>

### -field Flags

<dd>
<p>Specifies a combination of flip operations by Oring values in the DXGK_MULTIPLANE_OVERLAY_FLAGS enumeration.</p>
</dd>

### -field SrcRect

<dd>
<p>Specifies the source rectangle, of type RECT, relative to the source resource.</p>
</dd>

### -field DstRect

<dd>
<p>Specifies the destination rectangle, of type RECT, relative to the monitor resolution.</p>
</dd>

### -field ClipRect

<dd>
<p>Specifies additional clipping information, of type RECT, relative to the DstRect rectangle, after the data has been stretched according to the values of SrcRect and DstRect.</p>
<p>The driver and hardware can use the ClipRect member to apply a common stretch factor as the clipping changes when an app occludes part of the DstRect destination rectangle.</p>
</dd>

### -field Rotation

<dd>
<p>Specifies the clockwise rotation of the overlay plane, given as a value from the D3DDDI_ROTATION enumeration.</p>
</dd>

### -field Blend

<dd>
<p>Specifies the blend mode that applies to this overlay plane and the plane beneath it, given as a value from the DXGK_MULTIPLANE_OVERLAY_BLEND enumeration.</p>
</dd>

### -field ColorSpaceType

<dd>
<p>Specifies the colorspace configuration, given as a value from the D3DDDI_COLOR_SPACE_TYPE enumeration.</p>
</dd>

### -field StretchQuality

<dd>
<p>Specifies the overlay plane's stretch quality, given as a value from the DXGK_MULTIPLANE_OVERLAY_STRETCH_QUALITY enumeration.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h</dt>
</dl>
</td>
</tr>
</table>