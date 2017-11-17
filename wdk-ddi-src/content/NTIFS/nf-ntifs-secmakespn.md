---
UID: NF.ntifs.SecMakeSPN
title: SecMakeSPN
author: windows-driver-content
description: SecMakeSPN creates a service provider name string that can be used when communicating with specific security service providers.
old-location: ifsk\secmakespn.htm
ms.assetid: e294832a-f0f2-49ab-b215-7c0e67e5ec13
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: Ntifs.h, FltKernel.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SecMakeSPN
req.alt-loc: Ksecdd.lib,Ksecdd.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ksecdd.lib
req.dll: 
req.irql: <= APC_LEVEL
ms.keywords: SecMakeSPN
req.iface: 
---

# SecMakeSPN function



## -description
<p><b>SecMakeSPN</b> creates a service provider name string that can be used when communicating with specific security service providers. </p>


## -syntax

````
NTSTATUS SecMakeSPN(
  _In_    PUNICODE_STRING ServiceClass,
  _In_    PUNICODE_STRING ServiceName,
  _In_    PUNICODE_STRING InstanceName,
  _In_    USHORT          InstancePort,
  _In_    PUNICODE_STRING Referrer,
  _Inout_ PUNICODE_STRING Spn,
  _Out_   PULONG          Length,
  _In_    BOOLEAN         Allocate
);
````


## -parameters
<dl>

### -param <i>ServiceClass</i> [in]

<dd>
<p>A pointer to a Unicode string specifying the service class for the security service provider. </p>
</dd>

### -param <i>ServiceName</i> [in]

<dd>
<p>A pointer to a Unicode string specifying the service name for the security service provider. </p>
</dd>

### -param <i>InstanceName</i> [in]

<dd>
<p>A pointer to an optional Unicode string specifying the instance name for connecting with the security service provider. </p>
</dd>

### -param <i>InstancePort</i> [in]

<dd>
<p>An optional variable specifying the instance port for connecting with the security service provider. </p>
</dd>

### -param <i>Referrer</i> [in]

<dd>
<p>A pointer to an optional Unicode string specifying the referrer name for connecting with the security service provider. </p>
</dd>

### -param <i>Spn</i> [in, out]

<dd>
<p>A pointer to a Unicode string for storing the security service provider name string created by this function.</p>
</dd>

### -param <i>Length</i> [out]

<dd>
<p>A pointer to an optional variable for storing the length of the security service provider name string created by this function.</p>
</dd>

### -param <i>Allocate</i> [in]

<dd>
<p>A Boolean variable indicating if the memory for storing the <i>Spn</i> Unicode string should be allocated by this function. If this parameter is true, memory for <i>Spn</i> will be allocated from paged pool.</p>
</dd>
</dl>

## -returns
<p><b>SecMakeSPN</b> returns STATUS_SUCCESS on success or one of the following error codes on failure: </p><dl>
<dt><b>STATUS_BUFFER_OVERFLOW</b></dt>
</dl><p>The <i>Allocate</i> parameter was set to false and one of the following conditions occurred:</p>

<p>The <i>Spn </i>parameter was a null pointer.</p>

<p>The maximum length for the <i>Spn</i> Unicode string parameter was too small.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>A total length of the <i>Spn</i> parameter exceeds 65535 bytes.</p><dl>
<dt><b>STATUS_NO_MEMORY</b></dt>
</dl><p>The <i>Allocate</i> parameter was set to true, but the memory allocation request failed.</p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h or FltKernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ksecdd.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556585">SecMakeSPNEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556592">SecMakeSPNEx2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20SecMakeSPN function%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
