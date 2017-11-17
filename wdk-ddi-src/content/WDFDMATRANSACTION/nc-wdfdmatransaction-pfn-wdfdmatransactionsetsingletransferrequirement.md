---
UID: NC.wdfdmatransaction.PFN_WDFDMATRANSACTIONSETSINGLETRANSFERREQUIREMENT
title: PFN_WDFDMATRANSACTIONSETSINGLETRANSFERREQUIREMENT
author: windows-driver-content
description: 
ms.assetid: e179c82e-e59c-48dc-bf3a-6d21021bcfce
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

# PFN_WDFDMATRANSACTIONSETSINGLETRANSFERREQUIREMENT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDMATRANSACTIONSETSINGLETRANSFERREQUIREMENT PfnWdfdmatransactionsetsingletransferrequirement; 

// Definition

WDFAPI PfnWdfdmatransactionsetsingletransferrequirement 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDMATRANSACTION DmaTransaction
	BOOLEAN RequireSingleTransfer
)
{...}

PFN_WDFDMATRANSACTIONSETSINGLETRANSFERREQUIREMENT 


```

## -parameters

### -param DriverGlobals: 
### -param DmaTransaction: 
### -param RequireSingleTransfer: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also