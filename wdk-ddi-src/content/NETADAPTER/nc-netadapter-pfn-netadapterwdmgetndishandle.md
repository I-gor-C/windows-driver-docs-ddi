---
UID: NC.netadapter.PFN_NETADAPTERWDMGETNDISHANDLE
title: *PFN_NETADAPTERWDMGETNDISHANDLE
author: windows-driver-content
description: 
ms.assetid: 5b4b23a9-5ef6-47e4-8ec0-dc5761f5c723
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

# *PFN_NETADAPTERWDMGETNDISHANDLE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_NETADAPTERWDMGETNDISHANDLE *PfnNetadapterwdmgetndishandle; 

// Definition

NDIS_HANDLE *PfnNetadapterwdmgetndishandle 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETADAPTER Adapter
)
{...}

*PFN_NETADAPTERWDMGETNDISHANDLE 


```

## -parameters

### -param DriverGlobals: 
### -param Adapter: 



## -returns

Returns NDIS_HANDLE that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also