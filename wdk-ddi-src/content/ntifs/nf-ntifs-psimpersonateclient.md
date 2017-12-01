---
UID: NF.ntifs.PsImpersonateClient
title: PsImpersonateClient
author: windows-driver-content
description: The PsImpersonateClient routine causes a server thread to impersonate a client.
old-location: ifsk\psimpersonateclient.htm
old-project: ifsk
ms.assetid: 69cc1253-07eb-43cf-abc7-5ad02ecb014d
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: PsImpersonateClient
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows XP and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PsImpersonateClient
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

# PsImpersonateClient function



## -description
<p>The <b>PsImpersonateClient</b> routine causes a server thread to impersonate a client. </p>


## -syntax

````
NTSTATUS PsImpersonateClient(
  _Inout_ PETHREAD                     Thread,
  _In_    PACCESS_TOKEN                Token,
  _In_    BOOLEAN                      CopyOnOpen,
  _In_    BOOLEAN                      EffectiveOnly,
  _In_    SECURITY_IMPERSONATION_LEVEL ImpersonationLevel
);
````


## -parameters
<dl>

### -param <i>Thread</i> [in, out]

<dd>
<p>Pointer to the server thread that is to impersonate the client. </p>
</dd>

### -param <i>Token</i> [in]

<dd>
<p>Pointer to the token to be assigned as the impersonation token. This token can be a primary token or an impersonation token. Set to <b>NULL</b> to end the impersonation. </p>
</dd>

### -param <i>CopyOnOpen</i> [in]

<dd>
<p>Specifies whether the token can be opened directly. Set to <b>TRUE</b> to specify that the token cannot be opened directly. In this case, the token must be duplicated, and the duplicate token used instead. Set to <b>FALSE</b> to allow the token to be opened directly. </p>
</dd>

### -param <i>EffectiveOnly</i> [in]

<dd>
<p>Set to <b>FALSE</b> to allow the server to enable groups and privileges that are currently disabled in the client security context, <b>TRUE</b> otherwise.</p>
</dd>

### -param <i>ImpersonationLevel</i> [in]

<dd>
<p>A <a href="..\wudfddi\ne-wudfddi--security-impersonation-level.md">SECURITY_IMPERSONATION_LEVEL</a> value that specifies the impersonation level at which the server is to access the token. </p>
</dd>
</dl>

## -returns
<p><b>PsImpersonateClient</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value, such as the following: </p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p>It was not possible to impersonate a client because of job restrictions.</p><dl>
<dt><b>STATUS_NO_MEMORY</b></dt>
</dl><p>There was insufficient memory to complete the operation.</p>

<p> </p>

## -remarks
<p><b>PsImpersonateClient</b> causes the specified server thread to impersonate the specified client. </p>

<p>The server thread could already be impersonating a client when <b>PsImpersonateClient</b> is called. If this is the case, the reference count on the token representing that client is decremented. To preserve this token for later use, drivers should call <a href="..\ntifs\nf-ntifs-psreferenceimpersonationtoken.md">PsReferenceImpersonationToken</a> before calling <b>PsImpersonateClient</b> and save the pointer that is returned by <b>PsReferenceImpersonationToken</b>. </p>

<p>To end the new impersonation and return the server thread to the previous impersonation, call <b>PsImpersonateClient</b> again, passing the saved pointer for the <i>Token</i> parameter. To end all impersonations, call the <a href="..\ntifs\nf-ntifs-psreverttoself.md">PsRevertToSelf</a> routine.</p>

<p>Otherwise, to end the impersonation and return the server thread to its original security context (that is, the one represented by its primary token), call <b>PsImpersonateClient</b> again, passing a <b>NULL</b> pointer for the <i>Token</i> parameter. </p>

<p>The <b>PsImpersonateClient</b> routine can fail to successfully return the server thread to the previous impersonation if the thread is already impersonating or there are job restrictions.</p>

<p>It is extremely unsafe to raise the privilege state of an untrusted user thread (take a user's thread and impersonate LocalSystem, for example). If an untrusted user thread had its privilege raised, the user could grab the thread token after it has been elevated and subvert the security of the entire system. </p>

<p>In cases where a higher privilege state is required, the task should be dispatched to a work queue where the task can be safely handled by system worker thread . This way no impersonation is necessary.</p>

<p>The <a href="..\ntifs\nf-ntifs-seimpersonateclientex.md">SeImpersonateClientEx</a> routine can be used to cause a thread to impersonate a user.</p>

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
<p>Available in Windows XP and later versions of the Windows operating systems.</p>
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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddk\nf-ntddk-psgetcurrentthread.md">PsGetCurrentThread</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-psreferenceimpersonationtoken.md">PsReferenceImpersonationToken</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-psreverttoself.md">PsRevertToSelf</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-seimpersonateclientex.md">SeImpersonateClientEx</a>
</dt>
<dt>
<a href="..\wudfddi\ne-wudfddi--security-impersonation-level.md">SECURITY_IMPERSONATION_LEVEL</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20PsImpersonateClient routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
