---
UID: NS:d3dkmddi._DXGK_MULTIPLANE_OVERLAY_FLAGS
title: "_DXGK_MULTIPLANE_OVERLAY_FLAGS"
author: windows-driver-content
description: Identifies a flip operation to be performed on an overlay plane.
old-location: display\dxgk_multiplane_overlay_flags.htm
old-project: display
ms.assetid: 2592e308-1d34-464f-8301-9ece54b4d017
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: DXGK_MULTIPLANE_OVERLAY_FLAGS, _DXGK_MULTIPLANE_OVERLAY_FLAGS, display.dxgk_multiplane_overlay_flags, d3dkmddi/DXGK_MULTIPLANE_OVERLAY_FLAGS, DXGK_MULTIPLANE_OVERLAY_FLAGS structure [Display Devices]
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
-	DXGK_MULTIPLANE_OVERLAY_FLAGS
product: Windows
targetos: Windows
req.typenames: DXGK_MULTIPLANE_OVERLAY_FLAGS
---

# _DXGK_MULTIPLANE_OVERLAY_FLAGS structure
Identifies a flip operation to be performed on an overlay plane.

## Syntax
````
typedef struct _DXGK_MULTIPLANE_OVERLAY_FLAGS {
  union {
    struct {
      UINT VerticalFlip  :1;
      UINT HorizontalFlip  :1;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_0)
      UINT PanelFitterPostComposition;
      UINT Reserved  :29;
#else 
      UINT Reserved  :30;
#endif 
    };
    UINT   Value;
  };
} DXGK_MULTIPLANE_OVERLAY_FLAGS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8.1 Windows 8.1 |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |