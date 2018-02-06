---
UID: NE:d3dkmdt._DXGK_DISPLAY_USAGE
title: "_DXGK_DISPLAY_USAGE"
author: windows-driver-content
description: Enum used to specify the display type being used.
old-location: display\dxgk_display_usage.htm
old-project: display
ms.assetid: 07B51679-4E9B-4360-AA4A-D5BD9BADB4FC
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: d3dkmdt/PDXGK_DISPLAY_USAGE, DXGK_DISPLAY_USAGE enumeration [Display Devices], DXGK_DU_INVALID, d3dkmdt/DXGK_DU_INVALID, DXGK_DISPLAY_USAGE, d3dkmdt/DXGK_DU_GENERIC, DXGK_DU_AR, *PDXGK_DISPLAY_USAGE, DXGK_DU_GENERIC, d3dkmdt/DXGK_DU_VR, d3dkmdt/DXGK_DISPLAY_USAGE, d3dkmdt/DXGK_DU_AR, _DXGK_DISPLAY_USAGE, PDXGK_DISPLAY_USAGE, PDXGK_DISPLAY_USAGE enumeration pointer [Display Devices], display.dxgk_display_usage, DXGK_DU_VR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmdt.h
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	d3dkmdt.h
apiname:
-	DXGK_DISPLAY_USAGE
product: Windows
targetos: Windows
req.typenames: DXGK_DISPLAY_USAGE, *PDXGK_DISPLAY_USAGE
---

# _DXGK_DISPLAY_USAGE Enumeration
Enum used to specify the display type being used.

## Syntax
````
typedef enum _DXGK_DISPLAY_USAGE { 
  DXGK_DU_INVALID  = 0,
  DXGK_DU_GENERIC,
  DXGK_DU_AR,
  DXGK_DU_VR
} DXGK_DISPLAY_USAGE, *PDXGK_DISPLAY_USAGE;
````

## Constants

<table>
            
                <tr>
                    <td>BYTE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DXGK_DU_AR</td>
                    <td>A head mounted augmented reality display.</td>
                </tr>
            
                <tr>
                    <td>DXGK_DU_GENERIC</td>
                    <td>Generic display type.</td>
                </tr>
            
                <tr>
                    <td>DXGK_DU_INVALID</td>
                    <td>Invalid type.</td>
                </tr>
            
                <tr>
                    <td>DXGK_DU_MAX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DXGK_DU_VR</td>
                    <td>A head mounted virtual reality display.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3dkmdt.h |