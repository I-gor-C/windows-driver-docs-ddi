---
UID: NS:d3dkmddi._DXGKCB_GETHANDLEDATAFLAGS
title: "_DXGKCB_GETHANDLEDATAFLAGS"
author: windows-driver-content
description: The DXGKCB_GETHANDLEDATAFLAGS structure indicates if allocations belong to a resource.
old-location: display\dxgkcb_gethandledataflags.htm
old-project: display
ms.assetid: 01689a2f-115a-4db8-b53d-38717c10a0ff
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DXGKCB_GETHANDLEDATAFLAGS, DXGKCB_GETHANDLEDATAFLAGS structure [Display Devices], DmStructs_a0288df8-0513-4823-9445-cd86ff45a186.xml, _DXGKCB_GETHANDLEDATAFLAGS, d3dkmddi/DXGKCB_GETHANDLEDATAFLAGS, display.dxgkcb_gethandledataflags
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
-	DXGKCB_GETHANDLEDATAFLAGS
product: Windows
targetos: Windows
req.typenames: DXGKCB_GETHANDLEDATAFLAGS
---

# _DXGKCB_GETHANDLEDATAFLAGS structure
The DXGKCB_GETHANDLEDATAFLAGS structure indicates if allocations belong to a resource.

## Syntax
````
typedef struct _DXGKCB_GETHANDLEDATAFLAGS {
  union {
    struct {
      UINT DeviceSpecific  :1;
      UINT Reserved  :31;
    };
    UINT Value;
  };
} DXGKCB_GETHANDLEDATAFLAGS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="..\d3dkmddi\ns-d3dkmddi-_dxgkargcb_gethandledata.md">DXGKARGCB_GETHANDLEDATA</a>