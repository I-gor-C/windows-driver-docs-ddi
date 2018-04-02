---
UID: NE:iddcx.IDDCX_GAMMARAMP_TYPE
title: IDDCX_GAMMARAMP_TYPE
author: windows-driver-content
description: An enumeration indicating the type of gamma ramp being set.
old-location: display\iddcx_gammaramp_type.htm
old-project: display
ms.assetid: 40fa5169-e295-429c-a63d-3e4ab9c14672
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: IDDCX_GAMMARAMP_TYPE, IDDCX_GAMMARAMP_TYPE enumeration [Display Devices], IDDCX_GAMMARAMP_TYPE_DEFAULT, IDDCX_GAMMARAMP_TYPE_RGB256x3x16, IDDCX_GAMMARAMP_TYPE_UNINITIALIZED, display.iddcx_gammaramp_type, iddcx/IDDCX_GAMMARAMP_TYPE, iddcx/IDDCX_GAMMARAMP_TYPE_DEFAULT, iddcx/IDDCX_GAMMARAMP_TYPE_RGB256x3x16, iddcx/IDDCX_GAMMARAMP_TYPE_UNINITIALIZED
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: iddcx.h
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
req.irql: "_requires_same_"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	iddcx.h
api_name:
-	IDDCX_GAMMARAMP_TYPE
product: Windows
targetos: Windows
req.typenames: 
---

# IDDCX_GAMMARAMP_TYPE Enumeration
An enumeration indicating the type of gamma ramp being set

## Syntax
```
typedef enum IDDCX_GAMMARAMP_TYPE {
  IDDCX_GAMMARAMP_TYPE_UNINITIALIZED  ,
  IDDCX_GAMMARAMP_TYPE_DEFAULT        ,
  IDDCX_GAMMARAMP_TYPE_RGB256x3x16    ,
  UINT
} ;
```

## Constants

<table>
            
                <tr>
                    <td>IDDCX_GAMMARAMP_TYPE_UNINITIALIZED</td>
                    <td>Indicates that an <b>IDDCX_GAMMARAMP_TYPE</b> variable has not yet been assigned a meaningful value.</td>
                </tr>
            
                <tr>
                    <td>IDDCX_GAMMARAMP_TYPE_DEFAULT</td>
                    <td>The gamma ramp is the default ramp</td>
                </tr>
            
                <tr>
                    <td>IDDCX_GAMMARAMP_TYPE_RGB256x3x16</td>
                    <td>Indicates that the gamma lookup table contains three arrays, one each for the red, green, and blue color channels. Each array has 256 16-bit values.</td>
                </tr>
            
                <tr>
                    <td>UINT</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | iddcx.h |