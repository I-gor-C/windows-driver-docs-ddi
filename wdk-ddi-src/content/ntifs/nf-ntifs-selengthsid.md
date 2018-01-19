---
UID : NF:ntifs.SeLengthSid
title : SeLengthSid macro
author : windows-driver-content
description : Obsolete.
old-location : ifsk\selengthsid.htm
old-project : ifsk
ms.assetid : f6539ab6-709e-43e4-9e3f-595cf59c85c5
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : SeLengthSid
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : macro
req.header : ntifs.h
req.include-header : Ntifs.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : SeLengthSid
req.alt-loc : ntifs.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : TOKEN_TYPE
---


# SeLengthSid function
This macro is exported to support existing driver binaries and is obsolete. Use <a href="..\ntifs\nf-ntifs-rtllengthsid.md">RtlLengthSid</a> instead.

## Syntax

````
  SeLengthSid(
    
);
````

## Parameters

`Sid`




## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntifs.h (include Ntifs.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |