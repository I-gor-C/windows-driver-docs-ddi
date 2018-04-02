---
UID: NS:d3dkmddi._DXGK_TRANSFERVIRTUALFLAGS
title: "_DXGK_TRANSFERVIRTUALFLAGS"
author: windows-driver-content
description: DXGK_TRANSFERVIRTUALFLAGS is used as part of an allocation transfer operation.
old-location: display\dxgk_transfervirtualflags.htm
old-project: display
ms.assetid: E5323A30-5BBE-4084-9F99-91FBDD680C12
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_TRANSFERVIRTUALFLAGS, DXGK_TRANSFERVIRTUALFLAGS structure [Display Devices], _DXGK_TRANSFERVIRTUALFLAGS, d3dkmddi/DXGK_TRANSFERVIRTUALFLAGS, display.dxgk_transfervirtualflags
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dkmddi.h
api_name:
-	DXGK_TRANSFERVIRTUALFLAGS
product: Windows
targetos: Windows
req.typenames: DXGK_TRANSFERVIRTUALFLAGS
---

# _DXGK_TRANSFERVIRTUALFLAGS structure
<b>DXGK_TRANSFERVIRTUALFLAGS</b> is used as part of an allocation transfer operation.

## Syntax
```
typedef struct _DXGK_TRANSFERVIRTUALFLAGS {
  union {
    struct {
      UINT  : 1  Src64KBPages;
      UINT  : 1  Dst64KBPages;
      UINT  : 30 Reserved;
    };
    UINT Flags;
  };
} DXGK_TRANSFERVIRTUALFLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |