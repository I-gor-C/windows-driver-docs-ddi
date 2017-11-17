---
UID: NC.ntddk.PDRIVER_EXCPTN_CALLBACK~r2
title: PDRIVER_EXCPTN_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 4a57e13f-0369-4520-bc49-e8a90a735b31
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

# PDRIVER_EXCPTN_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PDRIVER_EXCPTN_CALLBACK PdriverExcptnCallback; 

// Definition

VOID PdriverExcptnCallback 
(
	PVOID Context
	PMCA_EXCEPTION BankLog
)
{...}

PDRIVER_EXCPTN_CALLBACK 


```

## -parameters

### -param Context: 
### -param BankLog: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also