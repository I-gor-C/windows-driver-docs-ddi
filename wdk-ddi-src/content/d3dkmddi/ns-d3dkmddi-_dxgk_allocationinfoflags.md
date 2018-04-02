---
UID: NS:d3dkmddi._DXGK_ALLOCATIONINFOFLAGS
title: "_DXGK_ALLOCATIONINFOFLAGS"
author: windows-driver-content
description: The DXGK_ALLOCATIONINFOFLAGS structure identifies properties for an allocation. The display miniport driver specifies these flags for the video memory manager.
old-location: display\dxgk_allocationinfoflags.htm
old-project: display
ms.assetid: 04bd00c3-83a8-44bb-9493-cf7f43f10602
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_ALLOCATIONINFOFLAGS, DXGK_ALLOCATIONINFOFLAGS structure [Display Devices], DmStructs_4e6e499c-8427-4c0f-977d-92f648ab027e.xml, _DXGK_ALLOCATIONINFOFLAGS, d3dkmddi/DXGK_ALLOCATIONINFOFLAGS, display.dxgk_allocationinfoflags
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
-	DXGK_ALLOCATIONINFOFLAGS
product: Windows
targetos: Windows
req.typenames: DXGK_ALLOCATIONINFOFLAGS
---

# _DXGK_ALLOCATIONINFOFLAGS structure
The DXGK_ALLOCATIONINFOFLAGS structure identifies properties for an allocation. The display miniport driver specifies these flags for the video memory manager.

## Syntax
```
typedef struct _DXGK_ALLOCATIONINFOFLAGS {
  union {
    struct {
      UINT  : 1 CpuVisible;
      UINT  : 1 PermanentSysMem;
      UINT  : 1 Cached;
      UINT  : 1 Protected;
      UINT  : 1 ExistingSysMem;
      UINT  : 1 ExistingKernelSysMem;
      UINT  : 1 FromEndOfSegment;
      UINT  : 1 Swizzled;
      UINT  : 1 Overlay;
      UINT  : 1 Capture;
      UINT  : 1 UseAlternateVA;
      UINT  : 1 SynchronousPaging;
      UINT  : 1 LinkMirrored;
      UINT  : 1 LinkInstanced;
      UINT  : 1 HistoryBuffer;
      UINT  : 1 AccessedPhysically;
      UINT  : 1 ExplicitResidencyNotification;
      UINT  : 1 HardwareProtected;
      UINT  : 1 CpuVisibleOnDemand;
      UINT  : 4 Reserved;
      UINT  : 1 DXGK_ALLOC_RESERVED16;
      UINT  : 1 DXGK_ALLOC_RESERVED15;
      UINT  : 1 DXGK_ALLOC_RESERVED14;
      UINT  : 1 DXGK_ALLOC_RESERVED13;
      UINT  : 1 DXGK_ALLOC_RESERVED12;
      UINT  : 1 DXGK_ALLOC_RESERVED11;
      UINT  : 1 DXGK_ALLOC_RESERVED10;
      UINT  : 1 DXGK_ALLOC_RESERVED9;
      UINT  : 1 DXGK_ALLOC_RESERVED4;
      UINT  : 1 DXGK_ALLOC_RESERVED3;
      UINT  : 1 DXGK_ALLOC_RESERVED2;
      UINT  : 1 DXGK_ALLOC_RESERVED1;
      UINT  : 1 DXGK_ALLOC_RESERVED0;
    };
    UINT Value;
  };
} DXGK_ALLOCATIONINFOFLAGS;
```

## Members


## Remarks
You can specify properties of an allocation by setting bits in the 32-bit <b>Value</b> member or by setting individual members of the structure in the union that the <b>DXGK_ALLOCATIONINFOFLAGS</b> structure contains.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff560960">DXGK_ALLOCATIONINFO</a>



<a href="https://msdn.microsoft.com/d315ff53-4a9f-46a3-ad74-d65a5eb72de1">DxgkDdiBuildPagingBuffer</a>



<a href="https://msdn.microsoft.com/69022797-432a-410b-8cbf-e1ef7111e7ea">pfnLockCb</a>



<a href="https://msdn.microsoft.com/6684f350-da27-478d-ab7b-36e395f7df8d">pfnUnlockCb</a>