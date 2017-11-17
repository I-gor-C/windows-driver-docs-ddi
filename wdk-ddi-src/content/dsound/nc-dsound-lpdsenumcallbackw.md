---
UID: NC.dsound.LPDSENUMCALLBACKW
title: LPDSENUMCALLBACKW
author: windows-driver-content
description: 
ms.assetid: 94cb1976-05df-46f8-b5dc-b53bad42bc78
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dsound.h
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

# LPDSENUMCALLBACKW callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

LPDSENUMCALLBACKW Lpdsenumcallbackw; 

// Definition

BOOL Lpdsenumcallbackw 
(
	 LPGUID
	 LPCWSTR
	 LPCWSTR
	 LPVOID
)
{...}

LPDSENUMCALLBACKW 


```

## -parameters

### -param LPGUID: 
### -param LPCWSTR: 
### -param LPCWSTR: 
### -param LPVOID: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also