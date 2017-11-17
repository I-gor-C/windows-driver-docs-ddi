---
UID: NC.extsfns.PGET_CPU_PSPEED_INFO
title: PGET_CPU_PSPEED_INFO
author: windows-driver-content
description: 
ms.assetid: cf4ba6eb-f4e7-4772-b24b-de2ba21b87fe
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: extsfns.h
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

# PGET_CPU_PSPEED_INFO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PGET_CPU_PSPEED_INFO PgetCpuPspeedInfo; 

// Definition

HRESULT PgetCpuPspeedInfo 
(
	IN PDEBUG_CLIENT Client
	OUT PDEBUG_CPU_SPEED_INFO pCpuSpeedInfo
)
{...}

PGET_CPU_PSPEED_INFO 


```

## -parameters

### -param Client: 
### -param pCpuSpeedInfo: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also