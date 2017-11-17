---
UID: NC.extsfns.PKDEXTS_GET_PTE_INFO
title: PKDEXTS_GET_PTE_INFO
author: windows-driver-content
description: 
ms.assetid: 2f30e562-7878-4924-88ec-49f556b183c6
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: extsfns.h
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

# PKDEXTS_GET_PTE_INFO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PKDEXTS_GET_PTE_INFO PkdextsGetPteInfo; 

// Definition

HRESULT PkdextsGetPteInfo 
(
	PDEBUG_CLIENT Client
	ULONG64 Virtual
	PKDEXTS_PTE_INFO PteInfo
)
{...}

PKDEXTS_GET_PTE_INFO 


```

## -parameters

### -param Client: 
### -param Virtual: 
### -param PteInfo: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also