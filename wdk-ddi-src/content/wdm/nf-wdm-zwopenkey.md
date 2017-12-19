---
UID: NF.wdm.ZwOpenKey
title: ZwOpenKey function
author: windows-driver-content
description: The ZwOpenKey routine opens an existing registry key.
old-location: kernel\zwopenkey.htm
old-project: kernel
ms.assetid: e92f0297-8bfc-496d-a00b-e7b5711c7856
ms.author: windowsdriverdev
ms.date: 12/15/2017
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
req.product: Windows 10 or later.
---

# ZwOpenKey function



## -description
The <b>ZwOpenKey</b> routine opens an existing registry key. 



## -syntax

````
NTSTATUS ZwOpenKey(
  _Out_ PHANDLE            KeyHandle,
  _In_  ACCESS_MASK        DesiredAccess,
  _In_  POBJECT_ATTRIBUTES ObjectAttributes
);
````


## -parameters

### -param KeyHandle [out]

Pointer to the HANDLE variable that receives the handle to the key.


### -param DesiredAccess [in]

Specifies an <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a> value that determines the requested access to the object. For more information, see the <i>DesiredAccess</i> parameter of <a href="kernel.zwcreatekey">ZwCreateKey</a>. 


### -param ObjectAttributes [in]

Pointer to an <a href="kernel.object_attributes">OBJECT_ATTRIBUTES</a> structure that specifies the object name and other attributes. Use <a href="kernel.initializeobjectattributes">InitializeObjectAttributes</a> to initialize this structure. If the caller is not running in a system thread context, it must set the OBJ_KERNEL_HANDLE attribute when it calls <b>InitializeObjectAttributes</b>. 


## -returns
<b>ZwOpenKey</b> returns STATUS_SUCCESS if the given key was opened. Otherwise, it can return an error status, including the following:
<dl>
<dt><b>STATUS_INVALID_HANDLE</b></dt>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl>

## -remarks
<b>ZwOpenKey</b> supplies a handle that the caller can use to manipulate a registry key. The routine provides a subset of the functionality of <a href="kernel.zwcreatekey">ZwCreateKey</a>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565537">Using the Registry in a Driver</a>.

If the specified key does not exist, <b>ZwOpenKey</b> returns an error status and does not return a key handle.

Once the handle pointed to by <i>KeyHandle</i> is no longer in use, the driver must call <a href="kernel.zwclose">ZwClose</a> to close it.

<b>ZwOpenKey</b> ignores the security information in the structure that the <i>ObjectAttributes</i> parameter points to.

If the caller is not running in a system thread context, it must ensure that any handles it creates are private handles. Otherwise, the handle can be accessed by the process in whose context the driver is running. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff557758">Object Handles</a>.

For more information about working with registry keys, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565537">Using the Registry in a Driver</a>.


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
Available starting with Windows 2000.

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
<a href="kernel.initializeobjectattributes">InitializeObjectAttributes</a>
</dt>
<dt>
<a href="kernel.zwcreatekey">ZwCreateKey</a>
</dt>
<dt>
<a href="kernel.zwdeletekey">ZwDeleteKey</a>
</dt>
<dt>
<a href="kernel.zwenumeratekey">ZwEnumerateKey</a>
</dt>
<dt>
<a href="kernel.zwenumeratevaluekey">ZwEnumerateValueKey</a>
</dt>
<dt>
<a href="kernel.zwflushkey">ZwFlushKey</a>
</dt>
<dt>
<a href="kernel.zwquerykey">ZwQueryKey</a>
</dt>
<dt>
<a href="kernel.zwqueryvaluekey">ZwQueryValueKey</a>
</dt>
<dt>
<a href="kernel.zwsetvaluekey">ZwSetValueKey</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwOpenKey routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

