---
UID : NS:d3dumddi._DXVADDI_EXTENDEDFORMAT
title : "_DXVADDI_EXTENDEDFORMAT"
author : windows-driver-content
description : The DXVADDI_EXTENDEDFORMAT structure describes the extended format of the video frame.
old-location : display\dxvaddi_extendedformat.htm
old-project : display
ms.assetid : e4f863bd-12ec-489d-a6e0-6b9242fbb0b0
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : "_DXVADDI_EXTENDEDFORMAT, d3dumddi/DXVADDI_EXTENDEDFORMAT, display.dxvaddi_extendedformat, DXVA2_Structs_31dd9223-b889-4db9-acc0-520c8f16410a.xml, DXVADDI_EXTENDEDFORMAT structure [Display Devices], DXVADDI_EXTENDEDFORMAT"
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
req.typenames : DXVADDI_EXTENDEDFORMAT
---

# _DXVADDI_EXTENDEDFORMAT structure
The DXVADDI_EXTENDEDFORMAT structure describes the extended format of the video frame.

## Syntax
````
typedef struct _DXVADDI_EXTENDEDFORMAT {
  union {
    struct {
      UINT SampleFormat  :8;
      UINT VideoChromaSubsampling  :4;
      UINT NominalRange  :3;
      UINT VideoTransferMatrix  :3;
      UINT VideoLighting  :4;
      UINT VideoPrimaries  :5;
      UINT VideoTransferFunction  :5;
    };
    UINT   Value;
  };
} DXVADDI_EXTENDEDFORMAT;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="..\d3dumddi\ns-d3dumddi-_dxvaddi_videodesc.md">DXVADDI_VIDEODESC</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVADDI_EXTENDEDFORMAT structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>