---
UID: NC.sercx.PFN_SERCX2CUSTOMRECEIVETRANSACTIONCREATE
title: PFN_SERCX2CUSTOMRECEIVETRANSACTIONCREATE
author: windows-driver-content
description: 
ms.assetid: a4acfd13-5379-434f-ae0c-9f66316e697f
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

# PFN_SERCX2CUSTOMRECEIVETRANSACTIONCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCX2CUSTOMRECEIVETRANSACTIONCREATE PfnSercx2customreceivetransactioncreate; 

// Definition

WDFAPI PfnSercx2customreceivetransactioncreate 
(
	PSERCX_DRIVER_GLOBALS DriverGlobals
	SERCX2CUSTOMRECEIVE CustomReceive
	PSERCX2_CUSTOM_RECEIVE_TRANSACTION_CONFIG CustomReceiveTransactionConfig
	PWDF_OBJECT_ATTRIBUTES Attributes
	SERCX2CUSTOMRECEIVETRANSACTION *CustomReceiveTransaction
)
{...}

PFN_SERCX2CUSTOMRECEIVETRANSACTIONCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param CustomReceive: 
### -param CustomReceiveTransactionConfig: 
### -param Attributes: 
### -param *CustomReceiveTransaction: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also