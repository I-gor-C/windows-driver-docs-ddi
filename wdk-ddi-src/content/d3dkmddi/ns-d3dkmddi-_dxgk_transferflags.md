---
UID: NS:d3dkmddi._DXGK_TRANSFERFLAGS
title: "_DXGK_TRANSFERFLAGS"
author: windows-driver-content
description: The DXGK_TRANSFERFLAGS structure identifies the type of transfer operation to set up in a call to the DxgkDdiBuildPagingBuffer function.
old-location: display\dxgk_transferflags.htm
old-project: display
ms.assetid: b56657ac-98ff-482a-a2af-ffbfb8602248
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_TRANSFERFLAGS, DXGK_TRANSFERFLAGS structure [Display Devices], DmStructs_91973ccf-775f-4e97-bb1a-17cd1343a4f8.xml, _DXGK_TRANSFERFLAGS, d3dkmddi/DXGK_TRANSFERFLAGS, display.dxgk_transferflags
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
-	DXGK_TRANSFERFLAGS
product:
- Windows
targetos: Windows
req.typenames: DXGK_TRANSFERFLAGS
---

# _DXGK_TRANSFERFLAGS structure
The DXGK_TRANSFERFLAGS structure identifies the type of transfer operation to set up in a call to the <a href="https://msdn.microsoft.com/d315ff53-4a9f-46a3-ad74-d65a5eb72de1">DxgkDdiBuildPagingBuffer</a> function.

## Syntax
```
typedef struct _DXGK_TRANSFERFLAGS {
  union {
    struct {
      UINT  : 1  Swizzle;
      UINT  : 1  Unswizzle;
      UINT  : 1  AllocationIsIdle;
      UINT  : 1  TransferStart;
      UINT  : 1  TransferEnd;
      UINT  : 27 Reserved;
    };
    UINT Value;
  };
} DXGK_TRANSFERFLAGS;
```

## Members


## Remarks
You can set the transfer-operation type by setting bits in the 32-bit <b>Value</b> member or by setting individual members of the structure in the union that DXGK_TRANSFERFLAGS contains.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff557540">DXGKARG_BUILDPAGINGBUFFER</a>



<a href="https://msdn.microsoft.com/d315ff53-4a9f-46a3-ad74-d65a5eb72de1">DxgkDdiBuildPagingBuffer</a>