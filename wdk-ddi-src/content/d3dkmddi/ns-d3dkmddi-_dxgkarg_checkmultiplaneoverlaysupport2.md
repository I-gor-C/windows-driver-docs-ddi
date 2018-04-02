---
UID: NS:d3dkmddi._DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT2
title: "_DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT2"
author: windows-driver-content
description: DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT2 is passed to the DxgkDdiCheckMultiPlaneOverlaySupport2 function to determine whether a specific multi-plane overlay configuration is supported.
old-location: display\dxgkarg_checkmultiplaneoverlaysupport2.htm
old-project: display
ms.assetid: 477EBC8A-04A5-4904-AC62-0FA7DB861ACC
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*IN_OUT_PDXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT2, DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT2, DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT2 structure [Display Devices], _DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT2, d3dkmddi/DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT2, display.dxgkarg_checkmultiplaneoverlaysupport2"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
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
-	DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT2
product:
- Windows
targetos: Windows
req.typenames: DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT2
---

# _DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT2 structure
<b>DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT2</b> is passed to the  <a href="https://msdn.microsoft.com/A453B59F-0DD1-4FFF-A0E6-09494211780F">DxgkDdiCheckMultiPlaneOverlaySupport2</a> function to determine whether a specific multi-plane overlay configuration is supported.

## Syntax
```
typedef struct _DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT2 {
  UINT                                              PlaneCount;
  DXGK_MULTIPLANE_OVERLAY_PLANE_WITH_SOURCE         *pPlanes;
  BOOL                                              Supported;
  DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO ReturnInfo;
} DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT2;
```

## Members


`PlaneCount`

The number of planes to be enabled.

`pPlanes`

A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/dn914479">DXGK_MULTIPLANE_OVERLAY_PLANE_WITH_SOURCE</a> 
                                                                        structure that specifies support attributes that the hardware
                                                                        provides for multi-plane overlays.

`Supported`

<b>TRUE</b> if the multi-plane overlay configuration can be supported, otherwise <b>FALSE</b>.

`ReturnInfo`

Specifies additional information.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn914479">DXGK_MULTIPLANE_OVERLAY_PLANE_WITH_SOURCE</a>



<a href="https://msdn.microsoft.com/A453B59F-0DD1-4FFF-A0E6-09494211780F">DxgkDdiCheckMultiPlaneOverlaySupport2</a>