---
UID: NC.ucmtcpciportcontroller.PFN_UCMTCPCIPORTCONTROLLERSTOP
title: PFN_UCMTCPCIPORTCONTROLLERSTOP
author: windows-driver-content
description: 
ms.assetid: e9a901d7-13c8-40d2-b45c-81a1d7f18869
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

# PFN_UCMTCPCIPORTCONTROLLERSTOP callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_UCMTCPCIPORTCONTROLLERSTOP PfnUcmtcpciportcontrollerstop; 

// Definition

WDFAPI PfnUcmtcpciportcontrollerstop 
(
	PUCMTCPCI_DRIVER_GLOBALS DriverGlobals
	UCMTCPCIPORTCONTROLLER PortControllerObject
)
{...}

PFN_UCMTCPCIPORTCONTROLLERSTOP 


```

## -parameters

### -param DriverGlobals: 
### -param PortControllerObject: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also