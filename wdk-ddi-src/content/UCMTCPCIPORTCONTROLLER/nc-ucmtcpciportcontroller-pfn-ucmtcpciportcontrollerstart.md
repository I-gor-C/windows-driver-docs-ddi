---
UID: NC.ucmtcpciportcontroller.PFN_UCMTCPCIPORTCONTROLLERSTART
title: PFN_UCMTCPCIPORTCONTROLLERSTART
author: windows-driver-content
description: 
ms.assetid: 358b00be-da67-4791-bc4a-c02994b69b86
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

# PFN_UCMTCPCIPORTCONTROLLERSTART callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_UCMTCPCIPORTCONTROLLERSTART PfnUcmtcpciportcontrollerstart; 

// Definition

WDFAPI PfnUcmtcpciportcontrollerstart 
(
	PUCMTCPCI_DRIVER_GLOBALS DriverGlobals
	UCMTCPCIPORTCONTROLLER PortControllerObject
)
{...}

PFN_UCMTCPCIPORTCONTROLLERSTART 


```

## -parameters

### -param DriverGlobals: 
### -param PortControllerObject: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also