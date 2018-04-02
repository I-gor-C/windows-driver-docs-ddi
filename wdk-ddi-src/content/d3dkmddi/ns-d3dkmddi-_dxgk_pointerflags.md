---
UID: NS:d3dkmddi._DXGK_POINTERFLAGS
title: "_DXGK_POINTERFLAGS"
author: windows-driver-content
description: The DXGK_POINTERFLAGS structure identifies mouse pointer capabilities of the display miniport driver that the driver provides through a call to its DxgkDdiQueryAdapterInfo function.
old-location: display\dxgk_pointerflags.htm
old-project: display
ms.assetid: 0d49a089-700e-42c0-a1f3-7b181b8aef96
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_POINTERFLAGS, DXGK_POINTERFLAGS structure [Display Devices], DmStructs_e2e2d800-cf64-44f9-95a2-a5eca8b8c303.xml, _DXGK_POINTERFLAGS, d3dkmddi/DXGK_POINTERFLAGS, display.dxgk_pointerflags
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
-	DXGK_POINTERFLAGS
product:
- Windows
targetos: Windows
req.typenames: DXGK_POINTERFLAGS
---

# _DXGK_POINTERFLAGS structure
The DXGK_POINTERFLAGS structure identifies mouse pointer capabilities of the display miniport driver that the driver provides through a call to its <a href="https://msdn.microsoft.com/f2f4c54c-7413-48e5-a165-d71f35642b6c">DxgkDdiQueryAdapterInfo</a> function.

## Syntax
```
typedef struct _DXGK_POINTERFLAGS {
  union {
    struct {
      UINT  : 1  Monochrome;
      UINT  : 1  Color;
      UINT  : 1  MaskedColor;
      UINT  : 29 Reserved;
    };
    UINT Value;
  };
} DXGK_POINTERFLAGS;
```

## Members


## Remarks
The display miniport driver can specify mouse pointer capabilities by setting bits in the 32-bit <b>Value</b> member or by setting individual members of the structure in the union that DXGK_POINTERFLAGS contains.

The driver always specifies a color mouse pointer by using a A8R8G8B8 pixel format.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff557621">DXGKARG_QUERYADAPTERINFO</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561062">DXGK_DRIVERCAPS</a>



<a href="https://msdn.microsoft.com/f2f4c54c-7413-48e5-a165-d71f35642b6c">DxgkDdiQueryAdapterInfo</a>