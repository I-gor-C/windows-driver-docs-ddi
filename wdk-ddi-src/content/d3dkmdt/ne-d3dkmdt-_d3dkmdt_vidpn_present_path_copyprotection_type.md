---
UID: NE:d3dkmdt._D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_TYPE
title: "_D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_TYPE"
author: windows-driver-content
description: The D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_TYPE enumeration is used to indicate the type of copy protection that is supported by a VidPN present path.
old-location: display\d3dkmdt_vidpn_present_path_copyprotection_type.htm
old-project: display
ms.assetid: ee9405a6-7d56-4ca6-98c2-fd04addef8cd
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_TYPE, D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_TYPE enumeration [Display Devices], D3DKMDT_VPPMT_MACROVISION_APSTRIGGER, D3DKMDT_VPPMT_MACROVISION_FULLSUPPORT, D3DKMDT_VPPMT_NOPROTECTION, D3DKMDT_VPPMT_UNINITIALIZED, DmEnums_48fdc75d-b1cb-4bc2-80b1-0aa79b16f480.xml, _D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_TYPE, d3dkmdt/D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_TYPE, d3dkmdt/D3DKMDT_VPPMT_MACROVISION_APSTRIGGER, d3dkmdt/D3DKMDT_VPPMT_MACROVISION_FULLSUPPORT, d3dkmdt/D3DKMDT_VPPMT_NOPROTECTION, d3dkmdt/D3DKMDT_VPPMT_UNINITIALIZED, display.d3dkmdt_vidpn_present_path_copyprotection_type
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
-	D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_TYPE
product:
- Windows
targetos: Windows
req.typenames: D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_TYPE
---

# _D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_TYPE Enumeration
The D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_TYPE enumeration is used to indicate the type of copy protection that is supported by a VidPN present path.

## Syntax
```
typedef enum _D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_TYPE {
  D3DKMDT_VPPMT_UNINITIALIZED            ,
  D3DKMDT_VPPMT_NOPROTECTION             ,
  D3DKMDT_VPPMT_MACROVISION_APSTRIGGER   ,
  D3DKMDT_VPPMT_MACROVISION_FULLSUPPORT
} D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_TYPE;
```

## Constants

<table>
            
                <tr>
                    <td>D3DKMDT_VPPMT_UNINITIALIZED</td>
                    <td>Indicates that a variable of type D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_TYPE has not yet been assigned a meaningful value.</td>
                </tr>
            
                <tr>
                    <td>D3DKMDT_VPPMT_NOPROTECTION</td>
                    <td>Indicates that the path has no copy protection.</td>
                </tr>
            
                <tr>
                    <td>D3DKMDT_VPPMT_MACROVISION_APSTRIGGER</td>
                    <td>Indicates that the path provides support for Rovi's (formerly Macrovision) analog protection system (APS).</td>
                </tr>
            
                <tr>
                    <td>D3DKMDT_VPPMT_MACROVISION_FULLSUPPORT</td>
                    <td>Indicates that the path provides full Rovi (formerly Macrovision) copy protection support.</td>
                </tr>
</table>

## Remarks

The <b>CopyProtectionType</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546656">D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION</a> structure is a value from the D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_TYPE enumeration.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmdt.h (include D3dkmdt.h) |