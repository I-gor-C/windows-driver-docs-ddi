---
UID: NC.miniport.PBANKED_SECTION_ROUTINE
title: PBANKED_SECTION_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 4393252f-b610-48f4-a303-e5aa8d9edafa
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: miniport.h
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

# PBANKED_SECTION_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PBANKED_SECTION_ROUTINE PbankedSectionRoutine; 

// Definition

VOID PbankedSectionRoutine 
(
	ULONG ReadBank
	ULONG WriteBank
	PVOID Context
)
{...}

PBANKED_SECTION_ROUTINE 


```

## -parameters

### -param ReadBank: 
### -param WriteBank: 
### -param Context: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also