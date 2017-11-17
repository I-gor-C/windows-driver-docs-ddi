---
UID: NC.classpnp.PCLASS_INTERPRET_SENSE_INFO
title: PCLASS_INTERPRET_SENSE_INFO
author: windows-driver-content
description: 
ms.assetid: 335399ec-430a-41ae-9f65-3f50152c15b9
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: classpnp.h
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

# PCLASS_INTERPRET_SENSE_INFO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCLASS_INTERPRET_SENSE_INFO PclassInterpretSenseInfo; 

// Definition

BOOLEAN PclassInterpretSenseInfo 
(
	PDEVICE_OBJECT Fdo
	PIRP OriginalRequest
	PSCSI_REQUEST_BLOCK Srb
	UCHAR MajorFunctionCode
	ULONG IoDeviceCode
	ULONG PreviousRetryCount
	SRB_HISTORY *RequestHistory
	NTSTATUS *Status
	LONGLONG *RetryIn100nsUnits
)
{...}

PCLASS_INTERPRET_SENSE_INFO 


```

## -parameters

### -param Fdo: 
### -param OriginalRequest: 
### -param Srb: 
### -param MajorFunctionCode: 
### -param IoDeviceCode: 
### -param PreviousRetryCount: 
### -param *RequestHistory: 
### -param *Status: 
### -param *RetryIn100nsUnits: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also