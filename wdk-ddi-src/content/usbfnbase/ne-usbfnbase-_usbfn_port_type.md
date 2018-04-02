---
UID: NE:usbfnbase._USBFN_PORT_TYPE
title: "_USBFN_PORT_TYPE"
author: windows-driver-content
description: Defines the possible port types that can be returned by the client driver during port detection.
old-location: buses\usbfn_port_type.htm
old-project: usbref
ms.assetid: D45F8CD0-CB54-4DE4-BD6B-FF6A35FCBFEC
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PUSBFN_PORT_TYPE, USBFN_PORT_TYPE, USBFN_PORT_TYPE enumeration [Buses], UsbfnChargingDownstreamPort, UsbfnDedicatedChargingPort, UsbfnInvalidDedicatedChargingPort, UsbfnPortTypeMaximum, UsbfnProprietaryDedicatedChargingPort, UsbfnStandardDownstreamPort, UsbfnUnknownPort, _USBFN_PORT_TYPE, buses.usbfn_port_type, usbfnbase/USBFN_PORT_TYPE, usbfnbase/UsbfnChargingDownstreamPort, usbfnbase/UsbfnDedicatedChargingPort, usbfnbase/UsbfnInvalidDedicatedChargingPort, usbfnbase/UsbfnPortTypeMaximum, usbfnbase/UsbfnProprietaryDedicatedChargingPort, usbfnbase/UsbfnStandardDownstreamPort, usbfnbase/UsbfnUnknownPort"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: usbfnbase.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
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
-	usbfnbase.h
api_name:
-	USBFN_PORT_TYPE
product:
- Windows
targetos: Windows
req.typenames: USBFN_PORT_TYPE, *PUSBFN_PORT_TYPE
req.product: Windows 10 or later.
---

# _USBFN_PORT_TYPE Enumeration
Defines the possible port types that can be returned by the client driver during port detection.

## Syntax
```
typedef enum _USBFN_PORT_TYPE {
  UsbfnUnknownPort                       ,
  UsbfnStandardDownstreamPort            ,
  UsbfnChargingDownstreamPort            ,
  UsbfnDedicatedChargingPort             ,
  UsbfnInvalidDedicatedChargingPort      ,
  UsbfnProprietaryDedicatedChargingPort  ,
  UsbfnPortTypeMaximum
} *PUSBFN_PORT_TYPE, USBFN_PORT_TYPE;
```

## Constants

<table>
            
                <tr>
                    <td>UsbfnUnknownPort</td>
                    <td>Port detection was unable to determine the port type.</td>
                </tr>
            
                <tr>
                    <td>UsbfnStandardDownstreamPort</td>
                    <td>The upstream port has been detected as a standard downstream port (SDP) (as defined in the Battery Charging Specification, revision 1.2).</td>
                </tr>
            
                <tr>
                    <td>UsbfnChargingDownstreamPort</td>
                    <td>The upstream port has been detected as a charging downstream port (CDP), as defined in the Battery Charging Specification, revision 1.2.</td>
                </tr>
            
                <tr>
                    <td>UsbfnDedicatedChargingPort</td>
                    <td>The upstream port has been detected as a dedicated charging port (DCP) (as defined in the Battery Charging Specification, revision 1.2).</td>
                </tr>
            
                <tr>
                    <td>UsbfnInvalidDedicatedChargingPort</td>
                    <td>The upstream port has been detected as a dedicated charging port that does not comply with the Battery Charging Specification, revision 1.2.</td>
                </tr>
            
                <tr>
                    <td>UsbfnProprietaryDedicatedChargingPort</td>
                    <td>A proprietary charger was attached.</td>
                </tr>
            
                <tr>
                    <td>UsbfnPortTypeMaximum</td>
                    <td>The maximum value of the enumeration.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | usbfnbase.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt187995">USBFN_GET_ATTACH_ACTION</a>