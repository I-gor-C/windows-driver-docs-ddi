---
UID: NF.ntifs.RtlInitializeSid
title: RtlInitializeSid
author: windows-driver-content
description: The RtlInitializeSid routine initializes a security identifier (SID) structure.
old-location: ifsk\rtlinitializesid.htm
old-project: ifsk
ms.assetid: 6b87483f-8d5e-4e1d-839d-2271990dcbaa
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RtlInitializeSid
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available on Microsoft Windows 2000 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlInitializeSid
req.alt-loc: NtosKrnl.exe,Ntdll.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe (kernel mode); Ntdll.dll (user mode)
req.irql: < DISPATCH_LEVEL
req.iface: 
---

# RtlInitializeSid function



## -description
<p>The <b>RtlInitializeSid</b> routine initializes a security identifier (SID) structure. </p>


## -syntax

````
NTSTATUS RtlInitializeSid(
  _Out_ PSID                      Sid,
  _In_  PSID_IDENTIFIER_AUTHORITY IdentifierAuthority,
  _In_  UCHAR                     SubAuthorityCount
);
````


## -parameters
<dl>

### -param <i>Sid</i> [out]

<dd>
<p>Pointer to a caller-allocated SID structure to be initialized. </p>
</dd>

### -param <i>IdentifierAuthority</i> [in]

<dd>
<p>Pointer to an SID_IDENTIFIER_AUTHORITY structure to set in the SID structure. </p>
</dd>

### -param <i>SubAuthorityCount</i> [in]

<dd>
<p>Number of subauthorities to set in the SID. Subauthority values must be set separately, as described in the following Remarks section. </p>
</dd>
</dl>

## -returns
<p><b>RtlInitializeSid</b> returns one of the following:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The SID was successfully initialized.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The specified <i>SubAuthorityCount</i> value is invalid.</p>

<p> </p>

## -remarks
<p>Although <b>RtlInitializeSid</b> sets the number of subauthorities for the SID, it does not set the subauthority values. This must be done separately by calling <b>RtlSubAuthoritySid</b>. </p>

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
<p>Version</p>
</th>
<td width="70%">
<p>This routine is available on Microsoft Windows 2000 and later. </p>
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
<p>&lt; DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntifs\nf-ntifs-rtlsubauthoritysid.md">RtlSubAuthoritySid</a>
</dt>
<dt>
<a href="ifsk.sid">SID</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--sid-identifier-authority.md">SID_IDENTIFIER_AUTHORITY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlInitializeSid routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
