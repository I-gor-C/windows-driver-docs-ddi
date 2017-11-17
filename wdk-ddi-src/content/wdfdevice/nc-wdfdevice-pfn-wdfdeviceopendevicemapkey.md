---
UID: NC.wdfdevice.PFN_WDFDEVICEOPENDEVICEMAPKEY
title: PFN_WDFDEVICEOPENDEVICEMAPKEY
author: windows-driver-content
description: 
ms.assetid: fd74435c-1cf4-40e4-9eb3-7a63adfb8bad
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfdevice.h
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

# PFN_WDFDEVICEOPENDEVICEMAPKEY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEOPENDEVICEMAPKEY PfnWdfdeviceopendevicemapkey; 

// Definition

WDFAPI PfnWdfdeviceopendevicemapkey 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PCUNICODE_STRING KeyName
	ACCESS_MASK DesiredAccess
	PWDF_OBJECT_ATTRIBUTES KeyAttributes
	WDFKEY *Key
)
{...}

PFN_WDFDEVICEOPENDEVICEMAPKEY 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param KeyName: 
### -param DesiredAccess: 
### -param KeyAttributes: 
### -param *Key: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also