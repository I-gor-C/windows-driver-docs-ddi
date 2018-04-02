---
UID: NS:d3dkmddi._DXGK_DESCRIBEALLOCATIONFLAGS
title: "_DXGK_DESCRIBEALLOCATIONFLAGS"
author: windows-driver-content
description: Used in the DXGKARG_DESCRIBEALLOCATION.Flags member to describe whether an existing allocation is being queried for its display mode.
old-location: display\dxgk_describeallocationflags.htm
old-project: display
ms.assetid: f5cab74a-19ce-45d1-9c6f-461a98c4506c
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_DESCRIBEALLOCATIONFLAGS, DXGK_DESCRIBEALLOCATIONFLAGS structure [Display Devices], _DXGK_DESCRIBEALLOCATIONFLAGS, d3dkmddi/DXGK_DESCRIBEALLOCATIONFLAGS, display.dxgk_describeallocationflags
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
-	DXGK_DESCRIBEALLOCATIONFLAGS
product: Windows
targetos: Windows
req.typenames: DXGK_DESCRIBEALLOCATIONFLAGS
---

# _DXGK_DESCRIBEALLOCATIONFLAGS structure
Used in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557575">DXGKARG_DESCRIBEALLOCATION</a>.<b>Flags</b> member to describe whether an existing allocation is being queried for its display mode.

## Syntax
```
typedef struct _DXGK_DESCRIBEALLOCATIONFLAGS {
  union {
    struct {
      UINT  : 1  CheckDisplayMode;
      UINT  : 31 Reserved;
    };
    UINT Value;
  };
} DXGK_DESCRIBEALLOCATIONFLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff557575">DXGKARG_DESCRIBEALLOCATION</a>