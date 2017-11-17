---
UID: NC.wdfrequest.PFN_WDFREQUESTRETRIEVEINPUTWDMMDL
title: PFN_WDFREQUESTRETRIEVEINPUTWDMMDL
author: windows-driver-content
description: 
ms.assetid: 638b8d28-5be5-4984-a997-aa107e91aa2b
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

# PFN_WDFREQUESTRETRIEVEINPUTWDMMDL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREQUESTRETRIEVEINPUTWDMMDL PfnWdfrequestretrieveinputwdmmdl; 

// Definition

WDFAPI PfnWdfrequestretrieveinputwdmmdl 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFREQUEST Request
	PMDL *Mdl
)
{...}

PFN_WDFREQUESTRETRIEVEINPUTWDMMDL 


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