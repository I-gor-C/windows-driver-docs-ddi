---
UID: NC.netadapter.PFN_NETADAPTERSETDATAPATHCAPABILITIES
title: PFN_NETADAPTERSETDATAPATHCAPABILITIES
author: windows-driver-content
description: 
ms.assetid: 339e6a6b-cb38-45da-8cd1-2c138dab2167
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

# PFN_NETADAPTERSETDATAPATHCAPABILITIES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETADAPTERSETDATAPATHCAPABILITIES PfnNetadaptersetdatapathcapabilities; 

// Definition

WDFAPI PfnNetadaptersetdatapathcapabilities 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETADAPTER Adapter
	PNET_ADAPTER_DATAPATH_CAPABILITIES DataPathCapabilities
)
{...}

PFN_NETADAPTERSETDATAPATHCAPABILITIES 


```

## -parameters

### -param DriverGlobals: 
### -param Adapter: 
### -param DataPathCapabilities: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also