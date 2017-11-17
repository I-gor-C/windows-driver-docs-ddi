---
UID: NC.ntifs.QUERY_SECURITY_PACKAGE_INFO_FN_W
title: QUERY_SECURITY_PACKAGE_INFO_FN_W
author: windows-driver-content
description: 
ms.assetid: 23061bf2-e3db-4642-bcd8-d5351bd5bbd9
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntifs.h
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

# QUERY_SECURITY_PACKAGE_INFO_FN_W callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

QUERY_SECURITY_PACKAGE_INFO_FN_W QuerySecurityPackageInfoFnW; 

// Definition

SECURITY_STATUS QuerySecurityPackageInfoFnW 
(
	PSECURITY_STRING 
	SEC_WCHAR *
	PSecPkgInfoW *
)
{...}

QUERY_SECURITY_PACKAGE_INFO_FN_W 


```

## -parameters

### -param : 
### -param *: 
### -param *: 



## -returns

Returns SECURITY_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also