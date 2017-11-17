---
UID: NC.wdfdriver.PFN_WDFDRIVEROPENPARAMETERSREGISTRYKEY
title: PFN_WDFDRIVEROPENPARAMETERSREGISTRYKEY
author: windows-driver-content
description: 
ms.assetid: d4ac9c28-2a30-443b-a46e-9f7ef2ccae08
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfdriver.h
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

# PFN_WDFDRIVEROPENPARAMETERSREGISTRYKEY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDRIVEROPENPARAMETERSREGISTRYKEY PfnWdfdriveropenparametersregistrykey; 

// Definition

WDFAPI PfnWdfdriveropenparametersregistrykey 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDRIVER Driver
	ACCESS_MASK DesiredAccess
	PWDF_OBJECT_ATTRIBUTES KeyAttributes
	WDFKEY *Key
)
{...}

PFN_WDFDRIVEROPENPARAMETERSREGISTRYKEY 


```

## -parameters

### -param DriverGlobals: 
### -param Driver: 
### -param DesiredAccess: 
### -param KeyAttributes: 
### -param *Key: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also