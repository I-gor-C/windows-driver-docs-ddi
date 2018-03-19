---
UID: NS:ucmmanager._UCM_CONNECTOR_TYPEC_CONFIG
title: "_UCM_CONNECTOR_TYPEC_CONFIG"
author: windows-driver-content
description: Describes the configuration options for a Type-C connector.
old-location: buses\ucm_connector_type_c_config.htm
old-project: usbref
ms.assetid: F3C17CD8-F423-46E7-891F-E428235CEF3D
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: "*PUCM_CONNECTOR_TYPEC_CONFIG, PUCM_CONNECTOR_TYPEC_CONFIG, PUCM_CONNECTOR_TYPEC_CONFIG structure pointer [Buses], UCM_CONNECTOR_TYPEC_CONFIG, UCM_CONNECTOR_TYPEC_CONFIG structure [Buses], _UCM_CONNECTOR_TYPEC_CONFIG, buses.ucm_connector_type_c_config, ucmmanager/PUCM_CONNECTOR_TYPEC_CONFIG, ucmmanager/UCM_CONNECTOR_TYPEC_CONFIG"
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
-	UCM_CONNECTOR_TYPEC_CONFIG
product: Windows
targetos: Windows
req.typenames: UCM_CONNECTOR_TYPEC_CONFIG, *PUCM_CONNECTOR_TYPEC_CONFIG
req.product: Windows 10 or later.
---

# _UCM_CONNECTOR_TYPEC_CONFIG structure
Describes the configuration options for a Type-C connector.

## Syntax
````
typedef struct _UCM_CONNECTOR_TYPEC_CONFIG {
  ULONG                           Size;
  BOOLEAN                         IsSupported;
  ULONG                           SupportedOperatingModes;
  ULONG                           SupportedPowerSourcingCapabilities;
  BOOLEAN                         AudioAccessoryCapable;
  PFN_UCM_CONNECTOR_SET_DATA_ROLE EvtSetDataRole;
} UCM_CONNECTOR_TYPEC_CONFIG, *PUCM_CONNECTOR_TYPEC_CONFIG;
````

## Members


`Size`

Size of the <b>UCM_CONNECTOR_TYPEC_CONFIG</b> structure.

`IsSupported`

TRUE indicates a Type-C connector. FALSE, otherwise.  is supported.

`SupportedOperatingModes`

Indicates the supported operating mode of the connector. This value is a bitwise OR of <a href="..\ucmtypes\ne-ucmtypes-_ucm_typec_operating_mode.md">UCM_TYPEC_OPERATING_MODE</a>-typed flags.

`SupportedPowerSourcingCapabilities`

Indicates the supported power source capabilities of the connector. This value is a bitwise OR of <a href="..\ucmtypes\ne-ucmtypes-_ucm_typec_current.md">UCM_TYPEC_CURRENT</a>-typed flags.

`AudioAccessoryCapable`

Indicates whether the connector is capable of detecting a USB Type-C analog input as 3.5 mm audio jack.

`EvtSetDataRole`

A pointer to the client driver's implementation of the <a href="..\ucmmanager\nc-ucmmanager-evt_ucm_connector_set_data_role.md">EVT_UCM_CONNECTOR_SET_DATA_ROLE</a> callback function.

## Remarks
Initialize this structure by calling <a href="..\ucmmanager\nf-ucmmanager-ucm_connector_typec_config_init.md">UCM_CONNECTOR_TYPEC_CONFIG_INIT</a>. An initialized <b>UCM_CONNECTOR_TYPEC_CONFIG</b> structure is an input parameter value to <a href="..\ucmmanager\nf-ucmmanager-ucmconnectorcreate.md">UcmConnectorCreate</a> that is used by Policy Manager to create a connector object.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Minimum KMDF version** | 1.15 |
| **Minimum UMDF version** | 2.15 |
| **Header** | ucmmanager.h (include Ucmcx.h) |

## See Also

<a href="..\ucmmanager\nf-ucmmanager-ucmconnectorcreate.md">UcmConnectorCreate</a>