---
UID: NC.wdfchildlist.PFN_WDFCHILDLISTREQUESTCHILDEJECT
title: PFN_WDFCHILDLISTREQUESTCHILDEJECT
author: windows-driver-content
description: 
ms.assetid: dc1cc77f-4eaa-448a-aae2-4f1d6c1a19b9
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

# PFN_WDFCHILDLISTREQUESTCHILDEJECT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFCHILDLISTREQUESTCHILDEJECT PfnWdfchildlistrequestchildeject; 

// Definition

WDFAPI PfnWdfchildlistrequestchildeject 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFCHILDLIST ChildList
	PWDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER IdentificationDescription
)
{...}

PFN_WDFCHILDLISTREQUESTCHILDEJECT 


```

## -parameters

### -param DriverGlobals: 
### -param ChildList: 
### -param IdentificationDescription: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also