---
UID : NS:d3dumddi._FORMATOP
title : _FORMATOP
author : windows-driver-content
description : The FORMATOP structure describes a surface format and operations that can be performed with such a surface.
old-location : display\formatop.htm
old-project : display
ms.assetid : e846a41a-9d9c-4ccb-a478-260f333333f1
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : d3dumddi/FORMATOP, FORMATOP_PLANAR (0x02000000L), FORMATOP_CAPTURE (0x08000000L), FORMATOP_MEMBEROFGROUP_ARGB (0x00080000L), FORMATOP_SAME_FORMAT_RENDERTARGET (0x00000010L), FORMATOP_MULTIPLANE_OVERLAY (0x20000000L), FORMATOP_CONVERT_TO_ARGB (0x00002000L), FORMATOP_ZSTENCIL_WITH_ARBITRARY_COLOR_DEPTH (0x00000080L), FORMATOP_PIXELSIZE (0x00001000L), FORMATOP_VOLUMETEXTURE (0x00000002L), display.formatop, FORMATOP_SAME_FORMAT_UP_TO_ALPHA_RENDERTARGET (0x00000100L), FORMATOP_BUMPMAP (0x00010000L), _FORMATOP, FORMATOP, FORMATOP_SRGBWRITE (0x00100000L), FORMATOP_NOFILTER (0x00040000L), FORMATOP_CUBETEXTURE (0x00000004L), FORMATOP_TEXTURE (0x00000001L), FORMATOP_ZSTENCIL (0x00000040L), FORMATOP_3DACCELERATION (0x00000800L), FORMATOP_VIDEO_ENCODER (0x10000000L), FORMATOP_OVERLAY (0x04000000L), FORMATOP_OFFSCREEN_RENDERTARGET (0x00000008L), FORMATOP_SRGBREAD (0x00008000L), FORMATOP_NOALPHABLEND (0x00200000L), FORMATOP_DMAP (0x00020000L), FORMATOP structure [Display Devices], D3D_other_Structs_c60ed644-61b9-4700-8944-131765951138.xml, FORMATOP_NOTEXCOORDWRAPNORMIP (0x01000000L), FORMATOP_DISPLAYMODE (0x00000400L), FORMATOP_AUTOGENMIPMAP (0x00400000L), FORMATOP_OFFSCREENPLAIN (0x00004000L), FORMATOP_VERTEXTEXTURE (0x00800000L)
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3dumddi.h
req.include-header : D3dumddi.h
req.target-type : Windows
req.target-min-winverclnt : Available in Windows Vista and later versions of the Windows operating systems.
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
req.typenames : FORMATOP
---

# _FORMATOP structure
The <b>FORMATOP</b> structure describes a surface format and operations that can be performed with such a surface.

## Syntax
````
typedef struct _FORMATOP {
  D3DDDIFORMAT Format;
  UINT         Operations;
  UINT         FlipMsTypes;
  UINT         BltMsTypes;
  UINT         PrivateFormatBitCount;
} FORMATOP;
````

## Members


`BltMsTypes`

[out] A 32-bitmask for windowed multiple sampling.

`FlipMsTypes`

[out] A 32-bitmask for full-screen multiple sampling.

`Format`

[in] The <a href="..\d3dukmdt\ne-d3dukmdt-_d3dddiformat.md">D3DDDIFORMAT</a>-typed value that indicates the pixel format of the surface.

`Operations`

[out] A valid bitwise <b>OR</b> of the following flags that indicate the operations that can be performed on surfaces with the pixel format that is specified in the <b>Format</b> member. Some of the following flags imply that other flags should be used. If a driver sets a flag that implies other flags, the driver is not required to set the implied flags, and the Direct3D runtime determines the use of the implied flags.

`PrivateFormatBitCount`

[out] The bits per pixel of a pixel format that is private to the driver (that is, not one of the standard pixel formats that are defined by the <a href="..\d3dukmdt\ne-d3dukmdt-_d3dddiformat.md">D3DDDIFORMAT</a> enumeration type).


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="..\d3dumddi\ns-d3dumddi-_d3dddiarg_getcaps.md">D3DDDIARG_GETCAPS</a>

<a href="..\d3dukmdt\ne-d3dukmdt-_d3dddiformat.md">D3DDDIFORMAT</a>

<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_getcaps.md">GetCaps</a>

<a href="..\d3dukmdt\ns-d3dukmdt-_d3dddi_resourceflags2.md">D3DDDI_RESOURCEFLAGS2</a>

<a href="..\d3dumddi\ne-d3dumddi-_d3dddicaps_type.md">D3DDDICAPS_TYPE</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20FORMATOP structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>