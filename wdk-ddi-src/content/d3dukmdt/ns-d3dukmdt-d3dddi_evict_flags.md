---
UID: NS:d3dukmdt.D3DDDI_EVICT_FLAGS
title: D3DDDI_EVICT_FLAGS
author: windows-driver-content
description: D3DDDI_EVICT_FLAGS specifies the eviction behavior.
old-location: display\d3dddi_evict_flags.htm
old-project: display
ms.assetid: 443671F1-98F5-4F9F-900B-37E3E50770CE
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDI_EVICT_FLAGS, D3DDDI_EVICT_FLAGS structure [Display Devices], d3dukmdt/D3DDDI_EVICT_FLAGS, display.d3dddi_evict_flags
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: D3dumddi.h, D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
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
-	d3dukmdt.h
api_name:
-	D3DDDI_EVICT_FLAGS
product: Windows
targetos: Windows
req.typenames: D3DDDI_EVICT_FLAGS
---

# D3DDDI_EVICT_FLAGS structure
<b>D3DDDI_EVICT_FLAGS</b> specifies the eviction behavior.

## Syntax
```
typedef struct D3DDDI_EVICT_FLAGS {
  union {
    struct {
      UINT  : 1  EvictOnlyIfNecessary;
      UINT  : 1  NotWrittenTo;
      UINT  : 30 Reserved;
    };
    UINT Value;
  };
};
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | d3dukmdt.h (include D3dumddi.h, D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn906774">D3DKMTEvict</a>



<a href="https://msdn.microsoft.com/5E66A522-BC1C-4E7C-8732-87D40F99BBDA">pfnEvictCb</a>