---
UID: NS:d3dumddi._D3DDDIARG_VOLUMEBLT1
title: "_D3DDDIARG_VOLUMEBLT1"
author: windows-driver-content
description: Describes parameters for a volume bit-block transfer (bitblt) operation.
old-location: display\d3dddiarg_volumeblt1.htm
old-project: display
ms.assetid: 685aad54-03f5-4e3c-83a7-a44745acc4fb
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDIARG_VOLUMEBLT1, D3DDDIARG_VOLUMEBLT1 structure [Display Devices], _D3DDDIARG_VOLUMEBLT1, d3dumddi/D3DDDIARG_VOLUMEBLT1, display.d3dddiarg_volumeblt1
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
-	D3DDDIARG_VOLUMEBLT1
product:
- Windows
targetos: Windows
req.typenames: D3DDDIARG_VOLUMEBLT1
---

# _D3DDDIARG_VOLUMEBLT1 structure
Describes parameters for a volume bit-block transfer (bitblt) operation.

## Syntax
```
typedef struct _D3DDDIARG_VOLUMEBLT1 {
  HANDLE    hDstResource;
  HANDLE    hSrcResource;
  UINT      DstX;
  UINT      DstY;
  UINT      DstZ;
  D3DDDIBOX SrcBox;
  UINT      CopyFlags;
} D3DDDIARG_VOLUMEBLT1;
```

## Members


`hDstResource`

[in] A handle to the destination surface.

`hSrcResource`

[in] A handle to the source surface.

`DstX`

[in] The width, in screen coordinates, of the destination volume in which the source volume is copied.

`DstY`

[in] The height, in screen coordinates, of the destination volume in which the source volume is copied.

`DstZ`

[in] The depth, in screen coordinates, of the destination volume in which the source volume is copied.

`SrcBox`

[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/hh451148">D3DDDIBOX</a> structure that describes the source volume texture to copy to the destination.

`CopyFlags`

A value that specifies characteristics of a copy operation as a bitwise OR of the values in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451175">D3DDDI_COPY_FLAGS</a> enumeration type.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh451148">D3DDDIBOX</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh451175">D3DDDI_COPY_FLAGS</a>