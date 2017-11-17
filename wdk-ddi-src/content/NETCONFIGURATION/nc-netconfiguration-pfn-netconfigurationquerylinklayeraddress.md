---
UID: NC.netconfiguration.PFN_NETCONFIGURATIONQUERYLINKLAYERADDRESS
title: PFN_NETCONFIGURATIONQUERYLINKLAYERADDRESS
author: windows-driver-content
description: 
ms.assetid: d1f7de40-2ff2-400d-96ee-2b6c03cef1fd
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: netconfiguration.h
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

# PFN_NETCONFIGURATIONQUERYLINKLAYERADDRESS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETCONFIGURATIONQUERYLINKLAYERADDRESS PfnNetconfigurationquerylinklayeraddress; 

// Definition

WDFAPI PfnNetconfigurationquerylinklayeraddress 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETCONFIGURATION Configuration
	PNET_ADAPTER_LINK_LAYER_ADDRESS LinkLayerAddress
)
{...}

PFN_NETCONFIGURATIONQUERYLINKLAYERADDRESS 


```

## -parameters

### -param DriverGlobals: 
### -param Configuration: 
### -param LinkLayerAddress: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also