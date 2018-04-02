---
UID: NS:ucmmanager._UCM_CONNECTOR_TYPEC_ATTACH_PARAMS
title: "_UCM_CONNECTOR_TYPEC_ATTACH_PARAMS"
author: windows-driver-content
description: Describes the partner that is currently attached to the connector.
old-location: buses\ucm_connector_typec_attach_params.htm
old-project: usbref
ms.assetid: D1D4B9D8-0BBF-4592-9EC8-ED294D6D0C90
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PUCM_CONNECTOR_TYPEC_ATTACH_PARAMS, PUCM_CONNECTOR_TYPEC_ATTACH_PARAMS, PUCM_CONNECTOR_TYPEC_ATTACH_PARAMS structure pointer [Buses], UCM_CONNECTOR_TYPEC_ATTACH_PARAMS, UCM_CONNECTOR_TYPEC_ATTACH_PARAMS structure [Buses], _UCM_CONNECTOR_TYPEC_ATTACH_PARAMS, buses.ucm_connector_typec_attach_params, ucmmanager/PUCM_CONNECTOR_TYPEC_ATTACH_PARAMS, ucmmanager/UCM_CONNECTOR_TYPEC_ATTACH_PARAMS"
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
-	UCM_CONNECTOR_TYPEC_ATTACH_PARAMS
product:
- Windows
targetos: Windows
req.typenames: UCM_CONNECTOR_TYPEC_ATTACH_PARAMS, *PUCM_CONNECTOR_TYPEC_ATTACH_PARAMS
req.product: Windows 10 or later.
---

# _UCM_CONNECTOR_TYPEC_ATTACH_PARAMS structure
Describes the partner that is currently attached to the connector.

## Syntax
```
typedef struct _UCM_CONNECTOR_TYPEC_ATTACH_PARAMS {
  ULONG              Size;
  UCM_TYPEC_PARTNER  Partner;
  UCM_TYPEC_CURRENT  CurrentAdvertisement;
  UCM_CHARGING_STATE ChargingState;
} *PUCM_CONNECTOR_TYPEC_ATTACH_PARAMS, UCM_CONNECTOR_TYPEC_ATTACH_PARAMS;
```

## Members


`Size`

Size of the <b>UCM_CONNECTOR_TYPEC_ATTACH_PARAMS</b> structure.

`Partner`



`CurrentAdvertisement`

Power sourcing capabilities of: the partner port when <b>PortPartnerType</b> is <b>UcmTypeCPortStateDfp</b>; the local port when <b>PortPartnerType</b> is not <b>UcmTypeCPortStateDfp</b>.

`ChargingState`

Optional. Charging state of the port indicated by one of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187921">UCM_CHARGING_STATE</a>-typed flags.

## Remarks
Initialize this structure by calling <a href="https://msdn.microsoft.com/library/windows/hardware/mt187929">UCM_CONNECTOR_TYPEC_ATTACH_PARAMS_INIT</a>. An initialized <b>UCM_CONNECTOR_TYPEC_ATTACH_PARAMS</b> structure is an input parameter value to <a href="https://msdn.microsoft.com/library/windows/hardware/mt187915">UcmConnectorTypeCAttach</a> that is used by the client driver to notify UcmCx about the Attached state of the port.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Minimum KMDF version** | 1.15 |
| **Minimum UMDF version** | 2.15 |
| **Header** | ucmmanager.h (include Ucmcx.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt187915">UcmConnectorTypeCAttach</a>