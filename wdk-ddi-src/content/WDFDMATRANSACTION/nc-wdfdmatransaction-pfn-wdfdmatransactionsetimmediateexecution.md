---
UID: NC.wdfdmatransaction.PFN_WDFDMATRANSACTIONSETIMMEDIATEEXECUTION
title: PFN_WDFDMATRANSACTIONSETIMMEDIATEEXECUTION
author: windows-driver-content
description: 
ms.assetid: e306376b-e508-446b-ac53-4a6096d0c35b
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

# PFN_WDFDMATRANSACTIONSETIMMEDIATEEXECUTION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDMATRANSACTIONSETIMMEDIATEEXECUTION PfnWdfdmatransactionsetimmediateexecution; 

// Definition

WDFAPI PfnWdfdmatransactionsetimmediateexecution 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDMATRANSACTION DmaTransaction
	BOOLEAN UseImmediateExecution
)
{...}

PFN_WDFDMATRANSACTIONSETIMMEDIATEEXECUTION 


```

## -parameters

### -param DriverGlobals: 
### -param DmaTransaction: 
### -param UseImmediateExecution: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also