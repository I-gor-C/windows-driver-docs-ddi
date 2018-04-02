---
UID: NF:ntifs.SecMakeSPNEx
title: SecMakeSPNEx function
author: windows-driver-content
description: SecMakeSPNEx creates a service provider name string that can be used when communicating with specific security service providers.
old-location: ifsk\secmakespnex.htm
old-project: ifsk
ms.assetid: 5000be89-144c-405c-93ea-3e9372e0a677
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: SecMakeSPNEx, SecMakeSPNEx function [Installable File System Drivers], ifsk.secmakespnex, ksecddref_3c4441b9-ed78-473f-ac3c-35a644018499.xml, ntifs/SecMakeSPNEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h, FltKernel.h
req.target-type: Universal
req.target-min-winverclnt: This function is only available on Microsoft Windows XP and later.
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
req.lib: Ksecdd.lib
req.dll: 
req.irql: "<= APC_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	LibDef
api_location:
-	Ksecdd.lib
-	Ksecdd.dll
api_name:
-	SecMakeSPNEx
product:
- Windows
targetos: Windows
req.typenames: TOKEN_TYPE
---


# SecMakeSPNEx function
<b>SecMakeSPNEx</b> creates a service provider name string that can be used when communicating with specific security service providers.

## Syntax

```
KSECDDDECLSPEC NTSTATUS SecMakeSPNEx(
  IN PUNICODE_STRING              ServiceClass,
  IN PUNICODE_STRING              ServiceName,
  IN PUNICODE_STRING InstanceName OPTIONAL,
  IN USHORT InstancePort          OPTIONAL,
  IN PUNICODE_STRING Referrer     OPTIONAL,
  IN PUNICODE_STRING TargetInfo   OPTIONAL,
  IN OUT PUNICODE_STRING          Spn,
  OUT PULONG Length               OPTIONAL,
  IN BOOLEAN                      Allocate
);
```

## Parameters

`ServiceClass`

A pointer to a Unicode string specifying the service class for the security service provider.

`ServiceName`

A pointer to a Unicode string specifying the service name for the security service provider.

`OPTIONAL`

TBD

`OPTIONAL`

TBD

`OPTIONAL`

TBD

`OPTIONAL`

TBD

`Spn`

A pointer to a Unicode string for storing the security service provider name string created by this function.

`OPTIONAL`

TBD

`Allocate`

A Boolean variable indicating if the memory for storing the <i>Spn</i> Unicode string should be allocated by this function. If this parameter is true, memory for <i>Spn</i> will be allocated from paged pool.


## Return Value

<b>SecMakeSPNEx</b> returns STATUS_SUCCESS on success or one of the following error codes on failure: 

<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_BUFFER_OVERFLOW</b></dt>
</dl>
</td>
<td width="60%">
The <i>Allocate</i> parameter was set to false and one of the following conditions occurred:

The <i>Spn </i>parameter was a null pointer.

The maximum length for the <i>Spn</i> Unicode string parameter was too small.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>
</td>
<td width="60%">
A total length of the <i>Spn</i> parameter exceeds 65535 bytes.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_NO_MEMORY</b></dt>
</dl>
</td>
<td width="60%">
The <i>Allocate</i> parameter was set to true, but the memory allocation request failed.

</td>
</tr>
</table>

## Remarks

<b>SecMakeSPNEx</b> is an enhanced version of <b>SecMakeSPN</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | This function is only available on Microsoft Windows XP and later.  |
| **Target Platform** | Universal |
| **Header** | ntifs.h (include Ntifs.h, FltKernel.h) |
| **Library** | Ksecdd.lib |
| **IRQL** | "<= APC_LEVEL" |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff556584">SecMakeSPN</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff556592">SecMakeSPNEx2</a>