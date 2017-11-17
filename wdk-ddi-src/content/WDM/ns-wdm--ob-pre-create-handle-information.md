---
UID: NS.wdm._OB_PRE_CREATE_HANDLE_INFORMATION
title: OB_PRE_CREATE_HANDLE_INFORMATION
author: windows-driver-content
description: The OB_PRE_CREATE_HANDLE_INFORMATION structure provides information to an ObjectPreCallback routine about a thread or process handle that is being opened.
old-location: kernel\ob_pre_create_handle_information.htm
ms.assetid: 50fd7666-cdec-4bdb-b350-2c2222124020
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Server 2008 and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: OB_PRE_CREATE_HANDLE_INFORMATION
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
ms.keywords: OB_PRE_CREATE_HANDLE_INFORMATION, OB_PRE_CREATE_HANDLE_INFORMATION, *POB_PRE_CREATE_HANDLE_INFORMATION
req.iface: 
req.product: Windows 10 or later.
---

# OB_PRE_CREATE_HANDLE_INFORMATION structure



## -description
<p>The <b>OB_PRE_CREATE_HANDLE_INFORMATION</b> structure provides information to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff557745">ObjectPreCallback</a> routine about a thread or process handle that is being opened.</p>


## -syntax

````
typedef struct _OB_PRE_CREATE_HANDLE_INFORMATION {
  ACCESS_MASK DesiredAccess;
  ACCESS_MASK OriginalDesiredAccess;
} OB_PRE_CREATE_HANDLE_INFORMATION, *POB_PRE_CREATE_HANDLE_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>DesiredAccess</b>

<dd>
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a> value that specifies the access rights to grant for the handle. By default, this member equals <i>OriginalDesiredAccess</i>, but the <i>ObjectPreCallback</i> routine can modify this value to restrict the access that is granted.</p>
<p>Drivers can use the following flags for handles to processes:</p>
<table>
<tr>
<th>Flag</th>
<th>Allowed operations</th>
</tr>
<tr>
<td>
<p>PROCESS_CREATE_PROCESS</p>
</td>
<td>
<p>Create a new child process of the process.</p>
</td>
</tr>
<tr>
<td>
<p>PROCESS_CREATE_THREAD</p>
</td>
<td>
<p>Create a new thread in the context of the process.</p>
</td>
</tr>
<tr>
<td>
<p>PROCESS_DUP_HANDLE</p>
</td>
<td>
<p>Duplicate handles to or from the context of the process, such as by calling the user-mode <b>DuplicateHandle</b> routine.</p>
</td>
</tr>
<tr>
<td>
<p>PROCESS_SET_QUOTA</p>
</td>
<td>
<p>Set the working set size for the process, such as by calling the user-mode <b>SetProcessWorkingSetSize</b> routine.</p>
</td>
</tr>
<tr>
<td>
<p>PROCESS_SET_INFORMATION</p>
</td>
<td>
<p>Modify process settings, such as by calling the user-mode <b>SetPriorityClass</b> routine.</p>
</td>
</tr>
<tr>
<td>
<p>PROCESS_SUSPEND_RESUME</p>
</td>
<td>
<p>Suspend or resume the process.</p>
</td>
</tr>
<tr>
<td>
<p>PROCESS_TERMINATE</p>
</td>
<td>
<p>Terminate the process, such as by calling the user-mode <b>TerminateProcess</b> routine..</p>
</td>
</tr>
<tr>
<td>
<p>PROCESS_VM_OPERATIONS</p>
</td>
<td>
<p>Modify the address space of the process, such as by calling the user-mode <b>WriteProcessMemory</b> and <b>VirtualProtectEx</b> routines.</p>
</td>
</tr>
<tr>
<td>
<p>PROCESS_VM_WRITE</p>
</td>
<td>
<p>Write to the address space of the process, such as by calling the user-mode <b>WriteProcessMemory</b> routine.</p>
</td>
</tr>
</table>
<p> </p>
<p>Drivers can use the following flags for handles to threads:</p>
<table>
<tr>
<th>Flag</th>
<th>Allowed operations</th>
</tr>
<tr>
<td>
<p>THREAD_DIRECT_IMPERSONATION</p>
</td>
<td>
<p>Enable a server thread to impersonate one of its clients.</p>
</td>
</tr>
<tr>
<td>
<p>THREAD_IMPERSONATE</p>
</td>
<td>
<p>Impersonate the operating system's anonymous logon token, such as by calling the user-mode <b>ImpersonateAnonymousToken</b> routine.</p>
</td>
</tr>
<tr>
<td>
<p>THREAD_SET_CONTEXT</p>
</td>
<td>
<p>Modify the thread's execution context, such as by calling the user-mode <b>SetThreadContext</b> routine.</p>
</td>
</tr>
<tr>
<td>
<p>THREAD_SET_INFORMATION</p>
</td>
<td>
<p>Modify thread settings, such as by calling the user-mode <b>SetThreadIdealProcessor</b> routine. The operations that are permitted by this access right are a superset of those that are permitted by the THREAD_SET_LIMITED_INFORMATION access right.</p>
</td>
</tr>
<tr>
<td>
<p>THREAD_SET_LIMITED_INFORMATION</p>
</td>
<td>
<p>Modify a limited set of thread settings, such as by calling the user-mode <b>SetThreadAffinityMask</b> and <b>SetThreadPriorityBoost</b> routines.</p>
</td>
</tr>
<tr>
<td>
<p>THREAD_SET_THREAD_TOKEN</p>
</td>
<td>
<p>Modify properties of the thread's impersonation token, such as by calling the user-mode <b>SetTokenInformation</b> routine.</p>
</td>
</tr>
<tr>
<td>
<p>THREAD_SUSPEND_RESUME</p>
</td>
<td>
<p>Suspend or resume the thread, such as by calling the user-mode <b>SuspendThread</b> and <b>ResumeThread</b> routines.</p>
</td>
</tr>
<tr>
<td>
<p>THREAD_TERMINATE</p>
</td>
<td>
<p>Terminate the thread, such as by calling the user-mode <b>TerminateThread</b> routine.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>OriginalDesiredAccess</b>

<dd>
<p>An ACCESS_MASK value that specifies the original access that was requested for the handle.</p>
</dd>
</dl>

## -remarks
<p>You can never add access rights beyond what is specified in the <b>DesiredAccess</b> member. If the access right is listed as a modifiable flag, the access right can be removed.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Server 2008 and later versions of the Windows operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557745">ObjectPreCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20OB_PRE_CREATE_HANDLE_INFORMATION structure%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
