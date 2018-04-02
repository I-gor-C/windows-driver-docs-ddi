---
UID: NS:d3dkmddi._DXGK_DISCARDCONTENTFLAGS
title: "_DXGK_DISCARDCONTENTFLAGS"
author: windows-driver-content
description: The DXGK_DISCARDCONTENTFLAGS structure identifies the type of discard-content operation to set up in a call to the DxgkDdiBuildPagingBuffer function.
old-location: display\dxgk_discardcontentflags.htm
old-project: display
ms.assetid: 0a93d3a2-0274-4b14-9c4b-9ed31a48e600
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_DISCARDCONTENTFLAGS, DXGK_DISCARDCONTENTFLAGS structure [Display Devices], DmStructs_9ff479c6-8592-4ebd-b001-c0a7d58772f2.xml, _DXGK_DISCARDCONTENTFLAGS, d3dkmddi/DXGK_DISCARDCONTENTFLAGS, display.dxgk_discardcontentflags
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dkmddi.h
api_name:
-	DXGK_DISCARDCONTENTFLAGS
product: Windows
targetos: Windows
req.typenames: DXGK_DISCARDCONTENTFLAGS
---

# _DXGK_DISCARDCONTENTFLAGS structure
The DXGK_DISCARDCONTENTFLAGS structure identifies the type of discard-content operation to set up in a call to the <a href="https://msdn.microsoft.com/d315ff53-4a9f-46a3-ad74-d65a5eb72de1">DxgkDdiBuildPagingBuffer</a> function.

## Syntax
```
typedef struct _DXGK_DISCARDCONTENTFLAGS {
  union {
    struct {
      UINT  : 1  AllocationIsIdle;
      UINT  : 31 Reserved;
    };
    UINT Value;
  };
} DXGK_DISCARDCONTENTFLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff557540">DXGKARG_BUILDPAGINGBUFFER</a>



<a href="https://msdn.microsoft.com/d315ff53-4a9f-46a3-ad74-d65a5eb72de1">DxgkDdiBuildPagingBuffer</a>