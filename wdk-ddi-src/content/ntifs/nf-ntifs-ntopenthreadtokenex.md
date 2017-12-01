---
UID: NF.ntifs.NtOpenThreadTokenEx
title: NtOpenThreadTokenEx
author: windows-driver-content
description: The ZwOpenThreadTokenEx routine opens the access token associated with a thread.
old-location: kernel\zwopenthreadtokenex.htm
old-project: kernel
ms.assetid: def462ee-30c6-44c0-8639-f8f7d3d0b69e
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NtOpenThreadTokenEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows XP and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ZwOpenThreadTokenEx,NtOpenThreadTokenEx
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: PowerIrpDDis, HwStorPortProhibitedDDIs
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

# NtOpenThreadTokenEx function



## -description
<p>The <b>ZwOpenThreadTokenEx</b> routine opens the access token associated with a thread. </p>


## -syntax

````
NTSTATUS ZwOpenThreadTokenEx(
  _In_  HANDLE      ThreadHandle,
  _In_  ACCESS_MASK DesiredAccess,
  _In_  BOOLEAN     OpenAsSelf,
  _In_  ULONG       HandleAttributes,
  _Out_ PHANDLE     TokenHandle
);
````


## -parameters
<dl>

### -param <i>ThreadHandle</i> [in]

<dd>
<p>Handle to the thread whose access token is to be opened. The handle must have THREAD_QUERY_INFORMATION access. Use the <b>NtCurrentThread</b> macro to specify the current thread. </p>
</dd>

### -param <i>DesiredAccess</i> [in]

<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a> structure specifying the requested types of access to the access token. These requested access types are compared with the token's discretionary access-control list (<a href="..\ntifs\ns-ntifs--acl.md">DACL</a>) to determine which access rights are granted or denied. </p>
</dd>

### -param <i>OpenAsSelf</i> [in]

<dd>
<p>Boolean value specifying whether the access check is to be made against the security context of the thread calling <b>ZwOpenThreadTokenEx</b> or against the security context of the process for the calling thread. </p>
<p>If this parameter is <b>FALSE</b>, the access check is performed using the security context for the calling thread. If the thread is impersonating a client, this security context can be that of a client process. If this parameter is <b>TRUE</b>, the access check is made using the security context of the process for the calling thread. </p>
</dd>

### -param <i>HandleAttributes</i> [in]

<dd>
<p>Attributes for the created handle. Only OBJ_KERNEL_HANDLE is currently supported. If the caller is not running in the system process context, it must specify OBJ_KERNEL_HANDLE for this parameter. </p>
</dd>

### -param <i>TokenHandle</i> [out]

<dd>
<p>Pointer to a caller-allocated variable that receives a handle to the newly opened access token. </p>
</dd>
</dl>

## -returns
<p><b>ZwOpenThreadTokenEx</b> returns STATUS_SUCCESS or an appropriate error status. Possible error status codes include the following: </p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p><i>ThreadHandle</i> did not have THREAD_QUERY_INFORMATION access. </p><dl>
<dt><b>STATUS_CANT_OPEN_ANONYMOUS</b></dt>
</dl><p>The client requested the SecurityAnonymous impersonation level. However, an anonymous token cannot be opened. For more information, see <a href="..\wudfddi\ne-wudfddi--security-impersonation-level.md">SECURITY_IMPERSONATION_LEVEL</a>. </p><dl>
<dt><b>STATUS_INVALID_HANDLE</b></dt>
</dl><p><i>ThreadHandle</i> was not a valid handle. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The specified <i>HandleAttributes</i> did not include OBJ_KERNEL_HANDLE. </p><dl>
<dt><b>STATUS_NO_TOKEN</b></dt>
</dl><p>An attempt has been made to open a token associated with a thread that is not currently impersonating a client. </p><dl>
<dt><b>STATUS_OBJECT_TYPE_MISMATCH</b></dt>
</dl><p><i>ThreadHandle</i> was not a thread handle. </p>

<p> </p>

## -remarks
<p><b>ZwOpenThreadTokenEx</b> opens the access token associated with a thread and returns a handle for that token. </p>

<p>The <i>OpenAsSelf</i> parameter allows a server process to open the access token for a client process when the client process has specified the SecurityIdentification impersonation level for the <b>SECURITY_IMPERSONATION_LEVEL</b> enumerated type. Without this parameter, the calling process is not be able to open the client's access token using the client's security context because it is impossible to open executive-level objects using the SecurityIdentification impersonation level. </p>

<p>Any handle obtained by calling <b>ZwOpenThreadTokenEx</b> must eventually be released by calling <b>ZwClose</b>. </p>

<p>Driver routines that run in a process context other than that of the system process must set the OBJ_KERNEL_HANDLE attribute for the <i>HandleAttributes</i> parameter of <b>ZwOpenThreadTokenEx</b>. This restricts the use of the handle returned by <b>ZwOpenThreadTokenEx</b> to processes running in kernel mode. Otherwise, the handle can be accessed by the process in whose context the driver is running. </p>

<p>For more information about security and access control, see the documentation on these topics in the Windows SDK.</p>

<p>For calls from kernel-mode drivers, the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>.</p>

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
<p>Available in Windows XP and later versions of Windows. </p>
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
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.wdm_powerirpddis">PowerIrpDDis</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--acl.md">ACL</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-psdereferenceprimarytoken.md">PsDereferencePrimaryToken</a>
</dt>
<dt>
<a href="..\wudfddi\ne-wudfddi--security-impersonation-level.md">SECURITY_IMPERSONATION_LEVEL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwclose.md">ZwClose</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-zwopenprocesstokenex.md">ZwOpenProcessTokenEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwOpenThreadTokenEx routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
