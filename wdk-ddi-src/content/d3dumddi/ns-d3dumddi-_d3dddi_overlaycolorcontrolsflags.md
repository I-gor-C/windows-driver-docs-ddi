---
UID : NS:d3dumddi._D3DDDI_OVERLAYCOLORCONTROLSFLAGS
title : "_D3DDDI_OVERLAYCOLORCONTROLSFLAGS"
author : windows-driver-content
description : The D3DDDI_OVERLAYCOLORCONTROLSFLAGS structure identifies color-control settings that the overlay hardware supports.
old-location : display\d3dddi_overlaycolorcontrolsflags.htm
old-project : display
ms.assetid : 12907aee-7c67-48f9-bf0f-84428f2d4fa7
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.d3dddi_overlaycolorcontrolsflags, _D3DDDI_OVERLAYCOLORCONTROLSFLAGS, D3D_other_Structs_ada675f2-18ed-4597-bcc4-803d8598ae66.xml, D3DDDI_OVERLAYCOLORCONTROLSFLAGS structure [Display Devices], d3dumddi/D3DDDI_OVERLAYCOLORCONTROLSFLAGS, D3DDDI_OVERLAYCOLORCONTROLSFLAGS
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
req.typenames : D3DDDI_OVERLAYCOLORCONTROLSFLAGS
---

# _D3DDDI_OVERLAYCOLORCONTROLSFLAGS structure
The D3DDDI_OVERLAYCOLORCONTROLSFLAGS structure identifies color-control settings that the overlay hardware supports.

## Syntax
````
typedef struct _D3DDDI_OVERLAYCOLORCONTROLSFLAGS {
  union {
    struct {
      UINT Brightness  :1;
      UINT Contrast  :1;
      UINT Hue  :1;
      UINT Saturation  :1;
      UINT Sharpness  :1;
      UINT Gamma  :1;
      UINT ColorEnable  :1;
      UINT Reserved  :25;
    };
    UINT   Value;
  };
} D3DDDI_OVERLAYCOLORCONTROLSFLAGS;
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

<a href="..\d3dumddi\ns-d3dumddi-_d3dddi_overlaycolorcontrols.md">D3DDDI_OVERLAYCOLORCONTROLS</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_OVERLAYCOLORCONTROLSFLAGS structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>