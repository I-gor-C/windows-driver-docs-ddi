---
UID: NC.spbcx.PFN_SPBREQUESTGETTRANSFERPARAMETERS
title: PFN_SPBREQUESTGETTRANSFERPARAMETERS
author: windows-driver-content
description: 
ms.assetid: bcda49c9-14bd-420a-8ffb-18b6afaf747d
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: spbcx.h
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

# PFN_SPBREQUESTGETTRANSFERPARAMETERS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SPBREQUESTGETTRANSFERPARAMETERS PfnSpbrequestgettransferparameters; 

// Definition

WDFAPI PfnSpbrequestgettransferparameters 
(
	PSPB_DRIVER_GLOBALS DriverGlobals
	SPBREQUEST SpbRequest
	ULONG Index
	SPB_TRANSFER_DESCRIPTOR *TransferDescriptor
	PMDL *TransferBuffer
)
{...}

PFN_SPBREQUESTGETTRANSFERPARAMETERS 


```

## -parameters

### -param DriverGlobals: 
### -param SpbRequest: 
### -param Index: 
### -param *TransferDescriptor: 
### -param *TransferBuffer: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also