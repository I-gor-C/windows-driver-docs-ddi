---
UID: NS.d3dkmthk.D3DKMT_MULTIPLANE_OVERLAY_ATTRIBUTES
title: D3DKMT_MULTIPLANE_OVERLAY_ATTRIBUTES
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmt_multiplane_overlay_attributes.htm
ms.assetid: 07abf207-62ab-42d1-84b0-74815d1d42b8
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_MULTIPLANE_OVERLAY_ATTRIBUTES
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
ms.keywords: D3DKMT_MULTIPLANE_OVERLAY_ATTRIBUTES, D3DKMT_MULTIPLANE_OVERLAY_ATTRIBUTES
req.iface: 
---

# D3DKMT_MULTIPLANE_OVERLAY_ATTRIBUTES structure



## -description
<p>Reserved for system use. Do not use in your driver.</p>


## -syntax

````
typedef struct D3DKMT_MULTIPLANE_OVERLAY_ATTRIBUTES {
  UINT                                         Flags;
  RECT                                         SrcRect;
  RECT                                         DstRect;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM1_3)
  RECT                                         ClipRect;
#endif 
  D3DDDI_ROTATION                              Rotation;
  D3DKMT_MULTIPLANE_OVERLAY_BLEND              Blend;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM1_3)
  UINT                                         DirtyRectCount;
  RECT                                         pDirtyRects;
#else 
  UINT                                         NumFilters;
  void                                         *pFilters;
#endif 
  D3DKMT_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT VideoFrameFormat;
  UINT                                         YCbCrFlags;
  D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT      StereoFormat;
  BOOL                                         StereoLeftViewFrame0;
  BOOL                                         StereoBaseViewFrame0;
  DXGKMT_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE   StereoFlipMode;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM1_3)
  DXGKMT_MULTIPLANE_OVERLAY_STRETCH_QUALITY    StretchQuality;
#endif 
} D3DKMT_MULTIPLANE_OVERLAY_ATTRIBUTES;
````


## -struct-fields
<dl>

### -field <b>Flags</b>

<dd></dd>

### -field <b>SrcRect</b>

<dd></dd>

### -field <b>DstRect</b>

<dd></dd>

### -field <b>ClipRect</b>

<dd></dd>

### -field <b>Rotation</b>

<dd></dd>

### -field <b>Blend</b>

<dd></dd>

### -field <b>DirtyRectCount</b>

<dd></dd>

### -field <b>pDirtyRects</b>

<dd></dd>

### -field <b>NumFilters</b>

<dd></dd>

### -field <b>pFilters</b>

<dd></dd>

### -field <b>VideoFrameFormat</b>

<dd></dd>

### -field <b>YCbCrFlags</b>

<dd></dd>

### -field <b>StereoFormat</b>

<dd></dd>

### -field <b>StereoLeftViewFrame0</b>

<dd></dd>

### -field <b>StereoBaseViewFrame0</b>

<dd></dd>

### -field <b>StereoFlipMode</b>

<dd></dd>

### -field <b>StretchQuality</b>

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
<dt>D3dkmthk.h</dt>
</dl>
</td>
</tr>
</table>