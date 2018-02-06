---
UID: NS:d3dkmddi._DXGK_MULTIPLANE_OVERLAY_YCbCr_FLAGS
title: "_DXGK_MULTIPLANE_OVERLAY_YCbCr_FLAGS"
author: windows-driver-content
description: Identifies YUV range and conversion info that describes a multiplane overlay.
old-location: display\dxgk_multiplane_overlay_ycbcr_flags.htm
old-project: display
ms.assetid: c3a463b1-fc6f-4834-87e5-1d694f2823f9
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: DXGK_MULTIPLANE_OVERLAY_YCbCr_FLAGS, d3dkmddi/DXGK_MULTIPLANE_OVERLAY_YCbCr_FLAGS, _DXGK_MULTIPLANE_OVERLAY_YCbCr_FLAGS, display.dxgk_multiplane_overlay_ycbcr_flags, DXGK_MULTIPLANE_OVERLAY_YCbCr_FLAGS structure [Display Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
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
req.irql: PASSIVE_LEVEL
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	D3dkmddi.h
apiname:
-	DXGK_MULTIPLANE_OVERLAY_YCbCr_FLAGS
product: Windows
targetos: Windows
req.typenames: DXGK_MULTIPLANE_OVERLAY_YCbCr_FLAGS
---

# _DXGK_MULTIPLANE_OVERLAY_YCbCr_FLAGS structure
Identifies YUV range and conversion info that describes a multiplane overlay.

## Syntax
````
typedef struct _DXGK_MULTIPLANE_OVERLAY_YCbCr_FLAGS {
  union {
    struct {
      UINT NominalRange  :1;
      UINT Bt709  :1;
      UINT xvYCC  :1;
      UINT Reserved  :29;
    };
    UINT   Value;
  };
} DXGK_MULTIPLANE_OVERLAY_YCbCr_FLAGS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8.1 Windows 8.1 |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |