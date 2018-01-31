---
UID : NS:d3dkmddi._DXGK_OPENALLOCATIONFLAGS
title : "_DXGK_OPENALLOCATIONFLAGS"
author : windows-driver-content
description : The DXGK_OPENALLOCATIONFLAGS structure identifies the operation to perform for allocations.
old-location : display\dxgk_openallocationflags.htm
old-project : display
ms.assetid : 6dae69b1-ff48-4d43-bc01-e7ad7bb7acc9
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : DXGK_OPENALLOCATIONFLAGS, display.dxgk_openallocationflags, d3dkmddi/DXGK_OPENALLOCATIONFLAGS, _DXGK_OPENALLOCATIONFLAGS, DmStructs_3b5228f0-93fa-434a-b2ca-9007c372d9ed.xml, DXGK_OPENALLOCATIONFLAGS structure [Display Devices]
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
req.typenames : DXGK_OPENALLOCATIONFLAGS
---

# _DXGK_OPENALLOCATIONFLAGS structure
The DXGK_OPENALLOCATIONFLAGS structure identifies the operation to perform for allocations.

## Syntax
````
typedef struct _DXGK_OPENALLOCATIONFLAGS {
  union {
    struct {
      UINT Create  :1;
      UINT ReadOnly  :1;
      UINT Reserved  :30;
    };
    UINT Value;
  };
} DXGK_OPENALLOCATIONFLAGS;
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

<a href="..\d3dkmddi\ns-d3dkmddi-_dxgkarg_openallocation.md">DXGKARG_OPENALLOCATION</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_OPENALLOCATIONFLAGS structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>