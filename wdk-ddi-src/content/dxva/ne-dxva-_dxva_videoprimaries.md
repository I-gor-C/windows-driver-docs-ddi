---
UID: NE:dxva._DXVA_VideoPrimaries
title: "_DXVA_VideoPrimaries"
author: windows-driver-content
description: The DXVA_VideoPrimaries enumeration type contains enumerators that identify the color primaries, which state which RGB basis functions are used.
old-location: display\dxva_videoprimaries.htm
old-project: display
ms.assetid: 8aa6ba31-aec0-4a92-ad0e-6c19b796e398
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXVA_VideoPrimaries, DXVA_VideoPrimaries enumeration [Display Devices], DXVA_VideoPrimariesMask, DXVA_VideoPrimariesShift, DXVA_VideoPrimaries_BT470_2_SysBG, DXVA_VideoPrimaries_BT470_2_SysM, DXVA_VideoPrimaries_BT709, DXVA_VideoPrimaries_EBU3213, DXVA_VideoPrimaries_SMPTE170M, DXVA_VideoPrimaries_SMPTE240M, DXVA_VideoPrimaries_SMPTE_C, DXVA_VideoPrimaries_Unknown, DXVA_VideoPrimaries_reserved, _DXVA_VideoPrimaries, display.dxva_videoprimaries, dxva/DXVA_VideoPrimaries, dxva/DXVA_VideoPrimariesMask, dxva/DXVA_VideoPrimariesShift, dxva/DXVA_VideoPrimaries_BT470_2_SysBG, dxva/DXVA_VideoPrimaries_BT470_2_SysM, dxva/DXVA_VideoPrimaries_BT709, dxva/DXVA_VideoPrimaries_EBU3213, dxva/DXVA_VideoPrimaries_SMPTE170M, dxva/DXVA_VideoPrimaries_SMPTE240M, dxva/DXVA_VideoPrimaries_SMPTE_C, dxva/DXVA_VideoPrimaries_Unknown, dxva/DXVA_VideoPrimaries_reserved, dxvaref_c0e5c7be-4039-438c-a883-30bb242a5c50.xml
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
-	DXVA_VideoPrimaries
product: Windows
targetos: Windows
req.typenames: DXVA_VideoPrimaries
---

# _DXVA_VideoPrimaries Enumeration
The DXVA_VideoPrimaries enumeration type contains enumerators that identify the color primaries, which state which RGB basis functions are used.

## Syntax
```
typedef enum _DXVA_VideoPrimaries {
  DXVA_VideoPrimariesShift           ,
  DXVA_VideoPrimariesMask            ,
  DXVA_VideoPrimaries_Unknown        ,
  DXVA_VideoPrimaries_reserved       ,
  DXVA_VideoPrimaries_BT709          ,
  DXVA_VideoPrimaries_BT470_2_SysM   ,
  DXVA_VideoPrimaries_BT470_2_SysBG  ,
  DXVA_VideoPrimaries_SMPTE170M      ,
  DXVA_VideoPrimaries_SMPTE240M      ,
  DXVA_VideoPrimaries_EBU3213        ,
  DXVA_VideoPrimaries_SMPTE_C
} DXVA_VideoPrimaries;
```

## Constants

<table>
            
                <tr>
                    <td>DXVA_VideoPrimariesShift</td>
                    <td>Specifies to shift bits by 22 positions (DXVA_ExtColorData_ShiftBase + 14, or 8 + 14).</td>
                </tr>
            
                <tr>
                    <td>DXVA_VideoPrimariesMask</td>
                    <td>Specifies the color primaries mask. 5 (0x07C00000) bits of a DWORD can be used to specify color primaries.</td>
                </tr>
            
                <tr>
                    <td>DXVA_VideoPrimaries_Unknown</td>
                    <td>Specifies that color primaries are not specified. The default is BT709.</td>
                </tr>
            
                <tr>
                    <td>DXVA_VideoPrimaries_reserved</td>
                    <td>Reserved.</td>
                </tr>
            
                <tr>
                    <td>DXVA_VideoPrimaries_BT709</td>
                    <td>Specifies BT709 primaries (including sRGB, scRGB).</td>
                </tr>
            
                <tr>
                    <td>DXVA_VideoPrimaries_BT470_2_SysM</td>
                    <td>Specifies BT470-2 SysM primaries, which are the original NTSC primaries.</td>
                </tr>
            
                <tr>
                    <td>DXVA_VideoPrimaries_BT470_2_SysBG</td>
                    <td>Specifies BT470-2 SysBG primaries.</td>
                </tr>
            
                <tr>
                    <td>DXVA_VideoPrimaries_SMPTE170M</td>
                    <td>Specifies SMPTE170M primaries, which are rarely used analog NTSC primaries (also known as SMPTE RP 145).</td>
                </tr>
            
                <tr>
                    <td>DXVA_VideoPrimaries_SMPTE240M</td>
                    <td>Specifies SMPTE240M primaries.</td>
                </tr>
            
                <tr>
                    <td>DXVA_VideoPrimaries_EBU3213</td>
                    <td>Specifies EBU3213 primaries.</td>
                </tr>
            
                <tr>
                    <td>DXVA_VideoPrimaries_SMPTE_C</td>
                    <td>Specifies SMPTE_C primaries, which are analog '79 NTSC primaries.</td>
                </tr>
</table>

## Remarks

One of the enumerators of DXVA_VideoPrimaries can be specified in the <b>VideoPrimaries</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563967">DXVA_ExtendedFormat</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | This enumeration type applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later. This enumeration type applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later. |
| **Header** | dxva.h (include Dxva.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff563967">DXVA_ExtendedFormat</a>