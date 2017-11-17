---
UID: NC.ucmmanager.PFN_UCMCONNECTORPDCONNECTIONSTATECHANGED
title: PFN_UCMCONNECTORPDCONNECTIONSTATECHANGED
author: windows-driver-content
description: 
ms.assetid: b8d0387f-cff7-4a93-ae1f-0cf9122e8aff
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

# PFN_UCMCONNECTORPDCONNECTIONSTATECHANGED callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_UCMCONNECTORPDCONNECTIONSTATECHANGED PfnUcmconnectorpdconnectionstatechanged; 

// Definition

WDFAPI PfnUcmconnectorpdconnectionstatechanged 
(
	PUCM_DRIVER_GLOBALS DriverGlobals
	UCMCONNECTOR Connector
	PUCM_CONNECTOR_PD_CONN_STATE_CHANGED_PARAMS Params
)
{...}

PFN_UCMCONNECTORPDCONNECTIONSTATECHANGED 


```

## -parameters

### -param DriverGlobals: 
### -param Connector: 
### -param Params: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also