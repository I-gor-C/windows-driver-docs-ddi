---
UID: NC.netadapter.PFN_NETADAPTERDEVICEINITCONFIG
title: PFN_NETADAPTERDEVICEINITCONFIG
author: windows-driver-content
description: 
ms.assetid: 9d0e4c2e-ba94-4686-8fb6-32fe33ec56a4
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: netadapter.h
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

# PFN_NETADAPTERDEVICEINITCONFIG callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETADAPTERDEVICEINITCONFIG PfnNetadapterdeviceinitconfig; 

// Definition

WDFAPI PfnNetadapterdeviceinitconfig 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
)
{...}

PFN_NETADAPTERDEVICEINITCONFIG 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also