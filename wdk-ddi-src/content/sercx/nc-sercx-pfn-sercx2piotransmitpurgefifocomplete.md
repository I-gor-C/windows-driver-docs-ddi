---
UID: NC.sercx.PFN_SERCX2PIOTRANSMITPURGEFIFOCOMPLETE
title: PFN_SERCX2PIOTRANSMITPURGEFIFOCOMPLETE
author: windows-driver-content
description: 
ms.assetid: 6df42f47-1447-4b93-924a-673cfb96364d
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

# PFN_SERCX2PIOTRANSMITPURGEFIFOCOMPLETE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCX2PIOTRANSMITPURGEFIFOCOMPLETE PfnSercx2piotransmitpurgefifocomplete; 

// Definition

WDFAPI PfnSercx2piotransmitpurgefifocomplete 
(
	PSERCX_DRIVER_GLOBALS DriverGlobals
	SERCX2PIOTRANSMIT PioTransmit
	ULONG BytesPurged
)
{...}

PFN_SERCX2PIOTRANSMITPURGEFIFOCOMPLETE 


```

## -parameters

### -param DriverGlobals: 
### -param PioTransmit: 
### -param BytesPurged: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also