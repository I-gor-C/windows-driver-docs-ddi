---
UID: NE:d3dkmddi._DXGK_DISPLAYPANELORIENTATION
title: "_DXGK_DISPLAYPANELORIENTATION"
author: windows-driver-content
description: Enum used to express the orientation of an integrated panel.
old-location: display\dxgk_displaypanelorientation.htm
old-project: display
ms.assetid: 49758A57-EFCE-4E9C-9BF6-74F6EFD356D9
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DXGK_DISPLAYPANELORIENTATION, DXGK_DISPLAYPANELORIENTATION enumeration [Display Devices], DXGK_DPO_0, DXGK_DPO_180, DXGK_DPO_270, DXGK_DPO_90, _DXGK_DISPLAYPANELORIENTATION, d3dkmddi/DXGK_DISPLAYPANELORIENTATION, d3dkmddi/DXGK_DPO_0, d3dkmddi/DXGK_DPO_180, d3dkmddi/DXGK_DPO_270, d3dkmddi/DXGK_DPO_90, display.dxgk_displaypanelorientation
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dkmddi.h
api_name:
-	DXGK_DISPLAYPANELORIENTATION
product: Windows
targetos: Windows
req.typenames: DXGK_DISPLAYPANELORIENTATION
---

# _DXGK_DISPLAYPANELORIENTATION Enumeration
Enum used to express the orientation of an integrated panel.

## Syntax
````
typedef enum _DXGK_DISPLAYPANELORIENTATION { 
  DXGK_DPO_0    = 0,
  DXGK_DPO_90   = 1,
  DXGK_DPO_180  = 2,
  DXGK_DPO_270  = 3
} DXGK_DISPLAYPANELORIENTATION;
````

## Constants

<table>
            
                <tr>
                    <td>DXGK_DPO_0</td>
                    <td>Indicates a 0 degree rotation.</td>
                </tr>
            
                <tr>
                    <td>DXGK_DPO_180</td>
                    <td>Indicates a 180 degree rotation.</td>
                </tr>
            
                <tr>
                    <td>DXGK_DPO_270</td>
                    <td>Indicates a 270 degree rotation.</td>
                </tr>
            
                <tr>
                    <td>DXGK_DPO_90</td>
                    <td>Indicates a 90 degree rotation.</td>
                </tr>
            
                <tr>
                    <td>UINT</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3dkmddi.h |