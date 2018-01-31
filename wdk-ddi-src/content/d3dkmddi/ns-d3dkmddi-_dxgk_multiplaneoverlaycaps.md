---
UID : NS:d3dkmddi._DXGK_MULTIPLANEOVERLAYCAPS
title : "_DXGK_MULTIPLANEOVERLAYCAPS"
author : windows-driver-content
description : Multiplane overlay capabilities returned by the DxgkDdiGetMultiPlaneOverlayCaps function.
old-location : display\dxgk_multiplaneoverlaycaps.htm
old-project : display
ms.assetid : E3F590EA-2B3B-464B-9D72-708B24CA3052
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.dxgk_multiplaneoverlaycaps, DXGK_MULTIPLANEOVERLAYCAPS, _DXGK_MULTIPLANEOVERLAYCAPS, DXGK_MULTIPLANEOVERLAYCAPS structure [Display Devices], d3dkmddi/DXGK_MULTIPLANEOVERLAYCAPS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3dkmddi.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : DXGK_MULTIPLANEOVERLAYCAPS
---

# _DXGK_MULTIPLANEOVERLAYCAPS structure
Multiplane overlay capabilities returned by the DxgkDdiGetMultiPlaneOverlayCaps function.

## Syntax
````
typedef struct _DXGK_MULTIPLANEOVERLAYCAPS {
  union {
    struct {
      UINT Rotation  :1;
      UINT RotationWithoutIndependentFlip  :1;
      UINT VerticalFlip  :1;
      UINT HorizontalFlip  :1;
      UINT StretchRGB  :1;
      UINT StretchYUV  :1;
      UINT BilinearFilter  :1;
      UINT HighFilter  :1;
      UINT Shared  :1;
      UINT Immediate  :1;
      UINT Plane0ForVirtualModeOnly  :1;
      UINT Reserved  :21;
    };
    UINT Value;
  };
} DXGK_MULTIPLANEOVERLAYCAPS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmddi.h |