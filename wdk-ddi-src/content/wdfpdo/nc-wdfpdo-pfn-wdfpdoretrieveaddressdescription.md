---
UID: NC.wdfpdo.PFN_WDFPDORETRIEVEADDRESSDESCRIPTION
title: PFN_WDFPDORETRIEVEADDRESSDESCRIPTION
author: windows-driver-content
description: 
ms.assetid: e3cbe9ba-1f85-48db-9e06-9d29bf8508d8
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

# PFN_WDFPDORETRIEVEADDRESSDESCRIPTION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFPDORETRIEVEADDRESSDESCRIPTION PfnWdfpdoretrieveaddressdescription; 

// Definition

WDFAPI PfnWdfpdoretrieveaddressdescription 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PWDF_CHILD_ADDRESS_DESCRIPTION_HEADER AddressDescription
)
{...}

PFN_WDFPDORETRIEVEADDRESSDESCRIPTION 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param AddressDescription: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also