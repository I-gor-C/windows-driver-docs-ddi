---
UID: NC.sercx.PFN_SERCX2CUSTOMTRANSMITTRANSACTIONCREATE
title: PFN_SERCX2CUSTOMTRANSMITTRANSACTIONCREATE
author: windows-driver-content
description: 
ms.assetid: 14968c8e-a37c-458b-ae09-802cfec41c00
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

# PFN_SERCX2CUSTOMTRANSMITTRANSACTIONCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCX2CUSTOMTRANSMITTRANSACTIONCREATE PfnSercx2customtransmittransactioncreate; 

// Definition

WDFAPI PfnSercx2customtransmittransactioncreate 
(
	PSERCX_DRIVER_GLOBALS DriverGlobals
	SERCX2CUSTOMTRANSMIT CustomTransmit
	PSERCX2_CUSTOM_TRANSMIT_TRANSACTION_CONFIG CustomTransmitTransactionConfig
	PWDF_OBJECT_ATTRIBUTES Attributes
	SERCX2CUSTOMTRANSMITTRANSACTION *CustomTransmitTransaction
)
{...}

PFN_SERCX2CUSTOMTRANSMITTRANSACTIONCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param CustomTransmit: 
### -param CustomTransmitTransactionConfig: 
### -param Attributes: 
### -param *CustomTransmitTransaction: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also