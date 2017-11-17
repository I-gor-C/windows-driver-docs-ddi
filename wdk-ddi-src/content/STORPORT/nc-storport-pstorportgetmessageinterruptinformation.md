---
UID: NC.storport.PStorPortGetMessageInterruptInformation
title: PStorPortGetMessageInterruptInformation
author: windows-driver-content
description: 
ms.assetid: 61e80780-cda0-4dd5-9eaf-ca69540da59f
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: storport.h
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

# PStorPortGetMessageInterruptInformation callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PStorPortGetMessageInterruptInformation Pstorportgetmessageinterruptinformation; 

// Definition

BOOLEAN Pstorportgetmessageinterruptinformation 
(
	PVOID HwDeviceExtension
	ULONG MessageId
	PMESSAGE_INTERRUPT_INFORMATION InterruptInfo
)
{...}

PStorPortGetMessageInterruptInformation 


```

## -parameters

### -param HwDeviceExtension: 
### -param MessageId: 
### -param InterruptInfo: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also