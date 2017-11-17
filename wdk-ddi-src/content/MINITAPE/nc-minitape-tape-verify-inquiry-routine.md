---
UID: NC.minitape.TAPE_VERIFY_INQUIRY_ROUTINE
title: TAPE_VERIFY_INQUIRY_ROUTINE
author: windows-driver-content
description: 
ms.assetid: b980f9d7-7943-4002-9775-135d0a8a8b47
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

# TAPE_VERIFY_INQUIRY_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

TAPE_VERIFY_INQUIRY_ROUTINE TapeVerifyInquiryRoutine; 

// Definition

BOOLEAN TapeVerifyInquiryRoutine 
(
	PINQUIRYDATA InquiryData
	PMODE_CAPABILITIES_PAGE ModeCapabilitiesPage
)
{...}

TAPE_VERIFY_INQUIRY_ROUTINE 


```

## -parameters

### -param InquiryData: 
### -param ModeCapabilitiesPage: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also