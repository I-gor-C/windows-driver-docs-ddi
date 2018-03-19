---
UID: NE:ucmtypes._UCM_TYPEC_CURRENT
title: "_UCM_TYPEC_CURRENT"
author: windows-driver-content
description: Defines different Type-C current levels, as defined in the Type-C specification.
old-location: buses\ucm_type_c_current.htm
old-project: usbref
ms.assetid: 5A603C0E-BBB8-4909-B7B0-EAADF428CB5F
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: UCM_TYPEC_CURRENT, UCM_TYPEC_CURRENT enumeration [Buses], UcmTypeCCurrent1500mA, UcmTypeCCurrent3000mA, UcmTypeCCurrentDefaultUsb, UcmTypeCCurrentInvalid, _UCM_TYPEC_CURRENT, buses.ucm_type_c_current, ucmtypes/UCM_TYPEC_CURRENT, ucmtypes/UcmTypeCCurrent1500mA, ucmtypes/UcmTypeCCurrent3000mA, ucmtypes/UcmTypeCCurrentDefaultUsb, ucmtypes/UcmTypeCCurrentInvalid
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ucmtypes.h
req.include-header: Ucmcx.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.15
req.umdf-ver: 2.15
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
-	Ucmtypes.h
api_name:
-	UCM_TYPEC_CURRENT
product: Windows
targetos: Windows
req.typenames: UCM_TYPEC_CURRENT
req.product: Windows 10 or later.
---

# _UCM_TYPEC_CURRENT Enumeration
Defines different Type-C current levels, as defined in the Type-C specification.

## Syntax
````
typedef enum _UCM_TYPE_C_CURRENT { 
  UcmTypeCCurrentInvalid     = 0x0,
  UcmTypeCCurrentDefaultUsb  = 0x1,
  UcmTypeCCurrent1500mA      = 0x2,
  UcmTypeCCurrent3000mA      = 0x4
} UCM_TYPEC_CURRENT;
````

## Constants

<table>
            
                <tr>
                    <td>UcmTypeCCurrentInvalid</td>
                    <td>Indicates the power sourcing current state is invalid.</td>
                </tr>
            
                <tr>
                    <td>UcmTypeCCurrentDefaultUsb</td>
                    <td>Indicates the power sourcing current is the default USB current.</td>
                </tr>
            
                <tr>
                    <td>UcmTypeCCurrent1500mA</td>
                    <td>Indicates the power sourcing current is 1500 mA.</td>
                </tr>
            
                <tr>
                    <td>UcmTypeCCurrent3000mA</td>
                    <td>Indicates the power sourcing current is 3000 mA.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Minimum KMDF version** | 1.15 |
| **Minimum UMDF version** | 2.15 |
| **Header** | ucmtypes.h (include Ucmcx.h) |

## See Also

<a href="..\ucmmanager\nf-ucmmanager-ucmconnectortypecattach.md">UcmConnectorTypeCAttach</a>



<a href="..\ucmmanager\nf-ucmmanager-ucmconnectortypeccurrentadchanged.md">UcmConnectorTypeCCurrentAdChanged</a>