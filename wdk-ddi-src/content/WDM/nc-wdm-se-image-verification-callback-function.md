---
UID: NC.wdm.SE_IMAGE_VERIFICATION_CALLBACK_FUNCTION
title: SE_IMAGE_VERIFICATION_CALLBACK_FUNCTION
author: windows-driver-content
description: 
ms.assetid: 74702ae5-15cf-464f-b2d7-9a1a3ad1d5f7
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

# SE_IMAGE_VERIFICATION_CALLBACK_FUNCTION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

SE_IMAGE_VERIFICATION_CALLBACK_FUNCTION SeImageVerificationCallbackFunction; 

// Definition

VOID SeImageVerificationCallbackFunction 
(
	PVOID CallbackContext
	SE_IMAGE_TYPE ImageType
	PBDCB_IMAGE_INFORMATION ImageInformation
)
{...}

SE_IMAGE_VERIFICATION_CALLBACK_FUNCTION PSE_IMAGE_VERIFICATION_CALLBACK_FUNCTION


```

## -parameters

### -param CallbackContext: 
### -param ImageType: 
### -param ImageInformation: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also