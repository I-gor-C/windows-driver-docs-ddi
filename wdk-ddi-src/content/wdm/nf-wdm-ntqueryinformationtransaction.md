---
UID: NF.wdm.NtQueryInformationTransaction
title: NtQueryInformationTransaction
author: windows-driver-content
description: The ZwQueryInformationTransaction routine retrieves information about a specified transaction.
old-location: kernel\zwqueryinformationtransaction.htm
old-project: kernel
ms.assetid: b4a4cc4b-8f23-4dd6-81d3-4cb2c861ba4f
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: NtQueryInformationTransaction
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
req.alt-api: ZwQueryInformationTransaction,NtQueryInformationTransaction
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

# NtQueryInformationTransaction function



## -description
<p>The <b>ZwQueryInformationTransaction</b> routine retrieves information about a specified transaction.</p>


## -syntax

````
NTSTATUS ZwQueryInformationTransaction(
  _In_      HANDLE                        TransactionHandle,
  _In_      TRANSACTION_INFORMATION_CLASS TransactionInformationClass,
  _Out_     PVOID                         TransactionInformation,
  _In_      ULONG                         TransactionInformationLength,
  _Out_opt_ PULONG                        ReturnLength
);
````


## -parameters
<dl>

### -param <i>TransactionHandle</i> [in]

<dd>
<p>A handle to a <a href="https://msdn.microsoft.com/124105bd-70be-49b1-8ea4-af6ba1f3cf16">transaction object</a> that was obtained by a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff566429">ZwCreateTransaction</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff567033">ZwOpenTransaction</a>. The handle must have TRANSACTION_QUERY_INFORMATION access to the object.</p>
</dd>

### -param <i>TransactionInformationClass</i> [in]

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff564800">TRANSACTION_INFORMATION_CLASS</a>-typed value that specifies the information to obtain. The value must be one of the following values:</p>
<ul>
<li>
<p><b>TransactionBasicInformation</b></p>
</li>
<li>
<p><b>TransactionPropertiesInformation</b></p>
</li>
<li>
<p><b>TransactionEnlistmentInformation</b></p>
</li>
</ul>
<p>The <b>TransactionFullInformation</b> value is not used with <b>ZwQueryInformationTransaction</b>.</p>
</dd>

### -param <i>TransactionInformation</i> [out]

<dd>
<p>A pointer to a caller-allocated buffer that receives the information that the <i>TransactionInformationClass</i> parameter specifies. The buffer's structure type must be <a href="https://msdn.microsoft.com/library/windows/hardware/ff564781">TRANSACTION_BASIC_INFORMATION</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff564844">TRANSACTION_PROPERTIES_INFORMATION</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff564787">TRANSACTION_ENLISTMENTS_INFORMATION</a>.</p>
</dd>

### -param <i>TransactionInformationLength</i> [in]

<dd>
<p>The length, in bytes, of the buffer that the <i>TransactionInformation</i> parameter points to, including the length of any additional array elements that the caller has allocated to receive information.</p>
</dd>

### -param <i>ReturnLength</i> [out, optional]

<dd>
<p>A pointer to a caller-allocated variable that receives the length, in bytes, of the information that KTM writes to the <i>TransactionInformation</i> buffer. This parameter is optional and can be <b>NULL</b>. </p>
</dd>
</dl>

## -returns
<p><b>ZwQueryInformationTransaction</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this routine might return one of the following values: </p><dl>
<dt><b>STATUS_INVALID_INFO_CLASS</b></dt>
</dl><p>The <i>TransactionInformationClass</i> parameter's value is invalid.</p><dl>
<dt><b>STATUS_INFO_LENGTH_MISMATCH</b></dt>
</dl><p>The length of the buffer that is specified by the <i>TransactionInformationLength</i> parameter is incorrect.</p><dl>
<dt><b>STATUS_OBJECT_TYPE_MISMATCH</b></dt>
</dl><p>The handle that the <i>TransactionHandle </i>parameter specifies is not a handle to a transaction object.</p><dl>
<dt><b>STATUS_INVALID_HANDLE</b></dt>
</dl><p>An object handle is invalid.</p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p>The caller does not have appropriate access to the transaction object.</p><dl>
<dt><b>STATUS_BUFFER_OVERFLOW</b></dt>
</dl><p>The buffer that the <i>TransactionInformation </i>parameter specifies is too small.</p>

<p> </p>

<p>The routine might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

## -remarks
<p>For more information about how to use <b>ZwQueryInformationTransaction</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff542876">Creating a Transactional Client</a>.</p>

<p><b>NtQueryInformationTransaction</b> and <b>ZwQueryInformationTransaction</b> are two versions of the same Windows Native System Services routine.</p>

<p>For calls from kernel-mode drivers, the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>.</p>

<p>For more information about how to use <b>ZwQueryInformationTransaction</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff542876">Creating a Transactional Client</a>.</p>

<p><b>NtQueryInformationTransaction</b> and <b>ZwQueryInformationTransaction</b> are two versions of the same Windows Native System Services routine.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975204">PowerIrpDDis</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564679">TmGetTransactionId</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564781">TRANSACTION_BASIC_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564787">TRANSACTION_ENLISTMENTS_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564800">TRANSACTION_INFORMATION_CLASS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564844">TRANSACTION_PROPERTIES_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566429">ZwCreateTransaction</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567033">ZwOpenTransaction</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567104">ZwSetInformationTransaction</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwQueryInformationTransaction routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
