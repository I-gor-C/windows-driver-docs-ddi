---
UID: NS:d3dkmddi._DXGK_MULTIPLANE_OVERLAY_FLAGS
title: "_DXGK_MULTIPLANE_OVERLAY_FLAGS"
author: windows-driver-content
description: Identifies a flip operation to be performed on an overlay plane.
old-location: display\dxgk_multiplane_overlay_flags.htm
old-project: display
ms.assetid: 2592e308-1d34-464f-8301-9ece54b4d017
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_MULTIPLANE_OVERLAY_FLAGS, DXGK_MULTIPLANE_OVERLAY_FLAGS structure [Display Devices], _DXGK_MULTIPLANE_OVERLAY_FLAGS, d3dkmddi/DXGK_MULTIPLANE_OVERLAY_FLAGS, display.dxgk_multiplane_overlay_flags
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	D3dkmddi.h
api_name:
-	DXGK_MULTIPLANE_OVERLAY_FLAGS
product: Windows
targetos: Windows
req.typenames: DXGK_MULTIPLANE_OVERLAY_FLAGS
---

# _DXGK_MULTIPLANE_OVERLAY_FLAGS structure
Identifies a flip operation to be performed on an overlay plane.

## Syntax
```
typedef struct _DXGK_MULTIPLANE_OVERLAY_FLAGS {
  union {
    struct {
      UINT  : 1  VerticalFlip;
      UINT  : 1  HorizontalFlip;
      UINT  : 30 Reserved;
    };
    UINT Value;
  };
} DXGK_MULTIPLANE_OVERLAY_FLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8.1 Windows 8.1 |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |