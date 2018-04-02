---
UID: NS:d3dkmdt._DXGK_TARGETMODE_DETAIL_TIMING
title: "_DXGK_TARGETMODE_DETAIL_TIMING"
author: windows-driver-content
description: The DXGK_TARGETMODE_DETAIL_TIMING structure describes a video present target's additional timing modes that are compatible with the display device.
old-location: display\dxgk_targetmode_detail_timing.htm
old-project: display
ms.assetid: bf5e53fa-bafd-4325-be8e-97d1c6aa334e
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_TARGETMODE_DETAIL_TIMING, DXGK_TARGETMODE_DETAIL_TIMING structure [Display Devices], DmStructs_e09b214e-5cd4-430e-b5ba-ece083bbb71c.xml, _DXGK_TARGETMODE_DETAIL_TIMING, d3dkmdt/DXGK_TARGETMODE_DETAIL_TIMING, display.dxgk_targetmode_detail_timing
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of the Windows operating systems.
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
-	d3dkmdt.h
api_name:
-	DXGK_TARGETMODE_DETAIL_TIMING
product:
- Windows
targetos: Windows
req.typenames: DXGK_TARGETMODE_DETAIL_TIMING
---

# _DXGK_TARGETMODE_DETAIL_TIMING structure
The DXGK_TARGETMODE_DETAIL_TIMING structure describes a video present target's additional timing modes that are compatible with the display device.

## Syntax
```
typedef struct _DXGK_TARGETMODE_DETAIL_TIMING {
  D3DKMDT_VIDEO_SIGNAL_STANDARD    VideoStandard;
  UINT                             TimingId;
  DISPLAYID_DETAILED_TIMING_TYPE_I DetailTiming;
} DXGK_TARGETMODE_DETAIL_TIMING;
```

## Members


`VideoStandard`

[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff546632">D3DKMDT_VIDEO_SIGNAL_STANDARD</a>-typed value that indicates the supported video signal standard.

`TimingId`

[in] A UINT value that describes the registry ID of the video standard data described by <b>VideoStandard</b>. The high 8 bits indicate the target mode's video standard. The low 24 bits indicate the mode index in the video standard.

`DetailTiming`

[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff554014">DISPLAYID_DETAILED_TIMING_TYPE_I</a>-typed value that indicates the target mode data for a video present target.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 7 and later versions of the Windows operating systems. Available in Windows 7 and later versions of the Windows operating systems. |
| **Header** | d3dkmdt.h (include D3dkmdt.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff546632">D3DKMDT_VIDEO_SIGNAL_STANDARD</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff554014">DISPLAYID_DETAILED_TIMING_TYPE_I</a>