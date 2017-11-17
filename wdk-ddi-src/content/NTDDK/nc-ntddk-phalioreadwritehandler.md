---
UID: NC.ntddk.PHALIOREADWRITEHANDLER
title: PHALIOREADWRITEHANDLER
author: windows-driver-content
description: 
ms.assetid: af01bfda-2904-4af3-bdbf-541066f31b64
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

# PHALIOREADWRITEHANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PHALIOREADWRITEHANDLER Phalioreadwritehandler; 

// Definition

NTSTATUS Phalioreadwritehandler 
(
	BOOLEAN fRead
	ULONG dwAddr
	ULONG dwSize
	PULONG pdwData
)
{...}

PHALIOREADWRITEHANDLER 


```

## -parameters

### -param fRead: 
### -param dwAddr: 
### -param dwSize: 
### -param pdwData: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also