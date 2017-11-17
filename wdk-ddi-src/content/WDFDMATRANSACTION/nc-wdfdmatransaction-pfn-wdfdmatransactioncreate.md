---
UID: NC.wdfdmatransaction.PFN_WDFDMATRANSACTIONCREATE
title: PFN_WDFDMATRANSACTIONCREATE
author: windows-driver-content
description: 
ms.assetid: a1845c1d-3caa-422d-99f4-48413ece8d2a
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

# PFN_WDFDMATRANSACTIONCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDMATRANSACTIONCREATE PfnWdfdmatransactioncreate; 

// Definition

WDFAPI PfnWdfdmatransactioncreate 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDMAENABLER DmaEnabler
	PWDF_OBJECT_ATTRIBUTES Attributes
	WDFDMATRANSACTION *DmaTransaction
)
{...}

PFN_WDFDMATRANSACTIONCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param DmaEnabler: 
### -param Attributes: 
### -param *DmaTransaction: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also