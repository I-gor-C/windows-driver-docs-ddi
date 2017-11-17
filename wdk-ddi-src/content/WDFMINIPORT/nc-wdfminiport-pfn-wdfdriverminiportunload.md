---
UID: NC.wdfminiport.PFN_WDFDRIVERMINIPORTUNLOAD
title: *PFN_WDFDRIVERMINIPORTUNLOAD
author: windows-driver-content
description: 
ms.assetid: 8381c007-fbbb-4d4a-9f06-c05608ffea71
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfminiport.h
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

# *PFN_WDFDRIVERMINIPORTUNLOAD callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_WDFDRIVERMINIPORTUNLOAD *PfnWdfdriverminiportunload; 

// Definition

VOID *PfnWdfdriverminiportunload 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDRIVER Driver
)
{...}

*PFN_WDFDRIVERMINIPORTUNLOAD 


```

## -parameters

### -param DriverGlobals: 
### -param Driver: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also