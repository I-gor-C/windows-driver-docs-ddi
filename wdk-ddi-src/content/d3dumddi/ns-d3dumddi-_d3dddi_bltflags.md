---
UID: NS:d3dumddi._D3DDDI_BLTFLAGS
title: "_D3DDDI_BLTFLAGS"
author: windows-driver-content
description: The D3DDDI_BLTFLAGS structure identifies the type of bit-block transfer (bitblt) to perform.
old-location: display\d3dddi_bltflags.htm
old-project: display
ms.assetid: 844d6aed-2ca2-45ef-bd53-54344dbdadbf
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDI_BLTFLAGS, D3DDDI_BLTFLAGS structure [Display Devices], D3D_other_Structs_8d70fa64-3813-4165-a64d-4e91287e05d5.xml, _D3DDDI_BLTFLAGS, d3dumddi/D3DDDI_BLTFLAGS, display.d3dddi_bltflags
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
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
-	d3dumddi.h
api_name:
-	D3DDDI_BLTFLAGS
product:
- Windows
targetos: Windows
req.typenames: D3DDDI_BLTFLAGS
---

# _D3DDDI_BLTFLAGS structure
The D3DDDI_BLTFLAGS structure identifies the type of bit-block transfer (bitblt) to perform.

## Syntax
```
typedef struct _D3DDDI_BLTFLAGS {
  union {
    struct {
      UINT  : 1  Point;
      UINT  : 1  Linear;
      UINT  : 1  SrcColorKey;
      UINT  : 1  DstColorKey;
      UINT  : 1  MirrorLeftRight;
      UINT  : 1  MirrorUpDown;
      UINT  : 1  LinearToSrgb;
      UINT  : 1  Rotate;
      UINT  : 1  BeginPresentToDwm;
      UINT  : 1  ContinuePresentToDwm;
      UINT  : 1  EndPresentToDwm;
      UINT  : 21 Reserved;
      UINT  : 1  Discard;
      UINT  : 1  NoOverwrite;
      UINT  : 1  Tileable;
      UINT  : 18 Reserved;
    };
    UINT Value;
  };
} D3DDDI_BLTFLAGS;
```

## Members


## Remarks
The <b>BeginPresentToDwm</b>, <b>ContinuePresentToDwm</b>, and <b>EndPresentToDwm</b> bit-field flags inform the user-mode display driver about the time when the Direct3D runtime performs parts of a DWM present operation.  Because DWM present operations can occur in multiple steps, the Direct3D runtime uses these flags to mark the steps in a sequence of bitblts. For example:  

<ul>
<li>If the present operation consists of one bitblt, the bitblt is marked as follows:<ul>
<li><b>BeginPresentToDwm</b> = <b>TRUE</b>;</li>
<li><b>ContinuePresentToDwm</b> = <b>FALSE</b>;</li>
<li><b>EndPresentToDwm</b> = <b>TRUE</b>;</li>
</ul>
</li>
<li>If the present operation consists of two bitblts, the bitblts are marked as shown in two sequential bitblt operations:<ol>
<li>First bitblt:<ul>
<li><b>BeginPresentToDwm</b> = <b>TRUE</b>;</li>
<li><b>ContinuePresentToDwm</b> = <b>FALSE</b>;</li>
<li><b>EndPresentToDwm</b> = <b>FALSE</b>;</li>
</ul>
</li>
<li>Second bitblt:<ul>
<li><b>BeginPresentToDwm</b> = <b>FALSE</b>;</li>
<li><b>ContinuePresentToDwm</b> = <b>FALSE</b>;</li>
<li><b>EndPresentToDwm</b> = <b>TRUE</b>;</li>
</ul>
</li>
</ol>
</li>
<li>If the present operation consists of three or more bitblts, the bitblts are marked as shown in the following sequential bitblt operations:<ol>
<li>First bitblt:<ul>
<li><b>BeginPresentToDwm</b> = <b>TRUE</b>;</li>
<li><b>ContinuePresentToDwm</b> = <b>FALSE</b>;</li>
<li><b>EndPresentToDwm</b> = <b>FALSE</b>;</li>
</ul>
</li>
<li>Second and successive bitblts, not including the final bitblt:<ul>
<li><b>BeginPresentToDwm</b> = <b>FALSE</b>;</li>
<li><b>ContinuePresentToDwm</b> = <b>TRUE</b>;</li>
<li><b>EndPresentToDwm</b> = <b>FALSE</b>;</li>
</ul>
</li>
<li>Final bitblt:<ul>
<li><b>BeginPresentToDwm</b> = <b>FALSE</b>;</li>
<li><b>ContinuePresentToDwm</b> = <b>FALSE</b>;</li>
<li><b>EndPresentToDwm</b> = <b>TRUE</b>;</li>
</ul>
</li>
</ol>
</li>
</ul>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows Vista. Available starting with Windows Vista. |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff542884">D3DDDIARG_BLT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh463886">Flush</a>