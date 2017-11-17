---
UID: NC.video.PVIDEO_WAIT_VSYNC_ACTIVE
title: PVIDEO_WAIT_VSYNC_ACTIVE
author: windows-driver-content
description: 
ms.assetid: 0c03ed45-783c-454f-9ab9-afdea53a8313
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

# PVIDEO_WAIT_VSYNC_ACTIVE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PVIDEO_WAIT_VSYNC_ACTIVE PvideoWaitVsyncActive; 

// Definition

VOID PvideoWaitVsyncActive 
(
	PVOID HwDeviceExtension
)
{...}

PVIDEO_WAIT_VSYNC_ACTIVE 


```

## -parameters

### -param HwDeviceExtension: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also