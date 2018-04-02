---
UID: NS:d3dkmddi._DXGK_PRESENTATIONCAPS
title: "_DXGK_PRESENTATIONCAPS"
author: windows-driver-content
description: The DXGK_PRESENTATIONCAPS structure identifies presentation capabilities of a display miniport driver that the driver provides through a call to its DxgkDdiQueryAdapterInfo function.
old-location: display\dxgk_presentationcaps.htm
old-project: display
ms.assetid: 38de4631-535f-4950-b361-d70f8c638c36
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_PRESENTATIONCAPS, DXGK_PRESENTATIONCAPS structure [Display Devices], DmStructs_67f7af73-6eaa-4ac8-ad04-1633bc1504af.xml, _DXGK_PRESENTATIONCAPS, d3dkmddi/DXGK_PRESENTATIONCAPS, display.dxgk_presentationcaps
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
-	DXGK_PRESENTATIONCAPS
product: Windows
targetos: Windows
req.typenames: DXGK_PRESENTATIONCAPS
---

# _DXGK_PRESENTATIONCAPS structure
The DXGK_PRESENTATIONCAPS structure identifies presentation capabilities of a display miniport driver that the driver provides through a call to its <a href="https://msdn.microsoft.com/f2f4c54c-7413-48e5-a165-d71f35642b6c">DxgkDdiQueryAdapterInfo</a> function.

## Syntax
```
typedef struct _DXGK_PRESENTATIONCAPS {
  union {
    struct {
      UINT  : 1 NoScreenToScreenBlt;
      UINT  : 1 NoOverlapScreenBlt;
      UINT  : 1 SupportKernelModeCommandBuffer;
      UINT  : 1 NoSameBitmapAlphaBlend;
      UINT  : 1 NoSameBitmapStretchBlt;
      UINT  : 1 NoSameBitmapTransparentBlt;
      UINT  : 1 NoSameBitmapOverlappedAlphaBlend;
      UINT  : 1 NoSameBitmapOverlappedStretchBlt;
      UINT  : 1 DriverSupportsCddDwmInterop;
      UINT  : 1 Reserved0;
      UINT  : 4 AlignmentShift;
      UINT  : 3 MaxTextureWidthShift;
      UINT  : 3 MaxTextureHeightShift;
      UINT  : 1 SupportAllBltRops;
      UINT  : 1 SupportMirrorStretchBlt;
      UINT  : 1 SupportMonoStretchBltModes;
      UINT  : 1 StagingRectStartPitchAligned;
      UINT  : 1 NoSameBitmapBitBlt;
      UINT  : 1 NoSameBitmapOverlappedBitBlt;
      UINT  : 1 Reserved1;
      UINT  : 1 NoTempSurfaceForClearTypeBlend;
      UINT  : 1 SupportSoftwareDeviceBitmaps;
      UINT  : 1 NoCacheCoherentApertureMemory;
      UINT  : 1 SupportLinearHeap;
      UINT  : 1 Reserved;
      UINT  : 4 Reserved;
    };
    UINT Value;
  };
} DXGK_PRESENTATIONCAPS;
```

## Members


## Remarks
A display miniport driver can specify presentation capabilities by setting bits in the 32-bit <b>Value</b> member or by setting individual members of the structure in the union that DXGK_PRESENTATIONCAPS contains.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff546039">D3DKMDT_GDISURFACETYPE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561062">DXGK_DRIVERCAPS</a>



<a href="https://msdn.microsoft.com/f2f4c54c-7413-48e5-a165-d71f35642b6c">DxgkDdiQueryAdapterInfo</a>



<a href="https://msdn.microsoft.com/5841934d-7e0a-4bb8-a7f8-17d8c0af351f">DxgkDdiRenderKm</a>