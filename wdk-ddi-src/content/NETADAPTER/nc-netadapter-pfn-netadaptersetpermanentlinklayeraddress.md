---
UID: NC.netadapter.PFN_NETADAPTERSETPERMANENTLINKLAYERADDRESS
title: PFN_NETADAPTERSETPERMANENTLINKLAYERADDRESS
author: windows-driver-content
description: 
ms.assetid: 98e132b3-63f1-4e68-83da-cd86ea4d9758
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

# PFN_NETADAPTERSETPERMANENTLINKLAYERADDRESS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETADAPTERSETPERMANENTLINKLAYERADDRESS PfnNetadaptersetpermanentlinklayeraddress; 

// Definition

WDFAPI PfnNetadaptersetpermanentlinklayeraddress 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETADAPTER Adapter
	PNET_ADAPTER_LINK_LAYER_ADDRESS LinkLayerAddress
)
{...}

PFN_NETADAPTERSETPERMANENTLINKLAYERADDRESS 


```

## -parameters

### -param DriverGlobals: 
### -param Adapter: 
### -param LinkLayerAddress: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also