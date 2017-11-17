---
UID: NC.hidport.HID_SEND_IDLE_CALLBACK
title: HID_SEND_IDLE_CALLBACK
author: windows-driver-content
description: 
ms.assetid: e4bc3de3-e5f1-494c-94f1-b503c9d8d8a2
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: hidport.h
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

# HID_SEND_IDLE_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

HID_SEND_IDLE_CALLBACK HidSendIdleCallback; 

// Definition

VOID HidSendIdleCallback 
(
	PVOID Context
)
{...}

HID_SEND_IDLE_CALLBACK 


```

## -parameters

### -param Context: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also