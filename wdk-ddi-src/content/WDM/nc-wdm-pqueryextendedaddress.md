---
UID: NC.wdm.PQUERYEXTENDEDADDRESS
title: PQUERYEXTENDEDADDRESS
author: windows-driver-content
description: 
ms.assetid: b7b0be60-fb26-4ca9-b937-b81cef6ec1eb
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdm.h
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

# PQUERYEXTENDEDADDRESS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PQUERYEXTENDEDADDRESS Pqueryextendedaddress; 

// Definition

VOID Pqueryextendedaddress 
(
	PVOID Context
	PULONG64 ExtendedAddress
)
{...}

PQUERYEXTENDEDADDRESS 


```

## -parameters

### -param Context: 
### -param ExtendedAddress: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also