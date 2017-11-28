---
UID: NF.wdm.NtCreateTransactionManager
title: NtCreateTransactionManager
author: windows-driver-content
description: The ZwCreateTransactionManager routine creates a new transaction manager object.
old-location: kernel\zwcreatetransactionmanager.htm
old-project: kernel
ms.assetid: 9c9f0a8b-7add-4ab1-835d-39f508ce32a9
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: NtCreateTransactionManager
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
req.alt-api: ZwCreateTransactionManager,NtCreateTransactionManager
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

# NtCreateTransactionManager function



## -description
<p>The <b>ZwCreateTransactionManager</b> routine creates a new transaction manager object.</p>


## -syntax

````
NTSTATUS ZwCreateTransactionManager(
  _Out_    PHANDLE            TmHandle,
  _In_     ACCESS_MASK        DesiredAccess,
  _In_opt_ POBJECT_ATTRIBUTES ObjectAttributes,
  _In_opt_ PUNICODE_STRING    LogFileName,
  _In_opt_ ULONG              CreateOptions,
  _In_opt_ ULONG              CommitStrength
);
````


## -parameters
<dl>

### -param <i>TmHandle</i> [out]

<dd>
<p>A pointer to a caller-allocated variable that receives a handle to the new <a href="https://msdn.microsoft.com/af53cda4-e2ab-47df-9311-a4da2a2ee08d">transaction manager object</a>.</p>
</dd>

### -param <i>DesiredAccess</i> [in]

<dd>
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a> value that specifies the caller's requested access to the transaction manager object. In addition to the access rights that are defined for all kinds of objects (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>), the caller can specify any of the following access right flags for transaction manager objects. </p>
<table>
<tr>
<th>ACCESS_MASK flag</th>
<th>Allows the caller to</th>
</tr>
<tr>
<td>
<p>TRANSACTIONMANAGER_CREATE_RM</p>
</td>
<td>
<p>Create a resource manager (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff566427">ZwCreateResourceManager</a>).</p>
</td>
</tr>
<tr>
<td>
<p>TRANSACTIONMANAGER_QUERY_INFORMATION</p>
</td>
<td>
<p>Obtain information about the transaction manager (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff567058">ZwQueryInformationTransactionManager</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff566450">ZwEnumerateTransactionObject</a>). Also required for <a href="https://msdn.microsoft.com/library/windows/hardware/ff567026">ZwOpenResourceManager</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff566429">ZwCreateTransaction</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff567033">ZwOpenTransaction</a>.) </p>
</td>
</tr>
<tr>
<td>
<p>TRANSACTIONMANAGER_RECOVER</p>
</td>
<td>
<p>Recover the transaction manager (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff567079">ZwRecoverTransactionManager</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff567089">ZwRollforwardTransactionManager</a>).</p>
</td>
</tr>
<tr>
<td>
<p>TRANSACTIONMANAGER_RENAME</p>
</td>
<td>
<p>Not used.</p>
</td>
</tr>
<tr>
<td>
<p>TRANSACTIONMANAGER_SET_INFORMATION</p>
</td>
<td>
<p>Not used.</p>
</td>
</tr>
</table>
<p> </p>
<p>Alternatively, you can specify one or more of the following <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a> bitmaps. These bitmaps combine the flags from the previous table with the STANDARD_RIGHTS_<i>XXX</i> flags that are described on the <b>ACCESS_MASK</b> reference page. You can also combine these bitmaps with additional flags from the preceding table. The following table shows how the bitmaps correspond to specific access rights.</p>
<table>
<tr>
<th>Rights bitmap</th>
<th>Set of specific access rights</th>
</tr>
<tr>
<td>
<p>TRANSACTIONMANAGER_GENERIC_READ</p>
</td>
<td>
<p>STANDARD_RIGHTS_READ and TRANSACTIONMANAGER_QUERY_INFORMATION</p>
</td>
</tr>
<tr>
<td>
<p>TRANSACTIONMANAGER_GENERIC_WRITE</p>
</td>
<td>
<p>STANDARD_RIGHTS_WRITE, TRANSACTIONMANAGER_SET_INFORMATION, TRANSACTIONMANAGER_RECOVER, TRANSACTIONMANAGER_RENAME, and TRANSACTIONMANAGER_CREATE_RM</p>
</td>
</tr>
<tr>
<td>
<p>TRANSACTIONMANAGER_GENERIC_EXECUTE</p>
</td>
<td>
<p>STANDARD_RIGHTS_EXECUTE</p>
</td>
</tr>
<tr>
<td>
<p>TRANSACTIONMANAGER_ALL_ACCESS</p>
</td>
<td>
<p>STANDARD_RIGHTS_REQUIRED, TRANSACTIONMANAGER_GENERIC_READ, TRANSACTIONMANAGER_GENERIC_WRITE, and TRANSACTIONMANAGER_GENERIC_EXECUTE </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>ObjectAttributes</i> [in, optional]

<dd>
<p>A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff557749">OBJECT_ATTRIBUTES</a> structure that specifies the object name and other attributes. Use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547804">InitializeObjectAttributes</a> routine to initialize this structure. If the caller is not running in a system thread context, it must set the OBJ_KERNEL_HANDLE attribute when it calls <b>InitializeObjectAttributes</b>. This parameter is optional and can be <b>NULL</b>.</p>
</dd>

### -param <i>LogFileName</i> [in, optional]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a> structure that contains the path and file name of a <a href="https://msdn.microsoft.com/d7ad0e16-d1f2-4c41-b647-95b5445c2708">CLFS log file stream</a> to be associated with the transaction manager object. This parameter must be <b>NULL</b> if the <i>CreateOptions</i> parameter is TRANSACTION_MANAGER_VOLATILE. Otherwise, this parameter must be non-<b>NULL</b>. For more information, see the following Remarks section.</p>
</dd>

### -param <i>CreateOptions</i> [in, optional]

<dd>
<p>Optional object creation flags. The following table contains the available flags, which are defined in Ktmtypes.h.</p>
<table>
<tr>
<th>Option flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>TRANSACTION_MANAGER_VOLATILE</p>
</td>
<td>
<p>The transaction manager object will be volatile. Therefore, it will not use a log file.</p>
</td>
</tr>
<tr>
<td>
<p>TRANSACTION_MANAGER_COMMIT_DEFAULT</p>
</td>
<td>
<p>For internal use only.</p>
</td>
</tr>
<tr>
<td>
<p>TRANSACTION_MANAGER_COMMIT_SYSTEM_VOLUME</p>
</td>
<td>
<p>For internal use only.</p>
</td>
</tr>
<tr>
<td>
<p>TRANSACTION_MANAGER_COMMIT_SYSTEM_HIVES</p>
</td>
<td>
<p>For internal use only.</p>
</td>
</tr>
<tr>
<td>
<p>TRANSACTION_MANAGER_COMMIT_LOWEST</p>
</td>
<td>
<p>For internal use only.</p>
</td>
</tr>
<tr>
<td>
<p>TRANSACTION_MANAGER_CORRUPT_FOR_RECOVERY</p>
</td>
<td>
<p>For internal use only.</p>
</td>
</tr>
<tr>
<td>
<p>TRANSACTION_MANAGER_CORRUPT_FOR_PROGRESS</p>
</td>
<td>
<p>For internal use only.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>CommitStrength</i> [in, optional]

<dd>
<p>Reserved for future use. This parameter must be zero. </p>
</dd>
</dl>

## -returns
<p><b>ZwCreateTransactionManager</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this routine might return one of the following values: </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The value of an input parameter is invalid.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>KTM could not allocate system resources (typically memory).</p><dl>
<dt><b>STATUS_LOG_CORRUPTION_DETECTED</b></dt>
</dl><p>KTM encountered an error while creating or opening the log file.</p><dl>
<dt><b>STATUS_INVALID_ACL</b></dt>
</dl><p>A security descriptor contains an invalid access control list (ACL).</p><dl>
<dt><b>STATUS_INVALID_SID</b></dt>
</dl><p>A security descriptor contains an invalid security identifier (SID).</p><dl>
<dt><b>STATUS_OBJECT_NAME_EXISTS</b></dt>
</dl><p>The object name that the <i>ObjectAttributes </i>parameter specifies already exists.</p><dl>
<dt><b>STATUS_OBJECT_NAME_COLLISION</b></dt>
</dl><p>The operating system detected a duplicate object name. The error might indicate that the log stream is already being used.</p><dl>
<dt><b>STATUS_OBJECT_NAME_INVALID</b></dt>
</dl><p>The object name that the <i>ObjectAttributes </i>parameter specifies is invalid.</p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p>The value of the <i>DesiredAccess</i> parameter is invalid.</p>

<p> </p>

<p>The routine might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

## -remarks
<p>If the log file stream that the <i>LogFileName </i>parameter specifies does not exist, KTM calls CLFS to create the stream. If the stream already exists, KTM calls CLFS to open the stream.</p>

<p>Your TPS component must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff567079">ZwRecoverTransactionManager</a> after it has called <b>ZwCreateTransactionManager</b></p>

<p>If your TPS component specifies the TRANSACTION_MANAGER_VOLATILE flag in the <i>CreateOptions </i>parameter, all resource managers that are associated with the transaction manager object must specify the RESOURCE_MANAGER_VOLATILE flag when they call <a href="https://msdn.microsoft.com/library/windows/hardware/ff566427">ZwCreateResourceManager</a>.</p>

<p>A TPS component that calls <b>ZwCreateTransactionManager</b> must eventually call <a href="https://msdn.microsoft.com/library/windows/hardware/ff566417">ZwClose</a> to close the object handle.</p>

<p>For more information about how use <b>ZwCreateTransactionManager</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff542865">Creating a Resource Manager</a>.</p>

<p><b>NtCreateTransactionManager</b> and <b>ZwCreateTransactionManager</b> are two versions of the same Windows Native System Services routine. </p>

<p>For calls from kernel-mode drivers, the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>.</p>

<p>If the log file stream that the <i>LogFileName </i>parameter specifies does not exist, KTM calls CLFS to create the stream. If the stream already exists, KTM calls CLFS to open the stream.</p>

<p>Your TPS component must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff567079">ZwRecoverTransactionManager</a> after it has called <b>ZwCreateTransactionManager</b></p>

<p>If your TPS component specifies the TRANSACTION_MANAGER_VOLATILE flag in the <i>CreateOptions </i>parameter, all resource managers that are associated with the transaction manager object must specify the RESOURCE_MANAGER_VOLATILE flag when they call <a href="https://msdn.microsoft.com/library/windows/hardware/ff566427">ZwCreateResourceManager</a>.</p>

<p>A TPS component that calls <b>ZwCreateTransactionManager</b> must eventually call <a href="https://msdn.microsoft.com/library/windows/hardware/ff566417">ZwClose</a> to close the object handle.</p>

<p>For more information about how use <b>ZwCreateTransactionManager</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff542865">Creating a Resource Manager</a>.</p>

<p><b>NtCreateTransactionManager</b> and <b>ZwCreateTransactionManager</b> are two versions of the same Windows Native System Services routine. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547804">InitializeObjectAttributes</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557749">OBJECT_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566417">ZwClose</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567035">ZwOpenTransactionManager</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567058">ZwQueryInformationTransactionManager</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567079">ZwRecoverTransactionManager</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567089">ZwRollforwardTransactionManager</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwCreateTransactionManager routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
