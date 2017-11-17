---
UID: NC.ucmmanager.PFN_UCMCONNECTORCREATE
title: PFN_UCMCONNECTORCREATE
author: windows-driver-content
description: 
ms.assetid: 860dfda3-b476-4446-a969-383eb19d3afe
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

# PFN_UCMCONNECTORCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_UCMCONNECTORCREATE PfnUcmconnectorcreate; 

// Definition

WDFAPI PfnUcmconnectorcreate 
(
	PUCM_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE WdfDevice
	PUCM_CONNECTOR_CONFIG Config
	PWDF_OBJECT_ATTRIBUTES Attributes
	UCMCONNECTOR *Connector
)
{...}

PFN_UCMCONNECTORCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param WdfDevice: 
### -param Config: 
### -param Attributes: 
### -param *Connector: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also