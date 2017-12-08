---
UID: NF.wdm.NtQueryInformationResourceManager
title: NtQueryInformationResourceManager
author: windows-driver-content
description: The ZwQueryInformationResourceManager routine retrieves information about a specified resource manager object.
old-location: kernel\zwqueryinformationresourcemanager.htm
old-project: kernel
ms.assetid: 6faeb410-486e-4b79-b942-62d16039d24b
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NtQueryInformationResourceManager
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later operating system versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ZwQueryInformationResourceManager,NtQueryInformationResourceManager
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
req.product: Windows 10 or later.
---

# NtQueryInformationResourceManager function



## -description
<p>The <b>ZwQueryInformationResourceManager</b> routine retrieves information about a specified <a href="https://msdn.microsoft.com/b44f2035-ee9f-453b-b12d-89ca36a8b280">resource manager object</a>.</p>


## -syntax

````
NTSTATUS ZwQueryInformationResourceManager(
  _In_      HANDLE                            ResourceManagerHandle,
  _In_      RESOURCEMANAGER_INFORMATION_CLASS ResourceManagerInformationClass,
  _Out_     PVOID                             ResourceManagerInformation,
  _In_      ULONG                             ResourceManagerInformationLength,
  _Out_opt_ PULONG                            ReturnLength
);
````


## -parameters
<dl>

### -param ResourceManagerHandle [in]

<dd>
<p>A handle to a resource manager object that was obtained by a previous call to <a href="..\wdm\nf-wdm-zwcreateresourcemanager.md">ZwCreateResourceManager</a> or <a href="..\wdm\nf-wdm-zwopenresourcemanager.md">ZwOpenResourceManager</a>. The handle must have RESOURCEMANAGER_QUERY_INFORMATION access to the object.</p>
</dd>

### -param ResourceManagerInformationClass [in]

<dd>
<p>A <a href="..\wdm\ne-wdm--resourcemanager-information-class.md">RESOURCEMANAGER_INFORMATION_CLASS</a>-typed value that specifies the information to retrieve. This value must be <b>ResourceManagerBasicInformation</b>.</p>
</dd>

### -param ResourceManagerInformation [out]

<dd>
<p>A pointer to a caller-allocated <a href="..\wdm\ns-wdm--resourcemanager-basic-information.md">RESOURCEMANAGER_BASIC_INFORMATION</a> structure that receives information from <b>ZwQueryInformationResourceManager</b>.</p>
</dd>

### -param ResourceManagerInformationLength [in]

<dd>
<p>The length, in bytes, of the buffer that the <i>ResourceManagerInformation</i> parameter points to.</p>
</dd>

### -param ReturnLength [out, optional]

<dd>
<p>A pointer to a caller-allocated variable that receives the length, in bytes, of the information that KTM writes to the <i>ResourceManagerInformation</i> buffer. This parameter is optional and can be <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p><b>ZwQueryInformationResourceManager</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this routine might return one of the following values: </p><dl>
<dt><b>STATUS_OBJECT_TYPE_MISMATCH</b></dt>
</dl><p>The specified handle is not a handle to a resource manager object.</p><dl>
<dt><b>STATUS_INVALID_HANDLE</b></dt>
</dl><p>An object handle is invalid.</p><dl>
<dt><b>STATUS_INVALID_INFO_CLASS</b></dt>
</dl><p>The <i>ResourceManagerInformationClass</i> parameter's value is invalid.</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The buffer size that the <i>ResourceManagerInformationLength </i>parameter specifies is smaller than the RESOURCEMANAGER_BASIC_INFORMATION structure.</p><dl>
<dt><b>STATUS_BUFFER_OVERFLOW</b></dt>
</dl><p>The buffer size that the <i>ResourceManagerInformationLength </i>parameter specifies is too small to receive all the variable-length information that is available.</p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p>The caller does not have appropriate access to the resource manager object.</p>

<p> </p>

<p>The routine might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

## -remarks
<p>For more information about the <b>ZwQueryInformationResourceManager</b> routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff542865">Creating a Resource Manager</a>.</p>

<p><b>NtQueryInformationResourceManager</b> and <b>ZwQueryInformationResourceManager</b> are two versions of the same Windows Native System Services routine.</p>

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
<p>Available in Windows Vista and later operating system versions.</p>
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
<a href="..\wdm\ns-wdm--resourcemanager-basic-information.md">RESOURCEMANAGER_BASIC_INFORMATION</a>
</dt>
<dt>
<a href="..\wdm\ne-wdm--resourcemanager-information-class.md">RESOURCEMANAGER_INFORMATION_CLASS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwcreateresourcemanager.md">ZwCreateResourceManager</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwopenresourcemanager.md">ZwOpenResourceManager</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwrecoverresourcemanager.md">ZwRecoverResourceManager</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwsetinformationresourcemanager.md">ZwSetInformationResourceManager</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwQueryInformationResourceManager routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
