---
UID: NS:d3dkmddi._DXGK_PRESENTATIONCAPS
title: "_DXGK_PRESENTATIONCAPS"
author: windows-driver-content
description: The DXGK_PRESENTATIONCAPS structure identifies presentation capabilities of a display miniport driver that the driver provides through a call to its DxgkDdiQueryAdapterInfo function.
old-location: display\dxgk_presentationcaps.htm
old-project: display
ms.assetid: 38de4631-535f-4950-b361-d70f8c638c36
ms.author: windowsdriverdev
ms.date: 2/26/2018
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
The DXGK_PRESENTATIONCAPS structure identifies presentation capabilities of a display miniport driver that the driver provides through a call to its <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_queryadapterinfo.md">DxgkDdiQueryAdapterInfo</a> function.

## Syntax
````
typedef struct _DXGK_PRESENTATIONCAPS {
  union {
    struct {
      UINT NoScreenToScreenBlt  :1;
      UINT NoOverlapScreenBlt  :1;
      UINT SupportKernelModeCommandBuffer  :1;
      UINT NoSameBitmapAlphaBlend  :1;
      UINT NoSameBitmapStretchBlt  :1;
      UINT NoSameBitmapTransparentBlt  :1;
      UINT NoSameBitmapOverlappedAlphaBlend  :1;
      UINT NoSameBitmapOverlappedStretchBlt  :1;
      UINT DriverSupportsCddDwmInterop  :1;
      UINT Reserved0  :1;
      UINT AlignmentShift  :4;
      UINT MaxTextureWidthShift  :3;
      UINT MaxTextureHeightShift  :3;
      UINT SupportAllBltRops  :1;
      UINT SupportMirrorStretchBlt  :1;
      UINT SupportMonoStretchBltModes  :1;
      UINT StagingRectStartPitchAligned  :1;
      UINT NoSameBitmapBitBlt  :1;
      UINT NoSameBitmapOverlappedBitBlt  :1;
      UINT Reserved1  :1;
      UINT NoTempSurfaceForClearTypeBlend  :1;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WIN8)
      UINT SupportSoftwareDeviceBitmaps  :1;
      UINT NoCacheCoherentApertureMemory  :1;
      UINT SupportLinearHeap  :1;
      UINT Reserved  :1;
#else 
      UINT Reserved  :4;
#endif 
    };
     Value;
  };
} DXGK_PRESENTATIONCAPS;
````

## Members


## Remarks
A display miniport driver can specify presentation capabilities by setting bits in the 32-bit <b>Value</b> member or by setting individual members of the structure in the union that DXGK_PRESENTATIONCAPS contains.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_drivercaps.md">DXGK_DRIVERCAPS</a>



<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_queryadapterinfo.md">DxgkDdiQueryAdapterInfo</a>



<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_renderkm.md">DxgkDdiRenderKm</a>



<a href="..\d3dkmdt\ne-d3dkmdt-_d3dkmdt_gdisurfacetype.md">D3DKMDT_GDISURFACETYPE</a>