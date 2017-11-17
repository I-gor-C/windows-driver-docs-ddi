---
UID: NC.sercx.PFN_SERCX2CUSTOMTRANSMITCREATE
title: PFN_SERCX2CUSTOMTRANSMITCREATE
author: windows-driver-content
description: 
ms.assetid: 0ee779d3-9c76-4069-b329-ba6427234726
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

# PFN_SERCX2CUSTOMTRANSMITCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCX2CUSTOMTRANSMITCREATE PfnSercx2customtransmitcreate; 

// Definition

WDFAPI PfnSercx2customtransmitcreate 
(
	PSERCX_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PSERCX2_CUSTOM_TRANSMIT_CONFIG CustomTransmitConfig
	PWDF_OBJECT_ATTRIBUTES Attributes
	SERCX2CUSTOMTRANSMIT *CustomTransmit
)
{...}

PFN_SERCX2CUSTOMTRANSMITCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param CustomTransmitConfig: 
### -param Attributes: 
### -param *CustomTransmit: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also