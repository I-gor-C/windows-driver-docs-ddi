---
UID: NC.wsk.PFN_WSK_RELEASE_DATAGRAM_INDICATION_LIST
title: PFN_WSK_RELEASE_DATAGRAM_INDICATION_LIST
author: windows-driver-content
description: 
ms.assetid: 75a8522a-93bb-486d-9b69-44d95c2f5f94
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wsk.h
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

# PFN_WSK_RELEASE_DATAGRAM_INDICATION_LIST callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WSK_RELEASE_DATAGRAM_INDICATION_LIST PfnWskReleaseDatagramIndicationList; 

// Definition

NTSTATUS PfnWskReleaseDatagramIndicationList 
(
	PWSK_SOCKET Socket
	PWSK_DATAGRAM_INDICATION DatagramIndication
)
{...}

PFN_WSK_RELEASE_DATAGRAM_INDICATION_LIST 


```

## -parameters

### -param Socket: 
### -param DatagramIndication: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also