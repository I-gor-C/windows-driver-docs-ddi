---
UID: NF:ntifs.IoFastQueryNetworkAttributes
title: IoFastQueryNetworkAttributes function
author: windows-driver-content
description: Reserved for system use.
old-location: ifsk\iofastquerynetworkattributes.htm
old-project: ifsk
ms.assetid: 69a3e9c2-8bd5-4f42-9de9-58f1eea8b9a2
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: IoFastQueryNetworkAttributes, IoFastQueryNetworkAttributes function [Installable File System Drivers], ifsk.iofastquerynetworkattributes, ioref_c2d35e20-00b0-48e3-9c0e-d13f5dd9b7f7.xml, ntifs/IoFastQueryNetworkAttributes
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ntifs.h
api_name:
-	IoFastQueryNetworkAttributes
product:
- Windows
targetos: Windows
req.typenames: TOKEN_TYPE
---


# IoFastQueryNetworkAttributes function
This routine is reserved for system use.

## Syntax

```
NTKERNELAPI BOOLEAN IoFastQueryNetworkAttributes(
  POBJECT_ATTRIBUTES             ObjectAttributes,
  ACCESS_MASK                    DesiredAccess,
  ULONG                          OpenOptions,
  PIO_STATUS_BLOCK               IoStatus,
  PFILE_NETWORK_OPEN_INFORMATION Buffer
);
```

## Parameters

`ObjectAttributes`

TBD

`DesiredAccess`

TBD

`OpenOptions`

TBD

`IoStatus`

TBD

`Buffer`

TBD


## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | ntifs.h (include Ntifs.h) |