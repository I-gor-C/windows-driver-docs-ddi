---
UID: NS:d3dkmddi._DXGK_COLORTRANSFORMCAPS
title: "_DXGK_COLORTRANSFORMCAPS"
author: windows-driver-content
description: This structure replaces the DXGK_GAMMARAMPCAPS structure in the DXGK_DRIVERCAPS structure to describe both the gamma and color transform capabilities of the display pipelines.
old-location: display\dxgk_colortransformcaps_.htm
old-project: display
ms.assetid: 83113D6C-44A1-4022-8101-061DEA9868E1
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_COLORTRANSFORMCAPS, DXGK_COLORTRANSFORMCAPS structure [Display Devices], PDXGK_COLORTRANSFORMCAPS, PDXGK_COLORTRANSFORMCAPS structure pointer [Display Devices], _DXGK_COLORTRANSFORMCAPS, d3dkmddi/DXGK_COLORTRANSFORMCAPS, d3dkmddi/PDXGK_COLORTRANSFORMCAPS, display.dxgk_colortransformcaps_
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
-	DXGK_COLORTRANSFORMCAPS
product:
- Windows
targetos: Windows
req.typenames: DXGK_COLORTRANSFORMCAPS
---

# _DXGK_COLORTRANSFORMCAPS structure
This structure replaces the DXGK_GAMMARAMPCAPS structure in the DXGK_DRIVERCAPS structure to describe both the gamma and color transform capabilities of the display pipelines.

## Syntax
```
typedef struct _DXGK_COLORTRANSFORMCAPS {
  union {
    struct {
      UINT  : 1  Gamma_Rgb256x3x16;
      UINT  : 1  Gamma_Dxgi1;
      UINT  : 1  Transform_3x4Matrix;
      UINT  : 1  Transform_3x4Matrix_WideColor;
      UINT  : 1  Transform_3x4Matrix_HighColor;
      UINT  : 27 Reserved;
      UINT  : 30 Reserved;
    };
    UINT Value;
  };
} DXGK_COLORTRANSFORMCAPS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3dkmddi.h |