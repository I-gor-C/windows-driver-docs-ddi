---
UID : NE:ucmtypes._UCM_TYPEC_CURRENT
title : "_UCM_TYPEC_CURRENT"
author : windows-driver-content
description : Defines different Type-C current levels, as defined in the Type-C specification.
old-location : buses\ucm_type_c_current.htm
old-project : usbref
ms.assetid : 5A603C0E-BBB8-4909-B7B0-EAADF428CB5F
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : ucmtypes/UcmTypeCCurrent3000mA, ucmtypes/UCM_TYPEC_CURRENT, UcmTypeCCurrentDefaultUsb, UcmTypeCCurrent3000mA, buses.ucm_type_c_current, ucmtypes/UcmTypeCCurrentDefaultUsb, _UCM_TYPEC_CURRENT, UcmTypeCCurrentInvalid, ucmtypes/UcmTypeCCurrentInvalid, UCM_TYPEC_CURRENT enumeration [Buses], UCM_TYPEC_CURRENT, ucmtypes/UcmTypeCCurrent1500mA, UcmTypeCCurrent1500mA
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ucmtypes.h
req.include-header : Ucmcx.h
req.target-type : Windows
req.target-min-winverclnt : Windows 10
req.target-min-winversvr : Windows Server 2016
req.kmdf-ver : 1.15
req.umdf-ver : 2.15
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : UCM_TYPEC_CURRENT
req.product : Windows 10 or later.
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
<td>UcmTypeCCurrent1500mA</td>
<td>Indicates the power sourcing current is 1500 mA.</td>
</tr>

<tr>
<td>UcmTypeCCurrent3000mA</td>
<td>Indicates the power sourcing current is 3000 mA.</td>
</tr>

<tr>
<td>UcmTypeCCurrentDefaultUsb</td>
<td>Indicates the power sourcing current is the default USB current.</td>
</tr>

<tr>
<td>UcmTypeCCurrentInvalid</td>
<td>Indicates the power sourcing current state is invalid.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** | 1.15 |
| **Minimum UMDF version** | 2.15 |
| **Header** | ucmtypes.h (include Ucmcx.h) |

## See Also

<a href="..\ucmmanager\nf-ucmmanager-ucmconnectortypecattach.md">UcmConnectorTypeCAttach</a>

<a href="..\ucmmanager\nf-ucmmanager-ucmconnectortypeccurrentadchanged.md">UcmConnectorTypeCCurrentAdChanged</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UCM_TYPEC_CURRENT enumeration%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>