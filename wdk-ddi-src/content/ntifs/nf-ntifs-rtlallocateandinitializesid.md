---
UID : NF:ntifs.RtlAllocateAndInitializeSid
title : RtlAllocateAndInitializeSid function
author : windows-driver-content
description : Reserved for system use.
old-location : ifsk\rtlallocateandinitializesid.htm
old-project : ifsk
ms.assetid : c58f4448-06f5-4eda-a254-e453defd1d6c
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : RtlAllocateAndInitializeSid
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
req.alt-api : RtlAllocateAndInitializeSid
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


# RtlAllocateAndInitializeSid function
The <b>RtlAllocateAndInitializeSid</b> routine is reserved for system use. See <a href="..\ntifs\nf-ntifs-rtlcopysid.md">RtlCopySid</a> and <a href="..\ntifs\nf-ntifs-rtlinitializesid.md">RtlInitializeSid</a>.

## Syntax

````
  RtlAllocateAndInitializeSid(
    
);
````

## Parameters

`IdentifierAuthority`



`SubAuthorityCount`



`SubAuthority0`



`SubAuthority1`



`SubAuthority2`



`SubAuthority3`



`SubAuthority4`



`SubAuthority5`



`SubAuthority6`



`SubAuthority7`



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