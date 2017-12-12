---
UID: NF.wdm.ZwDeleteValueKey
title: ZwDeleteValueKey function
author: windows-driver-content
description: The ZwDeleteValueKey routine deletes a value entry matching a name from an open key in the registry. If no such entry exists, an error is returned.
old-location: kernel\zwdeletevaluekey.htm
old-project: kernel
ms.assetid: e7fc9290-8f24-4b9f-822a-0bdce50dafb9
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: ZwDeleteValueKey
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h, Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ZwDeleteValueKey,NtDeleteValueKey
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

# ZwDeleteValueKey function



## -description
The <b>ZwDeleteValueKey</b> routine deletes a value entry matching a name from an open key in the registry. If no such entry exists, an error is returned. 



## -syntax

````
NTSTATUS ZwDeleteValueKey(
  _In_ HANDLE          KeyHandle,
  _In_ PUNICODE_STRING ValueName
);
````


## -parameters

### -param KeyHandle [in]

The handle to the registry key containing the value entry of interest. This key must have been opened with KEY_SET_VALUE set for the desired access. This handle is created by a successful call to <a href="kernel.zwcreatekey">ZwCreateKey</a> or <a href="kernel.zwopenkey">ZwOpenKey</a>. 


### -param ValueName [in]

Pointer to a <a href="kernel.unicode_string">UNICODE_STRING</a> structure that contains the name of the value entry to delete. This parameter can be an empty string if the value entry has no name. 


## -returns
<b>ZwDeleteValueKey</b> returns STATUS_SUCCESS or an appropriate error status representing the final completion status of the operation. Possible error status codes include the following: 
<dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl>The <i>KeyHandle</i> handle does not have the KEY_SET_VALUE access. 
<dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl>Additional resources required by this function were not available. 
<dl>
<dt><b>STATUS_INVALID_HANDLE</b></dt>
</dl>The specified <i>KeyHandle</i> parameter was a <b>NULL</b> pointer or not a valid pointer to an open registry key. 
<dl>
<dt><b>STATUS_OBJECT_NAME_NOT_FOUND</b></dt>
</dl>The <i>ValueName</i> registry key entry was not found. 

 


## -remarks
The <i>KeyHandle</i> passed to <b>ZwDeleteValueKey</b> must have been opened for delete access to succeed. The <i>DesiredAccess</i> values of KEY_SET_VALUE, KEY_WRITE, and KEY_ALL_ACCESS include the KEY_SET_VALUE access mask required for delete access. For a description of possible values for <i>DesiredAccess</i>, see <a href="kernel.zwcreatekey">ZwCreateKey</a>.

If callback functions are registered for this registry key, then these callback functions will be called.

Device drivers should not attempt to call <b>ZwDeleteValueKey</b> directly to delete value entries in a subkey of the <b>\Registry..\ResourceMap</b> key. Only the system can write or delete value entries in the <b>\Registry..\HardwareDescription</b> tree.

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
Available starting with Windows 2000.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, Ntifs.h, or Fltkernel.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
<dt>
<a href="kernel.zwcreatekey">ZwCreateKey</a>
</dt>
<dt>
<a href="kernel.zwdeletekey">ZwDeleteKey</a>
</dt>
<dt>
<a href="kernel.zwenumeratevaluekey">ZwEnumerateValueKey</a>
</dt>
<dt>
<a href="kernel.zwopenkey">ZwOpenKey</a>
</dt>
<dt>
<a href="kernel.zwqueryvaluekey">ZwQueryValueKey</a>
</dt>
<dt>
<a href="kernel.zwsetvaluekey">ZwSetValueKey</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwDeleteValueKey routine%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

