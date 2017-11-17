---
UID: NC.usbiodef.USB_IDLE_CALLBACK
title: USB_IDLE_CALLBACK
author: windows-driver-content
description: 
ms.assetid: d1f2b461-a118-4ff0-aae1-144553c76b30
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: usbiodef.h
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

# USB_IDLE_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

USB_IDLE_CALLBACK UsbIdleCallback; 

// Definition

VOID UsbIdleCallback 
(
	PVOID Context
)
{...}

USB_IDLE_CALLBACK 


```

## -parameters

### -param Context: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also