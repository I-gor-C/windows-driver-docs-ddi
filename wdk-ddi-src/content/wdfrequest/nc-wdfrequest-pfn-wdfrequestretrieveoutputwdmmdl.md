---
UID: NC.wdfrequest.PFN_WDFREQUESTRETRIEVEOUTPUTWDMMDL
title: PFN_WDFREQUESTRETRIEVEOUTPUTWDMMDL
author: windows-driver-content
description: 
ms.assetid: 5466dc34-1629-462b-be63-6e41ac9292ad
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfrequest.h
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

# PFN_WDFREQUESTRETRIEVEOUTPUTWDMMDL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREQUESTRETRIEVEOUTPUTWDMMDL PfnWdfrequestretrieveoutputwdmmdl; 

// Definition

WDFAPI PfnWdfrequestretrieveoutputwdmmdl 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFREQUEST Request
	PMDL *Mdl
)
{...}

PFN_WDFREQUESTRETRIEVEOUTPUTWDMMDL 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 
### -param *Mdl: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also