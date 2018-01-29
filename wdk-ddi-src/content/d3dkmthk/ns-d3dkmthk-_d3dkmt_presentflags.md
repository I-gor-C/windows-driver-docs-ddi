---
UID : NS:d3dkmthk._D3DKMT_PRESENTFLAGS
title : _D3DKMT_PRESENTFLAGS
author : windows-driver-content
description : The D3DKMT_PRESENTFLAGS structure identifies how to perform a present operation.
old-location : display\d3dkmt_presentflags.htm
old-project : display
ms.assetid : 2ebee0bd-90f0-4628-8ddf-9e8029b4959a
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : D3DKMT_PRESENTFLAGS, D3DKMT_PRESENTFLAGS structure [Display Devices], _D3DKMT_PRESENTFLAGS, OpenGL_Structs_bd28ba63-6019-4cc5-b1d0-7275a5a575b3.xml, display.d3dkmt_presentflags, d3dkmthk/D3DKMT_PRESENTFLAGS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3dkmthk.h
req.include-header : D3dkmthk.h
req.target-type : Windows
req.target-min-winverclnt : Available starting with Windows Vista.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : D3DKMT_PRESENTFLAGS
---

# _D3DKMT_PRESENTFLAGS structure
The D3DKMT_PRESENTFLAGS structure identifies how to perform a present operation.

## Syntax
````
typedef struct _D3DKMT_PRESENTFLAGS {
  union {
    struct {
      UINT Blt  :1;
      UINT ColorFill  :1;
      UINT Flip  :1;
      UINT FlipDoNotFlip  :1;
      UINT FlipDoNotWait  :1;
      UINT FlipRestart  :1;
      UINT DstRectValid  :1;
      UINT SrcRectValid  :1;
      UINT RestrictVidPnSource  :1;
      UINT SrcColorKey  :1;
      UINT DstColorKey  :1;
      UINT LinearToSrgb  :1;
      UINT PresentCountValid  :1;
      UINT Rotate  :1;
      UINT PresentToBitmap  :1;
      UINT RedirectedFlip  :1;
      UINT RedirectedBlt  :1;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WIN8)
      UINT FlipStereo  :1;
      UINT FlipStereoTemporaryMono  :1;
      UINT FlipStereoPreferRight  :1;
      UINT BltStereoUseRight  :1;
      UINT PresentHistoryTokenOnly  :1;
      UINT PresentRegionsValid  :1;
      UINT PresentDDA  :1;
      UINT ProtectedContentBlankedOut  :1;
      UINT RemoteSession  :1;
      UINT Reserved  :6;
#else 
      UINT Reserved  :15;
#endif 
    };
    UINT   Value;
  };
} D3DKMT_PRESENTFLAGS;
````

## Members


## Remarks
If any of the <b>FlipStereo</b>, <b>FlipStereoTemporaryMono</b>, or <b>FlipStereoPreferRight</b>  members are set, these conditions apply:
<ul>
<li>The <b>hAllocation</b> member of the <a href="..\d3dkmddi\ns-d3dkmddi-_dxgkarg_setvidpnsourceaddress.md">DXGKARG_SETVIDPNSOURCEADDRESS</a> structure should point to an allocation that is created with the <b>Stereo</b> member set in the <b>Flags</b> member of the <a href="..\d3dkmthk\ns-d3dkmthk-_d3dkmt_displaymode.md">D3DKMT_DISPLAYMODE</a> structure.</li>
<li>The <b>PrimarySegment</b> and <b>PrimaryAddress</b> members of <a href="..\d3dkmddi\ns-d3dkmddi-_dxgkarg_setvidpnsourceaddress.md">DXGKARG_SETVIDPNSOURCEADDRESS</a> should point to the starting physical address of the allocation.</li>
<li>The driver should honor the settings of the <b>FlipImmediate</b> and <b>FlipOnNextVSync</b> members of  the <a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_setvidpnsourceaddress_flags.md">DXGK_SETVIDPNSOURCEADDRESS_FLAGS</a> structure.</li>
</ul>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |

## See Also

<a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_setvidpnsourceaddress_flags.md">DXGK_SETVIDPNSOURCEADDRESS_FLAGS</a>

<a href="..\d3dkmthk\ns-d3dkmthk-_d3dkmt_present.md">D3DKMT_PRESENT</a>

<a href="..\d3dkmdt\ns-d3dkmdt-_d3dkmdt_vidpn_present_path.md">D3DKMDT_VIDPN_PRESENT_PATH</a>

<a href="..\d3dkmdt\ns-d3dkmdt-_d3dkmdt_vidpn_present_path_transformation.md">D3DKMDT_VIDPN_PRESENT_PATH_TRANSFORMATION</a>

<a href="..\d3dkmthk\ns-d3dkmthk-_d3dkmt_displaymode.md">D3DKMT_DISPLAYMODE</a>

<a href="..\d3dkmddi\ns-d3dkmddi-_dxgkarg_setvidpnsourceaddress.md">DXGKARG_SETVIDPNSOURCEADDRESS</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_PRESENTFLAGS structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>