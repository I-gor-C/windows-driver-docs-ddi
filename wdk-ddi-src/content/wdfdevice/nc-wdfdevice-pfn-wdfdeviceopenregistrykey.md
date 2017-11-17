---
UID: NC.wdfdevice.PFN_WDFDEVICEOPENREGISTRYKEY
title: PFN_WDFDEVICEOPENREGISTRYKEY
author: windows-driver-content
description: 
ms.assetid: 00245e36-3873-4e9d-92c9-330728fe846a
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

# PFN_WDFDEVICEOPENREGISTRYKEY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEOPENREGISTRYKEY PfnWdfdeviceopenregistrykey; 

// Definition

WDFAPI PfnWdfdeviceopenregistrykey 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	ULONG DeviceInstanceKeyType
	ACCESS_MASK DesiredAccess
	PWDF_OBJECT_ATTRIBUTES KeyAttributes
	WDFKEY *Key
)
{...}

PFN_WDFDEVICEOPENREGISTRYKEY 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param DeviceInstanceKeyType: 
### -param DesiredAccess: 
### -param KeyAttributes: 
### -param *Key: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also