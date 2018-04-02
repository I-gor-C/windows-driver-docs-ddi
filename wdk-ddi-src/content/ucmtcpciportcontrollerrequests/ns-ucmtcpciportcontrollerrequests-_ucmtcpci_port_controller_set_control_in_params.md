---
UID: NS:ucmtcpciportcontrollerrequests._UCMTCPCI_PORT_CONTROLLER_SET_CONTROL_IN_PARAMS
title: "_UCMTCPCI_PORT_CONTROLLER_SET_CONTROL_IN_PARAMS"
author: windows-driver-content
description: Stores the values of all control registers. This structure is used in the IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_CONTROL request.
old-location: buses\ucmtcpci_port_controller_set_control_in_params.htm
old-project: usbref
ms.assetid: d81d76a9-e482-4e22-93c0-a320905ee203
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PUCMTCPCI_PORT_CONTROLLER_SET_CONTROL_IN_PARAMS, PUCMTCPCI_PORT_CONTROLLER_SET_CONTROL_IN_PARAMS, PUCMTCPCI_PORT_CONTROLLER_SET_CONTROL_IN_PARAMS structure pointer [Buses], UCMTCPCI_PORT_CONTROLLER_SET_CONTROL_IN_PARAMS, UCMTCPCI_PORT_CONTROLLER_SET_CONTROL_IN_PARAMS structure [Buses], _UCMTCPCI_PORT_CONTROLLER_SET_CONTROL_IN_PARAMS, buses.ucmtcpci_port_controller_set_control_in_params, ucmtcpciportcontrollerrequests/PUCMTCPCI_PORT_CONTROLLER_SET_CONTROL_IN_PARAMS, ucmtcpciportcontrollerrequests/UCMTCPCI_PORT_CONTROLLER_SET_CONTROL_IN_PARAMS"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Ucmtcpciportcontrollerrequests.h
api_name:
-	UCMTCPCI_PORT_CONTROLLER_SET_CONTROL_IN_PARAMS
product:
- Windows
targetos: Windows
req.typenames: UCMTCPCI_PORT_CONTROLLER_SET_CONTROL_IN_PARAMS, *PUCMTCPCI_PORT_CONTROLLER_SET_CONTROL_IN_PARAMS
req.product: Windows 10 or later.
---

# _UCMTCPCI_PORT_CONTROLLER_SET_CONTROL_IN_PARAMS structure
Stores the values of all control registers. This structure is used in the <a href="https://msdn.microsoft.com/library/windows/hardware/mt805836">IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_CONTROL</a> request.

## Syntax
```
typedef struct _UCMTCPCI_PORT_CONTROLLER_SET_CONTROL_IN_PARAMS {
  UCMTCPCIPORTCONTROLLER                PortControllerObject;
  UCMTCPCI_PORT_CONTROLLER_CONTROL_TYPE ControlType;
  union {
    UCMTCPCI_PORT_CONTROLLER_FAULT_CONTROL FaultControl;
    UCMTCPCI_PORT_CONTROLLER_POWER_CONTROL PowerControl;
    UCMTCPCI_PORT_CONTROLLER_ROLE_CONTROL  RoleControl;
    UCMTCPCI_PORT_CONTROLLER_TCPC_CONTROL  TCPCControl;
  };
} *PUCMTCPCI_PORT_CONTROLLER_SET_CONTROL_IN_PARAMS, UCMTCPCI_PORT_CONTROLLER_SET_CONTROL_IN_PARAMS;
```

## Members


`PortControllerObject`

Handle to the port controller object that the client driver received in the previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/mt805844">UcmTcpciPortControllerCreate</a>.

`ControlType`

A <b>UCMTCPCI_PORT_CONTROLLER_CONTROL_TYPE</b>-value that 
                 indicates the type of control register. This enumeration is declared in UcmTcpciSpec.h.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ucmtcpciportcontrollerrequests.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt805836">IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_CONTROL</a>