---
UID : NS:d3dkmddi._DXGK_PRESENTFLAGS
title : _DXGK_PRESENTFLAGS
author : windows-driver-content
description : The DXGK_PRESENTFLAGS structure identifies, in bit-field flags, the type of present operation to perform.
old-location : display\dxgk_presentflags.htm
old-project : display
ms.assetid : ff1fe315-7824-4e61-83f5-6d75aba2a941
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _DXGK_PRESENTFLAGS, DXGK_PRESENTFLAGS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3dkmddi.h
req.include-header : D3dkmddi.h
req.target-type : Windows
req.target-min-winverclnt : Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : DXGK_PRESENTFLAGS
req.alt-loc : d3dkmddi.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : DXGK_PRESENTFLAGS
---

# _DXGK_PRESENTFLAGS structure
The DXGK_PRESENTFLAGS structure identifies, in bit-field flags, the type of present operation to perform.

## Syntax
````
typedef struct _DXGK_PRESENTFLAGS {
  union {
    struct {
      UINT Blt  :1;
      UINT ColorFill  :1;
      UINT Flip  :1;
      UINT FlipWithNoWait  :1;
      UINT SrcColorKey  :1;
      UINT DstColorKey  :1;
      UINT LinearToSrgb  :1;
      UINT Rotate  :1;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WIN8)
      UINT FlipStereo  :1;
      UINT FlipStereoTemporaryMono  :1;
      UINT FlipStereoPreferRight  :1;
      UINT BltStereoUseRight  :1;
      UINT FlipWithMultiPlaneOverlay  :1;
      UINT Reserved  :19;
#else 
      UINT Reserved  :24;
#endif 
    };
    UINT Value;
  };
} DXGK_PRESENTFLAGS;
````

## Members


    ## Remarks
        The <b>ColorFill</b>, <b>SrcColorKey</b>, and <b>DstColorKey</b> bit-field flags are mutually exclusive.

If any of the <b>FlipStereo</b>, <b>FlipStereoTemporaryMono</b>, or <b>FlipStereoPreferRight</b>  members are set, these conditions apply:

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

    ## See Also

        <dl>
<dt>
<a href="..\d3dkmdt\ns-d3dkmdt-_d3dkmdt_vidpn_present_path.md">D3DKMDT_VIDPN_PRESENT_PATH</a>
</dt>
<dt>
<a href="..\d3dkmdt\ns-d3dkmdt-_d3dkmdt_vidpn_present_path_transformation.md">D3DKMDT_VIDPN_PRESENT_PATH_TRANSFORMATION</a>
</dt>
<dt>
<a href="..\d3dkmthk\ns-d3dkmthk-_d3dkmt_displaymode.md">D3DKMT_DISPLAYMODE</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_drivercaps.md">DXGK_DRIVERCAPS</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_setvidpnsourceaddress_flags.md">DXGK_SETVIDPNSOURCEADDRESS_FLAGS</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi-_dxgkarg_present.md">DXGKARG_PRESENT</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi-_dxgkarg_queryadapterinfo.md">DXGKARG_QUERYADAPTERINFO</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi-_dxgkarg_setvidpnsourceaddress.md">DXGKARG_SETVIDPNSOURCEADDRESS</a>
</dt>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_present.md">DxgkDdiPresent</a>
</dt>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_queryadapterinfo.md">DxgkDdiQueryAdapterInfo</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_PRESENTFLAGS structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>