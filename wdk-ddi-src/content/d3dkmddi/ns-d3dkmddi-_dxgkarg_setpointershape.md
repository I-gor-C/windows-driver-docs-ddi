---
UID : NS:d3dkmddi._DXGKARG_SETPOINTERSHAPE
title : _DXGKARG_SETPOINTERSHAPE
author : windows-driver-content
description : The DXGKARG_SETPOINTERSHAPE structure describes the appearance of the mouse pointer and the location that it should be displayed in.
old-location : display\dxgkarg_setpointershape.htm
old-project : display
ms.assetid : fcb06620-8a30-4980-8733-35d7aabcc872
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _DXGKARG_SETPOINTERSHAPE, DXGKARG_SETPOINTERSHAPE
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
req.alt-api : DXGKARG_SETPOINTERSHAPE
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
req.typenames : DXGKARG_SETPOINTERSHAPE
---

# _DXGKARG_SETPOINTERSHAPE structure
The DXGKARG_SETPOINTERSHAPE structure describes the appearance of the mouse pointer and the location that it should be displayed in.

## Syntax
````
typedef struct _DXGKARG_SETPOINTERSHAPE {
  DXGK_POINTERFLAGS              Flags;
  UINT                           Width;
  UINT                           Height;
  UINT                           Pitch;
  D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId;
  const VOID                     *pPixels;
  UINT                           XHot;
  UINT                           YHot;
} DXGKARG_SETPOINTERSHAPE;
````

## Members

        
            `Flags`

            [in] A <a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_pointerflags.md">DXGK_POINTERFLAGS</a> structure that identifies, in bit-field flags, how to display the mouse pointer.
        
            `Height`

            [in] The height of the mouse pointer, in scan lines.
        
            `Pitch`

            [in] The width of the mouse pointer, in bytes.
        
            `pPixels`

            [in] A pointer to the start of the following bitmap depending on the bit-field flag that is set in the <b>Flags</b> member:

<table>
<tr>
<th>Bit-field flag</th>
<th>Bitmap</th>
</tr>
<tr>
<td>
<b>Monochrome</b>

</td>
<td>
        
            `VidPnSourceId`

            [in] The zero-based identification number of the video present source in a path of a video present network (VidPN) topology that the mouse pointer is located in.
        
            `Width`

            [in] The width of the mouse pointer, in pixels.
        
            `XHot`

            [in] The column, in pixels, that the mouse pointer is located on from the top left of the bitmap that <b>pPixels</b> points to.
        
            `YHot`

            [in] The row, in pixels, that the mouse pointer is located on from the top left of the bitmap that <b>pPixels</b> points to.

    ## Remarks
        The <b>XHot</b> and <b>YHot</b> members are used by display miniport drivers that are not associated with hardware, and these members can be ignored by drivers that control hardware.

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
<a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_pointerflags.md">DXGK_POINTERFLAGS</a>
</dt>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_setpointershape.md">DxgkDdiSetPointerShape</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARG_SETPOINTERSHAPE structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>