---
UID : NF:ntifs.RtlUnicodeToCustomCPN
title : RtlUnicodeToCustomCPN function
author : windows-driver-content
description : Reserved for system use.
old-location : ifsk\rtlunicodetocustomcpn.htm
old-project : ifsk
ms.assetid : db4335c1-b6c9-4afd-b30f-95b736be696b
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : RtlUnicodeToCustomCPN
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ntifs.h
req.include-header : Ntifs.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : RtlUnicodeToCustomCPN
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


# RtlUnicodeToCustomCPN function
The <b>RtlUnicodeToCustomCPN</b> routine is reserved for system use. See <a href="..\ntifs\nf-ntifs-rtlunicodetomultibyten.md">RtlUnicodeToMultiByteN</a> and <a href="..\ntifs\nf-ntifs-rtlunicodetooemn.md">RtlUnicodeToOemN</a>.

## Syntax

````
  RtlUnicodeToCustomCPN(
    
);
````

## Parameters

`CustomCP`



`CustomCPString`



`MaxBytesInCustomCPString`



`BytesInCustomCPString`



`UnicodeString`



`BytesInUnicodeString`




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