---
UID: NC.sercx.PFN_SERCX2PIORECEIVECREATE
title: PFN_SERCX2PIORECEIVECREATE
author: windows-driver-content
description: 
ms.assetid: 33090fb8-3839-4832-bdc2-5f62504e84a3
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

# PFN_SERCX2PIORECEIVECREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCX2PIORECEIVECREATE PfnSercx2pioreceivecreate; 

// Definition

WDFAPI PfnSercx2pioreceivecreate 
(
	PSERCX_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PSERCX2_PIO_RECEIVE_CONFIG PioReceiveConfig
	PWDF_OBJECT_ATTRIBUTES Attributes
	SERCX2PIORECEIVE *PioReceive
)
{...}

PFN_SERCX2PIORECEIVECREATE 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param PioReceiveConfig: 
### -param Attributes: 
### -param *PioReceive: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also