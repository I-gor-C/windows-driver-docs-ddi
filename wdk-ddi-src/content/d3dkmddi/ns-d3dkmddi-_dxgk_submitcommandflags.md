---
UID : NS:d3dkmddi._DXGK_SUBMITCOMMANDFLAGS
title : "_DXGK_SUBMITCOMMANDFLAGS"
author : windows-driver-content
description : The DXGK_SUBMITCOMMANDFLAGS structure identifies, in bit-field flags, information about a direct memory access (DMA) buffer to submit to the graphics processing unit (GPU).
old-location : display\dxgk_submitcommandflags.htm
old-project : display
ms.assetid : b73e49d1-3e71-4c36-b628-3d5a3975e5fa
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : DmStructs_c3c77059-3e18-4fe7-a845-b59bb117ba30.xml, display.dxgk_submitcommandflags, _DXGK_SUBMITCOMMANDFLAGS, DXGK_SUBMITCOMMANDFLAGS, d3dkmddi/DXGK_SUBMITCOMMANDFLAGS, DXGK_SUBMITCOMMANDFLAGS structure [Display Devices]
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
req.typenames : DXGK_SUBMITCOMMANDFLAGS
---

# _DXGK_SUBMITCOMMANDFLAGS structure
The DXGK_SUBMITCOMMANDFLAGS structure identifies, in bit-field flags, information about a direct memory access (DMA) buffer to submit to the graphics processing unit (GPU).

## Syntax
````
typedef struct _DXGK_SUBMITCOMMANDFLAGS {
  union {
    struct {
      UINT Paging  :1;
      UINT Present  :1;
      UINT RedirectedPresent  :1;
      UINT NullRendering  :1;
      UINT Flip  :1;
      UINT FlipWithNoWait  :1;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WIN8)
      UINT ContextSwitch  :1;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_0)
      UINT Resubmission  :1;
      UINT Reserved  :24;
#else 
      UINT Reserved  :25;
#endif 
#else 
      UINT Reserved  :26;
#endif 
    };
    UINT Value;
  };
} DXGK_SUBMITCOMMANDFLAGS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="..\d3dkmddi\ns-d3dkmddi-_dxgkarg_submitcommand.md">DXGKARG_SUBMITCOMMAND</a>

<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_submitcommand.md">DxgkDdiSubmitCommand</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_SUBMITCOMMANDFLAGS structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>