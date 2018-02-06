---
UID: NS:d3dkmddi._DXGK_PLANE_SPECIFIC_OUTPUT_FLAGS
title: "_DXGK_PLANE_SPECIFIC_OUTPUT_FLAGS"
author: windows-driver-content
description: A structure containing the flags that apply to a plane set by the driver.
old-location: display\dxgk_plane_specific_output_flags.htm
old-project: display
ms.assetid: 95D9C564-92F3-4165-8063-49D928F30475
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: "_DXGK_PLANE_SPECIFIC_OUTPUT_FLAGS, display.dxgk_plane_specific_output_flags, DXGK_PLANE_SPECIFIC_OUTPUT_FLAGS structure [Display Devices], d3dkmddi/DXGK_PLANE_SPECIFIC_OUTPUT_FLAGS, DXGK_PLANE_SPECIFIC_OUTPUT_FLAGS"
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
-	DXGK_PLANE_SPECIFIC_OUTPUT_FLAGS
product: Windows
targetos: Windows
req.typenames: DXGK_PLANE_SPECIFIC_OUTPUT_FLAGS
---

# _DXGK_PLANE_SPECIFIC_OUTPUT_FLAGS structure
A structure containing the flags that apply to a plane set by the driver.

## Syntax
````
typedef struct _DXGK_PLANE_SPECIFIC_OUTPUT_FLAGS {
  union {
    struct {
      UINT FlipConvertedToImmediate  :1;
      UINT  PostPresentNeeded  :1;
      UINT HsyncInterruptCompletion  :1;
      UINT Reserved  :29;
    };
    UINT Value;
  };
} DXGK_PLANE_SPECIFIC_OUTPUT_FLAGS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3dkmddi.h |