---
UID: NC.sercx.PFN_SERCX2CUSTOMRECEIVETRANSACTIONNEWDATANOTIFICATION
title: PFN_SERCX2CUSTOMRECEIVETRANSACTIONNEWDATANOTIFICATION
author: windows-driver-content
description: 
ms.assetid: e2e02eb0-b86b-4c7b-863e-7ee76d94846f
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

# PFN_SERCX2CUSTOMRECEIVETRANSACTIONNEWDATANOTIFICATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCX2CUSTOMRECEIVETRANSACTIONNEWDATANOTIFICATION PfnSercx2customreceivetransactionnewdatanotification; 

// Definition

WDFAPI PfnSercx2customreceivetransactionnewdatanotification 
(
	PSERCX_DRIVER_GLOBALS DriverGlobals
	SERCX2CUSTOMRECEIVETRANSACTION CustomReceiveTransaction
)
{...}

PFN_SERCX2CUSTOMRECEIVETRANSACTIONNEWDATANOTIFICATION 


```

## -parameters

### -param DriverGlobals: 
### -param CustomReceiveTransaction: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also