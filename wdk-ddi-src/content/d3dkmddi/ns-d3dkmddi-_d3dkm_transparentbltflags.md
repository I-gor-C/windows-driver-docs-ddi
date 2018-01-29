---
UID : NS:d3dkmddi._D3DKM_TRANSPARENTBLTFLAGS
title : _D3DKM_TRANSPARENTBLTFLAGS
author : windows-driver-content
description : The D3DKM_TRANSPARENTBLTFLAGS structure specifies the display adapter's ability to perform a hardware-accelerated bit-block transfer (bitblt) with transparency.
old-location : display\d3dkm_transparentbltflags.htm
old-project : display
ms.assetid : 8ac87e6e-bc24-45fe-b0c5-d253dd03da16
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.d3dkm_transparentbltflags, _D3DKM_TRANSPARENTBLTFLAGS, d3dkmddi/D3DKM_TRANSPARENTBLTFLAGS, D3DKM_TRANSPARENTBLTFLAGS structure [Display Devices], DmStructs_7190815e-5610-4c97-823f-8bdaae16c005.xml, D3DKM_TRANSPARENTBLTFLAGS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3dkmddi.h
req.include-header : D3dkmddi.h
req.target-type : Windows
req.target-min-winverclnt : Available in Windows 7 and later versions of the Windows operating systems.
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
req.typenames : D3DKM_TRANSPARENTBLTFLAGS
---

# _D3DKM_TRANSPARENTBLTFLAGS structure
The D3DKM_TRANSPARENTBLTFLAGS structure specifies the display adapter's ability to perform a hardware-accelerated bit-block transfer (bitblt) with transparency.

## Syntax
````
typedef struct _D3DKM_TRANSPARENTBLTFLAGS {
  union {
    struct {
      UINT HonorAlpha  :1;
    };
    UINT   Value;
  };
} D3DKM_TRANSPARENTBLTFLAGS;
````

## Members


## Remarks
For more information about how to use the members of this structure, see <a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_gdiarg_transparentblt.md">DXGK_GDIARG_TRANSPARENTBLT</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_gdiarg_transparentblt.md">DXGK_GDIARG_TRANSPARENTBLT</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKM_TRANSPARENTBLTFLAGS structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>