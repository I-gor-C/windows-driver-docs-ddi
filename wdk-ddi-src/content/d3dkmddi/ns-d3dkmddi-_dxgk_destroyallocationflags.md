---
UID: NS:d3dkmddi._DXGK_DESTROYALLOCATIONFLAGS
title: "_DXGK_DESTROYALLOCATIONFLAGS"
author: windows-driver-content
description: The DXGK_DESTROYALLOCATIONFLAGS structure identifies how to release allocations.
old-location: display\dxgk_destroyallocationflags.htm
old-project: display
ms.assetid: 8f848d68-cef4-45a2-bdda-1bc8c9df6272
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DXGK_DESTROYALLOCATIONFLAGS, DXGK_DESTROYALLOCATIONFLAGS structure [Display Devices], DmStructs_acc32f8d-3d16-493e-be05-e739bc635bd0.xml, _DXGK_DESTROYALLOCATIONFLAGS, d3dkmddi/DXGK_DESTROYALLOCATIONFLAGS, display.dxgk_destroyallocationflags
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
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
-	DXGK_DESTROYALLOCATIONFLAGS
product: Windows
targetos: Windows
req.typenames: DXGK_DESTROYALLOCATIONFLAGS
---

# _DXGK_DESTROYALLOCATIONFLAGS structure
The DXGK_DESTROYALLOCATIONFLAGS structure identifies how to release allocations.

## Syntax
````
typedef struct _DXGK_DESTROYALLOCATIONFLAGS {
  union {
    struct {
      UINT DestroyResource  :1;
      UINT Reserved  :31;
    };
    UINT Value;
  };
} DXGK_DESTROYALLOCATIONFLAGS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="..\d3dkmddi\ns-d3dkmddi-_dxgkarg_destroyallocation.md">DXGKARG_DESTROYALLOCATION</a>