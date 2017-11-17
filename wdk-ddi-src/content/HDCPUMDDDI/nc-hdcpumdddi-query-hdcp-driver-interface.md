---
UID: NC.hdcpumdddi.QUERY_HDCP_DRIVER_INTERFACE
title: QUERY_HDCP_DRIVER_INTERFACE
author: windows-driver-content
description: 
ms.assetid: a2b940ab-1bc3-4de2-bfca-06258ca06b9f
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

# QUERY_HDCP_DRIVER_INTERFACE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

QUERY_HDCP_DRIVER_INTERFACE QueryHdcpDriverInterface; 

// Definition

HRESULT QueryHdcpDriverInterface 
(
	UINT HDCPDriverInterfaceVersion
	UINT cbHDCPDriverInterface
	VOID *pHDCPDriverInterface
)
{...}

QUERY_HDCP_DRIVER_INTERFACE 


```

## -parameters

### -param HDCPDriverInterfaceVersion: 
### -param cbHDCPDriverInterface: 
### -param *pHDCPDriverInterface: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also