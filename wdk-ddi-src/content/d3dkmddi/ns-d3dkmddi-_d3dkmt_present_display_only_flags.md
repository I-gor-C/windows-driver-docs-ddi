---
UID: NS:d3dkmddi._D3DKMT_PRESENT_DISPLAY_ONLY_FLAGS
title: "_D3DKMT_PRESENT_DISPLAY_ONLY_FLAGS"
author: windows-driver-content
description: Indicates how a kernel mode display-only driver (KMDOD) is to perform a present operation.
old-location: display\d3dkmt_present_display_only_flags.htm
old-project: display
ms.assetid: a45dfdeb-06d2-49c8-a6e1-f42a43857492
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DKMT_PRESENT_DISPLAY_ONLY_FLAGS, D3DKMT_PRESENT_DISPLAY_ONLY_FLAGS structure [Display Devices], _D3DKMT_PRESENT_DISPLAY_ONLY_FLAGS, d3dkmddi/D3DKMT_PRESENT_DISPLAY_ONLY_FLAGS, display.d3dkmt_present_display_only_flags
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
-	D3DKMT_PRESENT_DISPLAY_ONLY_FLAGS
product:
- Windows
targetos: Windows
req.typenames: D3DKMT_PRESENT_DISPLAY_ONLY_FLAGS
---

# _D3DKMT_PRESENT_DISPLAY_ONLY_FLAGS structure
Indicates how a kernel mode display-only driver (KMDOD) is to perform a present operation.

## Syntax
```
typedef struct _D3DKMT_PRESENT_DISPLAY_ONLY_FLAGS {
  union {
    struct {
      UINT  : 1  Rotate;
      UINT  : 31 Reserved;
    };
    UINT Value;
  };
} D3DKMT_PRESENT_DISPLAY_ONLY_FLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff546647">D3DKMDT_VIDPN_PRESENT_PATH</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff546719">D3DKMDT_VIDPN_PRESENT_PATH_TRANSFORMATION</a>