---
UID: NC.wdfchildlist.PFN_WDFCHILDLISTRETRIEVEPDO
title: PFN_WDFCHILDLISTRETRIEVEPDO
author: windows-driver-content
description: 
ms.assetid: 424c4191-faa4-4adb-9766-db02381fae74
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

# PFN_WDFCHILDLISTRETRIEVEPDO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFCHILDLISTRETRIEVEPDO PfnWdfchildlistretrievepdo; 

// Definition

WDFAPI PfnWdfchildlistretrievepdo 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFCHILDLIST ChildList
	PWDF_CHILD_RETRIEVE_INFO RetrieveInfo
)
{...}

PFN_WDFCHILDLISTRETRIEVEPDO 


```

## -parameters

### -param DriverGlobals: 
### -param ChildList: 
### -param RetrieveInfo: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also