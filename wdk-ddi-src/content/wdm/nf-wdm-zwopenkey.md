---
UID: NF.wdm.ZwOpenKey
title: ZwOpenKey
author: windows-driver-content
description: The ZwOpenKey routine opens an existing registry key.
old-location: kernel\zwopenkey.htm
old-project: kernel
ms.assetid: e92f0297-8bfc-496d-a00b-e7b5711c7856
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ZwOpenKey
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
req.alt-api: ZwOpenKey
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlZwPassive, PowerIrpDDis, ZwRegistryOpen, HwStorPortProhibitedDDIs, ZwRegistryCreate, ZwRegistryOpen(storport)
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

# ZwOpenKey function



## -description
<p>The <b>ZwOpenKey</b> routine opens an existing registry key. </p>


## -syntax

````
NTSTATUS ZwOpenKey(
  _Out_ PHANDLE            KeyHandle,
  _In_  ACCESS_MASK        DesiredAccess,
  _In_  POBJECT_ATTRIBUTES ObjectAttributes
);
````


## -parameters
<dl>

### -param <i>KeyHandle</i> [out]

<dd>
<p>Pointer to the HANDLE variable that receives the handle to the key.</p>
</dd>

### -param <i>DesiredAccess</i> [in]

<dd>
<p>Specifies an <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a> value that determines the requested access to the object. For more information, see the <i>DesiredAccess</i> parameter of <a href="..\wdm\nf-wdm-zwcreatekey.md">ZwCreateKey</a>. </p>
</dd>

### -param <i>ObjectAttributes</i> [in]

<dd>
<p>Pointer to an <a href="..\d3dkmthk\ns-d3dkmthk--object-attributes.md">OBJECT_ATTRIBUTES</a> structure that specifies the object name and other attributes. Use <a href="..\wudfwdm\nf-wudfwdm-initializeobjectattributes.md">InitializeObjectAttributes</a> to initialize this structure. If the caller is not running in a system thread context, it must set the OBJ_KERNEL_HANDLE attribute when it calls <b>InitializeObjectAttributes</b>. </p>
</dd>
</dl>

## -returns
<p><b>ZwOpenKey</b> returns STATUS_SUCCESS if the given key was opened. Otherwise, it can return an error status, including the following:</p><dl>
<dt><b>STATUS_INVALID_HANDLE</b></dt>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl>

## -remarks
<p><b>ZwOpenKey</b> supplies a handle that the caller can use to manipulate a registry key. The routine provides a subset of the functionality of <a href="..\wdm\nf-wdm-zwcreatekey.md">ZwCreateKey</a>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565537">Using the Registry in a Driver</a>.</p>

<p>If the specified key does not exist, <b>ZwOpenKey</b> returns an error status and does not return a key handle.</p>

<p>Once the handle pointed to by <i>KeyHandle</i> is no longer in use, the driver must call <a href="..\wdm\nf-wdm-zwclose.md">ZwClose</a> to close it.</p>

<p><b>ZwOpenKey</b> ignores the security information in the structure that the <i>ObjectAttributes</i> parameter points to.</p>

<p>If the caller is not running in a system thread context, it must ensure that any handles it creates are private handles. Otherwise, the handle can be accessed by the process in whose context the driver is running. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff557758">Object Handles</a>.</p>

<p>For more information about working with registry keys, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565537">Using the Registry in a Driver</a>.</p>

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
<a href="devtest.wdm_irqlzwpassive">IrqlZwPassive</a>, <a href="devtest.wdm_powerirpddis">PowerIrpDDis</a>, <a href="devtest.wdm_zwregistryopen">ZwRegistryOpen</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>, <a href="devtest.storport_zwregistrycreate">ZwRegistryCreate</a>, <a href="devtest.storport_zwregistryopen">ZwRegistryOpen(storport)</a>
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
<a href="..\wdm\nf-wdm-zwcreatekey.md">ZwCreateKey</a>
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
<a href="..\wdm\nf-wdm-zwquerykey.md">ZwQueryKey</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwOpenKey routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
