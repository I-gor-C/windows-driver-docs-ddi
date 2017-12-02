---
UID: NF.wdm.ZwCreateKey
title: ZwCreateKey
author: windows-driver-content
description: The ZwCreateKey routine creates a new registry key or opens an existing one.
old-location: kernel\zwcreatekey.htm
old-project: kernel
ms.assetid: 333f54e8-738e-4d1f-8fd7-93f282d9b9d8
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ZwCreateKey
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ZwCreateKey,NtCreateKey
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlZwPassive, PowerIrpDDis, ZwRegistryCreate, ZwRegistryOpen, HwStorPortProhibitedDDIs, ZwRegistryCreate(storport)
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

# ZwCreateKey function



## -description
<p>The <b>ZwCreateKey</b> routine creates a new registry key or opens an existing one.</p>


## -syntax

````
NTSTATUS ZwCreateKey(
  _Out_      PHANDLE            KeyHandle,
  _In_       ACCESS_MASK        DesiredAccess,
  _In_       POBJECT_ATTRIBUTES ObjectAttributes,
  _Reserved_ ULONG              TitleIndex,
  _In_opt_   PUNICODE_STRING    Class,
  _In_       ULONG              CreateOptions,
  _Out_opt_  PULONG             Disposition
);
````


## -parameters
<dl>

### -param KeyHandle [out]

<dd>
<p>Pointer to a HANDLE variable that receives a handle to the key.</p>
</dd>

### -param DesiredAccess [in]

<dd>
<p>Specifies an <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a> value that determines the requested access to the object. In addition to the access rights that are defined for all types of objects (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>), the caller can specify one or more of the following access rights, which are specific to object directories:</p>
<table>
<tr>
<th><i>DesiredAccess </i>flag</th>
<th>Allows caller to do this</th>
</tr>
<tr>
<td>
<p>KEY_QUERY_VALUE</p>
</td>
<td>
<p>Read key values.</p>
</td>
</tr>
<tr>
<td>
<p>KEY_SET_VALUE</p>
</td>
<td>
<p>Write key values.</p>
</td>
</tr>
<tr>
<td>
<p>KEY_CREATE_SUB_KEY</p>
</td>
<td>
<p>Create subkeys for the key.</p>
</td>
</tr>
<tr>
<td>
<p>KEY_ENUMERATE_SUB_KEYS</p>
</td>
<td>
<p>Read the key's subkeys.</p>
</td>
</tr>
<tr>
<td>
<p>KEY_CREATE_LINK</p>
</td>
<td>
<p>Create a symbolic link to the key. This flag is not used by device and intermediate drivers.</p>
</td>
</tr>
<tr>
<td>
<p>KEY_NOTIFY</p>
</td>
<td>
<p>Ask to receive notification when the name, value, or attributes of the key change. For more information, see <a href="..\ntifs\nf-ntifs-zwnotifychangekey.md">ZwNotifyChangeKey</a>.</p>
</td>
</tr>
</table>
<p> </p>
<p>The caller can also specify one of the following constants, which combines several ACCESS_MASK flags.</p>
<table>
<tr>
<th>Constant</th>
<th>Consists of these ACCESS_MASK flags</th>
</tr>
<tr>
<td>
<p>KEY_READ</p>
</td>
<td>
<p>STANDARD_RIGHTS_READ, KEY_QUERY_VALUE, KEY_ENUMERATE_SUB_KEYS, and KEY_NOTIFY</p>
</td>
</tr>
<tr>
<td>
<p>KEY_WRITE</p>
</td>
<td>
<p>STANDARD_RIGHTS_WRITE, KEY_SET_VALUE, and KEY_CREATE_SUBKEY</p>
</td>
</tr>
<tr>
<td>
<p>KEY_EXECUTE</p>
</td>
<td>
<p>Same as KEY_READ.</p>
</td>
</tr>
<tr>
<td>
<p>KEY_ALL_ACCESS</p>
</td>
<td>
<p>STANDARD_RIGHTS_ALL, KEY_QUERY_VALUE, KEY_SET_VALUE, KEY_CREATE_SUB_KEY, KEY_ENUMERATE_SUB_KEYS, KEY_NOTIFY, and KEY_CREATE_LINK</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param ObjectAttributes [in]

<dd>
<p>Pointer to an <a href="..\d3dkmthk\ns-d3dkmthk--object-attributes.md">OBJECT_ATTRIBUTES</a> structure that specifies the object name and other attributes. Use <a href="..\wudfwdm\nf-wudfwdm-initializeobjectattributes.md">InitializeObjectAttributes</a> to initialize this structure. If the caller is not running in a system thread context, it must set the OBJ_KERNEL_HANDLE attribute when it calls <b>InitializeObjectAttributes</b>. </p>
</dd>

### -param TitleIndex 

<dd>
<p>Device and intermediate drivers set this parameter to zero. </p>
</dd>

### -param Class [in, optional]

<dd>
<p>Pointer to a Unicode string that contains the key's object class. This information is used by the configuration manager. </p>
</dd>

### -param CreateOptions [in]

<dd>
<p>Specifies the options to apply when creating or opening a key, specified as a compatible combination of the following flags.</p>
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
<p>Key is not preserved when the system is rebooted.</p>
</td>
</tr>
<tr>
<td>
<p>REG_OPTION_NON_VOLATILE</p>
</td>
<td>
<p>Key is preserved when the system is rebooted.</p>
</td>
</tr>
<tr>
<td>
<p>REG_OPTION_CREATE_LINK</p>
</td>
<td>
<p>The newly created key is a symbolic link. This flag is not used by device and intermediate drivers.</p>
</td>
</tr>
<tr>
<td>
<p>REG_OPTION_BACKUP_RESTORE</p>
</td>
<td>
<p>Key should be created or opened with special privileges that allow backup and restore operations. This flag is not used by device and intermediate drivers.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param Disposition [out, optional]

<dd>
<p>Pointer to a variable that receives a value indicating whether a new key was created or an existing one opened.</p>
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
</dd>
</dl>

## -returns
<p><b>ZwCreateKey</b> returns STATUS_SUCCESS on success, or the appropriate NTSTATUS error code on failure.</p>

## -remarks
<p><b>ZwCreateKey</b> supplies a handle that the caller can use to manipulate a registry key. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565537">Using the Registry in a Driver</a>.</p>

<p>Once the handle pointed to by <i>KeyHandle</i> is no longer in use, the driver must call <a href="..\wdm\nf-wdm-zwclose.md">ZwClose</a> to close it.</p>

<p>There are two alternate ways to specify the name of the file to be created or opened with <b>ZwCreateKey</b>:</p>

<p>As a fully qualified pathname, supplied in the <b>ObjectName</b> member of the input <i>ObjectAttributes</i>. The pathnames of registry keys begin with <b>\Registry</b>.</p>

<p>As pathname relative to another registry key, represented by the handle in the <b>RootDirectory</b> member of the input <i>ObjectAttributes</i>. </p>

<p>If the key specified by <i>ObjectAttributes</i> does not exist, the routine attempts to create the key. For this attempt to succeed, the new key must be a direct subkey of the key that is referred to by <b>RootDirectory</b>, and the key that <b>RootDirectory</b> refers to must have been opened for KEY_CREATE_SUB_KEY access.</p>

<p>If the specified key already exists, it is opened and its value is not affected in any way.</p>

<p>The security attributes specified by <i>ObjectAttributes</i> when a key is created determine whether the specified <i>DesiredAccess</i> is granted on subsequent calls to <b>ZwCreateKey</b> and <a href="..\wdm\nf-wdm-zwopenkey.md">ZwOpenKey</a>.</p>

<p>If the caller is not running in a system thread context, it must ensure that any handles it creates are private handles. Otherwise, the handle can be accessed by the process in whose context the driver is running. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff557758">Object Handles</a>.</p>

<p>For more information about working with registry keys, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565537">Using the Registry in a Driver</a>.</p>

<p>The <b>NtCreateKey</b> routine in the Windows kernel is not directly accessible to kernel-mode drivers. </p>

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
<a href="devtest.wdm_irqlzwpassive">IrqlZwPassive</a>, <a href="devtest.wdm_powerirpddis">PowerIrpDDis</a>, <a href="devtest.wdm_zwregistrycreate">ZwRegistryCreate</a>, <a href="devtest.wdm_zwregistryopen">ZwRegistryOpen</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>, <a href="devtest.storport_zwregistrycreate">ZwRegistryCreate(storport)</a>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwclose.md">ZwClose</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwdeletekey.md">ZwDeleteKey</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwenumeratekey.md">ZwEnumerateKey</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwenumeratevaluekey.md">ZwEnumerateValueKey</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwflushkey.md">ZwFlushKey</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-zwnotifychangekey.md">ZwNotifyChangeKey</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwopenkey.md">ZwOpenKey</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwqueryvaluekey.md">ZwQueryValueKey</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwsetvaluekey.md">ZwSetValueKey</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwCreateKey routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
