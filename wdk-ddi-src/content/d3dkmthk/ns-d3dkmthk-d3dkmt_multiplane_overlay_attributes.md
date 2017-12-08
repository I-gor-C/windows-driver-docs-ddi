---
UID: NS.D3DKMTHK.D3DKMT_MULTIPLANE_OVERLAY_ATTRIBUTES
title: D3DKMT_MULTIPLANE_OVERLAY_ATTRIBUTES
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmt_multiplane_overlay_attributes.htm
old-project: display
ms.assetid: 07abf207-62ab-42d1-84b0-74815d1d42b8
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: D3DKMT_MULTIPLANE_OVERLAY_ATTRIBUTES, D3DKMT_MULTIPLANE_OVERLAY_ATTRIBUTES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
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
---

# D3DKMT_MULTIPLANE_OVERLAY_ATTRIBUTES structure



## -description
Reserved for system use. Do not use in your driver.


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

### -field Flags


### -field SrcRect


### -field DstRect


### -field ClipRect


### -field Rotation


### -field Blend


### -field DirtyRectCount


### -field pDirtyRects


### -field NumFilters


### -field pFilters


### -field VideoFrameFormat


### -field YCbCrFlags


### -field StereoFormat


### -field StereoLeftViewFrame0


### -field StereoBaseViewFrame0


### -field StereoFlipMode


### -field StretchQuality


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