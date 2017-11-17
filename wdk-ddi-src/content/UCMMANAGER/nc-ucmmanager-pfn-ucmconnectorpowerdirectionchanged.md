---
UID: NC.ucmmanager.PFN_UCMCONNECTORPOWERDIRECTIONCHANGED
title: PFN_UCMCONNECTORPOWERDIRECTIONCHANGED
author: windows-driver-content
description: 
ms.assetid: 5df84162-8b9a-4a74-8847-2e1b22aa53c6
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ucmmanager.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.irql: 
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# PFN_UCMCONNECTORPOWERDIRECTIONCHANGED callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_UCMCONNECTORPOWERDIRECTIONCHANGED PfnUcmconnectorpowerdirectionchanged; 

// Definition

WDFAPI PfnUcmconnectorpowerdirectionchanged 
(
	PUCM_DRIVER_GLOBALS DriverGlobals
	UCMCONNECTOR Connector
	BOOLEAN Success
	UCM_POWER_ROLE CurrentPowerRole
)
{...}

PFN_UCMCONNECTORPOWERDIRECTIONCHANGED 


```

## -parameters

### -param DriverGlobals: 
### -param Connector: 
### -param Success: 
### -param CurrentPowerRole: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also