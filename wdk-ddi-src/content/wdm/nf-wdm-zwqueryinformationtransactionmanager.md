---
UID: NF.wdm.ZwQueryInformationTransactionManager
title: ZwQueryInformationTransactionManager
author: windows-driver-content
description: The ZwQueryInformationTransactionManager routine retrieves information about a specified transaction manager object.
old-location: kernel\zwqueryinformationtransactionmanager.htm
old-project: kernel
ms.assetid: c87e0635-ad0a-4832-97ed-30c731559fb9
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ZwQueryInformationTransactionManager
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
req.alt-api: ZwQueryInformationTransactionManager,NtQueryInformationTransactionManager
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

# ZwQueryInformationTransactionManager function



## -description
<p>The <b>ZwQueryInformationTransactionManager</b> routine retrieves information about a specified transaction manager object.</p>


## -syntax

````
NTSTATUS ZwQueryInformationTransactionManager(
  _In_      HANDLE                               TransactionManagerHandle,
  _In_      TRANSACTIONMANAGER_INFORMATION_CLASS TransactionManagerInformationClass,
  _Out_     PVOID                                TransactionManagerInformation,
  _In_      ULONG                                TransactionManagerInformationLength,
  _Out_opt_ PULONG                               ReturnLength
);
````


## -parameters
<dl>

### -param TransactionManagerHandle [in]

<dd>
<p>A handle to a <a href="https://msdn.microsoft.com/af53cda4-e2ab-47df-9311-a4da2a2ee08d">transaction manager object</a> that was obtained by a previous call to <a href="..\wdm\nf-wdm-zwcreatetransactionmanager.md">ZwCreateTransactionManager</a> or <a href="..\wdm\nf-wdm-zwopentransactionmanager.md">ZwOpenTransactionManager</a>. The handle must have TRANSACTIONMANAGER_QUERY_INFORMATION access to the object.</p>
</dd>

### -param TransactionManagerInformationClass [in]

<dd>
<p>A <a href="..\wdm\ne-wdm--transactionmanager-information-class.md">TRANSACTIONMANAGER_INFORMATION_CLASS</a>-typed enumeration value that specifies the information to be obtained. This value must be one of the following:</p>
<ul>
<li>
<p><b>TransactionManagerBasicInformation</b></p>
</li>
<li>
<p><b>TransactionManagerLogInformation</b></p>
</li>
<li>
<p><b>TransactionManagerLogPathInformation</b></p>
</li>
</ul>
<p>The enumeration's <b>TransactionManagerOnlineProbeInformation</b> value is not used with <b>ZwQueryInformationTransactionManager</b>. </p>
</dd>

### -param TransactionManagerInformation [out]

<dd>
<p>A pointer to a caller-allocated buffer that receives the information that the <i>TransactionManagerInformationClass</i> parameter specifies. The buffer's structure type must be <a href="..\wdm\ns-wdm--transactionmanager-basic-information.md">TRANSACTIONMANAGER_BASIC_INFORMATION</a>, <a href="..\wdm\ns-wdm--transactionmanager-log-information.md">TRANSACTIONMANAGER_LOG_INFORMATION</a>, <a href="..\wdm\ns-wdm--transactionmanager-logpath-information.md">TRANSACTIONMANAGER_LOGPATH_INFORMATION</a>, or <a href="..\wdm\ns-wdm--transactionmanager-recovery-information.md">TRANSACTIONMANAGER_RECOVERY_INFORMATION</a>.</p>
</dd>

### -param TransactionManagerInformationLength [in]

<dd>
<p>The length, in bytes, of the buffer that the <i>TransactionManagerInformation</i> parameter points to, including the length of any additional array elements that the caller has allocated to receive information.</p>
</dd>

### -param ReturnLength [out, optional]

<dd>
<p>A pointer to a caller-allocated variable that receives the length, in bytes, of the information that KTM writes to the <i>TransactionManagerInformation</i> buffer. This parameter is optional and can be <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p><b>ZwQueryInformationTransactionManager</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this routine might return one of the following values: </p><dl>
<dt><b>STATUS_INVALID_INFO_CLASS</b></dt>
</dl><p>The <i>TransactionManagerInformationClass</i> parameter's value is invalid.</p><dl>
<dt><b>STATUS_INFO_LENGTH_MISMATCH</b></dt>
</dl><p>The length of the buffer that is specified by the <i>TransactionManagerInformationLength </i>parameter is incorrect.</p><dl>
<dt><b>STATUS_OBJECT_TYPE_MISMATCH</b></dt>
</dl><p>The specified handle is not a handle to a transaction manager object.</p><dl>
<dt><b>STATUS_INVALID_HANDLE</b></dt>
</dl><p>An object handle is invalid.</p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p>The caller does not have appropriate access to the transaction manager object.</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The buffer that is specified by the <i>TransactionManagerInformation </i>parameter is too small.</p>

<p> </p>

<p>The routine might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

## -remarks
<p>For more information about how to use <b>ZwQueryInformationTransactionManager</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565415">Using Log Streams with KTM</a>.</p>

<p><b>NtQueryInformationTransactionManager</b> and <b>ZwQueryInformationTransactionManager</b> are two versions of the same Windows Native System Services routine.</p>

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
<a href="..\wdm\ns-wdm--transactionmanager-basic-information.md">TRANSACTIONMANAGER_BASIC_INFORMATION</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--transactionmanager-log-information.md">TRANSACTIONMANAGER_LOG_INFORMATION</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--transactionmanager-logpath-information.md">TRANSACTIONMANAGER_LOGPATH_INFORMATION</a>
</dt>
<dt>
<a href="..\wdm\ne-wdm--transactionmanager-information-class.md">TRANSACTIONMANAGER_INFORMATION_CLASS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwcreatetransactionmanager.md">ZwCreateTransactionManager</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwopentransactionmanager.md">ZwOpenTransactionManager</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwrecovertransactionmanager.md">ZwRecoverTransactionManager</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwrollforwardtransactionmanager.md">ZwRollforwardTransactionManager</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwQueryInformationTransactionManager routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
