---
UID: NC.hdcpumdddi.PFN_REPORT_ENCRYPTION_STATUS
title: PFN_REPORT_ENCRYPTION_STATUS
author: windows-driver-content
description: 
ms.assetid: 3850cbef-fd41-4b32-b858-e4bbce4f376e
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

# PFN_REPORT_ENCRYPTION_STATUS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_REPORT_ENCRYPTION_STATUS PfnReportEncryptionStatus; 

// Definition

VOID PfnReportEncryptionStatus 
(
	PVOID pOSContext
	HDCP_ENCRYPTION_STATUS EncryptionStatus
)
{...}

PFN_REPORT_ENCRYPTION_STATUS 


```

## -parameters

### -param pOSContext: 
### -param EncryptionStatus: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also