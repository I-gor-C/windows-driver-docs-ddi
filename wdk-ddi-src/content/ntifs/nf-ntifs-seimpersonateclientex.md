---
UID: NF.ntifs.SeImpersonateClientEx
title: SeImpersonateClientEx
author: windows-driver-content
description: The SeImpersonateClientEx routine causes a thread to impersonate a user.
old-location: ifsk\seimpersonateclientex.htm
old-project: ifsk
ms.assetid: 7a5043b9-2517-454a-a8d3-1ea09143c81a
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SeImpersonateClientEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 2000 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SeImpersonateClientEx
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

# SeImpersonateClientEx function



## -description
<p>The <b>SeImpersonateClientEx</b> routine causes a thread to impersonate a user.</p>


## -syntax

````
NTSTATUS SeImpersonateClientEx(
  _In_     PSECURITY_CLIENT_CONTEXT ClientContext,
  _In_opt_ PETHREAD                 ServerThread
);
````


## -parameters
<dl>

### -param <i>ClientContext</i> [in]

<dd>
<p>Pointer to the user's security client context.</p>
</dd>

### -param <i>ServerThread</i> [in, optional]

<dd>
<p>Pointer to the thread that is to impersonate the user. If not specified, the calling thread is used.</p>
</dd>
</dl>

## -returns
<p><b>SeImpersonateClientEx</b> returns an appropriate NTSTATUS value, such as the following: </p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The impersonation attempt succeeded.</p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p>The thread specified in <i>ServerThread</i> parameter did not have sufficient access rights to impersonate the user whose security client context is specified in the <i>ClientContext</i> parameter.</p><dl>
<dt><b>STATUS_NO_MEMORY</b></dt>
</dl><p><b>SeImpersonateClientEx</b> encountered a pool allocation failure when allocating memory for the impersonation information structure.</p>

<p> </p>

## -remarks
<p><b>SeImpersonateClientEx</b> is used to cause a thread to impersonate a user. The client security context in <i>ClientContext</i> is assumed to be up to date.</p>

<p>It is extremely unsafe to raise the privilege state of an untrusted user thread (take a user's thread and impersonate LocalSystem, for example). If an untrusted user thread had its privilege raised, the user could grab the thread token after it has been elevated and subvert the security of the entire system. </p>

<p>In cases where a higher privilege state is required, the task should be dispatched to a work queue where the task can be safely handled by system worker thread. This way no impersonation is necessary.</p>

<p>To end the impersonation of the user, call the <a href="ifsk.sestopimpersonatingclient">SeStopImpersonatingClient</a> routine.</p>

<p>The <a href="..\ntifs\nf-ntifs-psimpersonateclient.md">PsImpersonateClient</a> routine can be used to cause a server thread to impersonate a client.</p>

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
<p>Available in Windows 2000 and later versions of the Windows operating systems. </p>
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
<a href="..\ntifs\nf-ntifs-psimpersonateclient.md">PsImpersonateClient</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-secreateclientsecurity.md">SeCreateClientSecurity</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-secreateclientsecurityfromsubjectcontext.md">SeCreateClientSecurityFromSubjectContext</a>
</dt>
<dt>
<a href="ifsk.sestopimpersonatingclient">SeStopImpersonatingClient</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20SeImpersonateClientEx routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
