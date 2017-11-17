---
UID: NF.ntifs.FsRtlMupGetProviderIdFromName
title: FsRtlMupGetProviderIdFromName
author: windows-driver-content
description: The FsRtlMupGetProviderIdFromName routine gets the provider identifier of a network redirector that is registered with the multiple UNC provider (MUP) from the device name of the network redirector.
old-location: ifsk\fsrtlmupgetprovideridfromname.htm
ms.assetid: a572398c-1755-4fc6-844b-85059d4d02cb
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: The FsRtlMupGetProviderIdFromName function is available in Windows Vista and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlMupGetProviderIdFromName
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= APC_LEVEL
ms.keywords: FsRtlMupGetProviderIdFromName
req.iface: 
---

# FsRtlMupGetProviderIdFromName function



## -description
<p>The <b>FsRtlMupGetProviderIdFromName</b> routine gets the provider identifier of a network redirector that is registered with the multiple UNC provider (MUP) from the device name of the network redirector.</p>


## -syntax

````
NTSTATUS FsRtlMupGetProviderIdFromName(
  _In_  PUNICODE_STRING pProviderName,
  _Out_ PULONG32        pProviderId
);
````


## -parameters
<dl>

### -param <i>pProviderName</i> [in]

<dd>
<p>A pointer to a Unicode string that contains the device name of the network redirector.</p>
</dd>

### -param <i>pProviderId</i> [out]

<dd>
<p>A pointer to a ULONG32-typed variable that receives the provider identifier of the network redirector.</p>
</dd>
</dl>

## -returns
<p>The <b>FsRtlMupGetProviderIdFromName</b> routine returns one of the following NTSTATUS values.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The provider identifier of the network redirector was successfully returned in the variable that is pointed to by the <i>pProviderId </i>parameter.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>One of the parameters is <b>NULL</b>.</p><dl>
<dt><b>STATUS_OBJECT_NAME_NOT_FOUND</b></dt>
</dl><p>The name of the network redirector specified in the <i>pProviderName </i>parameter does not match the name of any of the UNC providers that are registered with the MUP.</p>

<p> </p>

## -remarks
<p>A file system filter driver can call the <b>FsRtlMupGetProviderIdFromName</b> routine to get the provider identifier of a network redirector from the name of the network redirector. The file system filter driver can quickly compare the value of this identifier to the value of other provider identifiers without needing to do a string comparison.</p>

<p>The value of the provider identifier for a particular network redirector remains the same if the network redirector is unloaded from the system and then reloaded back into the system.</p>

<p>To get the provider identifier of a network redirector from a file object, a file system filter driver can call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546981">FsRtlMupGetProviderInfoFromFileObject</a> routine.</p>

<p>A file system filter driver can call the <b>FsRtlMupGetProviderIdFromName</b> routine to get the provider identifier of a network redirector from the name of the network redirector. The file system filter driver can quickly compare the value of this identifier to the value of other provider identifiers without needing to do a string comparison.</p>

<p>The value of the provider identifier for a particular network redirector remains the same if the network redirector is unloaded from the system and then reloaded back into the system.</p>

<p>To get the provider identifier of a network redirector from a file object, a file system filter driver can call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546981">FsRtlMupGetProviderInfoFromFileObject</a> routine.</p>

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
<p>The FsRtlMupGetProviderIdFromName function is available in Windows Vista and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546981">FsRtlMupGetProviderInfoFromFileObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlMupGetProviderIdFromName routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
