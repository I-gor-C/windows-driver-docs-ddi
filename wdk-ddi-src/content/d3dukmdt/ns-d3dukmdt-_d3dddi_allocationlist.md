---
UID: NS:d3dukmdt._D3DDDI_ALLOCATIONLIST
title: "_D3DDDI_ALLOCATIONLIST"
author: windows-driver-content
description: The D3DDDI_ALLOCATIONLIST structure describes information about an allocation specification that is used in direct memory access (DMA) buffering.
old-location: display\d3dddi_allocationlist.htm
old-project: display
ms.assetid: 167ceb16-d7b9-4657-84cd-f3b9de5e5267
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDI_ALLOCATIONLIST, D3DDDI_ALLOCATIONLIST structure [Display Devices], D3D_other_Structs_0e766b30-b39d-4107-8739-0b9290e7d489.xml, _D3DDDI_ALLOCATIONLIST, d3dukmdt/D3DDDI_ALLOCATIONLIST, display.d3dddi_allocationlist
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: D3dumddi.h, D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows Vista.
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
-	d3dukmdt.h
api_name:
-	D3DDDI_ALLOCATIONLIST
product: Windows
targetos: Windows
req.typenames: D3DDDI_ALLOCATIONLIST
---

# _D3DDDI_ALLOCATIONLIST structure
The <b>D3DDDI_ALLOCATIONLIST</b> structure describes information about an allocation specification that is used in direct memory access (DMA) buffering.

## Syntax
```
typedef struct _D3DDDI_ALLOCATIONLIST {
  D3DKMT_HANDLE hAllocation;
  union {
    struct {
      UINT  : 1  WriteOperation;
      UINT  : 1  DoNotRetireInstance;
      UINT  : 3  OfferPriority;
      UINT  : 27 Reserved;
      UINT  : 30 Reserved;
    };
    UINT Value;
  };
} D3DDDI_ALLOCATIONLIST;
```

## Members


`hAllocation`

[in] The allocation handle returned by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547065">D3DKMTOpenResource</a> function in the <b>hAllocation</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544599">D3DDDI_OPENALLOCATIONINFO</a>   structure, or by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546807">D3DKMTCreateAllocation</a> function in the <b>hAllocation</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544364">D3DDDI_ALLOCATIONINFO</a> structure.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows Vista. Available starting with Windows Vista. |
| **Header** | d3dukmdt.h (include D3dumddi.h, D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/ce35bdac-af90-471f-af93-0e665be6c7f6">CreateDevice</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff542931">D3DDDIARG_CREATEDEVICE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544241">D3DDDICB_RENDER</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439275">D3DDDI_OFFER_PRIORITY</a>



<a href="https://msdn.microsoft.com/f242162e-6237-469c-b178-5a51dcf69e32">pfnRenderCb</a>