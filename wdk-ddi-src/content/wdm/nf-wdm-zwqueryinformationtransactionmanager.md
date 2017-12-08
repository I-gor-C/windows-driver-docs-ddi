---
UID: NF.wdm.ZwQueryInformationTransactionManager
title: ZwQueryInformationTransactionManager function
author: windows-driver-content
description: The ZwQueryInformationTransactionManager routine retrieves information about a specified transaction manager object.
old-location: kernel\zwqueryinformationtransactionmanager.htm
old-project: kernel
ms.assetid: c87e0635-ad0a-4832-97ed-30c731559fb9
ms.author: windowsdriverdev
ms.date: 12/6/2017
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
req.product: Windows 10 or later.
---

# ZwQueryInformationTransactionManager function



## -description
The <b>ZwQueryInformationTransactionManager</b> routine retrieves information about a specified transaction manager object.


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

### -param TransactionManagerHandle [in]

A handle to a <a href="https://msdn.microsoft.com/af53cda4-e2ab-47df-9311-a4da2a2ee08d">transaction manager object</a> that was obtained by a previous call to <a href="kernel.zwcreatetransactionmanager">ZwCreateTransactionManager</a> or <a href="kernel.zwopentransactionmanager">ZwOpenTransactionManager</a>. The handle must have TRANSACTIONMANAGER_QUERY_INFORMATION access to the object.

### -param TransactionManagerInformationClass [in]

A <a href="kernel.transactionmanager_information_class">TRANSACTIONMANAGER_INFORMATION_CLASS</a>-typed enumeration value that specifies the information to be obtained. This value must be one of the following:
<ul>
<li>
<b>TransactionManagerBasicInformation</b>
</li>
<li>
<b>TransactionManagerLogInformation</b>
</li>
<li>
<b>TransactionManagerLogPathInformation</b>
</li>
</ul>
The enumeration's <b>TransactionManagerOnlineProbeInformation</b> value is not used with <b>ZwQueryInformationTransactionManager</b>. 

### -param TransactionManagerInformation [out]

A pointer to a caller-allocated buffer that receives the information that the <i>TransactionManagerInformationClass</i> parameter specifies. The buffer's structure type must be <a href="kernel.transactionmanager_basic_information">TRANSACTIONMANAGER_BASIC_INFORMATION</a>, <a href="kernel.transactionmanager_log_information">TRANSACTIONMANAGER_LOG_INFORMATION</a>, <a href="kernel.transactionmanager_logpath_information">TRANSACTIONMANAGER_LOGPATH_INFORMATION</a>, or <a href="kernel.transactionmanager_recovery_information">TRANSACTIONMANAGER_RECOVERY_INFORMATION</a>.

### -param TransactionManagerInformationLength [in]

The length, in bytes, of the buffer that the <i>TransactionManagerInformation</i> parameter points to, including the length of any additional array elements that the caller has allocated to receive information.

### -param ReturnLength [out, optional]

A pointer to a caller-allocated variable that receives the length, in bytes, of the information that KTM writes to the <i>TransactionManagerInformation</i> buffer. This parameter is optional and can be <b>NULL</b>.

## -returns
<b>ZwQueryInformationTransactionManager</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this routine might return one of the following values: 
<dl>
<dt><b>STATUS_INVALID_INFO_CLASS</b></dt>
</dl>The <i>TransactionManagerInformationClass</i> parameter's value is invalid.
<dl>
<dt><b>STATUS_INFO_LENGTH_MISMATCH</b></dt>
</dl>The length of the buffer that is specified by the <i>TransactionManagerInformationLength </i>parameter is incorrect.
<dl>
<dt><b>STATUS_OBJECT_TYPE_MISMATCH</b></dt>
</dl>The specified handle is not a handle to a transaction manager object.
<dl>
<dt><b>STATUS_INVALID_HANDLE</b></dt>
</dl>An object handle is invalid.
<dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl>The caller does not have appropriate access to the transaction manager object.
<dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl>The buffer that is specified by the <i>TransactionManagerInformation </i>parameter is too small.

 

The routine might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.

## -remarks
For more information about how to use <b>ZwQueryInformationTransactionManager</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565415">Using Log Streams with KTM</a>.

<b>NtQueryInformationTransactionManager</b> and <b>ZwQueryInformationTransactionManager</b> are two versions of the same Windows Native System Services routine.

For calls from kernel-mode drivers, the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>.

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
Version
</th>
<td width="70%">
Available in Windows Vista and later operating system versions.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
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
PASSIVE_LEVEL
</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules
</th>
<td width="70%">
<a href="devtest.wdm_powerirpddis">PowerIrpDDis</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.transactionmanager_basic_information">TRANSACTIONMANAGER_BASIC_INFORMATION</a>
</dt>
<dt>
<a href="kernel.transactionmanager_log_information">TRANSACTIONMANAGER_LOG_INFORMATION</a>
</dt>
<dt>
<a href="kernel.transactionmanager_logpath_information">TRANSACTIONMANAGER_LOGPATH_INFORMATION</a>
</dt>
<dt>
<a href="kernel.transactionmanager_information_class">TRANSACTIONMANAGER_INFORMATION_CLASS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
<dt>
<a href="kernel.zwcreatetransactionmanager">ZwCreateTransactionManager</a>
</dt>
<dt>
<a href="kernel.zwopentransactionmanager">ZwOpenTransactionManager</a>
</dt>
<dt>
<a href="kernel.zwrecovertransactionmanager">ZwRecoverTransactionManager</a>
</dt>
<dt>
<a href="kernel.zwrollforwardtransactionmanager">ZwRollforwardTransactionManager</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwQueryInformationTransactionManager routine%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
