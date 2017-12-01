---
UID: NF.ntifs.NtQueryObject
title: NtQueryObject
author: windows-driver-content
description: The ZwQueryObject routine provides information about a supplied object.
old-location: kernel\zwqueryobject.htm
old-project: kernel
ms.assetid: 439658a5-d2db-4a31-a1eb-b8943c40cc96
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NtQueryObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h, FltKernel.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ZwQueryObject,NtQueryObject
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

# NtQueryObject function



## -description
<p>The <b>ZwQueryObject</b> routine provides information about a supplied object.</p>


## -syntax

````
NTSTATUS ZwQueryObject(
  _In_opt_  HANDLE                   Handle,
  _In_      OBJECT_INFORMATION_CLASS ObjectInformationClass,
  _Out_opt_ PVOID                    ObjectInformation,
  _In_      ULONG                    ObjectInformationLength,
  _Out_opt_ PULONG                   ReturnLength
);
````


## -parameters
<dl>

### -param <i>Handle</i> [in, optional]

<dd>
<p>A handle to the object to obtain information about.</p>
</dd>

### -param <i>ObjectInformationClass</i> [in]

<dd>
<p>Specifies an <a href="..\ntifs\ne-ntifs--object-information-class.md">OBJECT_INFORMATION_CLASS</a> value that determines the type of information returned in the <i>ObjectInformation</i> buffer.</p>
</dd>

### -param <i>ObjectInformation</i> [out, optional]

<dd>
<p>A pointer to a caller-allocated buffer that receives the requested information.</p>
</dd>

### -param <i>ObjectInformationLength</i> [in]

<dd>
<p>Specifies the size, in bytes, of the <i>ObjectInformation</i> buffer.</p>
</dd>

### -param <i>ReturnLength</i> [out, optional]

<dd>
<p>A pointer to a variable that receives the size, in bytes, of the requested key information. If <b>ZwQueryObject</b> returns STATUS_SUCCESS, the variable contains the amount of data returned. If <b>ZwQueryObject</b> returns STATUS_BUFFER_OVERFLOW or STATUS_BUFFER_TOO_SMALL, you can use the value of the variable to determine the required buffer size.</p>
</dd>
</dl>

## -returns
<p><b>ZwQueryObject</b> returns STATUS_SUCCESS or an appropriate error status. Possible error status codes include the following:</p><dl>
<dt><b>STATUS_ACCESS_DENIED </b></dt>
</dl><p>There were insufficient permissions to perform this query.</p><dl>
<dt><b>STATUS_INVALID_HANDLE</b></dt>
</dl><p>The supplied object handle is invalid.</p><dl>
<dt><b>STATUS_INFO_LENGTH_MISMATCH</b></dt>
</dl><p>The info length is not sufficient to hold the data.</p>

<p> </p>

## -remarks
<p>If the call to the <b>ZwQueryObject</b> function occurs in user mode, you should use the name "<b>NtQueryObject</b>" instead of "<b>ZwQueryObject</b>". </p>

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
<p>Available starting with Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h or FltKernel.h)</dt>
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
<a href="..\ntifs\ne-ntifs--object-information-class.md">OBJECT_INFORMATION_CLASS</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--public-object-basic-information.md">PUBLIC_OBJECT_BASIC_INFORMATION</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs---public-object-type-information.md">PUBLIC_OBJECT_TYPE_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwQueryObject routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
