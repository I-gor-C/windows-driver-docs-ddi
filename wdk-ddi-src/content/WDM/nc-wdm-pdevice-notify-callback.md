---
UID: NC.wdm.PDEVICE_NOTIFY_CALLBACK
title: PDEVICE_NOTIFY_CALLBACK
author: windows-driver-content
description: 
ms.assetid: f40d7da9-b0d6-4533-b48a-61c47adcda26
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdm.h
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

# PDEVICE_NOTIFY_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PDEVICE_NOTIFY_CALLBACK PdeviceNotifyCallback; 

// Definition

VOID PdeviceNotifyCallback 
(
	 PVOID
	 ULONG
)
{...}

PDEVICE_NOTIFY_CALLBACK 


```

## -parameters

### -param PVOID: 
### -param ULONG: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also