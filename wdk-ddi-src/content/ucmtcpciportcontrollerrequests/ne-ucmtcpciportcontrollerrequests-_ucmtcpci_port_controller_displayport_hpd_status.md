---
UID: NE:ucmtcpciportcontrollerrequests._UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_HPD_STATUS
title: "_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_HPD_STATUS"
author: windows-driver-content
description: Defines values to determine whether a DisplayPort device is plugged in.
old-location: buses\ucmtcpci_port_controller_displayport_hpd_status.htm
old-project: usbref
ms.assetid: 6BE5948B-DAC9-4448-AE22-108805BB364C
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_HPD_STATUS, UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_HPD_STATUS enumeration [Buses], UcmTcpciPortControllerHPDStatusHigh, UcmTcpciPortControllerHPDStatusLow, _UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_HPD_STATUS, buses.ucmtcpci_port_controller_displayport_hpd_status, ucmtcpciportcontrollerrequests/UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_HPD_STATUS, ucmtcpciportcontrollerrequests/UcmTcpciPortControllerHPDStatusHigh, ucmtcpciportcontrollerrequests/UcmTcpciPortControllerHPDStatusLow
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ucmtcpciportcontrollerrequests.h
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
-	Ucmtcpciportcontrollerrequests.h
api_name:
-	UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_HPD_STATUS
product:
- Windows
targetos: Windows
req.typenames: UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_HPD_STATUS
req.product: Windows 10 or later.
---

# _UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_HPD_STATUS Enumeration
Defines values to determine whether a DisplayPort device is plugged in.

## Syntax
```
typedef enum _UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_HPD_STATUS {
  UcmTcpciPortControllerHPDStatusLow   ,
  UcmTcpciPortControllerHPDStatusHigh
} UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_HPD_STATUS;
```

## Constants

<table>
            
                <tr>
                    <td>UcmTcpciPortControllerHPDStatusLow</td>
                    <td>The DisplayPort device is unplugged.</td>
                </tr>
            
                <tr>
                    <td>UcmTcpciPortControllerHPDStatusHigh</td>
                    <td>A DisplayPort device such as a monitor is plugged in.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ucmtcpciportcontrollerrequests.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt805831">IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_HPD_STATUS_CHANGED</a>