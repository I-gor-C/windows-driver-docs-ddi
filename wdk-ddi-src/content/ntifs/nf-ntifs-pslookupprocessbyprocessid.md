---
UID: NF.ntifs.PsLookupProcessByProcessId
title: PsLookupProcessByProcessId function
author: windows-driver-content
description: The PsLookupProcessByProcessId routine accepts the process ID of a process and returns a referenced pointer to EPROCESS structure of the process.
old-location: ifsk\pslookupprocessbyprocessid.htm
old-project: ifsk
ms.assetid: f9c4bcab-5584-4b26-b4ff-6067d7ef1890
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: PsLookupProcessByProcessId
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PsLookupProcessByProcessId
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
---

# PsLookupProcessByProcessId function



## -description
The <b>PsLookupProcessByProcessId</b> routine accepts the process ID of a process and returns a referenced pointer to EPROCESS structure of the process.



## -syntax

````
NTSTATUS PsLookupProcessByProcessId(
  _In_  HANDLE    ProcessId,
  _Out_ PEPROCESS *Process
);
````


## -parameters

### -param ProcessId [in]

Specifies the process ID of the process.


### -param Process [out]

Returns a referenced pointer to the EPROCESS structure of process specified by <i>ProcessId</i>.


## -returns
<b>PsLookupProcessByProcessId </b>returns STATUS_SUCCESS on success or an appropriate NTSTATUS value, such as: 
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>The process ID was not found.

 


## -remarks
This routine is available on Windows 2000 and later versions. 

If the call to <b>PsLookupProcessByProcessId</b> is successful, <b>PsLookupProcessByProcessID</b> increases the reference count on the object returned in the <i>Process</i> parameter. Consequently, when a driver has completed using the <i>Process</i> parameter, the driver must call <a href="kernel.obdereferenceobject">ObDereferenceObject</a> to dereference the <i>Process</i> parameter received from the <b>PsLookupProcessByProcessID</b> routine. 

The EPROCESS structure is an opaque data structure used internally by the operating system. This structure can be passed to other routines to access specific information in this structure.

A file system filter driver can enumerate active processes and then call <b>PsLookupProcessByProcessId</b> to convert a process ID to an EPROCESS structure. The process ID is available in the process create routine. A file system filter driver can set a process notification callback routine using <a href="kernel.pssetcreateprocessnotifyroutine">PsSetCreateProcessNotifyRoutine</a>. In the notification callback routine, the file system filter driver can use the passed in <i>ProcessId</i> parameter and call <b>PsLookupProcessByProcessID </b>to locate the EPROCESS structure. The <a href="kernel.pssetcreatethreadnotifyroutine">PsSetCreateThreadNotifyRoutine</a> can also be used to set a notification routine that returns the process ID when a thread ID is created.

The <b>PsLookupProcessByProcessId</b> routine contains pageable code. 


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= APC_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.obdereferenceobject">ObDereferenceObject</a>
</dt>
<dt>
<a href="kernel.psgetcurrentprocess">PsGetCurrentProcess</a>
</dt>
<dt>
<a href="kernel.psgetcurrentprocessid">PsGetCurrentProcessId</a>
</dt>
<dt>
<a href="kernel.psgetcurrentthread">PsGetCurrentThread</a>
</dt>
<dt>
<a href="kernel.psgetcurrentthreadid">PsGetCurrentThreadId</a>
</dt>
<dt>
<a href="ifsk.pslookupthreadbythreadid">PsLookupThreadByThreadId</a>
</dt>
<dt>
<a href="kernel.psremovecreatethreadnotifyroutine">PsRemoveCreateThreadNotifyRoutine</a>
</dt>
<dt>
<a href="kernel.psremoveloadimagenotifyroutine">PsRemoveLoadImageNotifyRoutine</a>
</dt>
<dt>
<a href="kernel.pssetcreateprocessnotifyroutine">PsSetCreateProcessNotifyRoutine</a>
</dt>
<dt>
<a href="kernel.pssetloadimagenotifyroutine">PsSetLoadImageNotifyRoutine</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20PsLookupProcessByProcessId routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

