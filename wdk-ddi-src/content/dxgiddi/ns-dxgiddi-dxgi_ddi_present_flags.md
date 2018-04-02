---
UID: NS:dxgiddi.DXGI_DDI_PRESENT_FLAGS
title: DXGI_DDI_PRESENT_FLAGS
author: windows-driver-content
description: Identifies how to perform a present operation.
old-location: display\dxgi_ddi_present_flags.htm
old-project: display
ms.assetid: 87f3b66a-0fcb-4325-ae23-7f89d6b389e6
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGI_DDI_PRESENT_FLAGS, DXGI_DDI_PRESENT_FLAGS structure [Display Devices], UMDisplayDriver_Dx10param_Structs_75234d4d-acce-4f1f-804c-f7128d885c2f.xml, display.dxgi_ddi_present_flags, dxgiddi/DXGI_DDI_PRESENT_FLAGS
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
-	DXGI_DDI_PRESENT_FLAGS
product:
- Windows
targetos: Windows
req.typenames: DXGI_DDI_PRESENT_FLAGS
---

# DXGI_DDI_PRESENT_FLAGS structure
Identifies how to perform a present operation.

## Syntax
```
typedef struct DXGI_DDI_PRESENT_FLAGS {
  union {
    struct {
      UINT  : 1  Blt;
      UINT  : 1  Flip;
      UINT  : 1  PreferRight;
      UINT  : 1  TemporaryMono;
      UINT  : 1  AllowTearing;
      UINT  : 1  AllowFlexibleRefresh;
      UINT  : 26 Reserved;
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

<a href="https://msdn.microsoft.com/library/windows/hardware/ff557464">DXGI_DDI_ARG_PRESENT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff569179">PresentDXGI</a>