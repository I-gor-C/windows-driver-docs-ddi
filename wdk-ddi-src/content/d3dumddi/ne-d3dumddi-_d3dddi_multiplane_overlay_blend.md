---
UID: NE:d3dumddi._D3DDDI_MULTIPLANE_OVERLAY_BLEND
title: "_D3DDDI_MULTIPLANE_OVERLAY_BLEND"
author: windows-driver-content
description: Identifies a blend operation to be performed on an overlay plane.
old-location: display\d3dddi_multiplane_overlay_blend.htm
old-project: display
ms.assetid: 1ee411f2-1779-41bd-808c-40639bb22662
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDI_MULTIPLANE_OVERLAY_BLEND, D3DDDI_MULTIPLANE_OVERLAY_BLEND enumeration [Display Devices], D3DDDI_MULTIPLANE_OVERLAY_BLEND_ALPHABLEND, D3DDDI_MULTIPLANE_OVERLAY_BLEND_OPAQUE, _D3DDDI_MULTIPLANE_OVERLAY_BLEND, d3dumddi/D3DDDI_MULTIPLANE_OVERLAY_BLEND, d3dumddi/D3DDDI_MULTIPLANE_OVERLAY_BLEND_ALPHABLEND, d3dumddi/D3DDDI_MULTIPLANE_OVERLAY_BLEND_OPAQUE, display.d3dddi_multiplane_overlay_blend
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	D3dumddi.h
api_name:
-	D3DDDI_MULTIPLANE_OVERLAY_BLEND
product:
- Windows
targetos: Windows
req.typenames: D3DDDI_MULTIPLANE_OVERLAY_BLEND
---

# _D3DDDI_MULTIPLANE_OVERLAY_BLEND Enumeration
Identifies a blend operation to be performed on an overlay plane.

## Syntax
```
typedef enum _D3DDDI_MULTIPLANE_OVERLAY_BLEND {
  D3DDDI_MULTIPLANE_OVERLAY_BLEND_OPAQUE      ,
  D3DDDI_MULTIPLANE_OVERLAY_BLEND_ALPHABLEND
} D3DDDI_MULTIPLANE_OVERLAY_BLEND;
```

## Constants

<table>
            
                <tr>
                    <td>D3DDDI_MULTIPLANE_OVERLAY_BLEND_OPAQUE</td>
                    <td>The overlay plane should ignore data in the alpha channel and make the blended plane entirely opaque.</td>
                </tr>
            
                <tr>
                    <td>D3DDDI_MULTIPLANE_OVERLAY_BLEND_ALPHABLEND</td>
                    <td>The overlay plane should use the pre-multiplied alpha channel in this plane to blend it with the plane beneath.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8.1 Windows 8.1 |
| **Header** | d3dumddi.h (include D3dumddi.h) |