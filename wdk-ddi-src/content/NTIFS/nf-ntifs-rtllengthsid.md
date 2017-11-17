---
UID: NF.ntifs.RtlLengthSid
title: RtlLengthSid
author: windows-driver-content
description: The RtlLengthSid routine returns the length, in bytes, of a valid security identifier (SID).
old-location: ifsk\rtllengthsid.htm
ms.assetid: 5d96061d-f1a2-4e45-b76e-5ada61d8accd
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlLengthSid
req.alt-loc: NtosKrnl.exe,ntdll.dll
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
ms.keywords: RtlLengthSid
req.iface: 
---

# RtlLengthSid function



## -description
<p>The <b>RtlLengthSid</b> routine returns the length, in bytes, of a valid security identifier (SID). </p>


## -syntax

````
ULONG RtlLengthSid(
  _In_ PSID Sid
);
````


## -parameters
<dl>

### -param <i>Sid</i> [in]

<dd>
<p>Pointer to the SID structure. Must point to a valid SID. </p>
</dd>
</dl>

## -returns
<p>If the SID structure is valid, <b>RtlLengthSid</b> returns the length, in bytes, of the SID structure.</p>

<p>If the SID structure is not valid, the return value is undefined. Before calling <b>RtlLengthSid</b>, pass the SID to <a href="https://msdn.microsoft.com/library/windows/hardware/ff553314">RtlValidSid</a> to verify that it is valid. </p>

## -remarks
<p>For more information about security and access control, see the documentation on these topics in the Microsoft Windows SDK. </p>

<p>For more information about security and access control, see the documentation on these topics in the Microsoft Windows SDK. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552256">RtlEqualPrefixSid</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552260">RtlEqualSid</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552998">RtlInitializeSid</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553083">RtlLengthRequiredSid</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlLengthSid routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
