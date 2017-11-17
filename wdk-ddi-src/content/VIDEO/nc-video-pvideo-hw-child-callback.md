---
UID: NC.video.PVIDEO_HW_CHILD_CALLBACK
title: PVIDEO_HW_CHILD_CALLBACK
author: windows-driver-content
description: 
ms.assetid: b7826020-30d9-4f9f-9574-fc10cb2d7907
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: video.h
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

# PVIDEO_HW_CHILD_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PVIDEO_HW_CHILD_CALLBACK PvideoHwChildCallback; 

// Definition

VP_STATUS PvideoHwChildCallback 
(
	PVOID HwDeviceExtension
	PVOID ChildDeviceExtension
)
{...}

PVIDEO_HW_CHILD_CALLBACK 


```

## -parameters

### -param HwDeviceExtension: 
### -param ChildDeviceExtension: 



## -returns

Returns VP_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also