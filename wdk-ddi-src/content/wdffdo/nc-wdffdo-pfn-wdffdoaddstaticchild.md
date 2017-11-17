---
UID: NC.wdffdo.PFN_WDFFDOADDSTATICCHILD
title: PFN_WDFFDOADDSTATICCHILD
author: windows-driver-content
description: 
ms.assetid: 87f9e698-77d0-4ad9-83de-cc5e55aaafbe
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdffdo.h
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

# PFN_WDFFDOADDSTATICCHILD callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFFDOADDSTATICCHILD PfnWdffdoaddstaticchild; 

// Definition

WDFAPI PfnWdffdoaddstaticchild 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Fdo
	WDFDEVICE Child
)
{...}

PFN_WDFFDOADDSTATICCHILD 


```

## -parameters

### -param DriverGlobals: 
### -param Fdo: 
### -param Child: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also