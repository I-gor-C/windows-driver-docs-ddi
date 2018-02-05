---
UID : NS:d3dkmddi._DXGK_PLANE_SPECIFIC_INPUT_FLAGS
title : "_DXGK_PLANE_SPECIFIC_INPUT_FLAGS"
author : windows-driver-content
description : A structure containing the input flags to be used for the driver that apply to a plane.
old-location : display\dxgk_plane_specific_input_flags.htm
old-project : display
ms.assetid : 39BE1343-D965-4750-9B94-B54127D873A5
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : DXGK_PLANE_SPECIFIC_INPUT_FLAGS structure [Display Devices], _DXGK_PLANE_SPECIFIC_INPUT_FLAGS, DXGK_PLANE_SPECIFIC_INPUT_FLAGS, d3dkmddi/DXGK_PLANE_SPECIFIC_INPUT_FLAGS, display.dxgk_plane_specific_input_flags
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
req.typenames : DXGK_PLANE_SPECIFIC_INPUT_FLAGS
---

# _DXGK_PLANE_SPECIFIC_INPUT_FLAGS structure
A structure containing the input flags to be used for the driver that apply to a plane.

## Syntax
````
typedef struct _DXGK_PLANE_SPECIFIC_INPUT_FLAGS {
  union {
    struct {
      UINT Enabled  :1;
      UINT FlipImmediate  :1;
      UINT FlipOnNextVSync  :1;
      UINT SharedPrimaryTransition  :1;
      UINT IndependentFlipExclusive  :1;
      UINT Reserved  :27;
    };
    UINT Value;
  };
} DXGK_PLANE_SPECIFIC_INPUT_FLAGS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3dkmddi.h |