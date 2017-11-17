---
UID: NC.netrequest.PFN_NETREQUESTRETRIEVEINPUTOUTPUTBUFFER
title: PFN_NETREQUESTRETRIEVEINPUTOUTPUTBUFFER
author: windows-driver-content
description: 
ms.assetid: 19546548-d272-45a8-8b95-354020e3ae68
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: netrequest.h
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

# PFN_NETREQUESTRETRIEVEINPUTOUTPUTBUFFER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETREQUESTRETRIEVEINPUTOUTPUTBUFFER PfnNetrequestretrieveinputoutputbuffer; 

// Definition

WDFAPI PfnNetrequestretrieveinputoutputbuffer 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETREQUEST Request
	UINT MininumInputLengthRequired
	UINT MininumOutputLengthRequired
	PVOID *InputOutputBuffer
	PUINT InputBufferLength
	PUINT OutputBufferLength
)
{...}

PFN_NETREQUESTRETRIEVEINPUTOUTPUTBUFFER 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 
### -param MininumInputLengthRequired: 
### -param MininumOutputLengthRequired: 
### -param *InputOutputBuffer: 
### -param InputBufferLength: 
### -param OutputBufferLength: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also