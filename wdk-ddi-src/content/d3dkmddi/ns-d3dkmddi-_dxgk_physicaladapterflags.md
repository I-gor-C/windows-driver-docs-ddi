---
UID: NS:d3dkmddi._DXGK_PHYSICALADAPTERFLAGS
title: "_DXGK_PHYSICALADAPTERFLAGS"
author: windows-driver-content
description: DXGK_PHYSICALADAPTERFLAGS defines a set of flags that used to indicate the type of memory management model that is supported by a device.
old-location: display\dxgk_physicaladapterflags.htm
old-project: display
ms.assetid: AACF0C99-D6E2-4C7C-BAE6-BF558FDAFDE0
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: DXGK_PHYSICALADAPTERFLAGS, DXGK_PHYSICALADAPTERFLAGS structure [Display Devices], _DXGK_PHYSICALADAPTERFLAGS, display.dxgk_physicaladapterflags, d3dkmddi/DXGK_PHYSICALADAPTERFLAGS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
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
req.irql: PASSIVE_LEVEL
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	d3dkmddi.h
apiname:
-	DXGK_PHYSICALADAPTERFLAGS
product: Windows
targetos: Windows
req.typenames: DXGK_PHYSICALADAPTERFLAGS
---

# _DXGK_PHYSICALADAPTERFLAGS structure
<b>DXGK_PHYSICALADAPTERFLAGS</b> defines a set of flags that used to indicate the type of memory management model that is supported by a device.

## Syntax
````
typedef struct _DXGK_PHYSICALADAPTERFLAGS {
  union {
    struct {
      UINT IoMmuSupported  :1;
      UINT GpuMmuSupported  :1;
      UINT MovingPagingSupported  :1;
      UINT VPRPagingContextRequired  :1;
      UINT Reserved  :28;
    };
    UINT   Value;
  };
} DXGK_PHYSICALADAPTERFLAGS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |