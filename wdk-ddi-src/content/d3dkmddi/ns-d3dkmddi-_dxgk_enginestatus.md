---
UID: NS:d3dkmddi._DXGK_ENGINESTATUS
title: "_DXGK_ENGINESTATUS"
author: windows-driver-content
description: Indicates the progress of a node within an active physical display adapter (engine) specified by a DXGKARG_QUERYENGINESTATUS structure.
old-location: display\dxgk_enginestatus.htm
old-project: display
ms.assetid: e052e3bc-688e-4aa8-b987-88ed6963774a
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_ENGINESTATUS, DXGK_ENGINESTATUS structure [Display Devices], _DXGK_ENGINESTATUS, d3dkmddi/DXGK_ENGINESTATUS, display.dxgk_enginestatus
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
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
-	DXGK_ENGINESTATUS
product: Windows
targetos: Windows
req.typenames: DXGK_ENGINESTATUS
---

# _DXGK_ENGINESTATUS structure
Indicates the progress of a node within an active physical display adapter (engine) specified by a <a href="https://msdn.microsoft.com/library/windows/hardware/hh451299">DXGKARG_QUERYENGINESTATUS</a> structure.

## Syntax
```
typedef struct _DXGK_ENGINESTATUS {
  union {
    struct {
      UINT  : 1  Responsive;
      UINT  : 31 Reserved;
    };
    UINT Value;
  };
} DXGK_ENGINESTATUS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh451299">DXGKARG_QUERYENGINESTATUS</a>