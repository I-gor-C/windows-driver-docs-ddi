---
UID: NC.wdfdmatransaction.PFN_WDFDMATRANSACTIONSETDEVICEADDRESSOFFSET
title: PFN_WDFDMATRANSACTIONSETDEVICEADDRESSOFFSET
author: windows-driver-content
description: 
ms.assetid: 6c986134-6486-4e74-87cb-3ac7e8915f23
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

# PFN_WDFDMATRANSACTIONSETDEVICEADDRESSOFFSET callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDMATRANSACTIONSETDEVICEADDRESSOFFSET PfnWdfdmatransactionsetdeviceaddressoffset; 

// Definition

WDFAPI PfnWdfdmatransactionsetdeviceaddressoffset 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDMATRANSACTION DmaTransaction
	ULONG Offset
)
{...}

PFN_WDFDMATRANSACTIONSETDEVICEADDRESSOFFSET 


```

## -parameters

### -param DriverGlobals: 
### -param DmaTransaction: 
### -param Offset: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also