---
UID: NS:d3dkmddi._DXGK_MULTIPLANEOVERLAYCAPS
title: "_DXGK_MULTIPLANEOVERLAYCAPS"
author: windows-driver-content
description: Multiplane overlay capabilities returned by the DxgkDdiGetMultiPlaneOverlayCaps function.
old-location: display\dxgk_multiplaneoverlaycaps.htm
old-project: display
ms.assetid: E3F590EA-2B3B-464B-9D72-708B24CA3052
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_MULTIPLANEOVERLAYCAPS, DXGK_MULTIPLANEOVERLAYCAPS structure [Display Devices], _DXGK_MULTIPLANEOVERLAYCAPS, d3dkmddi/DXGK_MULTIPLANEOVERLAYCAPS, display.dxgk_multiplaneoverlaycaps
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
-	DXGK_MULTIPLANEOVERLAYCAPS
product:
- Windows
targetos: Windows
req.typenames: DXGK_MULTIPLANEOVERLAYCAPS
---

# _DXGK_MULTIPLANEOVERLAYCAPS structure
Multiplane overlay capabilities returned by the DxgkDdiGetMultiPlaneOverlayCaps function.

## Syntax
```
typedef struct _DXGK_MULTIPLANEOVERLAYCAPS {
  union {
    struct {
      UINT  : 1  Rotation;
      UINT  : 1  RotationWithoutIndependentFlip;
      UINT  : 1  VerticalFlip;
      UINT  : 1  HorizontalFlip;
      UINT  : 1  StretchRGB;
      UINT  : 1  StretchYUV;
      UINT  : 1  BilinearFilter;
      UINT  : 1  HighFilter;
      UINT  : 1  Shared;
      UINT  : 1  Immediate;
      UINT  : 1  Plane0ForVirtualModeOnly;
      UINT  : 21 Reserved;
    };
    UINT Value;
  };
} DXGK_MULTIPLANEOVERLAYCAPS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3dkmddi.h |