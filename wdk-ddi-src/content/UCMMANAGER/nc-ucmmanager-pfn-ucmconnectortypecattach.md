---
UID: NC.ucmmanager.PFN_UCMCONNECTORTYPECATTACH
title: PFN_UCMCONNECTORTYPECATTACH
author: windows-driver-content
description: 
ms.assetid: 5e1f6f0e-0f29-407c-9226-787d0813d37c
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

# PFN_UCMCONNECTORTYPECATTACH callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_UCMCONNECTORTYPECATTACH PfnUcmconnectortypecattach; 

// Definition

WDFAPI PfnUcmconnectortypecattach 
(
	PUCM_DRIVER_GLOBALS DriverGlobals
	UCMCONNECTOR Connector
	PUCM_CONNECTOR_TYPEC_ATTACH_PARAMS Params
)
{...}

PFN_UCMCONNECTORTYPECATTACH 


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