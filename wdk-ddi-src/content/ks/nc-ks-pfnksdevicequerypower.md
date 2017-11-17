---
UID: NC.ks.PFNKSDEVICEQUERYPOWER
title: PFNKSDEVICEQUERYPOWER
author: windows-driver-content
description: 
ms.assetid: baee7968-42ae-4c75-81cc-ca898928eb64
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ks.h
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

# PFNKSDEVICEQUERYPOWER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSDEVICEQUERYPOWER Pfnksdevicequerypower; 

// Definition

NTSTATUS Pfnksdevicequerypower 
(
	PKSDEVICE Device
	PIRP Irp
	DEVICE_POWER_STATE DeviceTo
	DEVICE_POWER_STATE DeviceFrom
	SYSTEM_POWER_STATE SystemTo
	SYSTEM_POWER_STATE SystemFrom
	POWER_ACTION Action
)
{...}

PFNKSDEVICEQUERYPOWER 


```

## -parameters

### -param Device: 
### -param Irp: 
### -param DeviceTo: 
### -param DeviceFrom: 
### -param SystemTo: 
### -param SystemFrom: 
### -param Action: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also