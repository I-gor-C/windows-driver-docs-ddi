---
UID : NS:d3dumddi._DXVADDI_VIDEOPROCESSBLTFLAGS
title : _DXVADDI_VIDEOPROCESSBLTFLAGS
author : windows-driver-content
description : The DXVADDI_VIDEOPROCESSBLTFLAGS structure identifies changes in the current destination surface from the previous destination surface.
old-location : display\dxvaddi_videoprocessbltflags.htm
old-project : display
ms.assetid : 790a18fa-5481-432a-921b-6310a0ab78d7
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _DXVADDI_VIDEOPROCESSBLTFLAGS, DXVADDI_VIDEOPROCESSBLTFLAGS
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
req.alt-api : DXVADDI_VIDEOPROCESSBLTFLAGS
req.alt-loc : d3dumddi.h
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
req.typenames : DXVADDI_VIDEOPROCESSBLTFLAGS
---

# _DXVADDI_VIDEOPROCESSBLTFLAGS structure
The DXVADDI_VIDEOPROCESSBLTFLAGS structure identifies changes in the current destination surface from the previous destination surface.

## Syntax
````
typedef struct _DXVADDI_VIDEOPROCESSBLTFLAGS {
  union {
    struct {
      UINT BackgroundChanged  :1;
      UINT TargetRectChanged  :1;
      UINT ColorDataChanged  :1;
      UINT AlphaChanged  :1;
      UINT Reserved  :12;
      UINT DestData  :16;
    };
    UINT   Value;
  };
} DXVADDI_VIDEOPROCESSBLTFLAGS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dumddi.h (include D3dumddi.h) |

    ## See Also

        <dl>
<dt>
<a href="..\d3dumddi\ns-d3dumddi-_d3dddiarg_videoprocessblt.md">D3DDDIARG_VIDEOPROCESSBLT</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVADDI_VIDEOPROCESSBLTFLAGS structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>