---
UID: NC.wdffdo.PFN_WDFFDOINITOPENREGISTRYKEY
title: PFN_WDFFDOINITOPENREGISTRYKEY
author: windows-driver-content
description: 
ms.assetid: 792bcda4-d2e1-4554-a4f3-56ca99156707
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdffdo.h
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

# PFN_WDFFDOINITOPENREGISTRYKEY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFFDOINITOPENREGISTRYKEY PfnWdffdoinitopenregistrykey; 

// Definition

WDFAPI PfnWdffdoinitopenregistrykey 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	ULONG DeviceInstanceKeyType
	ACCESS_MASK DesiredAccess
	PWDF_OBJECT_ATTRIBUTES KeyAttributes
	WDFKEY *Key
)
{...}

PFN_WDFFDOINITOPENREGISTRYKEY 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param DeviceInstanceKeyType: 
### -param DesiredAccess: 
### -param KeyAttributes: 
### -param *Key: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also