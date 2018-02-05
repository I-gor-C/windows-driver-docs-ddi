---
UID : NS:d3dumddi._DXVADDI_VIDEOSAMPLEFLAGS
title : "_DXVADDI_VIDEOSAMPLEFLAGS"
author : windows-driver-content
description : The DXVADDI_VIDEOSAMPLEFLAGS structure identifies changes in the current sample frame from the previous sample frame.
old-location : display\dxvaddi_videosampleflags.htm
old-project : display
ms.assetid : 1dca2b12-0542-43a9-abff-203ea34cff90
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : DXVA2_Structs_8e0fce9f-8473-4bbc-9403-fb8755090a7d.xml, _DXVADDI_VIDEOSAMPLEFLAGS, d3dumddi/DXVADDI_VIDEOSAMPLEFLAGS, display.dxvaddi_videosampleflags, DXVADDI_VIDEOSAMPLEFLAGS structure [Display Devices], DXVADDI_VIDEOSAMPLEFLAGS
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
req.typenames : DXVADDI_VIDEOSAMPLEFLAGS
---

# _DXVADDI_VIDEOSAMPLEFLAGS structure
The DXVADDI_VIDEOSAMPLEFLAGS structure identifies changes in the current sample frame from the previous sample frame.

## Syntax
````
typedef struct _DXVADDI_VIDEOSAMPLEFLAGS {
  union {
    struct {
      UINT PaletteChanged  :1;
      UINT SrcRectChanged  :1;
      UINT DstRectChanged  :1;
      UINT ColorDataChanged  :1;
      UINT PlanarAlphaChanged  :1;
      UINT Reserved  :11;
      UINT SampleData  :16;
    };
    UINT   Value;
  };
} DXVADDI_VIDEOSAMPLEFLAGS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="..\d3dumddi\ns-d3dumddi-_dxvaddi_videosample.md">DXVADDI_VIDEOSAMPLE</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVADDI_VIDEOSAMPLEFLAGS structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>