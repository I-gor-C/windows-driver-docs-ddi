---
UID: NC.wdfdmatransaction.PFN_WDFDMATRANSACTIONEXECUTE
title: PFN_WDFDMATRANSACTIONEXECUTE
author: windows-driver-content
description: 
ms.assetid: 759de516-53cf-48e7-9679-a2f47aaac3fb
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

# PFN_WDFDMATRANSACTIONEXECUTE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDMATRANSACTIONEXECUTE PfnWdfdmatransactionexecute; 

// Definition

WDFAPI PfnWdfdmatransactionexecute 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDMATRANSACTION DmaTransaction
	WDFCONTEXT Context
)
{...}

PFN_WDFDMATRANSACTIONEXECUTE 


```

## -parameters

### -param DriverGlobals: 
### -param DmaTransaction: 
### -param Context: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also