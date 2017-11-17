---
UID: NF.ntifs.ZwOpenProcessTokenEx
title: ZwOpenProcessTokenEx
author: windows-driver-content
description: The ZwOpenProcessTokenEx routine opens the access token associated with a process.
old-location: kernel\zwopenprocesstokenex.htm
ms.assetid: 2ea6f764-b884-4764-a2ff-19d0170f9b31
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows XP and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ZwOpenProcessTokenEx,NtOpenProcessTokenEx
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
ms.keywords: ZwOpenProcessTokenEx
req.iface: 
---

# ZwOpenProcessTokenEx function



## -description
<p>The <b>ZwOpenProcessTokenEx</b> routine opens the access token associated with a process. </p>


## -syntax

````
NTSTATUS ZwOpenProcessTokenEx(
  _In_  HANDLE      ProcessHandle,
  _In_  ACCESS_MASK DesiredAccess,
  _In_  ULONG       HandleAttributes,
  _Out_ PHANDLE     TokenHandle
);
````


## -parameters
<dl>

### -param <i>ProcessHandle</i> [in]

<dd>
<p>Handle to the process whose access token is to be opened. The handle must have PROCESS_QUERY_INFORMATION access. Use the <b>NtCurrentProcess</b> macro, defined in Ntddk.h, to specify the current process. </p>
</dd>

### -param <i>DesiredAccess</i> [in]

<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a> structure specifying the requested types of access to the access token. These requested access types are compared with the token's discretionary access-control list (<a href="https://msdn.microsoft.com/dac27df2-fabd-4402-8daf-9317888dd30b">DACL</a>) to determine which accesses are granted or denied.</p>
</dd>

### -param <i>HandleAttributes</i> [in]

<dd>
<p>Attributes for the access token handle. Only OBJ_KERNEL_HANDLE is currently supported. If the caller is not running in the system process context, it must specify OBJ_KERNEL_HANDLE for this parameter. </p>
</dd>

### -param <i>TokenHandle</i> [out]

<dd>
<p>Pointer to a caller-allocated variable that receives a handle to the newly opened access token. </p>
</dd>
</dl>

## -returns
<p><b>ZwOpenProcessTokenEx</b> returns STATUS_SUCCESS or an appropriate error status. Possible error status codes include the following: </p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p><i>ProcessHandle</i> did not have PROCESS_QUERY_INFORMATION access. </p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>A new token handle could not be allocated. </p><dl>
<dt><b>STATUS_INVALID_HANDLE</b></dt>
</dl><p><i>ProcessHandle</i> was not a valid handle. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The specified <i>HandleAttributes</i> did not include OBJ_KERNEL_HANDLE. </p><dl>
<dt><b>STATUS_OBJECT_TYPE_MISMATCH</b></dt>
</dl><p><i>ProcessHandle</i> was not a process handle. </p><dl>
<dt><b>STATUS_PRIVILEGE_NOT_HELD</b></dt>
</dl><p>The caller does not have the privilege (SeSecurityPrivilege) necessary to create a token handle with the access specified in the <i>DesiredAccess</i> parameter. </p><dl>
<dt><b>STATUS_QUOTA_EXCEEDED</b></dt>
</dl><p>The process's memory quota is not sufficient to allocate the token handle. </p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>The token handle could not be created. </p>

<p> </p>

## -remarks
<p><b>ZwOpenProcessTokenEx</b> opens the access token associated with a process and returns a handle for that token. </p>

<p>Any handle obtained by calling <b>ZwOpenProcessTokenEx</b> must eventually be released by calling <b>ZwClose</b>. </p>

<p>Driver routines that run in a process context other than that of the system process must set the OBJ_KERNEL_HANDLE attribute for the <i>HandleAttributes</i> parameter of <b>ZwOpenProcessTokenEx</b>. This restricts the use of the handle returned by <b>ZwOpenProcessTokenEx</b> to processes running in kernel mode. Otherwise, the handle can be accessed by the process in whose context the driver is running. </p>

<p>For more information about security and access control, see the documentation on these topics in the Windows SDK. </p>

<p>For calls from kernel-mode drivers, the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>.</p>

<p><b>ZwOpenProcessTokenEx</b> opens the access token associated with a process and returns a handle for that token. </p>

<p>Any handle obtained by calling <b>ZwOpenProcessTokenEx</b> must eventually be released by calling <b>ZwClose</b>. </p>

<p>Driver routines that run in a process context other than that of the system process must set the OBJ_KERNEL_HANDLE attribute for the <i>HandleAttributes</i> parameter of <b>ZwOpenProcessTokenEx</b>. This restricts the use of the handle returned by <b>ZwOpenProcessTokenEx</b> to processes running in kernel mode. Otherwise, the handle can be accessed by the process in whose context the driver is running. </p>

<p>For more information about security and access control, see the documentation on these topics in the Windows SDK. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975204">PowerIrpDDis</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538866">ACL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551896">PsDereferencePrimaryToken</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566417">ZwClose</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567032">ZwOpenThreadTokenEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwOpenProcessTokenEx routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
