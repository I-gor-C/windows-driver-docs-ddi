---
UID: NC.ks.PFNKSPINSETDATAFORMAT
title: PFNKSPINSETDATAFORMAT
author: windows-driver-content
description: 
ms.assetid: 73d094b3-3a39-4b82-bb6b-dd7010785cb5
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ks.h
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

# PFNKSPINSETDATAFORMAT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSPINSETDATAFORMAT Pfnkspinsetdataformat; 

// Definition

NTSTATUS Pfnkspinsetdataformat 
(
	PKSPIN Pin
	PKSDATAFORMAT OldFormat
	PKSMULTIPLE_ITEM OldAttributeList
	 const KSDATARANGE *DataRange
	 const KSATTRIBUTE_LIST *AttributeRange
)
{...}

PFNKSPINSETDATAFORMAT 


```

## -parameters

### -param Pin: 
### -param OldFormat: 
### -param OldAttributeList: 
### -param *DataRange: 
### -param *AttributeRange: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also