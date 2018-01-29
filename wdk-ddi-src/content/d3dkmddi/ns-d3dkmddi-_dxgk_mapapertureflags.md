---
UID : NS:d3dkmddi._DXGK_MAPAPERTUREFLAGS
title : _DXGK_MAPAPERTUREFLAGS
author : windows-driver-content
description : The DXGK_MAPAPERTUREFLAGS structure identifies the type of map-aperture-segment operation to set up in a call to the DxgkDdiBuildPagingBuffer function.
old-location : display\dxgk_mapapertureflags.htm
old-project : display
ms.assetid : c6a6f98f-a4e3-47ed-b9e9-7303c824612d
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _DXGK_MAPAPERTUREFLAGS, d3dkmddi/DXGK_MAPAPERTUREFLAGS, DmStructs_74b5ec6e-0c62-419f-beb2-676d993c7496.xml, display.dxgk_mapapertureflags, DXGK_MAPAPERTUREFLAGS structure [Display Devices], DXGK_MAPAPERTUREFLAGS
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
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : DXGK_MAPAPERTUREFLAGS
---

# _DXGK_MAPAPERTUREFLAGS structure
The DXGK_MAPAPERTUREFLAGS structure identifies the type of map-aperture-segment operation to set up in a call to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_buildpagingbuffer.md">DxgkDdiBuildPagingBuffer</a> function.

## Syntax
````
typedef struct _DXGK_MAPAPERTUREFLAGS {
  union {
    struct {
      UINT CacheCoherent  :1;
      UINT Reserved  :31;
    };
    UINT Value;
  };
} DXGK_MAPAPERTUREFLAGS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="..\d3dkmddi\ns-d3dkmddi-_dxgkarg_buildpagingbuffer.md">DXGKARG_BUILDPAGINGBUFFER</a>

<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_buildpagingbuffer.md">DxgkDdiBuildPagingBuffer</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_MAPAPERTUREFLAGS structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>