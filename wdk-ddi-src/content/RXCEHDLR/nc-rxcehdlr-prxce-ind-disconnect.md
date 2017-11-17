---
UID: NC.rxcehdlr.PRXCE_IND_DISCONNECT
title: PRXCE_IND_DISCONNECT
author: windows-driver-content
description: 
ms.assetid: 6c45062c-67ac-42b9-a79b-9846b73447b4
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: rxcehdlr.h
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

# PRXCE_IND_DISCONNECT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PRXCE_IND_DISCONNECT PrxceIndDisconnect; 

// Definition

NTSTATUS PrxceIndDisconnect 
(
	IN PVOID pRxCeEventContext
	IN PRXCE_VC pVc
	IN int DisconnectDataLength
	IN PVOID DisconnectData
	IN int DisconnectInformationLength
	IN PVOID DisconnectInformation
	IN ULONG DisconnectFlags
)
{...}

PRXCE_IND_DISCONNECT 


```

## -parameters

### -param pRxCeEventContext: 
### -param pVc: 
### -param DisconnectDataLength: 
### -param DisconnectData: 
### -param DisconnectInformationLength: 
### -param DisconnectInformation: 
### -param DisconnectFlags: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also