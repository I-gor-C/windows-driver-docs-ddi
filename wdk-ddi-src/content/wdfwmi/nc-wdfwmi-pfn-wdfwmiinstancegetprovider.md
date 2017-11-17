---
UID: NC.wdfwmi.PFN_WDFWMIINSTANCEGETPROVIDER
title: PFN_WDFWMIINSTANCEGETPROVIDER
author: windows-driver-content
description: 
ms.assetid: 8194c4c9-b036-45e0-a0b9-645f400a704f
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfwmi.h
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

# PFN_WDFWMIINSTANCEGETPROVIDER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFWMIINSTANCEGETPROVIDER PfnWdfwmiinstancegetprovider; 

// Definition

WDFAPI PfnWdfwmiinstancegetprovider 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFWMIINSTANCE WmiInstance
)
{...}

PFN_WDFWMIINSTANCEGETPROVIDER 


```

## -parameters

### -param DriverGlobals: 
### -param WmiInstance: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also