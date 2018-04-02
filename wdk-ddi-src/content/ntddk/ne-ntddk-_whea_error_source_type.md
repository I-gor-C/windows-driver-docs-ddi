---
UID: NE:ntddk._WHEA_ERROR_SOURCE_TYPE
title: "_WHEA_ERROR_SOURCE_TYPE"
author: windows-driver-content
description: The WHEA_ERROR_SOURCE_TYPE enumeration defines the different types of error sources that can report hardware errors.
old-location: whea\whea_error_source_type.htm
old-project: whea
ms.assetid: d2615320-6c8a-4813-afb5-c5b510e5fde9
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: "*PWHEA_ERROR_SOURCE_TYPE, PWHEA_ERROR_SOURCE_TYPE, PWHEA_ERROR_SOURCE_TYPE enumeration pointer [WHEA Drivers and Applications], WHEA_ERROR_SOURCE_TYPE, WHEA_ERROR_SOURCE_TYPE enumeration [WHEA Drivers and Applications], WheaErrSrcTypeBOOT, WheaErrSrcTypeCMC, WheaErrSrcTypeCPE, WheaErrSrcTypeGeneric, WheaErrSrcTypeINIT, WheaErrSrcTypeIPFCMC, WheaErrSrcTypeIPFCPE, WheaErrSrcTypeIPFMCA, WheaErrSrcTypeMCE, WheaErrSrcTypeMax, WheaErrSrcTypeNMI, WheaErrSrcTypePCIe, WheaErrSrcTypeSCIGeneric, _WHEA_ERROR_SOURCE_TYPE, ntddk/PWHEA_ERROR_SOURCE_TYPE, ntddk/WHEA_ERROR_SOURCE_TYPE, ntddk/WheaErrSrcTypeBOOT, ntddk/WheaErrSrcTypeCMC, ntddk/WheaErrSrcTypeCPE, ntddk/WheaErrSrcTypeGeneric, ntddk/WheaErrSrcTypeINIT, ntddk/WheaErrSrcTypeIPFCMC, ntddk/WheaErrSrcTypeIPFCPE, ntddk/WheaErrSrcTypeIPFMCA, ntddk/WheaErrSrcTypeMCE, ntddk/WheaErrSrcTypeMax, ntddk/WheaErrSrcTypeNMI, ntddk/WheaErrSrcTypePCIe, ntddk/WheaErrSrcTypeSCIGeneric, whea.whea_error_source_type, whearef_786d549e-14b1-4945-a1ce-23c7112ff0c8.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
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
-	ntddk.h
api_name:
-	WHEA_ERROR_SOURCE_TYPE
product: Windows
targetos: Windows
req.typenames: WHEA_ERROR_SOURCE_TYPE, *PWHEA_ERROR_SOURCE_TYPE
---

# _WHEA_ERROR_SOURCE_TYPE Enumeration
The WHEA_ERROR_SOURCE_TYPE enumeration defines the different types of error sources that can report hardware errors.

## Syntax
```
typedef enum _WHEA_ERROR_SOURCE_TYPE {
  WheaErrSrcTypeMCE           ,
  WheaErrSrcTypeCMC           ,
  WheaErrSrcTypeCPE           ,
  WheaErrSrcTypeNMI           ,
  WheaErrSrcTypePCIe          ,
  WheaErrSrcTypeGeneric       ,
  WheaErrSrcTypeINIT          ,
  WheaErrSrcTypeBOOT          ,
  WheaErrSrcTypeSCIGeneric    ,
  WheaErrSrcTypeIPFMCA        ,
  WheaErrSrcTypeIPFCMC        ,
  WheaErrSrcTypeIPFCPE        ,
  WheaErrSrcTypeGenericV2     ,
  WheaErrSrcTypeSCIGenericV2  ,
  WheaErrSrcTypeMax
} *PWHEA_ERROR_SOURCE_TYPE, WHEA_ERROR_SOURCE_TYPE;
```

## Constants

<table>
            
                <tr>
                    <td>WheaErrSrcTypeMCE</td>
                    <td>A machine check exception (MCE).</td>
                </tr>
            
                <tr>
                    <td>WheaErrSrcTypeCMC</td>
                    <td>A corrected machine check (CMC).</td>
                </tr>
            
                <tr>
                    <td>WheaErrSrcTypeCPE</td>
                    <td>A corrected platform error (CPE).</td>
                </tr>
            
                <tr>
                    <td>WheaErrSrcTypeNMI</td>
                    <td>A nonmaskable interrupt (NMI).</td>
                </tr>
            
                <tr>
                    <td>WheaErrSrcTypePCIe</td>
                    <td>A PCI Express (PCIe) error.</td>
                </tr>
            
                <tr>
                    <td>WheaErrSrcTypeGeneric</td>
                    <td>A type of error source that does not conform to any of the other WHEA_ERROR_SOURCE_TYPE enumeration values.</td>
                </tr>
            
                <tr>
                    <td>WheaErrSrcTypeINIT</td>
                    <td>An Itanium processor INIT error.</td>
                </tr>
            
                <tr>
                    <td>WheaErrSrcTypeBOOT</td>
                    <td>A boot error source.</td>
                </tr>
            
                <tr>
                    <td>WheaErrSrcTypeSCIGeneric</td>
                    <td>A service control interrupt (SCI).</td>
                </tr>
            
                <tr>
                    <td>WheaErrSrcTypeIPFMCA</td>
                    <td>An Itanium processor machine check abort (MCA).</td>
                </tr>
            
                <tr>
                    <td>WheaErrSrcTypeIPFCMC</td>
                    <td>An Itanium processor corrected machine check (CMC).</td>
                </tr>
            
                <tr>
                    <td>WheaErrSrcTypeIPFCPE</td>
                    <td>An Itanium processor corrected platform error (CPE).</td>
                </tr>
            
                <tr>
                    <td>WheaErrSrcTypeGenericV2</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WheaErrSrcTypeSCIGenericV2</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WheaErrSrcTypeMax</td>
                    <td>The maximum number of error source types that can report hardware errors.</td>
                </tr>
</table>

## Remarks

The <a href="https://msdn.microsoft.com/library/windows/hardware/ff560505">WHEA_ERROR_SOURCE_DESCRIPTOR</a> structure contains a member of type WHEA_ERROR_SOURCE_TYPE that specifies the type of error source that is described by the structure.

The <a href="https://msdn.microsoft.com/library/windows/hardware/ff560465">WHEA_ERROR_PACKET</a> structure contains a member of type WHEA_ERROR_SOURCE_TYPE that specifies the type of error source that caused the error condition described by the structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. |
| **Header** | ntddk.h (include Ntddk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff560465">WHEA_ERROR_PACKET</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff560505">WHEA_ERROR_SOURCE_DESCRIPTOR</a>