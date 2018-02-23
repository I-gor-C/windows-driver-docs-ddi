---
UID: NS:d3dkmddi._DXGK_COLORTRANSFORMCAPS
title: "_DXGK_COLORTRANSFORMCAPS"
author: windows-driver-content
description: This structure replaces the DXGK_GAMMARAMPCAPS structure in the DXGK_DRIVERCAPS structure to describe both the gamma and color transform capabilities of the display pipelines.
old-location: display\dxgk_colortransformcaps_.htm
old-project: display
ms.assetid: 83113D6C-44A1-4022-8101-061DEA9868E1
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: d3dkmddi/PDXGK_COLORTRANSFORMCAPS, PDXGK_COLORTRANSFORMCAPS structure pointer [Display Devices], PDXGK_COLORTRANSFORMCAPS, d3dkmddi/DXGK_COLORTRANSFORMCAPS, DXGK_COLORTRANSFORMCAPS structure [Display Devices], DXGK_COLORTRANSFORMCAPS, display.dxgk_colortransformcaps_, _DXGK_COLORTRANSFORMCAPS
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	d3dkmddi.h
apiname:
-	DXGK_COLORTRANSFORMCAPS
product: Windows
targetos: Windows
req.typenames: DXGK_COLORTRANSFORMCAPS
---

# _DXGK_COLORTRANSFORMCAPS structure
This structure replaces the DXGK_GAMMARAMPCAPS structure in the DXGK_DRIVERCAPS structure to describe both the gamma and color transform capabilities of the display pipelines.

## Syntax
````
typedef struct _DXGK_COLORTRANSFORMCAPS  {
  union {
    struct {
      UINT Gamma_Rgb256x3x16  :1;
      UINT Gamma_Dxgi1  :1;
      UINT Transform_3x4Matrix  :1;
      UINT Transform_3x4Matrix_WideColor  :1;
      UINT Transform_3x4Matrix_HighColor  :1;
      UINT Reserved  :27;
    };
    UINT Value;
  };
} DXGK_COLORTRANSFORMCAPS , *PDXGK_COLORTRANSFORMCAPS ;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3dkmddi.h |