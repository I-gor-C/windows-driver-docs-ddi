---
UID: NC.kcom.KoCreateObjectHandler
title: KoCreateObjectHandler
author: windows-driver-content
description: 
ms.assetid: d80ee89a-a163-4f94-8d32-ce4fede4cdf9
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: kcom.h
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

# KoCreateObjectHandler callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

KoCreateObjectHandler Kocreateobjecthandler; 

// Definition

NTSTATUS Kocreateobjecthandler 
(
	REFCLSID ClassId
	IUnknown *UnkOuter
	REFIID InterfaceId
	PVOID *Interface
)
{...}

KoCreateObjectHandler 


```

## -parameters

### -param ClassId: 
### -param *UnkOuter: 
### -param InterfaceId: 
### -param *Interface: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also