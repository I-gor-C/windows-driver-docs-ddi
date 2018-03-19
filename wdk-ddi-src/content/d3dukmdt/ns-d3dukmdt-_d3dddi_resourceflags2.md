---
UID: NS:d3dukmdt._D3DDDI_RESOURCEFLAGS2
title: "_D3DDDI_RESOURCEFLAGS2"
author: windows-driver-content
description: Identifies the type of resource to create in a call to the driver's CreateResource2 function.
old-location: display\d3dddi_resourceflags2.htm
old-project: display
ms.assetid: 2edf2104-ad17-4c84-b991-57e64565029f
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: D3DDDI_RESOURCEFLAGS2, D3DDDI_RESOURCEFLAGS2 structure [Display Devices], _D3DDDI_RESOURCEFLAGS2, d3dukmdt/D3DDDI_RESOURCEFLAGS2, display.d3dddi_resourceflags2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: D3dukmdt.h, D3dkmddi.h
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	D3dukmdt.h
api_name:
-	D3DDDI_RESOURCEFLAGS2
product: Windows
targetos: Windows
req.typenames: D3DDDI_RESOURCEFLAGS2
---

# _D3DDDI_RESOURCEFLAGS2 structure
Identifies the type of resource to create in a call to the driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_createresource2.md">CreateResource2</a> function.

## Syntax
````
typedef struct _D3DDDI_RESOURCEFLAGS2 {
  union {
    struct {
      UINT VideoEncoder  :1;
      UINT UserMemory  :1;
#if ((DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM1_3) || \
     (D3D_UMD_INTERFACE_VERSION >= D3D_UMD_INTERFACE_VERSION_WDDM1_3))
      UINT CrossAdapter  :1;
      UINT Reserved  :29;
#else 
      UINT Reserved  :30;
#endif 
    };
    UINT   Value;
  };
} D3DDDI_RESOURCEFLAGS2;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | d3dukmdt.h (include D3dukmdt.h, D3dkmddi.h) |

## See Also

<a href="..\d3dumddi\ns-d3dumddi-_formatop.md">FORMATOP</a>



<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_createresource2.md">CreateResource2</a>