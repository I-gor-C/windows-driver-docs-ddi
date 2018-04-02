---
UID: NC:d3d10umddi.PFND3DWDDM1_3DDI_TILEDRESOURCEBARRIER
title: PFND3DWDDM1_3DDI_TILEDRESOURCEBARRIER
author: windows-driver-content
description: Specifies a data access ordering constraint between multiple tiled resources. For more info about this constraint, see Remarks.
old-location: display\tiledresourcebarrier.htm
old-project: display
ms.assetid: 9A2E9B3F-13E4-48D7-A3F3-E7CDCDD1E0CC
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3DWDDM1_3DDI_TILEDRESOURCEBARRIER, TiledResourceBarrier, TiledResourceBarrier callback function [Display Devices], d3d10umddi/TiledResourceBarrier, display.tiledresourcebarrier
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8.1,WDDM 1.3
req.target-min-winversvr: Windows Server 2012 R2
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
-	UserDefined
api_location:
-	D3d10umddi.h
api_name:
-	TiledResourceBarrier
product:
- Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3DWDDM1_3DDI_TILEDRESOURCEBARRIER callback function
Specifies a data access ordering constraint between multiple tiled resources. For more info about this constraint, see Remarks.

## Syntax

```
PFND3DWDDM1_3DDI_TILEDRESOURCEBARRIER Pfnd3dwddm13DdiTiledresourcebarrier;

void Pfnd3dwddm13DdiTiledresourcebarrier(
  D3D10DDI_HDEVICE hDevice,
  D3D11DDI_HANDLETYPE TiledResourceAccessBeforeBarrierHandleType,
  VOID *hTiledResourceAccessBeforeBarrier,
  D3D11DDI_HANDLETYPE TiledResourceAccessAfterBarrierHandleType,
  VOID *hTiledResourceAccessAfterBarrier
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`TiledResourceAccessBeforeBarrierHandleType`

A handle to the tiled resource.

`*hTiledResourceAccessBeforeBarrier`

A handle to a resource that was created with the <b>D3DWDDM1_3DDI_RESOURCE_MISC_TILED</b> flag. Access operations on this object must complete before the access operations on the object that <i>hTiledResourceAccessAfterBarrier</i> specifies.

`TiledResourceAccessAfterBarrierHandleType`

The <a href="https://msdn.microsoft.com/library/windows/hardware/ff542152">D3D11DDI_HANDLETYPE</a> handle type of the resources pointed to by the <i>hTiledResourceAccessBeforeBarrier</i> and <i>hTiledResourceAccessAfterBarrier</i> parameters.

`*hTiledResourceAccessAfterBarrier`

A handle to a resource that was created with the <b>D3DWDDM1_3DDI_RESOURCE_MISC_TILED</b> flag. Access operations on this object must begin after the access operations on the object that <i>hTiledResourceAccessBeforeBarrier</i> specifies.


## Return Value

None

The driver can use the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> callback function to set an error code.

The Direct3D runtime performs minimal validation of parameters.

## Remarks

Apps can use tiled resources to reuse tiles in different resources. But a device and driver might not be able to determine whether some memory in a tile pool that was just rendered to is now being used for reading.

The Direct3D runtime calls <i>TiledResourceBarrier</i> to inform the driver that operations issued to the resource before the call must complete before any accesses that occur after the call using a different tiled resource that shares the same memory.

Either or both of the <i>hTiledResourceAccessBeforeBarrier</i> and <i>hTiledResourceAccessAfterBarrier</i> parameters (before or after the barrier) can be <b>NULL</b>. <b>NULL</b> before the barrier means that all tiled resource accesses before the barrier must complete before the resource specified after the barrier can be referenced by the GPU. <b>NULL</b> after the barrier means that any tiled resources accessed after the barrier can only be executed by the GPU after accesses to the tiled resources before the barrier are finished. If both are <b>NULL</b>, all previous tiled resource accesses must be complete before any subsequent tiled resource access can proceed.

If no calls are made to <i>TiledResourceBarrier</i>,
                     the driver can assume that accesses to different tiled resources
                     do not conflict with each other.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8.1,WDDM 1.3 Windows Server 2012 R2 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff542152">D3D11DDI_HANDLETYPE</a>



<a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a>