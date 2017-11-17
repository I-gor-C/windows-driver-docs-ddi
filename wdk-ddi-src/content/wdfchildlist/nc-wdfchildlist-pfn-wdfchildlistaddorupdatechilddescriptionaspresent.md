---
UID: NC.wdfchildlist.PFN_WDFCHILDLISTADDORUPDATECHILDDESCRIPTIONASPRESENT
title: PFN_WDFCHILDLISTADDORUPDATECHILDDESCRIPTIONASPRESENT
author: windows-driver-content
description: 
ms.assetid: 6a9e0f5c-2594-41f4-97fe-10a825993dc1
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

# PFN_WDFCHILDLISTADDORUPDATECHILDDESCRIPTIONASPRESENT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFCHILDLISTADDORUPDATECHILDDESCRIPTIONASPRESENT PfnWdfchildlistaddorupdatechilddescriptionaspresent; 

// Definition

WDFAPI PfnWdfchildlistaddorupdatechilddescriptionaspresent 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFCHILDLIST ChildList
	PWDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER IdentificationDescription
	PWDF_CHILD_ADDRESS_DESCRIPTION_HEADER AddressDescription
)
{...}

PFN_WDFCHILDLISTADDORUPDATECHILDDESCRIPTIONASPRESENT 


```

## -parameters

### -param DriverGlobals: 
### -param ChildList: 
### -param IdentificationDescription: 
### -param AddressDescription: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also