---
UID: NC.hdcpumdddi.PFN_REPORT_AUTHENTICATION_RESULT
title: PFN_REPORT_AUTHENTICATION_RESULT
author: windows-driver-content
description: 
ms.assetid: e9a0d041-d37d-4233-a6b6-bbbd68bd7015
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: hdcpumdddi.h
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

# PFN_REPORT_AUTHENTICATION_RESULT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_REPORT_AUTHENTICATION_RESULT PfnReportAuthenticationResult; 

// Definition

VOID PfnReportAuthenticationResult 
(
	PVOID pOSContext
	HDCP_AUTHENTICATION_STATUS HdcpAuthenticationStatus
	ULONG64 DriverDefinedStatus
	BOOL fShouldRetry
)
{...}

PFN_REPORT_AUTHENTICATION_RESULT 


```

## -parameters

### -param pOSContext: 
### -param HdcpAuthenticationStatus: 
### -param DriverDefinedStatus: 
### -param fShouldRetry: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also