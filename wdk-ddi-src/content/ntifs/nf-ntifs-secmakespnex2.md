---
UID: NF.ntifs.SecMakeSPNEx2
title: SecMakeSPNEx2
author: windows-driver-content
description: SecMakeSPNEx2 creates a service provider name string that can be used when it communicates with specific security service providers.
old-location: ifsk\secmakespnex2.htm
old-project: ifsk
ms.assetid: abb8d45a-a698-41b0-94b3-c658fe3105bb
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SecMakeSPNEx2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h, FltKernel.h
req.target-type: Universal
req.target-min-winverclnt: This function is available on Windows Vista, Windows Server 2008, and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SecMakeSPNEx2
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
req.iface: 
---

# SecMakeSPNEx2 function



## -description
<p><b>SecMakeSPNEx2</b> creates a service provider name string that can be used when it communicates with specific security service providers.</p>


## -syntax

````
NTSTATUS SecMakeSPNEx2(
  _In_    PUNICODE_STRING ServiceClass,
  _In_    PUNICODE_STRING ServiceName,
  _In_    PUNICODE_STRING InstanceName,
  _In_    USHORT          InstancePort,
  _In_    PUNICODE_STRING Referrer,
  _In_    PUNICODE_STRING TargetInfo,
  _Inout_ PUNICODE_STRING Spn,
  _Out_   PULONG          TotalSize,
  _In_    BOOLEAN         Allocate,
  _In_    BOOLEAN         IsTargetInfoMarshaled
);
````


## -parameters
<dl>

### -param <i>ServiceClass</i> [in]

<dd>
<p>A pointer to a Unicode string that specifies the service class for the security service provider. </p>
</dd>

### -param <i>ServiceName</i> [in]

<dd>
<p>A pointer to a Unicode string that specifies the service name for the security service provider. </p>
</dd>

### -param <i>InstanceName</i> [in]

<dd>
<p>A pointer to an optional Unicode string that specifies the instance name that is used to connect with the security service provider. </p>
</dd>

### -param <i>InstancePort</i> [in]

<dd>
<p>An optional variable that specifies the instance port that is used to connect with the security service provider. </p>
</dd>

### -param <i>Referrer</i> [in]

<dd>
<p>A pointer to an optional Unicode string that specifies the referrer name that is used to connect with the security service provider. </p>
</dd>

### -param <i>TargetInfo</i> [in]

<dd>
<p>A pointer to an optional Unicode string that specifies target information that is used to connect with the security service provider. </p>
</dd>

### -param <i>Spn</i> [in, out]

<dd>
<p>A pointer to a Unicode string that receives the security service provider name string that is created by this function.</p>
</dd>

### -param <i>TotalSize</i> [out]

<dd>
<p>A pointer to an optional variable that receives the length of the security service provider name string that is created by this function.</p>
</dd>

### -param <i>Allocate</i> [in]

<dd>
<p>A Boolean variable that indicates if the memory that is used to store the <i>Spn</i> Unicode string should be allocated by this function. If this parameter is <b>TRUE</b>, memory for <i>Spn</i> will be allocated from paged pool.</p>
</dd>

### -param <i>IsTargetInfoMarshaled</i> [in]

<dd>
<p>A Boolean variable that indicates that the caller provided a marshaled <i>InTargetInfo</i> structure.  If <i>IsTargetInfoMarshaled</i> is <b>TRUE</b>, <i>InTargetInfo</i>-&gt;Buffer points to a string representation of the CREDENTIAL_TARGET_INFORMATION structure as returned by the <b>CredMarshalTargetInfo</b> function.</p>
</dd>
</dl>

## -returns
<p><b>SecMakeSPNEx2</b> returns STATUS_SUCCESS on success or one of the following error codes on failure: </p><dl>
<dt><b>STATUS_BUFFER_OVERFLOW</b></dt>
</dl><p>The <i>Allocate</i> parameter was set to <b>FALSE</b> and one of the following conditions occurred:</p>

<p>The <i>Spn </i>parameter was a <b>NULL</b> pointer.</p>

<p>The maximum length for the <i>Spn</i> Unicode string parameter was too small.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>A total length of the <i>Spn</i> parameter exceeds 65535 bytes.</p><dl>
<dt><b>STATUS_NO_MEMORY</b></dt>
</dl><p>The <i>Allocate</i> parameter was set to <b>TRUE</b>, but the memory allocation request failed.</p>

<p> </p>

## -remarks
<p><b>SecMakeSPNEx2</b> is an enhanced version of <b>SecMakeSPNEx</b>. </p>

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
<p>Version</p>
</th>
<td width="70%">
<p>This function is available on Windows Vista, Windows Server 2008, and later versions of the Windows operating systems.</p>
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
<a href="..\ntifs\nf-ntifs-secmakespn.md">SecMakeSPN</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-secmakespnex.md">SecMakeSPNEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20SecMakeSPNEx2 function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
