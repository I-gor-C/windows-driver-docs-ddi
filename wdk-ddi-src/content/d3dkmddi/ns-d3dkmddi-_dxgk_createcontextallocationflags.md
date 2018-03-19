---
UID: NS:d3dkmddi._DXGK_CREATECONTEXTALLOCATIONFLAGS
title: "_DXGK_CREATECONTEXTALLOCATIONFLAGS"
author: windows-driver-content
description: Specifies the properties of the context to be allocated.
old-location: display\dxgk_createcontextallocationflags.htm
old-project: display
ms.assetid: e80a314d-cef1-4289-84db-0a6b6531ae5f
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DXGK_CREATECONTEXTALLOCATIONFLAGS, DXGK_CREATECONTEXTALLOCATIONFLAGS structure [Display Devices], _DXGK_CREATECONTEXTALLOCATIONFLAGS, d3dkmddi/DXGK_CREATECONTEXTALLOCATIONFLAGS, display.dxgk_createcontextallocationflags
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
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
-	D3dkmddi.h
api_name:
-	DXGK_CREATECONTEXTALLOCATIONFLAGS
product: Windows
targetos: Windows
req.typenames: DXGK_CREATECONTEXTALLOCATIONFLAGS
---

# _DXGK_CREATECONTEXTALLOCATIONFLAGS structure
Specifies the properties of the context to be allocated.

## Syntax
````
typedef struct _DXGK_CREATECONTEXTALLOCATIONFLAGS {
  union {
    struct {
      UINT SharedAcrossContexts  :1;
      UINT Reserved  :31;
    };
    UINT Value;
  };
} DXGK_CREATECONTEXTALLOCATIONFLAGS;
````

## Members


## Remarks
The display miniport driver allocates GPU contexts or device-specific contexts by calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb_createcontextallocation.md">DxgkCbCreateContextAllocation</a>.

The <b>ContextAllocationFlags</b> member of the <a href="..\d3dkmddi\ns-d3dkmddi-_dxgkargcb_createcontextallocation.md">DXGKARGCB_CREATECONTEXTALLOCATION</a> structure is an <b>DXGK_CREATECONTEXTALLOCATIONFLAGS</b> data type.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="..\d3dkmddi\ns-d3dkmddi-_dxgkargcb_createcontextallocation.md">DXGKARGCB_CREATECONTEXTALLOCATION</a>



<a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb_createcontextallocation.md">DxgkCbCreateContextAllocation</a>