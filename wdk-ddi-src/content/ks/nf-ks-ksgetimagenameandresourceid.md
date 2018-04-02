---
UID: NF:ks.KsGetImageNameAndResourceId
title: KsGetImageNameAndResourceId function
author: windows-driver-content
description: The KsGetImageNameAndResourceId function returns the image name and resource identifier that corresponds to the RegKey handle.
old-location: stream\ksgetimagenameandresourceid.htm
old-project: stream
ms.assetid: e73c885c-94e2-42cf-ace6-1b7b62aa33f5
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: KsGetImageNameAndResourceId, KsGetImageNameAndResourceId function [Streaming Media Devices], ks/KsGetImageNameAndResourceId, ksfunc_b4a55bde-4bbb-494e-969c-924547251e1d.xml, stream.ksgetimagenameandresourceid
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
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
req.lib: Ks.lib
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	LibDef
api_location:
-	Ks.lib
-	Ks.dll
api_name:
-	KsGetImageNameAndResourceId
product:
- Windows
targetos: Windows
req.typenames: 
---


# KsGetImageNameAndResourceId function
The <b>KsGetImageNameAndResourceId</b> function returns the image name and resource identifier that corresponds to the <i>RegKey </i>handle.

## Syntax

```
KSDDKAPI NTSTATUS KsGetImageNameAndResourceId(
  HANDLE          RegKey,
  PUNICODE_STRING ImageName,
  PULONG_PTR      ResourceId,
  PULONG          ValueType
);
```

## Parameters

`RegKey`

Specifies a handle for which to return the image name and resource identifier.

`ImageName`

A caller-allocated buffer that receives the image name for the specified resource.

`ResourceId`

Pointer to a caller-supplied variable that receives the resource identifier.

`ValueType`

Pointer to a location into which the function returns the value type of the specified resource.


## Return Value

<b>KsGetImageNameAndResourceId</b> returns STATUS_SUCCESS if the requested values are found; otherwise, an error code is returned.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | ks.h (include Ks.h) |
| **Library** | Ks.lib |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff563391">KsMapModuleName</a>