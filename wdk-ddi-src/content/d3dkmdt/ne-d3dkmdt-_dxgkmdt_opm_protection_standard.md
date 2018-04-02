---
UID: NE:d3dkmdt._DXGKMDT_OPM_PROTECTION_STANDARD
title: "_DXGKMDT_OPM_PROTECTION_STANDARD"
author: windows-driver-content
description: The DXGKMDT_OPM_PROTECTION_STANDARD enumeration indicates the type of television signal for which a video output supports protection.
old-location: display\dxgkmdt_opm_protection_standard.htm
old-project: display
ms.assetid: 9f079edf-312a-4218-8b73-0325ccca5a05
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGKMDT_OPM_PROTECTION_STANDARD, DXGKMDT_OPM_PROTECTION_STANDARD enumeration [Display Devices], DXGKMDT_OPM_PROTECTION_STANDARD_ARIBTRB15_1125I, DXGKMDT_OPM_PROTECTION_STANDARD_ARIBTRB15_525I, DXGKMDT_OPM_PROTECTION_STANDARD_ARIBTRB15_525P, DXGKMDT_OPM_PROTECTION_STANDARD_ARIBTRB15_750P, DXGKMDT_OPM_PROTECTION_STANDARD_CEA805A_TYPEA_1125I, DXGKMDT_OPM_PROTECTION_STANDARD_CEA805A_TYPEA_525P, DXGKMDT_OPM_PROTECTION_STANDARD_CEA805A_TYPEA_750P, DXGKMDT_OPM_PROTECTION_STANDARD_CEA805A_TYPEB_1125I, DXGKMDT_OPM_PROTECTION_STANDARD_CEA805A_TYPEB_525P, DXGKMDT_OPM_PROTECTION_STANDARD_CEA805A_TYPEB_750P, DXGKMDT_OPM_PROTECTION_STANDARD_EIA608B_525, DXGKMDT_OPM_PROTECTION_STANDARD_EN300294_625I, DXGKMDT_OPM_PROTECTION_STANDARD_IEC61880_2_525I, DXGKMDT_OPM_PROTECTION_STANDARD_IEC61880_525I, DXGKMDT_OPM_PROTECTION_STANDARD_IEC62375_625P, DXGKMDT_OPM_PROTECTION_STANDARD_NONE, DXGKMDT_OPM_PROTECTION_STANDARD_OTHER, DmEnums_ce6cf9d1-ec7d-43bd-9204-2428751bdabf.xml, _DXGKMDT_OPM_PROTECTION_STANDARD, d3dkmdt/DXGKMDT_OPM_PROTECTION_STANDARD, d3dkmdt/DXGKMDT_OPM_PROTECTION_STANDARD_ARIBTRB15_1125I, d3dkmdt/DXGKMDT_OPM_PROTECTION_STANDARD_ARIBTRB15_525I, d3dkmdt/DXGKMDT_OPM_PROTECTION_STANDARD_ARIBTRB15_525P, d3dkmdt/DXGKMDT_OPM_PROTECTION_STANDARD_ARIBTRB15_750P, d3dkmdt/DXGKMDT_OPM_PROTECTION_STANDARD_CEA805A_TYPEA_1125I, d3dkmdt/DXGKMDT_OPM_PROTECTION_STANDARD_CEA805A_TYPEA_525P, d3dkmdt/DXGKMDT_OPM_PROTECTION_STANDARD_CEA805A_TYPEA_750P, d3dkmdt/DXGKMDT_OPM_PROTECTION_STANDARD_CEA805A_TYPEB_1125I, d3dkmdt/DXGKMDT_OPM_PROTECTION_STANDARD_CEA805A_TYPEB_525P, d3dkmdt/DXGKMDT_OPM_PROTECTION_STANDARD_CEA805A_TYPEB_750P, d3dkmdt/DXGKMDT_OPM_PROTECTION_STANDARD_EIA608B_525, d3dkmdt/DXGKMDT_OPM_PROTECTION_STANDARD_EN300294_625I, d3dkmdt/DXGKMDT_OPM_PROTECTION_STANDARD_IEC61880_2_525I, d3dkmdt/DXGKMDT_OPM_PROTECTION_STANDARD_IEC61880_525I, d3dkmdt/DXGKMDT_OPM_PROTECTION_STANDARD_IEC62375_625P, d3dkmdt/DXGKMDT_OPM_PROTECTION_STANDARD_NONE, d3dkmdt/DXGKMDT_OPM_PROTECTION_STANDARD_OTHER, display.dxgkmdt_opm_protection_standard
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
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
-	d3dkmdt.h
api_name:
-	DXGKMDT_OPM_PROTECTION_STANDARD
product:
- Windows
targetos: Windows
req.typenames: DXGKMDT_OPM_PROTECTION_STANDARD
---

# _DXGKMDT_OPM_PROTECTION_STANDARD Enumeration
The DXGKMDT_OPM_PROTECTION_STANDARD enumeration indicates the type of television signal for which a video output supports protection.

## Syntax
```
typedef enum _DXGKMDT_OPM_PROTECTION_STANDARD {
  DXGKMDT_OPM_PROTECTION_STANDARD_OTHER                ,
  DXGKMDT_OPM_PROTECTION_STANDARD_NONE                 ,
  DXGKMDT_OPM_PROTECTION_STANDARD_IEC61880_525I        ,
  DXGKMDT_OPM_PROTECTION_STANDARD_IEC61880_2_525I      ,
  DXGKMDT_OPM_PROTECTION_STANDARD_IEC62375_625P        ,
  DXGKMDT_OPM_PROTECTION_STANDARD_EIA608B_525          ,
  DXGKMDT_OPM_PROTECTION_STANDARD_EN300294_625I        ,
  DXGKMDT_OPM_PROTECTION_STANDARD_CEA805A_TYPEA_525P   ,
  DXGKMDT_OPM_PROTECTION_STANDARD_CEA805A_TYPEA_750P   ,
  DXGKMDT_OPM_PROTECTION_STANDARD_CEA805A_TYPEA_1125I  ,
  DXGKMDT_OPM_PROTECTION_STANDARD_CEA805A_TYPEB_525P   ,
  DXGKMDT_OPM_PROTECTION_STANDARD_CEA805A_TYPEB_750P   ,
  DXGKMDT_OPM_PROTECTION_STANDARD_CEA805A_TYPEB_1125I  ,
  DXGKMDT_OPM_PROTECTION_STANDARD_ARIBTRB15_525I       ,
  DXGKMDT_OPM_PROTECTION_STANDARD_ARIBTRB15_525P       ,
  DXGKMDT_OPM_PROTECTION_STANDARD_ARIBTRB15_750P       ,
  DXGKMDT_OPM_PROTECTION_STANDARD_ARIBTRB15_1125I
} DXGKMDT_OPM_PROTECTION_STANDARD;
```

## Constants

<table>
            
                <tr>
                    <td>DXGKMDT_OPM_PROTECTION_STANDARD_OTHER</td>
                    <td>Indicates a protected television signal type other than those given in the following constants of this enumeration.</td>
                </tr>
            
                <tr>
                    <td>DXGKMDT_OPM_PROTECTION_STANDARD_NONE</td>
                    <td>Indicates that the video output does not support protection for any television signals.</td>
                </tr>
            
                <tr>
                    <td>DXGKMDT_OPM_PROTECTION_STANDARD_IEC61880_525I</td>
                    <td>Indicates that the video output supports the IEC61880_525I standard.</td>
                </tr>
            
                <tr>
                    <td>DXGKMDT_OPM_PROTECTION_STANDARD_IEC61880_2_525I</td>
                    <td>Indicates that the video output supports the IEC61880_2_525I standard.</td>
                </tr>
            
                <tr>
                    <td>DXGKMDT_OPM_PROTECTION_STANDARD_IEC62375_625P</td>
                    <td>Indicates that the video output supports the IEC62375_625P standard.</td>
                </tr>
            
                <tr>
                    <td>DXGKMDT_OPM_PROTECTION_STANDARD_EIA608B_525</td>
                    <td>Indicates that the video output supports the EIA608B_525 standard.</td>
                </tr>
            
                <tr>
                    <td>DXGKMDT_OPM_PROTECTION_STANDARD_EN300294_625I</td>
                    <td>Indicates that the video output supports the EN300294_625I standard.</td>
                </tr>
            
                <tr>
                    <td>DXGKMDT_OPM_PROTECTION_STANDARD_CEA805A_TYPEA_525P</td>
                    <td>Indicates that the video output supports the CEA805A_TYPEA_525P standard.</td>
                </tr>
            
                <tr>
                    <td>DXGKMDT_OPM_PROTECTION_STANDARD_CEA805A_TYPEA_750P</td>
                    <td>Indicates that the video output supports the CEA805A_TYPEA_750P standard.</td>
                </tr>
            
                <tr>
                    <td>DXGKMDT_OPM_PROTECTION_STANDARD_CEA805A_TYPEA_1125I</td>
                    <td>Indicates that the video output supports the CEA805A_TYPEA_1125I standard.</td>
                </tr>
            
                <tr>
                    <td>DXGKMDT_OPM_PROTECTION_STANDARD_CEA805A_TYPEB_525P</td>
                    <td>Indicates that the video output supports the CEA805A_TYPEB_525P standard.</td>
                </tr>
            
                <tr>
                    <td>DXGKMDT_OPM_PROTECTION_STANDARD_CEA805A_TYPEB_750P</td>
                    <td>Indicates that the video output supports the CEA805A_TYPEB_750P standard.</td>
                </tr>
            
                <tr>
                    <td>DXGKMDT_OPM_PROTECTION_STANDARD_CEA805A_TYPEB_1125I</td>
                    <td>Indicates that the video output supports the CEA805A_TYPEB_1125I standard.</td>
                </tr>
            
                <tr>
                    <td>DXGKMDT_OPM_PROTECTION_STANDARD_ARIBTRB15_525I</td>
                    <td>Indicates that the video output supports the ARIBTRB15_525I standard.</td>
                </tr>
            
                <tr>
                    <td>DXGKMDT_OPM_PROTECTION_STANDARD_ARIBTRB15_525P</td>
                    <td>Indicates that the video output supports the ARIBTRB15_525P standard.</td>
                </tr>
            
                <tr>
                    <td>DXGKMDT_OPM_PROTECTION_STANDARD_ARIBTRB15_750P</td>
                    <td>Indicates that the video output supports the ARIBTRB15_750P standard.</td>
                </tr>
            
                <tr>
                    <td>DXGKMDT_OPM_PROTECTION_STANDARD_ARIBTRB15_1125I</td>
                    <td>Indicates that the video output supports the ARIBTRB15_1125I standard.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmdt.h (include D3dkmdt.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff560830">DXGKMDT_OPM_ACP_AND_CGMSA_SIGNALING</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff560913">DXGKMDT_OPM_SET_ACP_AND_CGMSA_SIGNALING_PARAMETERS</a>



<a href="https://msdn.microsoft.com/a7829587-c1e7-43ec-a0bb-92bca94b7c3d">DxgkDdiOPMConfigureProtectedOutput</a>



<a href="https://msdn.microsoft.com/9f15df1e-bdf5-4634-97f1-78515664b594">DxgkDdiOPMGetCOPPCompatibleInformation</a>



<a href="https://msdn.microsoft.com/3d6559e5-776e-4fc0-b99a-8818cbcc289d">DxgkDdiOPMGetInformation</a>