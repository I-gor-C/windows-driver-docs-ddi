---
UID: NS:ucmmanager._UCM_CONNECTOR_PD_CONN_STATE_CHANGED_PARAMS
title: "_UCM_CONNECTOR_PD_CONN_STATE_CHANGED_PARAMS"
author: windows-driver-content
description: Describes the parameters for PD connection changed event.
old-location: buses\ucm_connector_pd_conn_state_changed_params.htm
old-project: usbref
ms.assetid: 9D8A2B47-1677-4660-B006-CA0D5741FC05
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PUCM_CONNECTOR_PD_CONN_STATE_CHANGED_PARAMS, PUCM_CONNECTOR_PD_CONN_STATE_CHANGED_PARAMS, PUCM_CONNECTOR_PD_CONN_STATE_CHANGED_PARAMS structure pointer [Buses], UCM_CONNECTOR_PD_CONN_STATE_CHANGED_PARAMS, UCM_CONNECTOR_PD_CONN_STATE_CHANGED_PARAMS structure [Buses], _UCM_CONNECTOR_PD_CONN_STATE_CHANGED_PARAMS, buses.ucm_connector_pd_conn_state_changed_params, ucmmanager/PUCM_CONNECTOR_PD_CONN_STATE_CHANGED_PARAMS, ucmmanager/UCM_CONNECTOR_PD_CONN_STATE_CHANGED_PARAMS"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ucmmanager.h
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
-	Ucmmanager.h
api_name:
-	UCM_CONNECTOR_PD_CONN_STATE_CHANGED_PARAMS
product: Windows
targetos: Windows
req.typenames: UCM_CONNECTOR_PD_CONN_STATE_CHANGED_PARAMS, *PUCM_CONNECTOR_PD_CONN_STATE_CHANGED_PARAMS
req.product: Windows 10 or later.
---

# _UCM_CONNECTOR_PD_CONN_STATE_CHANGED_PARAMS structure
Describes the parameters for PD connection changed event.

## Syntax
```
typedef struct _UCM_CONNECTOR_PD_CONN_STATE_CHANGED_PARAMS {
  ULONG                      Size;
  UCM_PD_CONN_STATE          PdConnState;
  UCM_PD_REQUEST_DATA_OBJECT Rdo;
  UCM_CHARGING_STATE         ChargingState;
} *PUCM_CONNECTOR_PD_CONN_STATE_CHANGED_PARAMS, UCM_CONNECTOR_PD_CONN_STATE_CHANGED_PARAMS;
```

## Members


`Size`

Size of the <b>UCM_CONNECTOR_PD_CONN_STATE_CHANGED_PARAMS</b> structure.

`PdConnState`

The state of the connector indicated by one of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187934">UCM_PD_CONN_STATE</a>-typed flags.

`Rdo`

An initialized <a href="https://msdn.microsoft.com/library/windows/hardware/mt187942">UCM_PD_REQUEST_DATA_OBJECT</a> structure that describes the characteristics of the new connection state.

`ChargingState`

Charging state of the port indicated by one of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187921">UCM_CHARGING_STATE</a>-typed flags.

## Remarks
Initialize this structure by calling <a href="https://msdn.microsoft.com/library/windows/hardware/mt187927">UCM_CONNECTOR_PD_CONN_STATE_CHANGED_PARAMS_INIT</a>. An initialized <b>UCM_CONNECTOR_PD_CONN_STATE_CHANGED_PARAMS</b> structure is an input parameter value to <a href="https://msdn.microsoft.com/library/windows/hardware/mt187911">UcmConnectorPdConnectionStateChanged</a> that is used by the client driver to notify UcmCx about the Attached state of the port.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Minimum KMDF version** | 1.15 |
| **Minimum UMDF version** | 2.15 |
| **Header** | ucmmanager.h (include Ucmcx.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt187911">UcmConnectorPdConnectionStateChanged</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/mt187915">UcmConnectorTypeCAttach</a>