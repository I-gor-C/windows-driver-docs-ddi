---
UID: NC.wdfdmatransaction.PFN_WDFDMATRANSACTIONDMACOMPLETED
title: PFN_WDFDMATRANSACTIONDMACOMPLETED
author: windows-driver-content
description: 
ms.assetid: 891bf884-313f-402e-ab99-c8f0c72aff34
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfdmatransaction.h
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

# PFN_WDFDMATRANSACTIONDMACOMPLETED callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDMATRANSACTIONDMACOMPLETED PfnWdfdmatransactiondmacompleted; 

// Definition

WDFAPI PfnWdfdmatransactiondmacompleted 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDMATRANSACTION DmaTransaction
	NTSTATUS *Status
)
{...}

PFN_WDFDMATRANSACTIONDMACOMPLETED 


```

## -parameters

### -param DriverGlobals: 
### -param DmaTransaction: 
### -param *Status: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also