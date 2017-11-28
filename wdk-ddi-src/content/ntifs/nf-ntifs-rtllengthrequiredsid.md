---
UID: NF.ntifs.RtlLengthRequiredSid
title: RtlLengthRequiredSid
author: windows-driver-content
description: The RtlLengthRequiredSid routine returns the length, in bytes, of the buffer required to store a security identifier (SID) with a specified number of subauthorities.
old-location: ifsk\rtllengthrequiredsid.htm
old-project: ifsk
ms.assetid: 1d6aa888-8e61-4a0e-88ea-13842fc2fff2
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RtlLengthRequiredSid
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlLengthRequiredSid
req.alt-loc: NtosKrnl.exe,Ntdll.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe (kernel mode); 
Ntdll.dll (user mode)
req.irql: <= APC_LEVEL
req.iface: 
---

# RtlLengthRequiredSid function



## -description
<p>The <b>RtlLengthRequiredSid</b> routine returns the length, in bytes, of the buffer required to store a security identifier (SID) with a specified number of subauthorities. </p>


## -syntax

````
ULONG RtlLengthRequiredSid(
  _In_ ULONG SubAuthorityCount
);
````


## -parameters
<dl>

### -param <i>SubAuthorityCount</i> [in]

<dd>
<p>The number of subauthorities to be stored in the SID. </p>
</dd>
</dl>

## -returns
<p><b>RtlLengthRequiredSid</b> returns the length, in bytes, of the buffer required to store the SID structure. </p>

## -remarks
<p>For more information about security and access control, see the documentation on these topics in the Microsoft Windows SDK.</p>

<p>For more information about security and access control, see the documentation on these topics in the Microsoft Windows SDK.</p>

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
<dt>NtosKrnl.exe (kernel mode); </dt>
<dt>Ntdll.dll (user mode)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552256">RtlEqualPrefixSid</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552260">RtlEqualSid</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552998">RtlInitializeSid</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553085">RtlLengthSid</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553236">RtlSubAuthoritySid</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553314">RtlValidSid</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556740">SID</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlLengthRequiredSid routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
