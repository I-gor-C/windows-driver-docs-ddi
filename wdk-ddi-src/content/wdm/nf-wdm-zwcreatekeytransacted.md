---
UID: NF.wdm.ZwCreateKeyTransacted
title: ZwCreateKeyTransacted
author: windows-driver-content
description: The ZwCreateKeyTransacted routine creates a new registry key or opens an existing one, and it associates the key with a transaction.
old-location: kernel\zwcreatekeytransacted.htm
old-project: kernel
ms.assetid: c0cf38f4-2820-4177-93e6-2e20524d0353
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ZwCreateKeyTransacted
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ZwCreateKeyTransacted
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

# ZwCreateKeyTransacted function



## -description
<p>The <b>ZwCreateKeyTransacted</b> routine creates a new registry key or opens an existing one, and it associates the key with a transaction. </p>


## -syntax

````
NTSTATUS ZwCreateKeyTransacted(
  _Out_      PHANDLE            KeyHandle,
  _In_       ACCESS_MASK        DesiredAccess,
  _In_       POBJECT_ATTRIBUTES ObjectAttributes,
  _Reserved_ ULONG              TitleIndex,
  _In_opt_   PUNICODE_STRING    Class,
  _In_       ULONG              CreateOptions,
  _In_       HANDLE             TransactionHandle,
  _Out_opt_  PULONG             Disposition
);
````


## -parameters
<dl>

### -param KeyHandle [out]

<dd>
<p>A pointer to a HANDLE variable into which the routine writes the handle to the key. </p>
</dd>

### -param DesiredAccess [in]

<dd>
<p>Specifies the type of access to the key that the caller requests. This parameter is an <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a> value. For more information, see the description of the <i>DesiredAccess</i> parameter of the <a href="..\wdm\nf-wdm-zwcreatekey.md">ZwCreateKey</a> routine. </p>
</dd>

### -param ObjectAttributes [in]

<dd>
<p>A pointer to the object attributes of the key being opened. This parameter points to an <a href="..\d3dkmthk\ns-d3dkmthk--object-attributes.md">OBJECT_ATTRIBUTES</a> structure that must have been previously initialized by the <a href="..\wudfwdm\nf-wudfwdm-initializeobjectattributes.md">InitializeObjectAttributes</a> routine. The caller must specify the name of the registry key as the <i>ObjectName</i> parameter in the call to <b>InitializeObjectAttributes</b>. If the caller is not running in a system thread context, it must set the OBJ_KERNEL_HANDLE attribute when it calls <b>InitializeObjectAttributes</b>. </p>
</dd>

### -param TitleIndex 

<dd>
<p>Device and intermediate drivers set this parameter to zero. </p>
</dd>

### -param Class [in, optional]

<dd>
<p>Device and intermediate drivers set this parameter to <b>NULL</b>. </p>
</dd>

### -param CreateOptions [in]

<dd>
<p>Specifies the options to apply when the routine creates or opens the key. Set this parameter to zero or to the bitwise OR of one or more of the following REG_OPTION_<i>XXX</i> flag bits.</p>
<table>
<tr>
<th><i>CreateOptions</i> flag</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>REG_OPTION_VOLATILE</p>
</td>
<td>
<p>The key is <u>not</u> preserved after the computer restarts.</p>
</td>
</tr>
<tr>
<td>
<p>REG_OPTION_NON_VOLATILE</p>
</td>
<td>
<p>The key is preserved after the computer restarts.</p>
</td>
</tr>
<tr>
<td>
<p>REG_OPTION_CREATE_LINK</p>
</td>
<td>
<p>The key is a symbolic link. This flag is not used by device and intermediate drivers.</p>
</td>
</tr>
<tr>
<td>
<p>REG_OPTION_BACKUP_RESTORE</p>
</td>
<td>
<p>Open the key with special privileges that enable backup and restore operations. This flag is not used by device and intermediate drivers.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param TransactionHandle [in]

<dd>
<p>A handle to a <a href="https://msdn.microsoft.com/124105bd-70be-49b1-8ea4-af6ba1f3cf16">transaction object</a>. To obtain this handle, you can call the <a href="..\wdm\nf-wdm-zwcreatetransaction.md">ZwCreateTransaction</a> routine. Or, if you have a pointer to a transaction object, you can supply the pointer to the <a href="..\ntifs\nf-ntifs-obopenobjectbypointer.md">ObOpenObjectByPointer</a> routine to obtain the corresponding transaction handle.</p>
</dd>

### -param Disposition [out, optional]

<dd>
<p>A pointer to a location into which the routine writes one of the following values to indicate whether the call created a new key or opened an existing one.</p>
<table>
<tr>
<th><i>Disposition</i> value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>REG_CREATED_NEW_KEY</p>
</td>
<td>
<p>A new key was created.</p>
</td>
</tr>
<tr>
<td>
<p>REG_OPENED_EXISTING_KEY</p>
</td>
<td>
<p>An existing key was opened.</p>
</td>
</tr>
</table>
<p> </p>
<p>You can set <i>Disposition</i> = <b>NULL</b> if this information is not needed.</p>
</dd>
</dl>

## -returns
<p><b>ZwCreateKeyTransacted</b> returns STATUS_SUCCESS if the call successfully creates or opens the key. Possible error return values include the following:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p> The <i>ObjectAttributes</i> parameter is <b>NULL</b> or points to invalid information, or the <i>CreateOptions</i> parameter value specifies invalid options.</p><dl>
<dt><b>STATUS_OBJECT_PATH_SYNTAX_BAD</b></dt>
</dl><p>The registry path in the object attributes is invalid.</p><dl>
<dt><b>STATUS_OBJECT_NAME_NOT_FOUND</b></dt>
</dl><p>The registry path in the object attributes was not found.</p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p>The caller did not have the required access rights to open a handle for the named registry key.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>A memory allocation operation failed.</p>

<p> </p>

## -remarks
<p>This routine provides a handle that the caller can access a registry key with. Additionally, this routine associates the key with an active transaction.</p>

<p>After the handle that is pointed to by <i>KeyHandle</i> is no longer being used, the driver must call the <a href="..\wdm\nf-wdm-zwclose.md">ZwClose</a> routine to close it.</p>

<p>Like <b>ZwCreateKeyTransacted</b>, the <a href="..\wdm\nf-wdm-zwopenkeytransacted.md">ZwOpenKeyTransacted</a> routine associates a key with a transaction. Unlike <b>ZwCreateKeyTransacted</b>, which can create a new key or open an existing key, <b>ZwOpenKeyTransacted</b> can only open a registry key that already exists.</p>

<p>After a kernel-mode driver obtains a handle to a transaction (for example, by calling <b>ZwCreateTransaction</b>), the driver can perform a series of registry operations that are part of this transaction. The driver can close the transaction either by committing to the changes that were made in the transaction or by rolling back the transaction.</p>

<p>After the driver successfully completes all registry operations that are part of a transaction, it can call the <a href="..\wdm\nf-wdm-zwcommittransaction.md">ZwCommitTransaction</a> routine to commit to the changes. The driver can call the <a href="..\wdm\nf-wdm-zwrollbacktransaction.md">ZwRollbackTransaction</a> routine to roll back the transaction.</p>

<p>During a transaction, a registry operation is part of the transaction if the system call that performs the operation meets either of the following conditions:</p>

<p>The call specifies, as an input parameter, the transaction handle. For example, calls to <b>ZwCreateKeyTransacted</b> and <b>ZwOpenKeyTransacted</b> can associate one or more handles to registry keys with the transaction. </p>

<p>The call specifies, as an input parameter, a registry key handle that was obtained by a call to <b>ZwCreateKeyTransacted</b> or <b>ZwOpenKeyTransacted</b> to which the transaction handle was supplied. For example, a call to the <a href="..\wdm\nf-wdm-zwsetvaluekey.md">ZwSetValueKey</a> routine can use a key handle that was obtained in this way to set the value of a registry key as part of a transaction. </p>

<p>For more information about kernel-mode transactions, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565408">Using Kernel Transaction Manager</a>.</p>

<p>The security descriptor in the object attributes determines whether the access rights that are specified by the <i>DesiredAccess</i> parameter are granted on later calls to routines, such as <b>ZwOpenKeyTransacted</b> that access the key, or to routines, such as <b>ZwCreateKeyTransacted,</b> that create subkeys of the key.</p>

<p>If the kernel-mode caller is not running in a system thread context, it must ensure that any handles it creates are kernel handles. Otherwise, the handle can be accessed by the process in whose context the driver is running. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff557758">Object Handles</a>.</p>

<p>For more information about how to work with registry keys in kernel mode, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565537">Using the Registry in a Driver</a>. </p>

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
<p>Available in Windows Vista and later versions of Windows. </p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>
</dt>
<dt>
<a href="..\wudfwdm\nf-wudfwdm-initializeobjectattributes.md">InitializeObjectAttributes</a>
</dt>
<dt>
<a href="..\d3dkmthk\ns-d3dkmthk--object-attributes.md">OBJECT_ATTRIBUTES</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-obopenobjectbypointer.md">ObOpenObjectByPointer</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwclose.md">ZwClose</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwcommittransaction.md">ZwCommitTransaction</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwcreatekey.md">ZwCreateKey</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwcreatetransaction.md">ZwCreateTransaction</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwopenkeytransacted.md">ZwOpenKeyTransacted</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwrollbacktransaction.md">ZwRollbackTransaction</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwsetvaluekey.md">ZwSetValueKey</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwCreateKeyTransacted routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
