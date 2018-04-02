---
UID: NS:d3dkmddi._DXGK_PLANE_SPECIFIC_OUTPUT_FLAGS
title: "_DXGK_PLANE_SPECIFIC_OUTPUT_FLAGS"
author: windows-driver-content
description: A structure containing the flags that apply to a plane set by the driver.
old-location: display\dxgk_plane_specific_output_flags.htm
old-project: display
ms.assetid: 95D9C564-92F3-4165-8063-49D928F30475
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_PLANE_SPECIFIC_OUTPUT_FLAGS, DXGK_PLANE_SPECIFIC_OUTPUT_FLAGS structure [Display Devices], _DXGK_PLANE_SPECIFIC_OUTPUT_FLAGS, d3dkmddi/DXGK_PLANE_SPECIFIC_OUTPUT_FLAGS, display.dxgk_plane_specific_output_flags
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
-	DXGK_PLANE_SPECIFIC_OUTPUT_FLAGS
product:
- Windows
targetos: Windows
req.typenames: DXGK_PLANE_SPECIFIC_OUTPUT_FLAGS
---

# _DXGK_PLANE_SPECIFIC_OUTPUT_FLAGS structure
A structure containing the flags that apply to a plane set by the driver.

## Syntax
```
typedef struct _DXGK_PLANE_SPECIFIC_OUTPUT_FLAGS {
  union {
    struct {
      UINT  : 1  FlipConvertedToImmediate;
      UINT  : 1  PostPresentNeeded;
      UINT  : 1  HsyncInterruptCompletion;
      UINT  : 29 Reserved;
      UINT  : 30 Reserved;
    };
    UINT Value;
  };
} DXGK_PLANE_SPECIFIC_OUTPUT_FLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3dkmddi.h |