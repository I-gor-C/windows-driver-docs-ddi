---
UID: NC.wdfpdo.PFN_WDFPDORETRIEVEIDENTIFICATIONDESCRIPTION
title: PFN_WDFPDORETRIEVEIDENTIFICATIONDESCRIPTION
author: windows-driver-content
description: 
ms.assetid: d2ccca3a-dc8a-445e-a666-423b55a16265
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfpdo.h
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

# PFN_WDFPDORETRIEVEIDENTIFICATIONDESCRIPTION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFPDORETRIEVEIDENTIFICATIONDESCRIPTION PfnWdfpdoretrieveidentificationdescription; 

// Definition

WDFAPI PfnWdfpdoretrieveidentificationdescription 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PWDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER IdentificationDescription
)
{...}

PFN_WDFPDORETRIEVEIDENTIFICATIONDESCRIPTION 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param IdentificationDescription: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also