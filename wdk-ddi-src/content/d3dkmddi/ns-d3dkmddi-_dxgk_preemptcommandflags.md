---
UID: NS:d3dkmddi._DXGK_PREEMPTCOMMANDFLAGS
title: "_DXGK_PREEMPTCOMMANDFLAGS"
author: windows-driver-content
description: The DXGK_PREEMPTCOMMANDFLAGS structure specifies a union that contains either a structure with a reserved member or a 32-bit value. No bit-field flags are currently defined.
old-location: display\dxgk_preemptcommandflags.htm
old-project: display
ms.assetid: 24444451-7323-4e1a-9981-cf5caa00c4e3
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DXGK_PREEMPTCOMMANDFLAGS, DXGK_PREEMPTCOMMANDFLAGS structure [Display Devices], DmStructs_7163ce37-49c8-4b17-aadc-cd36ad5cac9d.xml, _DXGK_PREEMPTCOMMANDFLAGS, d3dkmddi/DXGK_PREEMPTCOMMANDFLAGS, display.dxgk_preemptcommandflags
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
-	DXGK_PREEMPTCOMMANDFLAGS
product: Windows
targetos: Windows
req.typenames: DXGK_PREEMPTCOMMANDFLAGS
---

# _DXGK_PREEMPTCOMMANDFLAGS structure
The DXGK_PREEMPTCOMMANDFLAGS structure specifies a union that contains either a structure with a reserved member or a 32-bit value. No bit-field flags are currently defined.

## Syntax
````
typedef struct _DXGK_PREEMPTCOMMANDFLAGS {
  union {
    struct {
      UINT Reserved  :32;
    };
    UINT Value;
  };
} DXGK_PREEMPTCOMMANDFLAGS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="..\d3dkmddi\ns-d3dkmddi-_dxgkarg_preemptcommand.md">DXGKARG_PREEMPTCOMMAND</a>