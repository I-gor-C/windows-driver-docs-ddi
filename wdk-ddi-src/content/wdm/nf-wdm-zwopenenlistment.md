---
UID: NF.wdm.ZwOpenEnlistment
title: ZwOpenEnlistment
author: windows-driver-content
description: The ZwOpenEnlistment routine obtains a handle to an existing enlistment object.
old-location: kernel\zwopenenlistment.htm
old-project: kernel
ms.assetid: b70d524f-2341-4b19-9c4a-f5095cb7f412
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: ZwOpenEnlistment
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later operating system versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ZwOpenEnlistment,NtOpenEnlistment
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

# ZwOpenEnlistment function



## -description
<p>The <b>ZwOpenEnlistment</b> routine obtains a handle to an existing <a href="https://msdn.microsoft.com/80e61475-4bb7-4eaa-b9f1-ff95eac9bc77">enlistment object</a>.</p>


## -syntax

````
NTSTATUS ZwOpenEnlistment(
  _Out_    PHANDLE            EnlistmentHandle,
  _In_     ACCESS_MASK        DesiredAccess,
  _In_     HANDLE             RmHandle,
  _In_     LPGUID             EnlistmentGuid,
  _In_opt_ POBJECT_ATTRIBUTES ObjectAttributes
);
````


## -parameters
<dl>

### -param <i>EnlistmentHandle</i> [out]

<dd>
<p>A pointer to a caller-allocated variable that receives a handle to an enlistment object if the call to <b>ZwOpenEnlistment</b> succeeds.</p>
</dd>

### -param <i>DesiredAccess</i> [in]

<dd>
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>-typed value that specifies the requested access to the enlistment object. For more information about how to specify this parameter, see the <i>DesiredAccess</i> parameter of <a href="https://msdn.microsoft.com/library/windows/hardware/ff566422">ZwCreateEnlistment</a>. This parameter cannot be zero.</p>
</dd>

### -param <i>RmHandle</i> [in]

<dd>
<p>A handle to a resource manager object that was obtained by a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff566427">ZwCreateResourceManager</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff567026">ZwOpenResourceManager</a>.</p>
</dd>

### -param <i>EnlistmentGuid</i> [in]

<dd>
<p>A pointer to a GUID that identifies the enlistment. For more information, see the following Remarks section.</p>
</dd>

### -param <i>ObjectAttributes</i> [in, optional]

<dd>
<p>A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff557749">OBJECT_ATTRIBUTES</a> structure that specifies the object's attributes. Use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547804">InitializeObjectAttributes</a> routine to initialize this structure, but specify only that routine's <i>InitializedAttributes</i> and <i>Attributes</i> parameters. If the caller is not running in a system thread context, it must set the OBJ_KERNEL_HANDLE flag in the <i>Attributes</i> parameter. This parameter is optional and can be <b>NULL</b>. </p>
</dd>
</dl>

## -returns
<p><b>ZwOpenEnlistment</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this routine might return one of the following values: </p><dl>
<dt><b>STATUS_INVALID_HANDLE</b></dt>
</dl><p>The object handle is invalid.</p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p>The caller does not have appropriate access to the enlistment object.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The <i>DesiredAccess</i> parameter's value is zero, or the <i>EnlistmentGuid</i> parameter's value is <b>NULL</b>.</p><dl>
<dt><b>STATUS_ENLISTMENT_NOT_FOUND</b></dt>
</dl><p>The enlistment that the <i>EnlistmentGuid</i> parameter specifies does not exist for the resource manager that the <i>RmHandle </i>parameter specifies.</p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p>The value of the <i>DesiredAccess</i> parameter is invalid.</p>

<p> </p>

<p>The routine might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

## -remarks
<p>Typically, a TPS component calls <b>ZwOpenEnlistment</b> after it receives an enlistment GUID from another TPS component that had previously called <a href="https://msdn.microsoft.com/library/windows/hardware/ff566422">ZwCreateEnlistment</a>. Most TPS designs do not require calling <b>ZwOpenEnlistment</b>.</p>

<p>A resource manager that calls <b>ZwOpenEnlistment</b> must eventually call <a href="https://msdn.microsoft.com/library/windows/hardware/ff566417">ZwClose</a> to close the object handle.</p>

<p>For more information about <b>ZwOpenEnlistment</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff544266">Enlistment Objects</a>.</p>

<p><b>NtOpenEnlistment</b> and <b>ZwOpenEnlistment</b> are two versions of the same Windows Native System Services routine.</p>

<p>For calls from kernel-mode drivers, the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>.</p>

<p>Typically, a TPS component calls <b>ZwOpenEnlistment</b> after it receives an enlistment GUID from another TPS component that had previously called <a href="https://msdn.microsoft.com/library/windows/hardware/ff566422">ZwCreateEnlistment</a>. Most TPS designs do not require calling <b>ZwOpenEnlistment</b>.</p>

<p>A resource manager that calls <b>ZwOpenEnlistment</b> must eventually call <a href="https://msdn.microsoft.com/library/windows/hardware/ff566417">ZwClose</a> to close the object handle.</p>

<p>For more information about <b>ZwOpenEnlistment</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff544266">Enlistment Objects</a>.</p>

<p><b>NtOpenEnlistment</b> and <b>ZwOpenEnlistment</b> are two versions of the same Windows Native System Services routine.</p>

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
<dt>Wdm.h (include Wdm.h or Ntifs.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547804">InitializeObjectAttributes</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557749">OBJECT_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566417">ZwClose</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566422">ZwCreateEnlistment</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566427">ZwCreateResourceManager</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567026">ZwOpenResourceManager</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567051">ZwQueryInformationEnlistment</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567094">ZwSetInformationEnlistment</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwOpenEnlistment routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
