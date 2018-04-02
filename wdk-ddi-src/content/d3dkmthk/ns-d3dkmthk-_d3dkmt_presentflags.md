---
UID: NS:d3dkmthk._D3DKMT_PRESENTFLAGS
title: "_D3DKMT_PRESENTFLAGS"
author: windows-driver-content
description: The D3DKMT_PRESENTFLAGS structure identifies how to perform a present operation.
old-location: display\d3dkmt_presentflags.htm
old-project: display
ms.assetid: 2ebee0bd-90f0-4628-8ddf-9e8029b4959a
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DKMT_PRESENTFLAGS, D3DKMT_PRESENTFLAGS structure [Display Devices], OpenGL_Structs_bd28ba63-6019-4cc5-b1d0-7275a5a575b3.xml, _D3DKMT_PRESENTFLAGS, d3dkmthk/D3DKMT_PRESENTFLAGS, display.d3dkmt_presentflags
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows Vista.
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
-	d3dkmthk.h
api_name:
-	D3DKMT_PRESENTFLAGS
product: Windows
targetos: Windows
req.typenames: D3DKMT_PRESENTFLAGS
---

# _D3DKMT_PRESENTFLAGS structure
The D3DKMT_PRESENTFLAGS structure identifies how to perform a present operation.

## Syntax
```
typedef struct _D3DKMT_PRESENTFLAGS {
  union {
    struct {
      UINT  : 1  Blt;
      UINT  : 1  ColorFill;
      UINT  : 1  Flip;
      UINT  : 1  FlipDoNotFlip;
      UINT  : 1  FlipDoNotWait;
      UINT  : 1  FlipRestart;
      UINT  : 1  DstRectValid;
      UINT  : 1  SrcRectValid;
      UINT  : 1  RestrictVidPnSource;
      UINT  : 1  SrcColorKey;
      UINT  : 1  DstColorKey;
      UINT  : 1  LinearToSrgb;
      UINT  : 1  PresentCountValid;
      UINT  : 1  Rotate;
      UINT  : 1  PresentToBitmap;
      UINT  : 1  RedirectedFlip;
      UINT  : 1  RedirectedBlt;
      UINT  : 1  FlipStereo;
      UINT  : 1  FlipStereoTemporaryMono;
      UINT  : 1  FlipStereoPreferRight;
      UINT  : 1  BltStereoUseRight;
      UINT  : 1  PresentHistoryTokenOnly;
      UINT  : 1  PresentRegionsValid;
      UINT  : 1  PresentDDA;
      UINT  : 1  ProtectedContentBlankedOut;
      UINT  : 1  RemoteSession;
      UINT  : 1  CrossAdapter;
      UINT  : 1  DurationValid;
      UINT  : 1  PresentIndirect;
      UINT  : 1  PresentHMD;
#if ...
      UINT  : 2  Reserved;
#elif
      UINT  : 6  Reserved;
#else
      UINT  : 15 Reserved;
#endif
    };
    UINT Value;
  };
} D3DKMT_PRESENTFLAGS;
```

## Members


## Remarks
If any of the <b>FlipStereo</b>, <b>FlipStereoTemporaryMono</b>, or <b>FlipStereoPreferRight</b>  members are set, these conditions apply:

<ul>
<li>The <b>hAllocation</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559484">DXGKARG_SETVIDPNSOURCEADDRESS</a> structure should point to an allocation that is created with the <b>Stereo</b> member set in the <b>Flags</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547942">D3DKMT_DISPLAYMODE</a> structure.</li>
<li>The <b>PrimarySegment</b> and <b>PrimaryAddress</b> members of <a href="https://msdn.microsoft.com/library/windows/hardware/ff559484">DXGKARG_SETVIDPNSOURCEADDRESS</a> should point to the starting physical address of the allocation.</li>
<li>The driver should honor the settings of the <b>FlipImmediate</b> and <b>FlipOnNextVSync</b> members of  the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562052">DXGK_SETVIDPNSOURCEADDRESS_FLAGS</a> structure.</li>
</ul>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows Vista. Available starting with Windows Vista. |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff546647">D3DKMDT_VIDPN_PRESENT_PATH</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff546719">D3DKMDT_VIDPN_PRESENT_PATH_TRANSFORMATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff547942">D3DKMT_DISPLAYMODE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff548168">D3DKMT_PRESENT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff559484">DXGKARG_SETVIDPNSOURCEADDRESS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff562052">DXGK_SETVIDPNSOURCEADDRESS_FLAGS</a>