---
UID: NS:d3dukmdt.D3DDDI_MAKERESIDENT_FLAGS
title: D3DDDI_MAKERESIDENT_FLAGS
author: windows-driver-content
description: D3DDDI_MAKERESIDENT_FLAGS is used with MakeResident (pfnMakeResidentCb or D3DKMTMakeResident) to instruct the OS to add a resource to the device residency list and increment the residency reference count on this allocation.
old-location: display\d3dddi_makeresident_flags.htm
old-project: display
ms.assetid: 1EC4F8EE-1284-4752-8941-F1C31415BF29
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDI_MAKERESIDENT_FLAGS, D3DDDI_MAKERESIDENT_FLAGS structure [Display Devices], d3dukmdt/D3DDDI_MAKERESIDENT_FLAGS, display.d3dddi_makeresident_flags
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
-	D3DDDI_MAKERESIDENT_FLAGS
product:
- Windows
targetos: Windows
req.typenames: D3DDDI_MAKERESIDENT_FLAGS
---

# D3DDDI_MAKERESIDENT_FLAGS structure
<b>D3DDDI_MAKERESIDENT_FLAGS</b> is used with <b>MakeResident</b> (<a href="https://msdn.microsoft.com/8D65C3F7-3D07-4341-A989-A1438F821802">pfnMakeResidentCb</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/dn906775">D3DKMTMakeResident</a>) to instruct the OS to add a resource to the device residency list and increment the residency reference count on this allocation.

## Syntax
```
typedef struct D3DDDI_MAKERESIDENT_FLAGS {
  union {
    struct {
      UINT  : 1  CantTrimFurther;
      UINT  : 1  MustSucceed;
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

<a href="https://msdn.microsoft.com/library/windows/hardware/dn906775">D3DKMTMakeResident</a>



<a href="https://msdn.microsoft.com/8D65C3F7-3D07-4341-A989-A1438F821802">pfnMakeResidentCb</a>