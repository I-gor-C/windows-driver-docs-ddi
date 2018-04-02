---
UID: NS:d3dkmddi._DXGK_VIDMMCAPS
title: "_DXGK_VIDMMCAPS"
author: windows-driver-content
description: The DXGK_VIDMMCAPS structure identifies the video memory management capabilities that a display miniport driver can support.
old-location: display\dxgk_vidmmcaps.htm
old-project: display
ms.assetid: c3df50a0-2388-4760-b6e2-ef6af650d0e2
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_VIDMMCAPS, DXGK_VIDMMCAPS structure [Display Devices], DmStructs_0ec3e7bb-c14e-41b8-a148-7f77153972e8.xml, _DXGK_VIDMMCAPS, d3dkmddi/DXGK_VIDMMCAPS, display.dxgk_vidmmcaps
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
-	DXGK_VIDMMCAPS
product:
- Windows
targetos: Windows
req.typenames: DXGK_VIDMMCAPS
---

# _DXGK_VIDMMCAPS structure
The <b>DXGK_VIDMMCAPS</b> structure identifies the video memory management capabilities that a display miniport driver can support.

## Syntax
```
typedef struct _DXGK_VIDMMCAPS {
  union {
    struct {
      UINT  : 1  OutOfOrderLock;
      UINT  : 1  DedicatedPagingEngine;
      UINT  : 1  PagingEngineCanSwizzle;
      UINT  : 1  SectionBackedPrimary;
      UINT  : 1  CrossAdapterResource;
      UINT  : 1  VirtualAddressingSupported;
      UINT  : 1  GpuMmuSupported;
      UINT  : 1  IoMmuSupported;
      UINT  : 1  ReplicateGdiContent;
      UINT  : 1  NonCpuVisiblePrimary;
      UINT  : 1  ParavirtualizationSupported;
#if ...
      UINT  : 21 Reserved;
#elif
      UINT  : 22 Reserved;
#elif
      UINT  : 27 Reserved;
#elif
      UINT  : 28 Reserved;
#else
      UINT  : 31 Reserved;
#endif
    };
    UINT Value;
  };
  UINT  PagingNode;
} DXGK_VIDMMCAPS;
```

## Members


`PagingNode`

The zero-based index of the node to use for paging operations. If the driver does not set the <b>MultiEngineAware</b> bit-field member of the <b>SchedulingCaps</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561062">DXGK_DRIVERCAPS</a> structure, the DirectX graphics kernel subsystem ignores the setting of <b>PagingNode</b>.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff561062">DXGK_DRIVERCAPS</a>