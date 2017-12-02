---
UID: NS.d3dkmddi._DXGK_MULTIPLANEOVERLAYCAPS
title: DXGK_MULTIPLANEOVERLAYCAPS
author: windows-driver-content
description: Multiplane overlay capabilities returned by the DxgkDdiGetMultiPlaneOverlayCaps function.
old-location: display\dxgk_multiplaneoverlaycaps.htm
old-project: display
ms.assetid: E3F590EA-2B3B-464B-9D72-708B24CA3052
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MULTIPLANEOVERLAYCAPS, DXGK_MULTIPLANEOVERLAYCAPS
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
req.alt-api: DXGK_MULTIPLANEOVERLAYCAPS
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

# DXGK_MULTIPLANEOVERLAYCAPS structure



## -description
<p>Multiplane overlay capabilities returned by the DxgkDdiGetMultiPlaneOverlayCaps function.</p>


## -syntax

````
typedef struct _DXGK_MULTIPLANEOVERLAYCAPS {
  union {
    struct {
      UINT Rotation  :1;
      UINT RotationWithoutIndependentFlip  :1;
      UINT VerticalFlip  :1;
      UINT HorizontalFlip  :1;
      UINT StretchRGB  :1;
      UINT StretchYUV  :1;
      UINT BilinearFilter  :1;
      UINT HighFilter  :1;
      UINT Shared  :1;
      UINT Immediate  :1;
      UINT Plane0ForVirtualModeOnly  :1;
      UINT Reserved  :21;
    };
    UINT Value;
  };
} DXGK_MULTIPLANEOVERLAYCAPS;
````


## -struct-fields
<dl>

### -field Rotation

<dd>
<p>When TRUE, indicates that the hardware supports rotating the plane 90, 180, or 270 degrees. 

If TRUE, RotationWithoutIndependentFlip should be FALSE.
</p>
</dd>

### -field RotationWithoutIndependentFlip

<dd>
<p>When TRUE, indicates that the driver can perform plane rotation of 90, 180, or 270 degrees, but IndependentFlip cannot be used when rotating the plane.

If TRUE, Rotation should be FALSE.
</p>
</dd>

### -field VerticalFlip

<dd>
<p>When TRUE, the hardware supports flipping the plane vertically.</p>
</dd>

### -field HorizontalFlip

<dd>
<p>When TRUE, the hardware supports flipping the plane horizontally.</p>
</dd>

### -field StretchRGB

<dd>
<p>When TRUE, the hardware supports stretching any plane containing RGB data.</p>
</dd>

### -field StretchYUV

<dd>
<p>When TRUE, the hardware supports stretching any plane containing YUV data.</p>
</dd>

### -field BilinearFilter

<dd>
<p>When TRUE, the hardware supports bilinear filtering.</p>
</dd>

### -field HighFilter

<dd>
<p>When TRUE, the hardware supports better than bilinear filtering.</p>
</dd>

### -field Shared

<dd>
<p>When TRUE, the multiplane overlay resources reported by the capabilities are shared across all VidPn sources.</p>
<p>When FALSE, the multiplane overlay resources reported by capabilities are dedicated to the specific VidPn source.</p>
</dd>

### -field Immediate

<dd>
<p>When TRUE, the HW supports immediate flips of the MPO plane.</p>
<p>If the flip contains changes that cannot be performed as an immediate flip, the driver can promote the flip to a VSYNC flip using the new HSync completion infrastructure.</p>
</dd>

### -field Plane0ForVirtualModeOnly

<dd>
<p>When TRUE, the hardware will always apply the stretch factor of plane 0 to the hardware cursor as well as the plane. This implies that stretching/shrinking of plane 0 should only occur when plane 0 is the desktop plane and when the stretching/shrinking is used for virtual mode support.

</p>
</dd>

### -field Reserved

<dd>
<p>This member is reserved and should be set to zero. Setting this member to zero is equivalent to setting the remaining 21 bits (0xFFFFFFFC) of the 32-bit <b>Value</b> member to zeros.</p>
</dd>

### -field Value

<dd></dd>
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