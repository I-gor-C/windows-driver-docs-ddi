---
UID: NE:dxva._DXVA_VideoLighting
title: "_DXVA_VideoLighting"
author: windows-driver-content
description: The DXVA_VideoLighting enumeration type contains enumerators that identify lighting conditions for viewing video.
old-location: display\dxva_videolighting.htm
old-project: display
ms.assetid: 09adfa3f-443b-4500-bb08-27f91da20778
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXVA_VideoLighting, DXVA_VideoLighting enumeration [Display Devices], DXVA_VideoLightingMask, DXVA_VideoLightingShift, DXVA_VideoLighting_Unknown, DXVA_VideoLighting_bright, DXVA_VideoLighting_dark, DXVA_VideoLighting_dim, DXVA_VideoLighting_office, _DXVA_VideoLighting, display.dxva_videolighting, dxva/DXVA_VideoLighting, dxva/DXVA_VideoLightingMask, dxva/DXVA_VideoLightingShift, dxva/DXVA_VideoLighting_Unknown, dxva/DXVA_VideoLighting_bright, dxva/DXVA_VideoLighting_dark, dxva/DXVA_VideoLighting_dim, dxva/DXVA_VideoLighting_office, dxvaref_c223ad8d-6e70-4672-b286-292a7e36d6f7.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: dxva.h
req.include-header: Dxva.h
req.target-type: Windows
req.target-min-winverclnt: This enumeration type applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.
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
-	dxva.h
api_name:
-	DXVA_VideoLighting
product: Windows
targetos: Windows
req.typenames: DXVA_VideoLighting
---

# _DXVA_VideoLighting Enumeration
The DXVA_VideoLighting enumeration type contains enumerators that identify lighting conditions for viewing video.

## Syntax
```
typedef enum _DXVA_VideoLighting {
  DXVA_VideoLightingShift     ,
  DXVA_VideoLightingMask      ,
  DXVA_VideoLighting_Unknown  ,
  DXVA_VideoLighting_bright   ,
  DXVA_VideoLighting_office   ,
  DXVA_VideoLighting_dim      ,
  DXVA_VideoLighting_dark
} DXVA_VideoLighting;
```

## Constants

<table>
            
                <tr>
                    <td>DXVA_VideoLightingShift</td>
                    <td>Specifies to shift bits by 18 positions (DXVA_ExtColorData_ShiftBase + 10, or 8 + 10).</td>
                </tr>
            
                <tr>
                    <td>DXVA_VideoLightingMask</td>
                    <td>Specifies the video lighting mask. 4 (0x003C0000) bits of a DWORD can be used to specify video lighting.</td>
                </tr>
            
                <tr>
                    <td>DXVA_VideoLighting_Unknown</td>
                    <td>Specifies that the video lighting condition is not specified. The default is dim.</td>
                </tr>
            
                <tr>
                    <td>DXVA_VideoLighting_bright</td>
                    <td>Specifies bright light for viewing video (for example, outside lighting conditions).</td>
                </tr>
            
                <tr>
                    <td>DXVA_VideoLighting_office</td>
                    <td>Specifies a medium brightness light for viewing video (for example, lighting conditions in home offices).</td>
                </tr>
            
                <tr>
                    <td>DXVA_VideoLighting_dim</td>
                    <td>Specifies a dim light for viewing video (for example, low-level lighting in a living room while watching television).</td>
                </tr>
            
                <tr>
                    <td>DXVA_VideoLighting_dark</td>
                    <td>Specifies near darkness for viewing video (for example, movie-theatre lighting).</td>
                </tr>
</table>

## Remarks

One of the enumerators of DXVA_VideoLighting can be specified in the <b>VideoLighting</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563967">DXVA_ExtendedFormat</a> structure.

The video lighting enumerators can be used to alter the gamma to generate a comparable experience in a different lighting condition.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | This enumeration type applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later. This enumeration type applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later. |
| **Header** | dxva.h (include Dxva.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff563967">DXVA_ExtendedFormat</a>