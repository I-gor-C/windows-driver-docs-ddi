---
UID: NC.srb.PHW_ADAPTER_CONTROL
title: PHW_ADAPTER_CONTROL
author: windows-driver-content
description: 
ms.assetid: 07755bfa-3585-4b46-9aeb-68afee97f4f9
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: srb.h
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

# PHW_ADAPTER_CONTROL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PHW_ADAPTER_CONTROL PhwAdapterControl; 

// Definition

SCSI_ADAPTER_CONTROL_STATUS PhwAdapterControl 
(
	PVOID DeviceExtension
	SCSI_ADAPTER_CONTROL_TYPE ControlType
	PVOID Parameters
)
{...}

PHW_ADAPTER_CONTROL 


```

## -parameters

### -param DeviceExtension: 
### -param ControlType: 
### -param Parameters: 



## -returns

Returns SCSI_ADAPTER_CONTROL_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also