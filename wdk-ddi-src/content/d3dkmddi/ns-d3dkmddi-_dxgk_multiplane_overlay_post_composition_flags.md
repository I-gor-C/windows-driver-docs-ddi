---
UID: NS:d3dkmddi._DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION_FLAGS
title: "_DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION_FLAGS"
author: windows-driver-content
description: A structure containing the flags describing the transformations applied to an image.
old-location: display\dxgk_multiplane_overlay_post_composition_flags.htm
old-project: display
ms.assetid: F7791AB9-6D20-4560-A478-E30F08C6AC3A
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: d3dkmddi/DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION_FLAGS, DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION_FLAGS, _DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION_FLAGS, DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION_FLAGS structure [Display Devices], display.dxgk_multiplane_overlay_post_composition_flags
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
-	DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION_FLAGS
product: Windows
targetos: Windows
req.typenames: DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION_FLAGS
---

# _DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION_FLAGS structure
A structure containing the flags describing the transformations applied to an image.

## Syntax
````
typedef struct _DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION_FLAGS {
  union {
    struct {
      UINT VerticalFlip  :1;
      UINT HorizontalFlip  :1;
      UINT Reserved  :30;
    };
    UINT Value;
  };
} DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION_FLAGS;
````

## Members


## Remarks
Applying VerticalFlip and HorizontalFlip simultaneously results in 180 degree rotation.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3dkmddi.h |