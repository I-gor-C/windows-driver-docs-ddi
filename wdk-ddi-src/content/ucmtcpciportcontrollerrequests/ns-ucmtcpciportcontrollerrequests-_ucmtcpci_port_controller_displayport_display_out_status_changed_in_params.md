---
UID: NS:ucmtcpciportcontrollerrequests._UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS_CHANGED_IN_PARAMS
title: "_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS_CHANGED_IN_PARAMS"
author: windows-driver-content
description: Stores information about display out status of the DisplayPort connection. This structure is used in the IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS_CHANGED request.
old-location: buses\_ucmtcpci_port_controller_displayport_display_out_status_changed_in_params.htm
old-project: usbref
ms.assetid: c808f607-b121-4406-bb9f-4c5be3f179e3
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PUCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS_CHANGED_IN_PARAMS, UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS_CHANGED_IN_PARAMS, UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS_CHANGED_IN_PARAMS structure [Buses], _UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS_CHANGED_IN_PARAMS, buses._ucmtcpci_port_controller_displayport_display_out_status_changed_in_params, ucmtcpciportcontrollerrequests/UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS_CHANGED_IN_PARAMS"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ucmtcpciportcontrollerrequests.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
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
-	Ucmtcpciportcontrollerrequests.h
api_name:
-	UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS_CHANGED_IN_PARAMS
product: Windows
targetos: Windows
req.typenames: UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS_CHANGED_IN_PARAMS, *PUCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS_CHANGED_IN_PARAMS
req.product: Windows 10 or later.
---

# _UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS_CHANGED_IN_PARAMS structure
Stores information about display out status of the DisplayPort connection. This structure is used in the 
             <a href="https://msdn.microsoft.com/5f174c0a-43aa-48eb-999b-077f1d68c0cb">IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS_CHANGED</a>  request.

## Syntax
```
typedef struct _UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS_CHANGED_IN_PARAMS {
  UCMTCPCIPORTCONTROLLER                                  PortControllerObject;
  UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS DisplayOutStatus;
  UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_PIN_ASSIGNMENT     PinAssignment;
} UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS_CHANGED_IN_PARAMS, *PUCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS_CHANGED_IN_PARAMS;
```

## Members


`PortControllerObject`

Handle to the port controller object that the client driver received in the previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/mt805844">UcmTcpciPortControllerCreate</a>.

`DisplayOutStatus`

A <a href="https://msdn.microsoft.com/c57da7f2-d484-479c-9d8a-626789d8b23e">UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS</a>-type value that indicates status.

`PinAssignment`

A <a href="https://msdn.microsoft.com/library/windows/hardware/mt805902">UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_PIN_ASSIGNMENT</a>-type value that indicates the pin that was changed.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10, version 1709 Windows 10, version 1709 |
| **Header** | ucmtcpciportcontrollerrequests.h |

## See Also

<a href="https://msdn.microsoft.com/5f174c0a-43aa-48eb-999b-077f1d68c0cb">IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS_CHANGED</a>