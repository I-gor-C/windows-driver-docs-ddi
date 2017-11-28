---
UID: NF.ntifs.RtlInitializeSidEx
title: RtlInitializeSidEx
author: windows-driver-content
description: The RtlInitializeSidEx routine initializes a pre-allocated security identifier (SID) structure.
old-location: ifsk\rtlinitializesidex.htm
old-project: ifsk
ms.assetid: 367D8BC1-07F4-474E-913A-5F825320A70C
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RtlInitializeSidEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available on Windows 10 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlInitializeSidEx
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
req.iface: 
---

# RtlInitializeSidEx function



## -description
<p>The <b>RtlInitializeSidEx</b> routine initializes a pre-allocated security identifier (SID) structure. </p>


## -syntax

````
NTSTATUS RtlInitializeSidEx(
  _Out_ PSID                      Sid,
  _In_  PSID_IDENTIFIER_AUTHORITY IdentifierAuthority,
  _In_  UCHAR                     SubAuthorityCount,
                                  ...
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
<p>Pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff556743">SID_IDENTIFIER_AUTHORITY</a> structure to set in the SID structure. </p>
</dd>

### -param <i>SubAuthorityCount</i> [in]

<dd>
<p>Number of sub-authorities to set in the SID.</p>
</dd>

### -param <i>...</i> 

<dd>
<p>The values to set each sub-authority. The caller must specify the SubAuthorityCount argument.</p>
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
<p>Version</p>
</th>
<td width="70%">
<p>This routine is available on Windows 10 and later. </p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553236">RtlSubAuthoritySid</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556740">SID</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556743">SID_IDENTIFIER_AUTHORITY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlInitializeSidEx routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
