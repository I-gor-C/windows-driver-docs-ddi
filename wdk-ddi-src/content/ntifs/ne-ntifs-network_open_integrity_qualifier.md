---
UID : NE:ntifs.NETWORK_OPEN_INTEGRITY_QUALIFIER
title : NETWORK_OPEN_INTEGRITY_QUALIFIER
author : windows-driver-content
description : The NETWORK_OPEN_INTEGRITY_QUALIFIER enumeration type contains values that identify the kind of integrity restriction to attach to a file.
old-location : ifsk\network_open_integrity_qualifier.htm
old-project : ifsk
ms.assetid : 6a51ee2e-2df6-44f4-8e95-776851d743a6
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : NETWORK_OPEN_INTEGRITY_QUALIFIER, NETWORK_OPEN_INTEGRITY_QUALIFIER
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ntifs.h
req.include-header : Ntifs.h
req.target-type : Windows
req.target-min-winverclnt : This enumeration type is available starting with Windows Vista.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : NETWORK_OPEN_INTEGRITY_QUALIFIER
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
req.irql : PASSIVE_LEVEL
req.typenames : NETWORK_OPEN_INTEGRITY_QUALIFIER
---

# NETWORK_OPEN_INTEGRITY_QUALIFIER Enumeration
The NETWORK_OPEN_INTEGRITY_QUALIFIER enumeration type contains values that identify the kind of integrity restriction to attach to a file.

## Syntax
````
typedef enum  { 
  NetworkOpenIntegrityAny        = 0,
  NetworkOpenIntegrityNone       = 1,
  NetworkOpenIntegritySigned     = 2,
  NetworkOpenIntegrityEncrypted  = 3,
  NetworkOpenIntegrityMaximum    = 4
} NETWORK_OPEN_INTEGRITY_QUALIFIER;
````

## Constants

<table>

<tr>
<td>NetworkOpenIntegrityAny</td>
<td>Indicates that the file has no integrity restrictions. That is, the file has no restrictions about how to sign, encrypt, and so on.</td>
</tr>

<tr>
<td>NetworkOpenIntegrityEncrypted</td>
<td>Indicates that the file is encrypted end-to-end.</td>
</tr>

<tr>
<td>NetworkOpenIntegrityMaximum</td>
<td>Indicates that the file has the best integrity that is available.</td>
</tr>

<tr>
<td>NetworkOpenIntegrityNone</td>
<td>Indicates that the file is not signed or encrypted.</td>
</tr>

<tr>
<td>NetworkOpenIntegritySigned</td>
<td>Indicates that the file is signed end-to-end.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntifs.h (include Ntifs.h) |