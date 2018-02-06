---
UID: NE:dxgiddi.DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS
title: DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS
author: windows-driver-content
description: Identifies overlay capabilities.
old-location: display\dxgi_ddi_multiplane_overlay_feature_caps.htm
old-project: display
ms.assetid: f64b3470-b4ae-4d3a-87ac-249429f17dfe
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_STEREO, DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_VERTICAL_FLIP, DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_DEINTERLACE, dxgiddi/DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS, DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_ROTATION, dxgiddi/DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_DEINTERLACE, dxgiddi/DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_STEREO, DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS, display.dxgi_ddi_multiplane_overlay_feature_caps, dxgiddi/DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_HORIZONTAL_FLIP, dxgiddi/DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_VERTICAL_FLIP, DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_HORIZONTAL_FLIP, DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS enumeration [Display Devices], dxgiddi/DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_ROTATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: dxgiddi.h
req.include-header: D3d10umddi.h
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	Dxgiddi.h
apiname:
-	DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS
product: Windows
targetos: Windows
req.typenames: DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS
---

# DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS Enumeration
Identifies overlay capabilities.

## Syntax
````
typedef enum DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS { 
  DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_ROTATION         = 0x1,
  DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_VERTICAL_FLIP    = 0x2,
  DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_HORIZONTAL_FLIP  = 0x4,
  DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_DEINTERLACE      = 0x8,
  DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_STEREO           = 0x10
} DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS;
````

## Constants

<table>
            
                <tr>
                    <td>DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_BILINEAR_FILTER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_DEINTERLACE</td>
                    <td>Reserved for system use. The user-mode display driver should not use this value.</td>
                </tr>
            
                <tr>
                    <td>DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_FULLSCREEN_POST_COMPOSITION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_HIGH_FILTER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_HORIZONTAL_FLIP</td>
                    <td>The overlay plane can flip the data horizontally, making it appear as a right-to-left mirror image.</td>
                </tr>
            
                <tr>
                    <td>DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_IMMEDIATE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_PLANE0_FOR_VIRTUAL_MODE_ONLY</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_RGB</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_ROTATION</td>
                    <td>The overlay plane can rotate the data 90, 180, and 270 degrees.</td>
                </tr>
            
                <tr>
                    <td>DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_ROTATION_WITHOUT_INDEPENDENT_FLIP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_SHARED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_STEREO</td>
                    <td>Reserved for system use. The user-mode display driver should not use this value.</td>
                </tr>
            
                <tr>
                    <td>DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_VERTICAL_FLIP</td>
                    <td>The overlay plane can flip the data vertically, making it appear upside-down.</td>
                </tr>
            
                <tr>
                    <td>DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS_YUV</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_RESERVED1</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8.1 Windows 8.1 |
| **Header** | dxgiddi.h (include D3d10umddi.h) |