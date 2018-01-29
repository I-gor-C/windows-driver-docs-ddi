---
UID : NS:ufxproprietarycharger._UFX_PROPRIETARY_CHARGER
title : _UFX_PROPRIETARY_CHARGER
author : windows-driver-content
description : Describes the proprietary charger's device power requirements.
old-location : buses\ufx_proprietary_charger.htm
old-project : usbref
ms.assetid : FAAEDAFE-69A8-4092-8301-DB159FD3583D
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : PUFX_PROPRIETARY_CHARGER, ufxproprietarycharger/PUFX_PROPRIETARY_CHARGER, UFX_PROPRIETARY_CHARGER structure [Buses], buses.ufx_proprietary_charger, ufxproprietarycharger/UFX_PROPRIETARY_CHARGER, *PUFX_PROPRIETARY_CHARGER, PUFX_PROPRIETARY_CHARGER structure pointer [Buses], UFX_PROPRIETARY_CHARGER, _UFX_PROPRIETARY_CHARGER
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ufxproprietarycharger.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PUFX_PROPRIETARY_CHARGER, UFX_PROPRIETARY_CHARGER"
req.product : Windows 10 or later.
---

# _UFX_PROPRIETARY_CHARGER structure
Describes the proprietary charger's device power requirements.

## Syntax
````
typedef struct _UFX_PROPRIETARY_CHARGER {
  GUID               ChargerId;
  DEVICE_POWER_STATE DxState;
} UFX_PROPRIETARY_CHARGER, *PUFX_PROPRIETARY_CHARGER;
````

## Members


`ChargerId`

Charger identifier used to identify a specific type of charger.

`DxState`

The minimum required device power state when it is connected, indicated by one of the <a href="..\wudfddi\ne-wudfddi-_device_power_state.md">DEVICE_POWER_STATE</a>-typed flags.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ufxproprietarycharger.h |