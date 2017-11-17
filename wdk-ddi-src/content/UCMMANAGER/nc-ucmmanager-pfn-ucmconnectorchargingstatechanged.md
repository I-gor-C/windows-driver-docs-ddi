---
UID: NC.ucmmanager.PFN_UCMCONNECTORCHARGINGSTATECHANGED
title: PFN_UCMCONNECTORCHARGINGSTATECHANGED
author: windows-driver-content
description: 
ms.assetid: 2271b3d1-a3da-4194-af47-f615c37e6c1c
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

# PFN_UCMCONNECTORCHARGINGSTATECHANGED callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_UCMCONNECTORCHARGINGSTATECHANGED PfnUcmconnectorchargingstatechanged; 

// Definition

WDFAPI PfnUcmconnectorchargingstatechanged 
(
	PUCM_DRIVER_GLOBALS DriverGlobals
	UCMCONNECTOR Connector
	UCM_CHARGING_STATE ChargingState
)
{...}

PFN_UCMCONNECTORCHARGINGSTATECHANGED 


```

## -parameters

### -param DriverGlobals: 
### -param Connector: 
### -param ChargingState: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also