---
UID: NC.ntddk.pKdReleaseIntegratedDeviceForDebugging
title: pKdReleaseIntegratedDeviceForDebugging
author: windows-driver-content
description: 
ms.assetid: c96d37c3-0341-485d-a66f-08924c7d4964
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntddk.h
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

# pKdReleaseIntegratedDeviceForDebugging callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

pKdReleaseIntegratedDeviceForDebugging Pkdreleaseintegrateddevicefordebugging; 

// Definition

NTSTATUS Pkdreleaseintegrateddevicefordebugging 
(
	PDEBUG_DEVICE_DESCRIPTOR IntegratedDevice
)
{...}

pKdReleaseIntegratedDeviceForDebugging 


```

## -parameters

### -param IntegratedDevice: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also