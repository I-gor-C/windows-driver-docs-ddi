---
UID: NC.d3dcaps.LPD3DENUMDEVICESCALLBACK
title: LPD3DENUMDEVICESCALLBACK
author: windows-driver-content
description: 
ms.assetid: 3470a48c-1f7c-4b89-90f3-5f1090f66348
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3dcaps.h
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

# LPD3DENUMDEVICESCALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

LPD3DENUMDEVICESCALLBACK Lpd3denumdevicescallback; 

// Definition

HRESULT Lpd3denumdevicescallback 
(
	GUID *lpGuid
	LPSTR lpDeviceDescription
	LPSTR lpDeviceName
	 LPD3DDEVICEDESC
	 LPD3DDEVICEDESC
	 LPVOID
)
{...}

LPD3DENUMDEVICESCALLBACK 


```

## -parameters

### -param *lpGuid: 
### -param lpDeviceDescription: 
### -param lpDeviceName: 
### -param LPD3DDEVICEDESC: 
### -param LPD3DDEVICEDESC: 
### -param LPVOID: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also