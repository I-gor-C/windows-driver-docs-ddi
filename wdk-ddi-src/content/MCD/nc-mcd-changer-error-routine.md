---
UID: NC.mcd.CHANGER_ERROR_ROUTINE
title: CHANGER_ERROR_ROUTINE
author: windows-driver-content
description: 
ms.assetid: f52ea1ff-3f87-4b16-a70c-978a3dad2bbb
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: mcd.h
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

# CHANGER_ERROR_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

CHANGER_ERROR_ROUTINE ChangerErrorRoutine; 

// Definition

VOID ChangerErrorRoutine 
(
	PDEVICE_OBJECT DeviceObject
	PSCSI_REQUEST_BLOCK Srb
	NTSTATUS *Status
	BOOLEAN *Retry
)
{...}

CHANGER_ERROR_ROUTINE 


```

## -parameters

### -param DeviceObject: 
### -param Srb: 
### -param *Status: 
### -param *Retry: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also