---
UID: NC.wdfpdo.PFN_WDFPDOUPDATEADDRESSDESCRIPTION
title: PFN_WDFPDOUPDATEADDRESSDESCRIPTION
author: windows-driver-content
description: 
ms.assetid: 3026dd58-1a2a-4652-a66a-70aa9beb1f06
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

# PFN_WDFPDOUPDATEADDRESSDESCRIPTION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFPDOUPDATEADDRESSDESCRIPTION PfnWdfpdoupdateaddressdescription; 

// Definition

WDFAPI PfnWdfpdoupdateaddressdescription 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PWDF_CHILD_ADDRESS_DESCRIPTION_HEADER AddressDescription
)
{...}

PFN_WDFPDOUPDATEADDRESSDESCRIPTION 


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