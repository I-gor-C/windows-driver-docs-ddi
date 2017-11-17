---
UID: NC.wdffdo.PFN_WDFFDOINITSETDEFAULTCHILDLISTCONFIG
title: PFN_WDFFDOINITSETDEFAULTCHILDLISTCONFIG
author: windows-driver-content
description: 
ms.assetid: 1b19b968-25f7-4909-9f0d-c4fc90c16932
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

# PFN_WDFFDOINITSETDEFAULTCHILDLISTCONFIG callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFFDOINITSETDEFAULTCHILDLISTCONFIG PfnWdffdoinitsetdefaultchildlistconfig; 

// Definition

WDFAPI PfnWdffdoinitsetdefaultchildlistconfig 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	PWDF_CHILD_LIST_CONFIG Config
	PWDF_OBJECT_ATTRIBUTES DefaultChildListAttributes
)
{...}

PFN_WDFFDOINITSETDEFAULTCHILDLISTCONFIG 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param Config: 
### -param DefaultChildListAttributes: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also