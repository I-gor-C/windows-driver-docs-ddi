---
UID: NS:d3dumddi.D3DDDIARG_PRESENTMULTIPLANEOVERLAY
title: D3DDDIARG_PRESENTMULTIPLANEOVERLAY
author: windows-driver-content
description: Specifies a multiplane overlay resource to display.
old-location: display\d3dddiarg_presentmultiplaneoverlay.htm
old-project: display
ms.assetid: 862441ee-8a6e-4ddc-8dba-d3d990f45cfc
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDIARG_PRESENTMULTIPLANEOVERLAY, D3DDDIARG_PRESENTMULTIPLANEOVERLAY structure [Display Devices], d3dumddi/D3DDDIARG_PRESENTMULTIPLANEOVERLAY, display.d3dddiarg_presentmultiplaneoverlay
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
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
-	HeaderDef
api_location:
-	D3dumddi.h
api_name:
-	D3DDDIARG_PRESENTMULTIPLANEOVERLAY
product: Windows
targetos: Windows
req.typenames: D3DDDIARG_PRESENTMULTIPLANEOVERLAY
---

# D3DDDIARG_PRESENTMULTIPLANEOVERLAY structure
Specifies a multiplane overlay resource to display.

## Syntax
```
typedef struct D3DDDIARG_PRESENTMULTIPLANEOVERLAY {
  D3DDDI_VIDEO_PRESENT_SOURCE_ID    VidPnSourceId;
  D3DDDI_PRESENTFLAGS               Flags;
  D3DDDI_FLIPINTERVAL_TYPE          FlipInterval;
  UINT                              PresentPlaneCount;
  D3DDDI_PRESENT_MULTIPLANE_OVERLAY *pPresentPlanes;
  UINT                              Reserved;
};
```

## Members


`VidPnSourceId`

[in] The zero-based video present network (VidPN) source identification number of the input that is to be displayed.

`Flags`

[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544639">D3DDDI_PRESENTFLAGS</a> structure that identifies, in bit-field flags, how to display.

`FlipInterval`

[in] A value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff544549">D3DDDI_FLIPINTERVAL_TYPE</a> that indicates the flip interval (that is, if the flip occurs after zero, one, two, three, or four vertical syncs).

`PresentPlaneCount`

[in] The number of overlay planes that are available to display.

`pPresentPlanes`

[in] A pointer to a structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/hh780245">D3DDDI_PRESENT_MULTIPLANE_OVERLAY</a> that  describes the overlay plane to display.

`Reserved`

[in] Reserved for system use. The driver should ignore this member.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8.1 Windows 8.1 |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff544549">D3DDDI_FLIPINTERVAL_TYPE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544639">D3DDDI_PRESENTFLAGS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh780245">D3DDDI_PRESENT_MULTIPLANE_OVERLAY</a>