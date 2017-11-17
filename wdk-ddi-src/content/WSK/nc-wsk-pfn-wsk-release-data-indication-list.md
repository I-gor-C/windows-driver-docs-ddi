---
UID: NC.wsk.PFN_WSK_RELEASE_DATA_INDICATION_LIST
title: PFN_WSK_RELEASE_DATA_INDICATION_LIST
author: windows-driver-content
description: 
ms.assetid: 53002f20-5a06-4ec5-9d0a-41383e282d2a
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

# PFN_WSK_RELEASE_DATA_INDICATION_LIST callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WSK_RELEASE_DATA_INDICATION_LIST PfnWskReleaseDataIndicationList; 

// Definition

NTSTATUS PfnWskReleaseDataIndicationList 
(
	PWSK_SOCKET Socket
	PWSK_DATA_INDICATION DataIndication
)
{...}

PFN_WSK_RELEASE_DATA_INDICATION_LIST 


```

## -parameters

### -param Socket: 
### -param DataIndication: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also