---
UID: NS:d3dkmddi._DXGK_FLIPCAPS
title: "_DXGK_FLIPCAPS"
author: windows-driver-content
description: The DXGK_FLIPCAPS structure identifies flipping capabilities of the display miniport driver that the driver provides through a call to its DxgkDdiQueryAdapterInfo function.
old-location: display\dxgk_flipcaps.htm
old-project: display
ms.assetid: 33399b7c-ce67-4c49-be26-2b2d759ff5a0
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_FLIPCAPS, DXGK_FLIPCAPS structure [Display Devices], DmStructs_11bba63e-8001-41d2-9c60-978024921994.xml, _DXGK_FLIPCAPS, d3dkmddi/DXGK_FLIPCAPS, display.dxgk_flipcaps
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
-	DXGK_FLIPCAPS
product:
- Windows
targetos: Windows
req.typenames: DXGK_FLIPCAPS
---

# _DXGK_FLIPCAPS structure
The <b>DXGK_FLIPCAPS</b> structure identifies flipping capabilities of the display miniport driver that the driver provides through a call to its <a href="https://msdn.microsoft.com/f2f4c54c-7413-48e5-a165-d71f35642b6c">DxgkDdiQueryAdapterInfo</a> function.

## Syntax
```
typedef struct _DXGK_FLIPCAPS {
  union {
    struct {
      UINT  : 1  FlipOnVSyncWithNoWait;
      UINT  : 1  FlipOnVSyncMmIo;
      UINT  : 1  FlipInterval;
      UINT  : 1  FlipImmediateMmIo;
      UINT  : 1  FlipIndependent;
      UINT  : 1  DdiPresentForIFlip;
      UINT  : 1  FlipImmediateOnHSync;
#if ...
      UINT  : 25 Reserved;
#elif
      UINT  : 27 Reserved;
#else
      UINT  : 28 Reserved;
#endif
    };
    UINT Value;
  };
} DXGK_FLIPCAPS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff557538">DXGKARGCB_NOTIFY_INTERRUPT_DATA</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff557618">DXGKARG_PRESENT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff557621">DXGKARG_QUERYADAPTERINFO</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff559484">DXGKARG_SETVIDPNSOURCEADDRESS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561062">DXGK_DRIVERCAPS</a>



<a href="https://msdn.microsoft.com/3df3f7d4-3721-46f5-b9e3-19bd3d870292">DxgkCbNotifyDpc</a>



<a href="https://msdn.microsoft.com/7968d26d-0195-463d-8954-e7ebef4f9dea">DxgkCbNotifyInterrupt</a>



<a href="https://msdn.microsoft.com/1a46b129-1e78-44e6-a609-59eab206692b">DxgkDdiPresent</a>



<a href="https://msdn.microsoft.com/f2f4c54c-7413-48e5-a165-d71f35642b6c">DxgkDdiQueryAdapterInfo</a>



<a href="https://msdn.microsoft.com/488c929b-3816-457f-b5c2-c176b93d5546">DxgkDdiSetVidPnSourceAddress</a>