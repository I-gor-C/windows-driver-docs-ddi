---
UID: NC.netadapter.PFN_NETADAPTERSETCURRENTLINKSTATE
title: PFN_NETADAPTERSETCURRENTLINKSTATE
author: windows-driver-content
description: 
ms.assetid: 18765675-df3b-4d48-89a5-41adf728e88c
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

# PFN_NETADAPTERSETCURRENTLINKSTATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETADAPTERSETCURRENTLINKSTATE PfnNetadaptersetcurrentlinkstate; 

// Definition

WDFAPI PfnNetadaptersetcurrentlinkstate 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETADAPTER Adapter
	PNET_ADAPTER_LINK_STATE CurrentLinkState
)
{...}

PFN_NETADAPTERSETCURRENTLINKSTATE 


```

## -parameters

### -param DriverGlobals: 
### -param Adapter: 
### -param CurrentLinkState: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also