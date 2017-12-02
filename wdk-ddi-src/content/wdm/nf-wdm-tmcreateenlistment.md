---
UID: NF.wdm.TmCreateEnlistment
title: TmCreateEnlistment
author: windows-driver-content
description: The TmCreateEnlistment routine creates a new enlistment object for a transaction.
old-location: kernel\tmcreateenlistment.htm
old-project: kernel
ms.assetid: 84fcbc30-993c-430b-a8b9-aefca44e478e
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: TmCreateEnlistment
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
req.alt-api: TmCreateEnlistment
req.alt-loc: NtosKrnl.exe,Ext-MS-Win-ntos-tm-l1-1-0.dll,tm.sys
req.ddi-compliance: 
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

# TmCreateEnlistment function



## -description
<p>The <b>TmCreateEnlistment</b> routine creates a new <a href="https://msdn.microsoft.com/80e61475-4bb7-4eaa-b9f1-ff95eac9bc77">enlistment object</a> for a transaction.</p>


## -syntax

````
NTSTATUS TmCreateEnlistment(
  _Out_    PHANDLE            EnlistmentHandle,
  _In_     KPROCESSOR_MODE    PreviousMode,
  _In_     ACCESS_MASK        DesiredAccess,
  _In_     POBJECT_ATTRIBUTES ObjectAttributes,
  _In_     PRKRESOURCEMANAGER ResourceManager,
  _In_     PKTRANSACTION      Transaction,
  _In_opt_ ULONG              CreateOptions,
  _In_     NOTIFICATION_MASK  NotificationMask,
  _In_opt_ PVOID              EnlistmentKey
);
````


## -parameters
<dl>

### -param EnlistmentHandle [out]

<dd>
<p>A pointer to a caller-allocated variable that receives a handle to the new enlistment object if the call to <b>TmCreateEnlistment</b> succeeds.</p>
</dd>

### -param PreviousMode [in]

<dd>
<p>The processor mode of the process that will use the enlistment handle to access the enlistment object. This value must be either <b>UserMode</b> or <b>KernelMode</b>.</p>
</dd>

### -param DesiredAccess [in]

<dd>
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a> value that specifies the caller's requested access to the enlistment object. For more information about this parameter, see the description of the <i>DesiredAccess</i> parameter for <a href="..\wdm\nf-wdm-zwcreateenlistment.md">ZwCreateEnlistment</a>.</p>
</dd>

### -param ObjectAttributes [in]

<dd>
<p>A pointer to an <a href="..\d3dkmthk\ns-d3dkmthk--object-attributes.md">OBJECT_ATTRIBUTES</a> structure that specifies the object name and other attributes. Use the <a href="..\wudfwdm\nf-wudfwdm-initializeobjectattributes.md">InitializeObjectAttributes</a> routine to initialize this structure. If the caller is not running in a system thread context, it must set the OBJ_KERNEL_HANDLE attribute when it calls <b>InitializeObjectAttributes</b>. This parameter is optional and can be <b>NULL</b>. </p>
</dd>

### -param ResourceManager [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/b44f2035-ee9f-453b-b12d-89ca36a8b280">resource manager object</a>. To obtain this pointer, your component must call <a href="..\wdm\nf-wdm-obreferenceobjectbyhandle.md">ObReferenceObjectByHandle</a> and supply the object handle that a previous call to <a href="..\wdm\nf-wdm-zwcreateresourcemanager.md">ZwCreateResourceManager</a> or <a href="..\wdm\nf-wdm-zwopenresourcemanager.md">ZwOpenResourceManager</a> provided.</p>
</dd>

### -param Transaction [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/124105bd-70be-49b1-8ea4-af6ba1f3cf16">transaction object</a>. To obtain this pointer, your component must call <a href="..\wdm\nf-wdm-obreferenceobjectbyhandle.md">ObReferenceObjectByHandle</a> and supply the object handle that a previous call to <a href="..\wdm\nf-wdm-zwcreatetransaction.md">ZwCreateTransaction</a> or <a href="..\wdm\nf-wdm-zwopentransaction.md">ZwOpenTransaction</a> provided. KTM adds this transaction to the list of transactions that the calling resource manager is handling.</p>
</dd>

### -param CreateOptions [in, optional]

<dd>
<p>Enlistment option flags. The following table contains the only available flag. </p>
<table>
<tr>
<th><i>CreateOptions</i> flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>ENLISTMENT_SUPERIOR</p>
</td>
<td>
<p>The caller is enlisting as a <a href="https://msdn.microsoft.com/6f6bf61a-fe53-47b5-9559-f76334969af8">superior transaction manager</a> for the specified transaction.</p>
</td>
</tr>
</table>
<p> </p>
<p>This parameter is optional and can be zero. </p>
</dd>

### -param NotificationMask [in]

<dd>
<p>A bitwise OR of the TRANSACTION_NOTIFY_<i>XXX</i> values that are defined in Ktmtypes.h. This mask value specifies the types of <a href="https://msdn.microsoft.com/library/windows/hardware/ff564815">transaction notifications</a> that KTM sends to the caller.</p>
</dd>

### -param EnlistmentKey [in, optional]

<dd>
<p>A pointer to caller-defined information that uniquely identifies the enlistment. The resource manager receives this pointer when it calls <a href="..\wdm\nf-wdm-zwgetnotificationresourcemanager.md">ZwGetNotificationResourceManager</a> or when KTM calls the <a href="kernel.resourcemanagernotification">ResourceManagerNotification</a> callback routine. The resource manager can maintain a reference count for this key by calling <a href="..\wdm\nf-wdm-tmreferenceenlistmentkey.md">TmReferenceEnlistmentKey</a> and <a href="..\wdm\nf-wdm-tmdereferenceenlistmentkey.md">TmDereferenceEnlistmentKey</a>. This parameter is optional and can be <b>NULL</b>. </p>
</dd>
</dl>

## -returns
<p><b>TmCreateEnlistment</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this routine might return one of the following values: </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The value of the <i>CreateOptions</i> or <i>NotificationMask</i> parameter is invalid, or KTM could not find the transaction that the <i>Transaction</i> parameter specifies.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>A memory allocation failed.</p><dl>
<dt><b>STATUS_TRANSACTIONMANAGER_NOT_ONLINE</b></dt>
</dl><p>The enlistment failed because KTM or the resource manager is not in an operational state.</p><dl>
<dt><b>STATUS_TRANSACTION_NOT_ACTIVE</b></dt>
</dl><p>The enlistment failed because the transaction that the <i>Transaction</i> parameter specifies is not active.</p><dl>
<dt><b>STATUS_TRANSACTION_SUPERIOR_EXISTS</b></dt>
</dl><p>The caller tried to register as a <a href="https://msdn.microsoft.com/6f6bf61a-fe53-47b5-9559-f76334969af8">superior transaction manager</a> but a superior enlistment already exists.</p><dl>
<dt><b>STATUS_TM_VOLATILE</b></dt>
</dl><p>The caller is trying to register as a superior transaction manager, but the caller's resource manager object is <a href="kernel.creating_a_resource_manager#kernel.creating_a_volatile_resource_manager#kernel.creating_a_volatile_resource_manager">volatile</a> while the associated transaction manager object is not volatile.</p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p>The value of the <i>DesiredAccess</i> parameter is invalid.</p>

<p> </p>

<p>The routine might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

## -remarks
<p>The <b>TmCreateEnlistment</b> routine is a pointer-based version of the <a href="..\wdm\nf-wdm-zwcreateenlistment.md">ZwCreateEnlistment</a> routine.</p>

<p>For information about when to use KTM's <b>Tm<i>Xxx</i></b> routines instead of <b>Zw<i>Xxx</i></b> routines, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565567">Using TmXxx Routines</a>.</p>

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
<a href="..\wdm\nf-wdm-obreferenceobjectbyhandle.md">ObReferenceObjectByHandle</a>
</dt>
<dt>
<a href="kernel.resourcemanagernotification">ResourceManagerNotification</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwcreateenlistment.md">ZwCreateEnlistment</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwcreateresourcemanager.md">ZwCreateResourceManager</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwcreatetransaction.md">ZwCreateTransaction</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwgetnotificationresourcemanager.md">ZwGetNotificationResourceManager</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwopenresourcemanager.md">ZwOpenResourceManager</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwopentransaction.md">ZwOpenTransaction</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20TmCreateEnlistment routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
