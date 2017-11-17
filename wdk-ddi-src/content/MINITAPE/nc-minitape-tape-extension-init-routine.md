---
UID: NC.minitape.TAPE_EXTENSION_INIT_ROUTINE
title: TAPE_EXTENSION_INIT_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 628e857c-20ed-4675-b5ca-47fec39c0d26
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: minitape.h
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

# TAPE_EXTENSION_INIT_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

TAPE_EXTENSION_INIT_ROUTINE TapeExtensionInitRoutine; 

// Definition

VOID TapeExtensionInitRoutine 
(
	PVOID MinitapeExtension
	PINQUIRYDATA InquiryData
	PMODE_CAPABILITIES_PAGE ModeCapabilitiesPage
)
{...}

TAPE_EXTENSION_INIT_ROUTINE 


```

## -parameters

### -param MinitapeExtension: 
### -param InquiryData: 
### -param ModeCapabilitiesPage: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also