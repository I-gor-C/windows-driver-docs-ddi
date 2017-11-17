---
UID: NC.wskndk.PFN_WSK_NDK_OPEN_ADAPTER
title: PFN_WSK_NDK_OPEN_ADAPTER
author: windows-driver-content
description: 
ms.assetid: 7480d6a4-6378-4778-a0c5-52a6e731ebcb
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wskndk.h
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

# PFN_WSK_NDK_OPEN_ADAPTER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WSK_NDK_OPEN_ADAPTER PfnWskNdkOpenAdapter; 

// Definition

NTSTATUS PfnWskNdkOpenAdapter 
(
	PWSK_CLIENT Client
	NDK_VERSION NdkVersion
	NET_IFINDEX IfIndex
	NDK_ADAPTER **ppNdkAdapter
)
{...}

PFN_WSK_NDK_OPEN_ADAPTER 


```

## -parameters

### -param Client: 
### -param NdkVersion: 
### -param IfIndex: 
### -param **ppNdkAdapter: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also