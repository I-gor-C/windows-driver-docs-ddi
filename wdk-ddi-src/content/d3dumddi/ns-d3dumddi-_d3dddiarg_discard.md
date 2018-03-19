---
UID: NS:d3dumddi._D3DDDIARG_DISCARD
title: "_D3DDDIARG_DISCARD"
author: windows-driver-content
description: Defines video display memory that can be discarded because the contents are no longer needed.
old-location: display\d3dddiarg_discard.htm
old-project: display
ms.assetid: 6efee74e-9e82-4631-8360-19061b0c015d
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: D3DDDIARG_DISCARD, D3DDDIARG_DISCARD structure [Display Devices], _D3DDDIARG_DISCARD, d3dumddi/D3DDDIARG_DISCARD, display.d3dddiarg_discard
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	D3dumddi.h
api_name:
-	D3DDDIARG_DISCARD
product: Windows
targetos: Windows
req.typenames: D3DDDIARG_DISCARD
---

# _D3DDDIARG_DISCARD structure
Defines video display memory that can be discarded because the contents are no longer needed.

## Syntax
````
typedef struct _D3DDDIARG_DISCARD {
  HANDLE     hResource;
  UINT       FirstSubResource;
  UINT       NumSubResources;
  const RECT *pRects;
  UINT       NumRects;
} D3DDDIARG_DISCARD;
````

## Members


`hResource`

A handle to the resource in which subresources are to be discarded.

`FirstSubResource`

The index of the first subresource to be discarded.

`NumSubResources`

The number of subresources to be discarded.

`pRects`

An array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a> structures for the rectangles in the resource view to discard. If <b>NULL</b>, the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_discard.md">Discard</a> function discards the entire surface.

`NumRects`

The number of rectangles in the array that the  <b>pRects</b> member specifies.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a>



<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_discard.md">Discard</a>