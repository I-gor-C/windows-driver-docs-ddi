---
UID: NS:d3dkmddi._DXGK_SUBMITCOMMANDFLAGS
title: "_DXGK_SUBMITCOMMANDFLAGS"
author: windows-driver-content
description: The DXGK_SUBMITCOMMANDFLAGS structure identifies, in bit-field flags, information about a direct memory access (DMA) buffer to submit to the graphics processing unit (GPU).
old-location: display\dxgk_submitcommandflags.htm
old-project: display
ms.assetid: b73e49d1-3e71-4c36-b628-3d5a3975e5fa
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_SUBMITCOMMANDFLAGS, DXGK_SUBMITCOMMANDFLAGS structure [Display Devices], DmStructs_c3c77059-3e18-4fe7-a845-b59bb117ba30.xml, _DXGK_SUBMITCOMMANDFLAGS, d3dkmddi/DXGK_SUBMITCOMMANDFLAGS, display.dxgk_submitcommandflags
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dkmddi.h
api_name:
-	DXGK_SUBMITCOMMANDFLAGS
product:
- Windows
targetos: Windows
req.typenames: DXGK_SUBMITCOMMANDFLAGS
---

# _DXGK_SUBMITCOMMANDFLAGS structure
The DXGK_SUBMITCOMMANDFLAGS structure identifies, in bit-field flags, information about a direct memory access (DMA) buffer to submit to the graphics processing unit (GPU).

## Syntax
```
typedef struct _DXGK_SUBMITCOMMANDFLAGS {
  union {
    struct {
      UINT  : 1  Paging;
      UINT  : 1  Present;
      UINT  : 1  RedirectedPresent;
      UINT  : 1  NullRendering;
      UINT  : 1  Flip;
      UINT  : 1  FlipWithNoWait;
      UINT  : 1  ContextSwitch;
      UINT  : 1  Resubmission;
      UINT  : 1  VirtualMachineData;
#if ...
      UINT  : 23 Reserved;
#elif
      UINT  : 24 Reserved;
#elif
      UINT  : 25 Reserved;
#else
      UINT  : 26 Reserved;
#endif
    };
    UINT Value;
  };
} DXGK_SUBMITCOMMANDFLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff559490">DXGKARG_SUBMITCOMMAND</a>



<a href="https://msdn.microsoft.com/de1925ab-e444-4cf6-acd9-8fdab26afcec">DxgkDdiSubmitCommand</a>