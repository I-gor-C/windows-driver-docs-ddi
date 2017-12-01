---
UID: NF.wdm.NtOpenTransaction
title: NtOpenTransaction
author: windows-driver-content
description: The ZwOpenTransaction routine obtains a handle to an existing transaction object.
old-location: kernel\zwopentransaction.htm
old-project: kernel
ms.assetid: 5ffa50af-24e6-4dab-81cc-6ac26356e9c6
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NtOpenTransaction
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
req.alt-api: ZwOpenTransaction,NtOpenTransaction
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

# NtOpenTransaction function



## -description
<p>The <b>ZwOpenTransaction</b> routine obtains a handle to an existing <a href="https://msdn.microsoft.com/124105bd-70be-49b1-8ea4-af6ba1f3cf16">transaction object</a>.</p>


## -syntax

````
NTSTATUS ZwOpenTransaction(
  _Out_    PHANDLE            TransactionHandle,
  _In_     ACCESS_MASK        DesiredAccess,
  _In_opt_ POBJECT_ATTRIBUTES ObjectAttributes,
  _In_     LPGUID             Uow,
  _In_opt_ HANDLE             TmHandle
);
````


## -parameters
<dl>

### -param <i>TransactionHandle</i> [out]

<dd>
<p>A pointer to a caller-allocated variable that receives a handle to the transaction object if <b>ZwOpenTransaction</b> returns STATUS_SUCCESS.</p>
</dd>

### -param <i>DesiredAccess</i> [in]

<dd>
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a> value that specifies the caller's requested access to the transaction object. For information about how to specify this parameter, see the <i>DesiredAccess</i> parameter of <a href="..\wdm\nf-wdm-zwcreatetransaction.md">ZwCreateTransaction</a>. </p>
</dd>

### -param <i>ObjectAttributes</i> [in, optional]

<dd>
<p>A pointer to an <a href="..\d3dkmthk\ns-d3dkmthk--object-attributes.md">OBJECT_ATTRIBUTES</a> structure that specifies the object's attributes. Use the <a href="..\wudfwdm\nf-wudfwdm-initializeobjectattributes.md">InitializeObjectAttributes</a> routine to initialize this structure, but specify only that routine's <i>InitializedAttributes</i> and <i>Attributes</i> parameters. If the caller is not running in a system thread context, it must set the OBJ_KERNEL_HANDLE flag in the <i>Attributes</i> parameter. The <i>ObjectAttributes</i> parameter is optional and can be <b>NULL</b>. </p>
</dd>

### -param <i>Uow</i> [in]

<dd>
<p>A pointer to a GUID that is a transaction object's <a href="https://msdn.microsoft.com/927a417b-35f5-49b8-85f3-7e6b1f5c0225">unit of work (UOW) identifier</a>. This GUID identifies the transaction object to open. </p>
</dd>

### -param <i>TmHandle</i> [in, optional]

<dd>
<p>A handle to a <a href="https://msdn.microsoft.com/af53cda4-e2ab-47df-9311-a4da2a2ee08d">transaction manager object</a>. If this parameter is not <b>NULL</b>, KTM searches only for transaction objects that belong to the specified transaction manager object. If this parameter is <b>NULL</b>, KTM searches all transaction objects.</p>
</dd>
</dl>

## -returns
<p><b>ZwCreateTransaction</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this routine might return one of the following values: </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The <i>DesiredAccess</i> or <i>Uow</i> parameter was zero.</p><dl>
<dt><b>STATUS_OBJECT_TYPE_MISMATCH</b></dt>
</dl><p>The specified handle is not a handle to a transaction object.</p><dl>
<dt><b>STATUS_INVALID_HANDLE</b></dt>
</dl><p>An object handle is invalid.</p><dl>
<dt><b>STATUS_TRANSACTION_NOT_FOUND</b></dt>
</dl><p>KTM could not find the transaction object.</p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p>The value of the <i>DesiredAccess</i> parameter is invalid.</p>

<p> </p>

<p>The routine might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

## -remarks
<p>Typically, a resource manager calls <b>ZwOpenTransaction</b> after it receives a transaction UOW from a transactional client that had previously called <a href="..\wdm\nf-wdm-zwcreatetransaction.md">ZwCreateTransaction</a>. </p>

<p>For more information about <b>ZwOpenTransaction</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff542865">Creating a Resource Manager</a>.</p>

<p><b>NtOpenTransaction</b> and <b>ZwOpenTransaction</b> are two versions of the same Windows Native System Services routine.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwcommittransaction.md">ZwCommitTransaction</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwcreatetransaction.md">ZwCreateTransaction</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwqueryinformationtransaction.md">ZwQueryInformationTransaction</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwrollbacktransaction.md">ZwRollbackTransaction</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwOpenTransaction routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
