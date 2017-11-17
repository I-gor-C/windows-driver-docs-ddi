---
UID: NC.sercx.PFN_SERCX2PIOTRANSMITCREATE
title: PFN_SERCX2PIOTRANSMITCREATE
author: windows-driver-content
description: 
ms.assetid: 074920c5-69c3-4b12-b8f5-04aa6650dc1d
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

# PFN_SERCX2PIOTRANSMITCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCX2PIOTRANSMITCREATE PfnSercx2piotransmitcreate; 

// Definition

WDFAPI PfnSercx2piotransmitcreate 
(
	PSERCX_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PSERCX2_PIO_TRANSMIT_CONFIG PioTransmitConfig
	PWDF_OBJECT_ATTRIBUTES Attributes
	SERCX2PIOTRANSMIT *PioTransmit
)
{...}

PFN_SERCX2PIOTRANSMITCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param PioTransmitConfig: 
### -param Attributes: 
### -param *PioTransmit: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also