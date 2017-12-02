---
UID: NF.ntifs.SeCreateClientSecurityFromSubjectContext
title: SeCreateClientSecurityFromSubjectContext
author: windows-driver-content
description: The SeCreateClientSecurityFromSubjectContext routine retrieves the access token for a security subject context and uses the result to initialize a security client context with the information needed to call SeImpersonateClientEx.
old-location: ifsk\secreateclientsecurityfromsubjectcontext.htm
old-project: ifsk
ms.assetid: 3b3b12b8-05f7-40e6-909c-b99bf18cc299
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: SeCreateClientSecurityFromSubjectContext
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
req.alt-api: SeCreateClientSecurityFromSubjectContext
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

# SeCreateClientSecurityFromSubjectContext function



## -description
<p>The <b>SeCreateClientSecurityFromSubjectContext</b> routine retrieves the access token for a security subject context and uses the result to initialize a security client context with the information needed to call <b>SeImpersonateClientEx</b>.</p>


## -syntax

````
NTSTATUS SeCreateClientSecurityFromSubjectContext(
  _In_  PSECURITY_SUBJECT_CONTEXT    SubjectContext,
  _In_  PSECURITY_QUALITY_OF_SERVICE ClientSecurityQos,
  _In_  BOOLEAN                      ServerIsRemote,
  _Out_ PSECURITY_CLIENT_CONTEXT     ClientContext
);
````


## -parameters
<dl>

### -param SubjectContext [in]

<dd>
<p>Pointer to the security subject context of the client to be impersonated.</p>
</dd>

### -param ClientSecurityQos [in]

<dd>
<p>Pointer to a caller-allocated SECURITY_QUALITY_OF_SERVICE structure indicating what form of impersonation is to be performed.</p>
</dd>

### -param ServerIsRemote [in]

<dd>
<p>Set to <b>TRUE</b> if the server of the client's request is remote.</p>
</dd>

### -param ClientContext [out]

<dd>
<p>Pointer to a caller-allocated SECURITY_CLIENT_CONTEXT structure to be initialized.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The security client context was successfully initialized.</p><dl>
<dt><b>STATUS_BAD_IMPERSONATION_LEVEL</b></dt>
</dl><p>The client to be impersonated is currently impersonating a client of its own, and one of the following is true:</p>

<p>The client's effective token cannot be passed on for use by another server, because its impersonation level is <b>SecurityAnonymous</b> or <b>SecurityIdentification</b>. </p>

<p><i>ServerIsRemote</i> is <b>TRUE</b>, and the client thread is impersonating its client at other than <b>SecurityDelegation</b> level.</p>

<p> </p>

## -remarks
<p><b>SeCreateClientSecurityFromSubjectContext</b> initializes a client security context block to represent a client's security context.</p>

<p>If the <b>ContextTrackingMode</b> member of <i>ClientSecurityQos</i> is set to SECURITY_DYNAMIC_TRACKING and <i>ServerIsRemote</i> is set to <b>FALSE</b>, <b>SeCreateClientSecurityFromSubjectContext</b> uses a reference to the client's effective token. Otherwise, <b>SeCreateClientSecurityFromSubjectContext</b> creates a copy of the client's token.</p>

<p>Each call to <b>SeCreateClientSecurityFromSubjectContext</b> must be matched by a subsequent call to <b>SeDeleteClientSecurity</b>.</p>

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
<a href="ifsk.security_subject_context">SECURITY_SUBJECT_CONTEXT</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-sedeleteclientsecurity.md">SeDeleteClientSecurity</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-seimpersonateclientex.md">SeImpersonateClientEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20SeCreateClientSecurityFromSubjectContext routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
