---
UID: NS:d3dumddi._D3DDDI_ISSUEQUERYFLAGS
title: "_D3DDDI_ISSUEQUERYFLAGS"
author: windows-driver-content
description: The D3DDDI_ISSUEQUERYFLAGS structure identifies the state of a query issue.
old-location: display\d3dddi_issuequeryflags.htm
old-project: display
ms.assetid: 68360c2e-4b03-40a3-a313-bdb9ef26a298
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDI_ISSUEQUERYFLAGS, D3DDDI_ISSUEQUERYFLAGS structure [Display Devices], D3D_other_Structs_794dd0b0-f24c-4e9e-befe-d79dd4efbaef.xml, _D3DDDI_ISSUEQUERYFLAGS, d3dumddi/D3DDDI_ISSUEQUERYFLAGS, display.d3dddi_issuequeryflags
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
-	D3DDDI_ISSUEQUERYFLAGS
product: Windows
targetos: Windows
req.typenames: D3DDDI_ISSUEQUERYFLAGS
---

# _D3DDDI_ISSUEQUERYFLAGS structure
The D3DDDI_ISSUEQUERYFLAGS structure identifies the state of a query issue.

## Syntax
```
typedef struct _D3DDDI_ISSUEQUERYFLAGS {
  union {
    struct {
      UINT  : 1  Begin;
      UINT  : 1  End;
      UINT  : 30 Reserved;
    };
    UINT Value;
  };
} D3DDDI_ISSUEQUERYFLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff543192">D3DDDIARG_ISSUEQUERY</a>