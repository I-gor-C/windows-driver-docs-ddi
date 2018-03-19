---
UID: NS:d3dkmddi._DXGKARG_FLIPOVERLAY
title: "_DXGKARG_FLIPOVERLAY"
author: windows-driver-content
description: The DXGKARG_FLIPOVERLAY structure describes a new allocation to display for the overlay.
old-location: display\dxgkarg_flipoverlay.htm
old-project: display
ms.assetid: c5396581-e9f2-47eb-bb82-1e54f5def4d0
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DXGKARG_FLIPOVERLAY, DXGKARG_FLIPOVERLAY structure [Display Devices], DmStructs_8ff06344-e7f5-44b1-95fc-d3b363428d43.xml, _DXGKARG_FLIPOVERLAY, d3dkmddi/DXGKARG_FLIPOVERLAY, display.dxgkarg_flipoverlay
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
-	DXGKARG_FLIPOVERLAY
product: Windows
targetos: Windows
req.typenames: DXGKARG_FLIPOVERLAY
---

# _DXGKARG_FLIPOVERLAY structure
The DXGKARG_FLIPOVERLAY structure describes a new allocation to display for the overlay.

## Syntax
````
typedef struct _DXGKARG_FLIPOVERLAY {
  HANDLE           hSource;
  PHYSICAL_ADDRESS SrcPhysicalAddress;
  UINT             SrcSegmentId;
  VOID             *pPrivateDriverData;
  UINT             PrivateDriverDataSize;
} DXGKARG_FLIPOVERLAY;
````

## Members


`hSource`

[in] A handle to the source allocation to be displayed.

`SrcPhysicalAddress`

[in] The physical address, within the segment that <b>SrcSegmentId</b> specifies, of the allocation to be displayed.

`SrcSegmentId`

[in] The identifier of a segment in which the allocation is currently paged.

`pPrivateDriverData`

[in] A pointer to a block of private data that is passed from the user-mode display driver to the display miniport driver.

`PrivateDriverDataSize`

[in] The size, in bytes, of the block of private data that <b>pPrivateDriverData</b> points to.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_flipoverlay.md">DxgkDdiFlipOverlay</a>