---
UID: NS:d3dumddi.D3DDDIARG_COPYFLAGS
title: D3DDDIARG_COPYFLAGS
author: windows-driver-content
description: Describes how to handle the existing contents of a resource during a copy or update operation of a region within that resource. Used by Windows Display Driver Model (WDDM) 1.3 and later user-mode display drivers.
old-location: display\d3dddiarg_copyflags.htm
old-project: display
ms.assetid: DA114D60-60EE-4D1D-B42C-A84CE54C8B95
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDIARG_COPYFLAGS, D3DDDIARG_COPYFLAGS structure [Display Devices], d3dumddi/D3DDDIARG_COPYFLAGS, display.d3dddiarg_copyflags
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
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
-	D3dumddi.h
api_name:
-	D3DDDIARG_COPYFLAGS
product: Windows
targetos: Windows
req.typenames: D3DDDIARG_COPYFLAGS
---

# D3DDDIARG_COPYFLAGS structure
Describes how to handle the existing contents of a resource during a copy or update operation of a region within that resource. Used by Windows Display Driver Model (WDDM) 1.3 and later user-mode display drivers.

## Syntax
```
typedef struct D3DDDIARG_COPYFLAGS {
  union {
    struct {
      UINT  : 1  NoOverwrite;
      UINT  : 1  Discard;
      UINT  : 22 Reserved1;
      UINT  : 1  BoxValid;
      UINT  : 7  Reserved2;
    };
    UINT Value;
  };
};
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8.1 Windows 8.1 |
| **Header** | d3dumddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn449153">D3DDDIARG_UPDATESUBRESOURCEUP</a>