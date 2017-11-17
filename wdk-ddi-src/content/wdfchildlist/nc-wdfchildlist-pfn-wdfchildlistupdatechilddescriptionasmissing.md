---
UID: NC.wdfchildlist.PFN_WDFCHILDLISTUPDATECHILDDESCRIPTIONASMISSING
title: PFN_WDFCHILDLISTUPDATECHILDDESCRIPTIONASMISSING
author: windows-driver-content
description: 
ms.assetid: 11ca9a3a-6a65-4e7b-9c7e-e4012b88035f
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

# PFN_WDFCHILDLISTUPDATECHILDDESCRIPTIONASMISSING callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFCHILDLISTUPDATECHILDDESCRIPTIONASMISSING PfnWdfchildlistupdatechilddescriptionasmissing; 

// Definition

WDFAPI PfnWdfchildlistupdatechilddescriptionasmissing 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFCHILDLIST ChildList
	PWDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER IdentificationDescription
)
{...}

PFN_WDFCHILDLISTUPDATECHILDDESCRIPTIONASMISSING 


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