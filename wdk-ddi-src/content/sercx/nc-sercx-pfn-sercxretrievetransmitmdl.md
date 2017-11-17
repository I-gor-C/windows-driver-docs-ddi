---
UID: NC.sercx.PFN_SERCXRETRIEVETRANSMITMDL
title: PFN_SERCXRETRIEVETRANSMITMDL
author: windows-driver-content
description: 
ms.assetid: 32db8b77-ded6-42d4-85a2-1f0885927442
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

# PFN_SERCXRETRIEVETRANSMITMDL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCXRETRIEVETRANSMITMDL PfnSercxretrievetransmitmdl; 

// Definition

WDFAPI PfnSercxretrievetransmitmdl 
(
	PSER_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PMDL *Mdl
)
{...}

PFN_SERCXRETRIEVETRANSMITMDL 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param *Mdl: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also