---
UID: NS:d3dkmddi._DXGK_CREATEALLOCATIONFLAGS
title: "_DXGK_CREATEALLOCATIONFLAGS"
author: windows-driver-content
description: The DXGK_CREATEALLOCATIONFLAGS structure identifies how to create allocations.
old-location: display\dxgk_createallocationflags.htm
old-project: display
ms.assetid: 3c6c5515-855a-4016-a327-958959981f0f
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_CREATEALLOCATIONFLAGS, DXGK_CREATEALLOCATIONFLAGS structure [Display Devices], DmStructs_320b15bf-5664-4fb9-9126-2c063ef75467.xml, _DXGK_CREATEALLOCATIONFLAGS, d3dkmddi/DXGK_CREATEALLOCATIONFLAGS, display.dxgk_createallocationflags
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows Vista.
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
-	DXGK_CREATEALLOCATIONFLAGS
product: Windows
targetos: Windows
req.typenames: DXGK_CREATEALLOCATIONFLAGS
---

# _DXGK_CREATEALLOCATIONFLAGS structure
The DXGK_CREATEALLOCATIONFLAGS structure identifies how to create allocations.

## Syntax
```
typedef struct _DXGK_CREATEALLOCATIONFLAGS {
  union {
    struct {
      UINT  : 1  Resource;
      UINT  : 31 Reserved;
    };
    UINT Value;
  };
} DXGK_CREATEALLOCATIONFLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows Vista. Available starting with Windows Vista. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff557559">DXGKARG_CREATEALLOCATION</a>