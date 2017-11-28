---
UID: NS.d3dkmddi._DXGKARG_GETMULTIPLANEOVERLAYCAPS
title: DXGKARG_GETMULTIPLANEOVERLAYCAPS
author: windows-driver-content
description: Arguments to the DxgkDdiGetMultiPlaneOverlayCaps function.
old-location: display\dxgkarg_getmultiplaneoverlaycaps.htm
old-project: display
ms.assetid: 4792107C-BAAA-48B5-AC9A-829C05795303
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKARG_GETMULTIPLANEOVERLAYCAPS, DXGKARG_GETMULTIPLANEOVERLAYCAPS
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
req.alt-api: DXGKARG_GETMULTIPLANEOVERLAYCAPS
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

# DXGKARG_GETMULTIPLANEOVERLAYCAPS structure



## -description
<p>Arguments to the DxgkDdiGetMultiPlaneOverlayCaps function.</p>


## -syntax

````
typedef struct _DXGKARG_GETMULTIPLANEOVERLAYCAPS {
  D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId;
  UINT                           MaxPlane;
  UINT                           MaxRGBPlanes;
  UINT                           MaxYUVPlanes;
  DXGK_MULTIPLANEOVERLAYCAPS     OverlayCaps;
  float                          MaxStretchFactor;
  float                          MaxShrinkFactor;
} DXGKARG_GETMULTIPLANEOVERLAYCAPS;
````


## -struct-fields
<dl>

### -field <b>VidPnSourceId</b>

<dd>
<p>[in] Indicates the VidPn source for which we are querying multiplane overlay capabilities.</p>
</dd>

### -field <b>MaxPlane</b>

<dd>
<p>[out] Indicates the total number of planes, including the DWM's primary, that can be supported simultaneously.</p>
</dd>

### -field <b>MaxRGBPlanes</b>

<dd>
<p>[out] Indicates the total number of RGB planes, including the DWM’s primary, that can be supported simultaneously.</p>
</dd>

### -field <b>MaxYUVPlanes</b>

<dd>
<p>[out] Indicates the total number of YUV planes that can be supported simultaneously.</p>
</dd>

### -field <b>OverlayCaps</b>

<dd>
<p>[out] A DXGK_MULTIPLANEOVERLAYCAPS structure indicating the plane capabilities.</p>
</dd>

### -field <b>MaxStretchFactor</b>

<dd>
<p>[out] Indicates the maximum stretch factor that can be applied to a plane.</p>
</dd>

### -field <b>MaxShrinkFactor</b>

<dd>
<p>[out] Indicates the maximum shrink factor that can be applied to a plane.</p>
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