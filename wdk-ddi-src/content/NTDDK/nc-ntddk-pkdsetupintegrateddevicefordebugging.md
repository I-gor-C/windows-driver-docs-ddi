---
UID: NC.ntddk.pKdSetupIntegratedDeviceForDebugging
title: pKdSetupIntegratedDeviceForDebugging
author: windows-driver-content
description: 
ms.assetid: e9fab1c4-5d8e-4703-bc5f-b9827a0f80e6
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

# pKdSetupIntegratedDeviceForDebugging callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

pKdSetupIntegratedDeviceForDebugging Pkdsetupintegrateddevicefordebugging; 

// Definition

NTSTATUS Pkdsetupintegrateddevicefordebugging 
(
	PVOID LoaderBlock
	OPTIONAL PDEBUG_DEVICE_DESCRIPTOR IntegratedDevice
)
{...}

pKdSetupIntegratedDeviceForDebugging 


```

## -parameters

### -param LoaderBlock: 
### -param IntegratedDevice: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also