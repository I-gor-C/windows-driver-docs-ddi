---
UID: NC.sercx.PFN_SERCXPROGRESSTRANSMIT
title: PFN_SERCXPROGRESSTRANSMIT
author: windows-driver-content
description: 
ms.assetid: 8e37df74-9ab4-4e4c-99c0-127ca90e85a6
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: sercx.h
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

# PFN_SERCXPROGRESSTRANSMIT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCXPROGRESSTRANSMIT PfnSercxprogresstransmit; 

// Definition

WDFAPI PfnSercxprogresstransmit 
(
	PSER_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	ULONG BytesTransmitted
	SERCX_STATUS TransmitStatus
)
{...}

PFN_SERCXPROGRESSTRANSMIT 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param BytesTransmitted: 
### -param TransmitStatus: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also