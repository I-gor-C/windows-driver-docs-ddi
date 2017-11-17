---
UID: NC.wsk.PFN_WSK_FREE_ADDRESS_INFO
title: PFN_WSK_FREE_ADDRESS_INFO
author: windows-driver-content
description: 
ms.assetid: b5fc3fc5-faad-42b0-a496-6afba448038e
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wsk.h
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

# PFN_WSK_FREE_ADDRESS_INFO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WSK_FREE_ADDRESS_INFO PfnWskFreeAddressInfo; 

// Definition

VOID PfnWskFreeAddressInfo 
(
	PWSK_CLIENT Client
	PADDRINFOEXW AddrInfo
)
{...}

PFN_WSK_FREE_ADDRESS_INFO 


```

## -parameters

### -param Client: 
### -param AddrInfo: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also