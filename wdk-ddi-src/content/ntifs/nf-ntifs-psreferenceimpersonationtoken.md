---
UID: NF.ntifs.PsReferenceImpersonationToken
title: PsReferenceImpersonationToken
author: windows-driver-content
description: The PsReferenceImpersonationToken routine increments the reference count of the impersonation token for the specified thread.
old-location: ifsk\psreferenceimpersonationtoken.htm
old-project: ifsk
ms.assetid: c72f48a8-ba51-423f-9105-7d78521dcae2
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: PsReferenceImpersonationToken
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: FltKernel.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PsReferenceImpersonationToken
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# PsReferenceImpersonationToken function



## -description
<p>The <b>PsReferenceImpersonationToken</b> routine increments the reference count of the impersonation token for the specified thread.</p>


## -syntax

````
PACCESS_TOKEN PsReferenceImpersonationToken(
  _Inout_ PETHREAD                      Thread,
  _Out_   PBOOLEAN                      CopyOnOpen,
  _Out_   PBOOLEAN                      EffectiveOnly,
  _Out_   PSECURITY_IMPERSONATION_LEVEL ImpersonationLevel
);
````


## -parameters
<dl>

### -param <i>Thread</i> [in, out]

<dd>
<p>Address of the thread whose impersonation token's reference count is to be incremented.</p>
</dd>

### -param <i>CopyOnOpen</i> [out]

<dd>
<p>Pointer to a caller-allocated Boolean variable. On return, this parameter receives <b>TRUE</b> if the token cannot be opened directly. In this case, the token must be duplicated, and the duplicate token must be used instead. If the token can be opened directly, this parameter receives <b>FALSE</b>. </p>
</dd>

### -param <i>EffectiveOnly</i> [out]

<dd>
<p>Pointer to a caller-allocated Boolean variable. On return, this parameter receives <b>FALSE</b> if the thread is allowed to enable groups and privileges that are currently disabled in the client security context, <b>TRUE</b> otherwise.</p>
</dd>

### -param <i>ImpersonationLevel</i> [out]

<dd>
<p>Pointer to a caller-allocated SECURITY_IMPERSONATION_LEVEL variable. On return, this parameter receives a value that specifies the impersonation level at which the thread is allowed to access the token. </p>
</dd>
</dl>

## -returns
<p><b>PsReferenceImpersonationToken</b> returns a pointer to the impersonation token for the given thread. If the thread is not currently impersonating a client, a <b>NULL</b> pointer is returned.</p>

## -remarks
<p>This routine is available starting with Microsoft Windows 2000. </p>

<p>If the thread is currently impersonating a client, <b>PsReferenceImpersonationToken</b> increments the reference count of the impersonation token and returns a pointer to the token. If the returned pointer is non-<b>NULL</b>, the impersonation token's reference count must be decremented by calling one of the following functions:</p>

<p><b>ObDereferenceObject</b>, for Windows 2000.</p>

<p><b>PsDereferenceImpersonationToken</b>, for Microsoft Windows XP or later.</p>

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
<dt>Ntifs.h (include FltKernel.h or Ntifs.h)</dt>
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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-obdereferenceobject.md">ObDereferenceObject</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-psdereferenceimpersonationtoken.md">PsDereferenceImpersonationToken</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-psimpersonateclient.md">PsImpersonateClient</a>
</dt>
<dt>
<a href="..\wudfddi\ne-wudfddi--security-impersonation-level.md">SECURITY_IMPERSONATION_LEVEL</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20PsReferenceImpersonationToken routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
