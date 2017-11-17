---
UID: NC.ucmtcpciportcontroller.PFN_UCMTCPCIPORTCONTROLLERALERT
title: PFN_UCMTCPCIPORTCONTROLLERALERT
author: windows-driver-content
description: 
ms.assetid: 4d703c79-3195-488b-88d1-8dac66217726
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ucmtcpciportcontroller.h
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

# PFN_UCMTCPCIPORTCONTROLLERALERT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_UCMTCPCIPORTCONTROLLERALERT PfnUcmtcpciportcontrolleralert; 

// Definition

WDFAPI PfnUcmtcpciportcontrolleralert 
(
	PUCMTCPCI_DRIVER_GLOBALS DriverGlobals
	UCMTCPCIPORTCONTROLLER PortControllerObject
	PUCMTCPCI_PORT_CONTROLLER_ALERT_DATA AlertData
	size_t NumberOfAlerts
)
{...}

PFN_UCMTCPCIPORTCONTROLLERALERT 


```

## -parameters

### -param DriverGlobals: 
### -param PortControllerObject: 
### -param AlertData: 
### -param NumberOfAlerts: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also