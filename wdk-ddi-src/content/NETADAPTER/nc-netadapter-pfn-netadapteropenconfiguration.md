---
UID: NC.netadapter.PFN_NETADAPTEROPENCONFIGURATION
title: PFN_NETADAPTEROPENCONFIGURATION
author: windows-driver-content
description: 
ms.assetid: eb5ae91d-33d0-45f9-906f-4e0c1b996a0e
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

# PFN_NETADAPTEROPENCONFIGURATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETADAPTEROPENCONFIGURATION PfnNetadapteropenconfiguration; 

// Definition

WDFAPI PfnNetadapteropenconfiguration 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETADAPTER Adapter
	PWDF_OBJECT_ATTRIBUTES ConfigurationAttributes
	NETCONFIGURATION *Configuration
)
{...}

PFN_NETADAPTEROPENCONFIGURATION 


```

## -parameters

### -param DriverGlobals: 
### -param Adapter: 
### -param ConfigurationAttributes: 
### -param *Configuration: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also