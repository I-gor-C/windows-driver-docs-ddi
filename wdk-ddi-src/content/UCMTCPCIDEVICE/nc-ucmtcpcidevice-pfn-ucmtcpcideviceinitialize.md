---
UID: NC.ucmtcpcidevice.PFN_UCMTCPCIDEVICEINITIALIZE
title: PFN_UCMTCPCIDEVICEINITIALIZE
author: windows-driver-content
description: 
ms.assetid: 472d822e-d7c6-4ff1-9879-84fdf814f276
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ucmtcpcidevice.h
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

# PFN_UCMTCPCIDEVICEINITIALIZE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_UCMTCPCIDEVICEINITIALIZE PfnUcmtcpcideviceinitialize; 

// Definition

WDFAPI PfnUcmtcpcideviceinitialize 
(
	PUCMTCPCI_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE WdfDevice
	PUCMTCPCI_DEVICE_CONFIG Config
)
{...}

PFN_UCMTCPCIDEVICEINITIALIZE 


```

## -parameters

### -param DriverGlobals: 
### -param WdfDevice: 
### -param Config: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also