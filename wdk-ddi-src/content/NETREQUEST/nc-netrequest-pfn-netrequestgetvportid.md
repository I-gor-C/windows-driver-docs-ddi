---
UID: NC.netrequest.PFN_NETREQUESTGETVPORTID
title: PFN_NETREQUESTGETVPORTID
author: windows-driver-content
description: 
ms.assetid: c786f855-48d4-4cae-9086-3a3cc121fea3
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: netrequest.h
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

# PFN_NETREQUESTGETVPORTID callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETREQUESTGETVPORTID PfnNetrequestgetvportid; 

// Definition

WDFAPI PfnNetrequestgetvportid 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETREQUEST Request
)
{...}

PFN_NETREQUESTGETVPORTID 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also