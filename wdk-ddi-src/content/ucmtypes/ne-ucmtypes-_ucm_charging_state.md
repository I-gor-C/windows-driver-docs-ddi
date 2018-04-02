---
UID: NE:ucmtypes._UCM_CHARGING_STATE
title: "_UCM_CHARGING_STATE"
author: windows-driver-content
description: Defines the charging state of a Type-C connector.
old-location: buses\ucm_charging_state.htm
old-project: usbref
ms.assetid: DDC3532A-0084-4C56-B540-C638AB7F7080
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PUCM_CHARGING_STATE, UCM_CHARGING_STATE, UCM_CHARGING_STATE enumeration [Buses], UcmChargingStateInvalid, UcmChargingStateNominalCharging, UcmChargingStateNotCharging, UcmChargingStateSlowCharging, UcmChargingStateTrickleCharging, _UCM_CHARGING_STATE, buses.ucm_charging_state, ucmtypes/ UcmChargingStateTrickleCharging, ucmtypes/UCM_CHARGING_STATE, ucmtypes/UcmChargingStateInvalid, ucmtypes/UcmChargingStateNominalCharging, ucmtypes/UcmChargingStateNotCharging, ucmtypes/UcmChargingStateSlowCharging"
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
-	UCM_CHARGING_STATE
product:
- Windows
targetos: Windows
req.typenames: UCM_CHARGING_STATE, *PUCM_CHARGING_STATE
req.product: Windows 10 or later.
---

# _UCM_CHARGING_STATE Enumeration
Defines the charging state of a Type-C connector.

## Syntax
```
typedef enum _UCM_CHARGING_STATE {
  UcmChargingStateInvalid          ,
  UcmChargingStateNotCharging      ,
  UcmChargingStateNominalCharging  ,
  UcmChargingStateSlowCharging     ,
  UcmChargingStateTrickleCharging
} *PUCM_CHARGING_STATE, UCM_CHARGING_STATE;
```

## Constants

<table>
            
                <tr>
                    <td>UcmChargingStateInvalid</td>
                    <td>Indicates the charging state is invalid.</td>
                </tr>
            
                <tr>
                    <td>UcmChargingStateNotCharging</td>
                    <td>Indicates the port is not drawing a charge.</td>
                </tr>
            
                <tr>
                    <td>UcmChargingStateNominalCharging</td>
                    <td>Indicates the port is drawing a nominal charge.</td>
                </tr>
            
                <tr>
                    <td>UcmChargingStateSlowCharging</td>
                    <td>Indicates the port is drawing a slow charge.</td>
                </tr>
            
                <tr>
                    <td>UcmChargingStateTrickleCharging</td>
                    <td>Indicates the port is drawing a trickle charge.</td>
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

<a href="https://msdn.microsoft.com/library/windows/hardware/mt187926">UCM_CONNECTOR_PD_CONN_STATE_CHANGED_PARAMS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/mt187928">UCM_CONNECTOR_TYPEC_ATTACH_PARAMS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/mt187911">UcmConnectorPdConnectionStateChanged</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/mt187915">UcmConnectorTypeCAttach</a>