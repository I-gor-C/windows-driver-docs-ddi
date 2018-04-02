---
UID: NS:d3dkmthk._D3DKMT_FLIPMODEL_PRESENTHISTORYTOKEN
title: "_D3DKMT_FLIPMODEL_PRESENTHISTORYTOKEN"
author: windows-driver-content
description: The D3DKMT_FLIPMODEL_PRESENTHISTORYTOKEN structure identifies a flip present-history operation.
old-location: display\d3dkmt_flipmodel_presenthistorytoken.htm
old-project: display
ms.assetid: dcf844e3-3346-485e-8965-c8cb824e2c78
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DKMT_FLIPMODEL_PRESENTHISTORYTOKEN, D3DKMT_FLIPMODEL_PRESENTHISTORYTOKEN structure [Display Devices], OpenGL_Structs_819c22ef-0bae-476a-9cbc-0169cd7fc82f.xml, _D3DKMT_FLIPMODEL_PRESENTHISTORYTOKEN, d3dkmthk/D3DKMT_FLIPMODEL_PRESENTHISTORYTOKEN, display.d3dkmt_flipmodel_presenthistorytoken
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: D3DKMT_FLIPMODEL_PRESENTHISTORYTOKEN is Supported starting with the Windows 7 operating system.
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dkmthk.h
api_name:
-	D3DKMT_FLIPMODEL_PRESENTHISTORYTOKEN
product:
- Windows
targetos: Windows
req.typenames: D3DKMT_FLIPMODEL_PRESENTHISTORYTOKEN
---

# _D3DKMT_FLIPMODEL_PRESENTHISTORYTOKEN structure
The D3DKMT_FLIPMODEL_PRESENTHISTORYTOKEN structure identifies a flip present-history operation.

## Syntax
```
typedef struct _D3DKMT_FLIPMODEL_PRESENTHISTORYTOKEN {
  UINT64                                    FenceValue;
  ULONG64                                   hLogicalSurface;
  UINT_PTR                                  dxgContext;
  D3DDDI_VIDEO_PRESENT_SOURCE_ID            VidPnSourceId;
  UINT                                      SwapChainIndex;
  UINT64                                    PresentLimitSemaphoreId;
  D3DDDI_FLIPINTERVAL_TYPE                  FlipInterval;
  D3DKMT_FLIPMODEL_PRESENTHISTORYTOKENFLAGS Flags;
  LONG64                                    hCompSurf;
  LUID                                      compSurfLuid;
  UINT64                                    confirmationCookie;
  UINT64                                    CompositionSyncKey;
  UINT                                      RemainingTokens;
  RECT                                      ScrollRect;
  POINT                                     ScrollOffset;
  UINT                                      PresentCount;
  FLOAT                                     RevealColor[4];
  D3DDDI_ROTATION                           Rotation;
  union {
    HANDLE             hSyncObject;
    D3DKMT_SCATTERBLTS ScatterBlts;
  };
  D3DKMT_HANDLE                             Reserved;
  RECT                                      SourceRect;
  UINT                                      DestWidth;
  UINT                                      DestHeight;
  RECT                                      TargetRect;
  FLOAT                                     Transform[6];
  UINT                                      CustomDuration;
  D3DDDI_FLIPINTERVAL_TYPE                  CustomDurationFlipInterval;
  UINT                                      PlaneIndex;
  D3DDDI_COLOR_SPACE_TYPE                   ColorSpace;
  D3DKMT_DIRTYREGIONS                       DirtyRegions;
} D3DKMT_FLIPMODEL_PRESENTHISTORYTOKEN;
```

## Members


`FenceValue`

[in] A 64-bit value that specifies the fence value that is used for the flip.

`hLogicalSurface`

[in] A 64-bit value that specifies the handle to a logical surface.

`dxgContext`



`VidPnSourceId`



`SwapChainIndex`

[in] The index of the surface in the swap chain that is used for the flip.

`PresentLimitSemaphoreId`

[in] A 64-bit value that identifies the present-limit semaphore.

`FlipInterval`

[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544549">D3DDDI_FLIPINTERVAL_TYPE</a>-typed value that indicates the flip interval (that is, if the flip occurs after zero, one, two, three, or four vertical syncs).

`Flags`

[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff547991">D3DKMT_FLIPMODEL_PRESENTHISTORYTOKENFLAGS</a> structure that identifies, in bit-field flags, attributes of a flip present-history operation.

`hCompSurf`

This member is reserved and should be set to zero.

Supported starting with Windows 8.

`compSurfLuid`



`confirmationCookie`



`CompositionSyncKey`

This member is reserved and should be set to zero.

Supported starting with Windows 8.

`RemainingTokens`

This member is reserved and should be set to zero.

Supported starting with Windows 8.

`ScrollRect`

This member is reserved and should be set to zero.

Supported starting with Windows 8.

`ScrollOffset`

This member is reserved and should be set to zero.

Supported starting with Windows 8.

`PresentCount`

This member is reserved and should be set to zero.

Supported starting with Windows 8.

`RevealColor`

This member is reserved and should be set to zero.

Supported starting with Windows 8.

`Rotation`

This member is reserved and should be set to zero.

Supported starting with Windows 8.

`Reserved`



`SourceRect`



`DestWidth`



`DestHeight`



`TargetRect`



`Transform`



`CustomDuration`



`CustomDurationFlipInterval`



`PlaneIndex`



`ColorSpace`



`DirtyRegions`

[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff547937">D3DKMT_DIRTYREGIONS</a> structure that identifies the active rectangles (dirty regions) of the flip surface.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | D3DKMT_FLIPMODEL_PRESENTHISTORYTOKEN is Supported starting with the Windows 7 operating system. D3DKMT_FLIPMODEL_PRESENTHISTORYTOKEN is Supported starting with the Windows 7 operating system. |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff544549">D3DDDI_FLIPINTERVAL_TYPE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff547937">D3DKMT_DIRTYREGIONS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff547991">D3DKMT_FLIPMODEL_PRESENTHISTORYTOKENFLAGS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff548188">D3DKMT_PRESENTHISTORYTOKEN</a>