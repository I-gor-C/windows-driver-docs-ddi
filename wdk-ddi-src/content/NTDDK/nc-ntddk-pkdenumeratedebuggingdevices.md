---
UID: NC.ntddk.pKdEnumerateDebuggingDevices
title: pKdEnumerateDebuggingDevices
author: windows-driver-content
description: 
ms.assetid: 60119e81-d717-4c4a-bc08-119fa2c2465e
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntddk.h
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

# pKdEnumerateDebuggingDevices callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

pKdEnumerateDebuggingDevices Pkdenumeratedebuggingdevices; 

// Definition

NTSTATUS Pkdenumeratedebuggingdevices 
(
	PVOID LoaderBlock
	PDEBUG_DEVICE_DESCRIPTOR Device
	PDEBUG_DEVICE_FOUND_FUNCTION Callback
)
{...}

pKdEnumerateDebuggingDevices 


```

## -parameters

### -param LoaderBlock: 
### -param Device: 
### -param Callback: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also