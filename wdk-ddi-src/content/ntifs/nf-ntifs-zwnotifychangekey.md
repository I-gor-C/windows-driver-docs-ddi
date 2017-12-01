---
UID: NF.ntifs.ZwNotifyChangeKey
title: ZwNotifyChangeKey
author: windows-driver-content
description: The ZwNotifyChangeKey routine allows a driver to request notification when a registry key changes.
old-location: kernel\zwnotifychangekey.htm
old-project: kernel
ms.assetid: 660c04b0-499b-40e7-94c2-5cb457e93f00
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ZwNotifyChangeKey
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ZwNotifyChangeKey,NtNotifyChangeKey
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

# ZwNotifyChangeKey function



## -description
<p>The <b>ZwNotifyChangeKey</b> routine allows a driver to request notification when a registry key changes.</p>


## -syntax

````
NTSTATUS ZwNotifyChangeKey(
  _In_      HANDLE           KeyHandle,
  _In_opt_  HANDLE           Event,
  _In_opt_  PIO_APC_ROUTINE  ApcRoutine,
  _In_opt_  PVOID            ApcContext,
  _Out_     PIO_STATUS_BLOCK IoStatusBlock,
  _In_      ULONG            CompletionFilter,
  _In_      BOOLEAN          WatchTree,
  _Out_opt_ PVOID            Buffer,
  _In_      ULONG            BufferSize,
  _In_      BOOLEAN          Asynchronous
);
````


## -parameters
<dl>

### -param <i>KeyHandle</i> [in]

<dd>
<p>Handle to the key to register a notification routine for. This handle is created by a successful call to <a href="..\wdm\nf-wdm-zwcreatekey.md">ZwCreateKey</a> or <a href="..\wdm\nf-wdm-zwopenkey.md">ZwOpenKey</a>. The caller must have specified KEY_NOTIFY access.</p>
</dd>

### -param <i>Event</i> [in, optional]

<dd>
<p>Handle to a caller-created event. If not <b>NULL</b>, the caller is placed into a wait state until the operation succeeds, at which time the event is set to the Signaled state. </p>
</dd>

### -param <i>ApcRoutine</i> [in, optional]

<dd>
<p> For a user-mode call, this parameter points to a caller-supplied APC routine that is run after the operation is completed. This parameter is optional and can be <b>NULL</b>.</p>
<p>  For a kernel-mode call, this parameter must be <b>NULL</b>.</p>
</dd>

### -param <i>ApcContext</i> [in, optional]

<dd>
<p>The meaning of this parameter depends on whether the routine is called from kernel mode or from user mode. For a kernel-mode call, set this parameter to one of the following <a href="..\wdm\ne-wdm--work-queue-type.md">WORK_QUEUE_TYPE</a> enumeration values:</p>
<ul>
<li>
<p>CriticalWorkQueue</p>
</li>
<li>
<p>DelayedWorkQueue</p>
</li>
</ul>
<p>The parameter value must be cast to type PVOID. For a user-mode call, this parameter points to a caller-specified context for the APC routine. This value is passed to the APC routine when it is run. </p>
</dd>

### -param <i>IoStatusBlock</i> [out]

<dd>
<p>Pointer to an <a href="..\wdm\ns-wdm--io-status-block.md">IO_STATUS_BLOCK</a> structure that contains the final status and information about the operation. For successful calls that return data, the number of bytes written to <i>Buffer</i> is supplied in <i>IoStatusBlock</i>-&gt;<b>Information</b>.</p>
</dd>

### -param <i>CompletionFilter</i> [in]

<dd>
<p>Bitmask of operations that cause the driver to be notified. Specify one or more of the following flags:</p>
<p></p>
<dl>

### -param <a id="REG_NOTIFY_CHANGE_NAME"></a><a id="reg_notify_change_name"></a>REG_NOTIFY_CHANGE_NAME

<dd>
<p>Notify the caller if a subkey is added or deleted.</p>
</dd>

### -param <a id="REG_NOTIFY_CHANGE_ATTRIBUTES"></a><a id="reg_notify_change_attributes"></a>REG_NOTIFY_CHANGE_ATTRIBUTES

<dd>
<p>Notify the caller of changes to the attributes of the key, such as the security descriptor information.</p>
</dd>

### -param <a id="REG_NOTIFY_CHANGE_LAST_SET"></a><a id="reg_notify_change_last_set"></a>REG_NOTIFY_CHANGE_LAST_SET

<dd>
<p>Notify the caller of changes to a value of the key. This can include adding or deleting a value, or changing an existing value. (The caller receives no notification if the new value written to the key matches the previous value of the key.)</p>
</dd>

### -param <a id="REG_NOTIFY_CHANGE_SECURITY"></a><a id="reg_notify_change_security"></a>REG_NOTIFY_CHANGE_SECURITY

<dd>
<p>Notify the caller of changes to the security descriptor of the key.</p>
</dd>
</dl>
</dd>

### -param <i>WatchTree</i> [in]

<dd>
<p>If <b>TRUE</b>, the driver is notified about changes to all subkeys of the specified key. If <b>FALSE</b>, the driver is only notified for changes to the specified key.</p>
</dd>

### -param <i>Buffer</i> [out, optional]

<dd>
<p>Reserved. Specify <b>NULL</b>.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>Reserved. Specify zero.</p>
</dd>

### -param <i>Asynchronous</i> [in]

<dd>
<p>If <b>FALSE</b>, the routine does not return until the specified event occurs. If <b>TRUE</b>, the routine returns immediately. </p>
</dd>
</dl>

## -returns
<p>The <b>ZwNotifyChangeKey</b> routine returns STATUS_SUCCESS on success, or the appropriate NTSTATUS value otherwise. If the caller specifies <b>TRUE</b> for the <i>Asynchronous</i> parameter, and the event has not yet occurred, the routine returns STATUS_PENDING.</p>

## -remarks
<p>If the call to the <b>ZwNotifyChangeKey</b> function occurs in user mode, you should use the name "<b>NtNotifyChangeKey</b>" instead of "<b>ZwNotifyChangeKey</b>". </p>

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
<dt>Ntifs.h (include Ntifs.h)</dt>
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
<a href="..\wdm\ns-wdm--io-status-block.md">IO_STATUS_BLOCK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwcreatekey.md">ZwCreateKey</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwopenkey.md">ZwOpenKey</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--work-queue-item.md">WORK_QUEUE_ITEM</a>
</dt>
<dt>
<a href="..\wdm\ne-wdm--work-queue-type.md">WORK_QUEUE_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwNotifyChangeKey routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
