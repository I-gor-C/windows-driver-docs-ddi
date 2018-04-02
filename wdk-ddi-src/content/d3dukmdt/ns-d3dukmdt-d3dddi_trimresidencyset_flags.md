---
UID: NS:d3dukmdt.D3DDDI_TRIMRESIDENCYSET_FLAGS
title: D3DDDI_TRIMRESIDENCYSET_FLAGS
author: windows-driver-content
description: D3DDDI_TRIMRESIDENCYSET_FLAGS is used with pfnTrimResidencySet to trim the residency list for a given device.
old-location: display\d3dddi_trimresidencyset_flags.htm
old-project: display
ms.assetid: B063561B-FA79-44B4-A058-71DB9CBF4804
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDI_TRIMRESIDENCYSET_FLAGS, D3DDDI_TRIMRESIDENCYSET_FLAGS structure [Display Devices], d3dukmdt/D3DDDI_TRIMRESIDENCYSET_FLAGS, display.d3dddi_trimresidencyset_flags
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
-	D3DDDI_TRIMRESIDENCYSET_FLAGS
product:
- Windows
targetos: Windows
req.typenames: D3DDDI_TRIMRESIDENCYSET_FLAGS
---

# D3DDDI_TRIMRESIDENCYSET_FLAGS structure
<b>D3DDDI_TRIMRESIDENCYSET_FLAGS</b> is used with <a href="https://msdn.microsoft.com/192F419C-F38F-4B42-8111-86D58D6781DA">pfnTrimResidencySet</a> to trim the residency list for a given device.

## Syntax
```
typedef struct D3DDDI_TRIMRESIDENCYSET_FLAGS {
  union {
    struct {
      UINT  : 1  PeriodicTrim;
      UINT  : 1  RestartPeriodicTrim;
      UINT  : 1  TrimToBudget;
      UINT  : 29 Reserved;
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

<a href="https://msdn.microsoft.com/192F419C-F38F-4B42-8111-86D58D6781DA">pfnTrimResidencySet</a>