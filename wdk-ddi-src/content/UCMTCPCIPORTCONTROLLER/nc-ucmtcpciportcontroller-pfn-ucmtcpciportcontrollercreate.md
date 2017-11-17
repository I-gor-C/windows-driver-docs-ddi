---
UID: NC.ucmtcpciportcontroller.PFN_UCMTCPCIPORTCONTROLLERCREATE
title: PFN_UCMTCPCIPORTCONTROLLERCREATE
author: windows-driver-content
description: 
ms.assetid: c3e9dac5-0596-4615-b32a-0f0e66a83276
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

# PFN_UCMTCPCIPORTCONTROLLERCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_UCMTCPCIPORTCONTROLLERCREATE PfnUcmtcpciportcontrollercreate; 

// Definition

WDFAPI PfnUcmtcpciportcontrollercreate 
(
	PUCMTCPCI_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE WdfDevice
	PUCMTCPCI_PORT_CONTROLLER_CONFIG Config
	PWDF_OBJECT_ATTRIBUTES Attributes
	UCMTCPCIPORTCONTROLLER *PortControllerObject
)
{...}

PFN_UCMTCPCIPORTCONTROLLERCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param WdfDevice: 
### -param Config: 
### -param Attributes: 
### -param *PortControllerObject: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also