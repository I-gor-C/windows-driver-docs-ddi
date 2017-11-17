---
UID: NC.wdfregistry.PFN_WDFREGISTRYCREATEKEY
title: PFN_WDFREGISTRYCREATEKEY
author: windows-driver-content
description: 
ms.assetid: 39013ba6-0777-4a8b-b4f5-6fd70c89697f
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

# PFN_WDFREGISTRYCREATEKEY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREGISTRYCREATEKEY PfnWdfregistrycreatekey; 

// Definition

WDFAPI PfnWdfregistrycreatekey 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFKEY ParentKey
	PCUNICODE_STRING KeyName
	ACCESS_MASK DesiredAccess
	ULONG CreateOptions
	PULONG CreateDisposition
	PWDF_OBJECT_ATTRIBUTES KeyAttributes
	WDFKEY *Key
)
{...}

PFN_WDFREGISTRYCREATEKEY 


```

## -parameters

### -param DriverGlobals: 
### -param ParentKey: 
### -param KeyName: 
### -param DesiredAccess: 
### -param CreateOptions: 
### -param CreateDisposition: 
### -param KeyAttributes: 
### -param *Key: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also