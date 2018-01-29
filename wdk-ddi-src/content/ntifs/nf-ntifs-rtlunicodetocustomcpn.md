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
ms.keywords : RtlUnicodeToCustomCPN, ifsk.rtlunicodetocustomcpn, rtlref_0c9942bd-a950-4d59-8fc7-58c41cfe78d4.xml, RtlUnicodeToCustomCPN function [Installable File System Drivers], ntifs/RtlUnicodeToCustomCPN
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
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : NtosKrnl.exe
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
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

TBD

`CustomCPString`

TBD

`MaxBytesInCustomCPString`

TBD

`BytesInCustomCPString`

TBD

`UnicodeString`

TBD

`BytesInUnicodeString`

TBD


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