---
UID: NS:d3dumddi._D3DDDI_OPENRESOURCEFLAGS
title: "_D3DDDI_OPENRESOURCEFLAGS"
author: windows-driver-content
description: The D3DDDI_OPENRESOURCEFLAGS structure identifies the type of resource to open.
old-location: display\d3dddi_openresourceflags.htm
old-project: display
ms.assetid: f65fda13-3d05-4e1b-b0c7-01e43a9bf09e
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDI_OPENRESOURCEFLAGS, D3DDDI_OPENRESOURCEFLAGS structure [Display Devices], D3D_other_Structs_918a41c9-09de-4916-a0d6-fd69f7c431c2.xml, _D3DDDI_OPENRESOURCEFLAGS, d3dumddi/D3DDDI_OPENRESOURCEFLAGS, display.d3dddi_openresourceflags
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
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
-	d3dumddi.h
api_name:
-	D3DDDI_OPENRESOURCEFLAGS
product:
- Windows
targetos: Windows
req.typenames: D3DDDI_OPENRESOURCEFLAGS
---

# _D3DDDI_OPENRESOURCEFLAGS structure
The D3DDDI_OPENRESOURCEFLAGS structure identifies the type of resource to open.

## Syntax
```
typedef struct _D3DDDI_OPENRESOURCEFLAGS {
  union {
    struct {
      UINT  : 1  Fullscreen;
      UINT  : 1  AlphaOverride;
      UINT  : 30 Reserved;
    };
    UINT Value;
  };
} D3DDDI_OPENRESOURCEFLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff543232">D3DDDIARG_OPENRESOURCE</a>