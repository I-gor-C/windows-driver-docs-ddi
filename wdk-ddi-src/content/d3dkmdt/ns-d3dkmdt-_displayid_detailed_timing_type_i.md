---
UID: NS:d3dkmdt._DISPLAYID_DETAILED_TIMING_TYPE_I
title: "_DISPLAYID_DETAILED_TIMING_TYPE_I"
author: windows-driver-content
description: The DISPLAYID_DETAILED_TIMING_TYPE_I structure specifies an additional target mode set for a video present target.
old-location: display\displayid_detailed_timing_type_i.htm
old-project: display
ms.assetid: 7b3fa3a4-a77a-4c5f-b157-1fbdc3a7be33
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DISPLAYID_DETAILED_TIMING_TYPE_I, DISPLAYID_DETAILED_TIMING_TYPE_I structure [Display Devices], DmStructs_75d5fd93-c7ae-4a57-9843-427c53a9416f.xml, _DISPLAYID_DETAILED_TIMING_TYPE_I, d3dkmdt/DISPLAYID_DETAILED_TIMING_TYPE_I, display.displayid_detailed_timing_type_i
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
-	DISPLAYID_DETAILED_TIMING_TYPE_I
product: Windows
targetos: Windows
req.typenames: DISPLAYID_DETAILED_TIMING_TYPE_I
---

# _DISPLAYID_DETAILED_TIMING_TYPE_I structure
The DISPLAYID_DETAILED_TIMING_TYPE_I structure specifies an additional target mode set for a video present target.

## Syntax
````
typedef struct _DISPLAYID_DETAILED_TIMING_TYPE_I {
  struct {
    ULONG PixelClock  :24;
    ULONG AspectRatio  :3;
    ULONG Reserved  :1;
    ULONG ScanningType  :1;
    ULONG StereoMode  :2;
    ULONG PreferredTiming  :1;
  };
  USHORT HorizontalActivePixels;
  USHORT HorizontalBlankPixels;
  struct {
    USHORT HorizontalFrontPorch  :15;
    USHORT HorizontalSyncPolarity  :1;
  };
  USHORT HorizontalSyncWidth;
  USHORT VerticalActiveLines;
  USHORT VerticalBlankLines;
  struct {
    USHORT VerticalFrontPorch  :15;
    USHORT VerticalSyncPolarity  :1;
  };
  USHORT VerticalSyncWidth;
} DISPLAYID_DETAILED_TIMING_TYPE_I;
````

## Members


`HorizontalActivePixels`

[in] The number of active pixels in the horizontal direction.

`HorizontalBlankPixels`

[in] The number of blank pixels in the horizontal direction.

`HorizontalSyncWidth`

[in] The horizontal sync interval, in pixels.

`VerticalActiveLines`

[in] The number of active scan lines.

`VerticalBlankLines`

[in] The number of blank scan lines.

`VerticalSyncWidth`

[in] The vertical sync interval, in number of lines.

## Remarks
The Microsoft DirectX graphics kernel subsystem fills this structure by reading the additional target mode data that is stored in the registry at the following path:

<b>HKEY_LOCAL_MACHINE\ SYSTEM\ CurrentControlSet\ Control\ GraphicsDrivers\ AdditionalTargetModeLists</b>

The graphics kernel subsystem also validates that each registry value meets the requirements described above for each respective member.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 7 and later versions of the Windows operating systems. Available in Windows 7 and later versions of the Windows operating systems. |
| **Header** | d3dkmdt.h (include D3dkmdt.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff554023">DISPLAYID_DETAILED_TIMING_TYPE_I_STEREO_MODE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff554017">DISPLAYID_DETAILED_TIMING_TYPE_I_ASPECT_RATIO</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff554026">DISPLAYID_DETAILED_TIMING_TYPE_I_SYNC_POLARITY</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff554019">DISPLAYID_DETAILED_TIMING_TYPE_I_SCANNING_MODE</a>