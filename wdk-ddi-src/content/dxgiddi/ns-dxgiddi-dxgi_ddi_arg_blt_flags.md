---
UID: NS:dxgiddi.DXGI_DDI_ARG_BLT_FLAGS
title: DXGI_DDI_ARG_BLT_FLAGS
author: windows-driver-content
description: The DXGI_DDI_ARG_BLT_FLAGS structure identifies the type of bit-block transfer (bitblt) to perform.
old-location: display\dxgi_ddi_arg_blt_flags.htm
old-project: display
ms.assetid: 812679d2-b05c-4533-b4b2-01b973b0d80f
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGI_DDI_ARG_BLT_FLAGS, DXGI_DDI_ARG_BLT_FLAGS structure [Display Devices], UMDisplayDriver_Dx10param_Structs_22ccf0e7-83cc-443e-b4a1-c1a2f3bc24a0.xml, display.dxgi_ddi_arg_blt_flags, dxgiddi/DXGI_DDI_ARG_BLT_FLAGS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dxgiddi.h
req.include-header: D3d10umddi.h
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	dxgiddi.h
api_name:
-	DXGI_DDI_ARG_BLT_FLAGS
product:
- Windows
targetos: Windows
req.typenames: DXGI_DDI_ARG_BLT_FLAGS
---

# DXGI_DDI_ARG_BLT_FLAGS structure
The DXGI_DDI_ARG_BLT_FLAGS structure identifies the type of bit-block transfer (bitblt) to perform.

## Syntax
```
typedef struct DXGI_DDI_ARG_BLT_FLAGS {
  union {
    struct {
      UINT  : 1  Resolve;
      UINT  : 1  Convert;
      UINT  : 1  Stretch;
      UINT  : 1  Present;
      UINT  : 28 Reserved;
    };
    UINT Value;
  };
};
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | dxgiddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff557447">DXGI_DDI_ARG_BLT</a>