---
UID: NC.wdfdmatransaction.PFN_WDFDMATRANSACTIONDMACOMPLETEDWITHLENGTH
title: PFN_WDFDMATRANSACTIONDMACOMPLETEDWITHLENGTH
author: windows-driver-content
description: 
ms.assetid: 1ca7bb8a-e487-4e2d-85c9-3279369c6e3b
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

# PFN_WDFDMATRANSACTIONDMACOMPLETEDWITHLENGTH callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDMATRANSACTIONDMACOMPLETEDWITHLENGTH PfnWdfdmatransactiondmacompletedwithlength; 

// Definition

WDFAPI PfnWdfdmatransactiondmacompletedwithlength 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDMATRANSACTION DmaTransaction
	size_t TransferredLength
	NTSTATUS *Status
)
{...}

PFN_WDFDMATRANSACTIONDMACOMPLETEDWITHLENGTH 


```

## -parameters

### -param DriverGlobals: 
### -param DmaTransaction: 
### -param TransferredLength: 
### -param *Status: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also