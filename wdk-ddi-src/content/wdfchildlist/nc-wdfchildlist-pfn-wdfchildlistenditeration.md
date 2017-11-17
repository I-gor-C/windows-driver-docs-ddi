---
UID: NC.wdfchildlist.PFN_WDFCHILDLISTENDITERATION
title: PFN_WDFCHILDLISTENDITERATION
author: windows-driver-content
description: 
ms.assetid: 20a611ff-74e5-425c-a26c-5b1dd77b577a
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfchildlist.h
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

# PFN_WDFCHILDLISTENDITERATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFCHILDLISTENDITERATION PfnWdfchildlistenditeration; 

// Definition

WDFAPI PfnWdfchildlistenditeration 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFCHILDLIST ChildList
	PWDF_CHILD_LIST_ITERATOR Iterator
)
{...}

PFN_WDFCHILDLISTENDITERATION 


```

## -parameters

### -param DriverGlobals: 
### -param ChildList: 
### -param Iterator: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also