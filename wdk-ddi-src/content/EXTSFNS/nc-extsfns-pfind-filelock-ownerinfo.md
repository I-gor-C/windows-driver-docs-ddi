---
UID: NC.extsfns.PFIND_FILELOCK_OWNERINFO
title: PFIND_FILELOCK_OWNERINFO
author: windows-driver-content
description: 
ms.assetid: 1711894e-8d7e-4873-a680-9f55ac82ed76
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: extsfns.h
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

# PFIND_FILELOCK_OWNERINFO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFIND_FILELOCK_OWNERINFO PfindFilelockOwnerinfo; 

// Definition

HRESULT PfindFilelockOwnerinfo 
(
	PDEBUG_CLIENT Client
	PKDEXT_FILELOCK_OWNER pFileLockOwner
)
{...}

PFIND_FILELOCK_OWNERINFO 


```

## -parameters

### -param Client: 
### -param pFileLockOwner: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also