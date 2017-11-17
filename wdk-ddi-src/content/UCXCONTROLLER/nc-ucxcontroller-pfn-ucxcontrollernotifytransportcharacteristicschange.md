---
UID: NC.ucxcontroller.PFN_UCXCONTROLLERNOTIFYTRANSPORTCHARACTERISTICSCHANGE
title: PFN_UCXCONTROLLERNOTIFYTRANSPORTCHARACTERISTICSCHANGE
author: windows-driver-content
description: 
ms.assetid: 439fd810-ae2a-474b-8288-41a8d84d6ed5
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ucxcontroller.h
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

# PFN_UCXCONTROLLERNOTIFYTRANSPORTCHARACTERISTICSCHANGE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_UCXCONTROLLERNOTIFYTRANSPORTCHARACTERISTICSCHANGE PfnUcxcontrollernotifytransportcharacteristicschange; 

// Definition

WDFAPI PfnUcxcontrollernotifytransportcharacteristicschange 
(
	PUCX_DRIVER_GLOBALS DriverGlobals
	UCXCONTROLLER Controller
	PUCX_CONTROLLER_TRANSPORT_CHARACTERISTICS UcxControllerTransportCharacteristics
)
{...}

PFN_UCXCONTROLLERNOTIFYTRANSPORTCHARACTERISTICSCHANGE 


```

## -parameters

### -param DriverGlobals: 
### -param Controller: 
### -param UcxControllerTransportCharacteristics: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also