---
UID: NC.ucmmanager.PFN_UCMCONNECTORPDSOURCECAPS
title: PFN_UCMCONNECTORPDSOURCECAPS
author: windows-driver-content
description: 
ms.assetid: 215575a1-d825-4c30-8042-605a36587b9b
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

# PFN_UCMCONNECTORPDSOURCECAPS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_UCMCONNECTORPDSOURCECAPS PfnUcmconnectorpdsourcecaps; 

// Definition

WDFAPI PfnUcmconnectorpdsourcecaps 
(
	PUCM_DRIVER_GLOBALS DriverGlobals
	UCMCONNECTOR Connector
	UCM_PD_POWER_DATA_OBJECT Pdos[]
	UCHAR PdoCount
)
{...}

PFN_UCMCONNECTORPDSOURCECAPS 


```

## -parameters

### -param DriverGlobals: 
### -param Connector: 
### -param Pdos[]: 
### -param PdoCount: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also