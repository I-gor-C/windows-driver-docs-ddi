---
UID: NS:ucmtcpciportcontroller._UCMTCPCI_PORT_CONTROLLER_ALERT_DATA
title: "_UCMTCPCI_PORT_CONTROLLER_ALERT_DATA"
author: windows-driver-content
description: Contains information about hardware alerts received on the port controller object. This structure is used in the UcmTcpciPortControllerAlert call. Call UCMTCPCI_PORT_CONTROLLER_ALERT_DATA_INIT to initialize this structure.
old-location: buses\ucmtcpci_port_controller_alert_data.htm
old-project: usbref
ms.assetid: 4b3c2fc8-d7c3-4223-a88e-5db9ad852618
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: "*PUCMTCPCI_PORT_CONTROLLER_ALERT_DATA, PUCMTCPCI_PORT_CONTROLLER_ALERT_DATA, PUCMTCPCI_PORT_CONTROLLER_ALERT_DATA structure pointer [Buses], UCMTCPCI_PORT_CONTROLLER_ALERT_DATA, UCMTCPCI_PORT_CONTROLLER_ALERT_DATA structure [Buses], _UCMTCPCI_PORT_CONTROLLER_ALERT_DATA, buses.ucmtcpci_port_controller_alert_data, ucmtcpciportcontroller/PUCMTCPCI_PORT_CONTROLLER_ALERT_DATA, ucmtcpciportcontroller/UCMTCPCI_PORT_CONTROLLER_ALERT_DATA"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ucmtcpciportcontroller.h
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
-	ucmtcpciportcontroller.h
api_name:
-	UCMTCPCI_PORT_CONTROLLER_ALERT_DATA
product: Windows
targetos: Windows
req.typenames: UCMTCPCI_PORT_CONTROLLER_ALERT_DATA, *PUCMTCPCI_PORT_CONTROLLER_ALERT_DATA
req.product: Windows 10 or later.
---

# _UCMTCPCI_PORT_CONTROLLER_ALERT_DATA structure
Contains information about hardware alerts received on the port controller object. This structure is used in the <a href="..\ucmtcpciportcontroller\nf-ucmtcpciportcontroller-ucmtcpciportcontrolleralert.md">UcmTcpciPortControllerAlert</a> call. Call <a href="..\ucmtcpciportcontroller\nf-ucmtcpciportcontroller-ucmtcpci_port_controller_alert_data_init.md">UCMTCPCI_PORT_CONTROLLER_ALERT_DATA_INIT</a> to initialize this structure.

## Syntax
````
typedef struct _UCMTCPCI_PORT_CONTROLLER_ALERT_DATA {
  ULONG                               Size;
  UCMTCPCI_PORT_CONTROLLER_ALERT_TYPE AlertType;
  union {
    UCMTCPCI_PORT_CONTROLLER_CC_STATUS       CCStatus;
    UCMTCPCI_PORT_CONTROLLER_POWER_STATUS    PowerStatus;
    UCMTCPCI_PORT_CONTROLLER_FAULT_STATUS    FaultStatus;
    PUCMTCPCI_PORT_CONTROLLER_RECEIVE_BUFFER ReceiveBuffer;
  };
} UCMTCPCI_PORT_CONTROLLER_ALERT_DATA, *PUCMTCPCI_PORT_CONTROLLER_ALERT_DATA;
````

## Members


`Size`

Size of this structure.

`AlertType`

A <a href="..\ucmtcpciportcontroller\ne-ucmtcpciportcontroller-_ucmtcpci_port_controller_alert_type.md">UCMTCPCI_PORT_CONTROLLER_ALERT_TYPE</a> value that indicates the type of hardware alert.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ucmtcpciportcontroller.h |

## See Also

<a href="..\ucmtcpciportcontroller\nf-ucmtcpciportcontroller-ucmtcpciportcontrolleralert.md">UcmTcpciPortControllerAlert</a>