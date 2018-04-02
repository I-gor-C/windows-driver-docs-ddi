---
UID: NE:d3dkmdt._DXGK_DISPLAY_TECHNOLOGY
title: "_DXGK_DISPLAY_TECHNOLOGY"
author: windows-driver-content
description: Enum used to specify the display technology being used.
old-location: display\dxgk_display_technology.htm
old-project: display
ms.assetid: 4612213A-E79F-4C3B-95B4-8C83C0B5FB32
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PDXGK_DISPLAY_TECHNOLOGY, DXGK_DISPLAY_TECHNOLOGY, DXGK_DISPLAY_TECHNOLOGY enumeration [Display Devices], DXGK_DT_INVALID, DXGK_DT_LCD, DXGK_DT_OLED, DXGK_DT_OTHER, PDXGK_DISPLAY_TECHNOLOGY, PDXGK_DISPLAY_TECHNOLOGY enumeration pointer [Display Devices], _DXGK_DISPLAY_TECHNOLOGY, d3dkmdt/DXGK_DISPLAY_TECHNOLOGY, d3dkmdt/DXGK_DT_INVALID, d3dkmdt/DXGK_DT_LCD, d3dkmdt/DXGK_DT_OLED, d3dkmdt/DXGK_DT_OTHER, d3dkmdt/PDXGK_DISPLAY_TECHNOLOGY, display.dxgk_display_technology"
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dkmdt.h
api_name:
-	DXGK_DISPLAY_TECHNOLOGY
product: Windows
targetos: Windows
req.typenames: DXGK_DISPLAY_TECHNOLOGY, *PDXGK_DISPLAY_TECHNOLOGY
---

# _DXGK_DISPLAY_TECHNOLOGY Enumeration
Enum used to specify the display technology being used.

## Syntax
```
typedef enum _DXGK_DISPLAY_TECHNOLOGY {
  DXGK_DT_INVALID    ,
  DXGK_DT_OTHER      ,
  DXGK_DT_LCD        ,
  DXGK_DT_OLED       ,
  DXGK_DT_PROJECTOR  ,
  DXGK_DT_MAX        ,
  BYTE
} DXGK_DISPLAY_TECHNOLOGY, *PDXGK_DISPLAY_TECHNOLOGY;
```

## Constants

<table>
            
                <tr>
                    <td>DXGK_DT_INVALID</td>
                    <td>Invalid type.</td>
                </tr>
            
                <tr>
                    <td>DXGK_DT_OTHER</td>
                    <td>A display technology which does not match one of the defined, valid types.</td>
                </tr>
            
                <tr>
                    <td>DXGK_DT_LCD</td>
                    <td>A display using an LCD panel.</td>
                </tr>
            
                <tr>
                    <td>DXGK_DT_OLED</td>
                    <td>A display using an OLED panel.</td>
                </tr>
            
                <tr>
                    <td>DXGK_DT_PROJECTOR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DXGK_DT_MAX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>BYTE</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3dkmdt.h |