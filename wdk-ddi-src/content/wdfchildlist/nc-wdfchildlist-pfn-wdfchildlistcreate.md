---
UID: NC.wdfchildlist.PFN_WDFCHILDLISTCREATE
title: PFN_WDFCHILDLISTCREATE
author: windows-driver-content
description: 
ms.assetid: a53c4638-c5e5-4454-bfe8-0885b5fb6a6e
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

# PFN_WDFCHILDLISTCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFCHILDLISTCREATE PfnWdfchildlistcreate; 

// Definition

WDFAPI PfnWdfchildlistcreate 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PWDF_CHILD_LIST_CONFIG Config
	PWDF_OBJECT_ATTRIBUTES ChildListAttributes
	WDFCHILDLIST *ChildList
)
{...}

PFN_WDFCHILDLISTCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param Config: 
### -param ChildListAttributes: 
### -param *ChildList: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also