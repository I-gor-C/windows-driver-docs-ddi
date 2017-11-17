---
UID: NC.netadapter.PFN_NETADAPTERCREATE
title: PFN_NETADAPTERCREATE
author: windows-driver-content
description: 
ms.assetid: 3ce30ebe-8c02-49f8-a5ed-9ef7ad41cc74
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

# PFN_NETADAPTERCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETADAPTERCREATE PfnNetadaptercreate; 

// Definition

WDFAPI PfnNetadaptercreate 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PWDF_OBJECT_ATTRIBUTES AdapterAttributes
	PNET_ADAPTER_CONFIG Configuration
	NETADAPTER *Adapter
)
{...}

PFN_NETADAPTERCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param AdapterAttributes: 
### -param Configuration: 
### -param *Adapter: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also