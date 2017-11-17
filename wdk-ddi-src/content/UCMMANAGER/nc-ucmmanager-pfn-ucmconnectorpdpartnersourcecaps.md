---
UID: NC.ucmmanager.PFN_UCMCONNECTORPDPARTNERSOURCECAPS
title: PFN_UCMCONNECTORPDPARTNERSOURCECAPS
author: windows-driver-content
description: 
ms.assetid: 9ce597a6-f6c7-41ea-bc91-09a5bc82f847
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

# PFN_UCMCONNECTORPDPARTNERSOURCECAPS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_UCMCONNECTORPDPARTNERSOURCECAPS PfnUcmconnectorpdpartnersourcecaps; 

// Definition

WDFAPI PfnUcmconnectorpdpartnersourcecaps 
(
	PUCM_DRIVER_GLOBALS DriverGlobals
	UCMCONNECTOR Connector
	UCM_PD_POWER_DATA_OBJECT Pdos[]
	UCHAR PdoCount
)
{...}

PFN_UCMCONNECTORPDPARTNERSOURCECAPS 


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