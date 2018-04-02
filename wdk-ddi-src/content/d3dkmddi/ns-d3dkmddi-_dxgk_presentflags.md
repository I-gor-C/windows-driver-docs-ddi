---
UID: NS:d3dkmddi._DXGK_PRESENTFLAGS
title: "_DXGK_PRESENTFLAGS"
author: windows-driver-content
description: The DXGK_PRESENTFLAGS structure identifies, in bit-field flags, the type of present operation to perform.
old-location: display\dxgk_presentflags.htm
old-project: display
ms.assetid: ff1fe315-7824-4e61-83f5-6d75aba2a941
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_PRESENTFLAGS, DXGK_PRESENTFLAGS structure [Display Devices], DmStructs_b8913202-bee3-4584-b323-6c6fb47a5c8d.xml, _DXGK_PRESENTFLAGS, d3dkmddi/DXGK_PRESENTFLAGS, display.dxgk_presentflags
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
-	DXGK_PRESENTFLAGS
product: Windows
targetos: Windows
req.typenames: DXGK_PRESENTFLAGS
---

# _DXGK_PRESENTFLAGS structure
The DXGK_PRESENTFLAGS structure identifies, in bit-field flags, the type of present operation to perform.

## Syntax
```
typedef struct _DXGK_PRESENTFLAGS {
  union {
    struct {
      UINT  : 1  Blt;
      UINT  : 1  ColorFill;
      UINT  : 1  Flip;
      UINT  : 1  FlipWithNoWait;
      UINT  : 1  SrcColorKey;
      UINT  : 1  DstColorKey;
      UINT  : 1  LinearToSrgb;
      UINT  : 1  Rotate;
      UINT  : 1  FlipStereo;
      UINT  : 1  FlipStereoTemporaryMono;
      UINT  : 1  FlipStereoPreferRight;
      UINT  : 1  BltStereoUseRight;
      UINT  : 1  FlipWithMultiPlaneOverlay;
      UINT  : 1  RedirectedFlip;
#if ...
      UINT  : 18 Reserved;
#elif
      UINT  : 19 Reserved;
#else
      UINT  : 24 Reserved;
#endif
    };
    UINT Value;
  };
} DXGK_PRESENTFLAGS;
```

## Members


## Remarks
The <b>ColorFill</b>, <b>SrcColorKey</b>, and <b>DstColorKey</b> bit-field flags are mutually exclusive.

If any of the <b>FlipStereo</b>, <b>FlipStereoTemporaryMono</b>, or <b>FlipStereoPreferRight</b>  members are set, these conditions apply:

<ul>
<li>The <b>hAllocation</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559484">DXGKARG_SETVIDPNSOURCEADDRESS</a> structure should point to an allocation that is created with the <b>Stereo</b> member set in the <b>Flags</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547942">D3DKMT_DISPLAYMODE</a> structure.</li>
<li>The <b>PrimarySegment</b> and <b>PrimaryAddress</b> members of <a href="https://msdn.microsoft.com/library/windows/hardware/ff559484">DXGKARG_SETVIDPNSOURCEADDRESS</a> should point to the starting physical address of the allocation.</li>
<li>The driver should honor the settings of the <b>FlipImmediate</b> and <b>FlipOnNextVSync</b> members of  the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562052">DXGK_SETVIDPNSOURCEADDRESS_FLAGS</a> structure.</li>
</ul>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff546647">D3DKMDT_VIDPN_PRESENT_PATH</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff546719">D3DKMDT_VIDPN_PRESENT_PATH_TRANSFORMATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff547942">D3DKMT_DISPLAYMODE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff557618">DXGKARG_PRESENT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff557621">DXGKARG_QUERYADAPTERINFO</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff559484">DXGKARG_SETVIDPNSOURCEADDRESS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561062">DXGK_DRIVERCAPS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff562052">DXGK_SETVIDPNSOURCEADDRESS_FLAGS</a>



<a href="https://msdn.microsoft.com/1a46b129-1e78-44e6-a609-59eab206692b">DxgkDdiPresent</a>



<a href="https://msdn.microsoft.com/f2f4c54c-7413-48e5-a165-d71f35642b6c">DxgkDdiQueryAdapterInfo</a>