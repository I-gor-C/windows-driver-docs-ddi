---
UID: NC.wdfregistry.PFN_WDFREGISTRYOPENKEY
title: PFN_WDFREGISTRYOPENKEY
author: windows-driver-content
description: 
ms.assetid: 7c27a6d7-9c34-42f6-afb2-c8d30d2448c8
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfregistry.h
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

# PFN_WDFREGISTRYOPENKEY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREGISTRYOPENKEY PfnWdfregistryopenkey; 

// Definition

WDFAPI PfnWdfregistryopenkey 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFKEY ParentKey
	PCUNICODE_STRING KeyName
	ACCESS_MASK DesiredAccess
	PWDF_OBJECT_ATTRIBUTES KeyAttributes
	WDFKEY *Key
)
{...}

PFN_WDFREGISTRYOPENKEY 


```

## -parameters

### -param DriverGlobals: 
### -param ParentKey: 
### -param KeyName: 
### -param DesiredAccess: 
### -param KeyAttributes: 
### -param *Key: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also