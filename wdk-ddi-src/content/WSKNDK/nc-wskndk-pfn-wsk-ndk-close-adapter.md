---
UID: NC.wskndk.PFN_WSK_NDK_CLOSE_ADAPTER
title: PFN_WSK_NDK_CLOSE_ADAPTER
author: windows-driver-content
description: 
ms.assetid: 07967348-0a83-4848-9220-d23a29aba2b0
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wskndk.h
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

# PFN_WSK_NDK_CLOSE_ADAPTER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WSK_NDK_CLOSE_ADAPTER PfnWskNdkCloseAdapter; 

// Definition

VOID PfnWskNdkCloseAdapter 
(
	PWSK_CLIENT Client
	NDK_ADAPTER *pNdkAdapter
)
{...}

PFN_WSK_NDK_CLOSE_ADAPTER 


```

## -parameters

### -param Client: 
### -param *pNdkAdapter: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also