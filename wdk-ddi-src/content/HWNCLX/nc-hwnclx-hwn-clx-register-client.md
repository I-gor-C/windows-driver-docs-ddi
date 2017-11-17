---
UID: NC.hwnclx.HWN_CLX_REGISTER_CLIENT
title: HWN_CLX_REGISTER_CLIENT
author: windows-driver-content
description: 
ms.assetid: 135ce8d5-4c1e-45c1-add2-bc4841277918
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: hwnclx.h
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

# HWN_CLX_REGISTER_CLIENT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

HWN_CLX_REGISTER_CLIENT HwnClxRegisterClient; 

// Definition

NTSTATUS HwnClxRegisterClient 
(
	WDFDRIVER Driver
	PHWN_CLIENT_REGISTRATION_PACKET RegistrationPacket
	PUNICODE_STRING RegistryPath
)
{...}

HWN_CLX_REGISTER_CLIENT PHWN_CLX_REGISTER_CLIENT


```

## -parameters

### -param Driver: 
### -param RegistrationPacket: 
### -param RegistryPath: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also