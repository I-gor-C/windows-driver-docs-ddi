---
UID: NS.d3dkmddi._DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION_FLAGS
title: DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION_FLAGS
author: windows-driver-content
description: A structure containing the flags describing the transformations applied to an image.
old-location: display\dxgk_multiplane_overlay_post_composition_flags.htm
ms.assetid: F7791AB9-6D20-4560-A478-E30F08C6AC3A
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION_FLAGS
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
ms.keywords: DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION_FLAGS, DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION_FLAGS
req.iface: 
---

# DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION_FLAGS structure



## -description
<p>A structure containing the flags describing the transformations applied to an image.</p>


## -syntax

````
typedef struct _DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION_FLAGS {
  union {
    struct {
      UINT VerticalFlip  :1;
      UINT HorizontalFlip  :1;
      UINT Reserved  :30;
    };
    UINT Value;
  };
} DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION_FLAGS;
````


## -struct-fields
<dl>

### -field <b>VerticalFlip</b>

<dd>
<p>Indicates that the image should be flipped vertically.</p>
</dd>

### -field <b>HorizontalFlip</b>

<dd>
<p>Indicates that the image should be flipped horizontally.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved and should be set to zero. Setting this member to zero is equivalent to setting the remaining 30 bits (0xFFFFFFFC) of the 32-bit <b>Value</b> member to zeros.</p>
</dd>

### -field <b>Value</b>

<dd></dd>
</dl>

## -remarks
<p>Applying VerticalFlip and HorizontalFlip simultaneously results in 180 degree rotation.</p>

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