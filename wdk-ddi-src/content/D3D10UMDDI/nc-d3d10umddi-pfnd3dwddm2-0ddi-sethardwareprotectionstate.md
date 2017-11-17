---
UID: NC.d3d10umddi.PFND3DWDDM2_0DDI_SETHARDWAREPROTECTIONSTATE
title: PFND3DWDDM2_0DDI_SETHARDWAREPROTECTIONSTATE
author: windows-driver-content
description: 
ms.assetid: 1618cbbb-f7fe-4a8d-8308-bb158e83f5e3
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3d10umddi.h
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

# PFND3DWDDM2_0DDI_SETHARDWAREPROTECTIONSTATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DWDDM2_0DDI_SETHARDWAREPROTECTIONSTATE Pfnd3dwddm20DdiSethardwareprotectionstate; 

// Definition

void Pfnd3dwddm20DdiSethardwareprotectionstate 
(
	 D3D10DDI_HDEVICE
	BOOL HwProtectionEnable
)
{...}

PFND3DWDDM2_0DDI_SETHARDWAREPROTECTIONSTATE 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param HwProtectionEnable: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also