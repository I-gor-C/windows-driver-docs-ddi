---
UID: NF.wdm.RtlCreateRegistryKey
title: RtlCreateRegistryKey
author: windows-driver-content
description: The RtlCreateRegistryKey routine adds a key object in the registry along a given relative path.
old-location: kernel\rtlcreateregistrykey.htm
old-project: kernel
ms.assetid: 2214acc8-b24a-4db4-9ce3-f639291428f2
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlCreateRegistryKey
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 2000 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlCreateRegistryKey
req.alt-loc: NtosKrnl.exe
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

# RtlCreateRegistryKey function



## -description
<p>The <b>RtlCreateRegistryKey</b> routine adds a key object in the registry along a given relative path.</p>


## -syntax

````
NTSTATUS RtlCreateRegistryKey(
  _In_ ULONG RelativeTo,
  _In_ PWSTR Path
);
````


## -parameters
<dl>

### -param RelativeTo [in]

<dd>
<p>Specifies whether <i>Path</i> is an absolute registry path or is relative to a predefined key path as one of the following.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>RTL_REGISTRY_ABSOLUTE</p>
</td>
<td>
<p>Path is an absolute registry path.</p>
</td>
</tr>
<tr>
<td>
<p>RTL_REGISTRY_SERVICES</p>
</td>
<td>
<p>Path is relative to <b>\Registry\Machine\System\CurrentControlSet\Services</b>.</p>
</td>
</tr>
<tr>
<td>
<p>RTL_REGISTRY_CONTROL</p>
</td>
<td>
<p>Path is relative to <b>\Registry\Machine\System\CurrentControlSet\Control</b>.</p>
</td>
</tr>
<tr>
<td>
<p>RTL_REGISTRY_WINDOWS_NT</p>
</td>
<td>
<p>Path is relative to <b>\Registry\Machine\Software\Microsoft\Windows NT\CurrentVersion</b>.</p>
</td>
</tr>
<tr>
<td>
<p>RTL_REGISTRY_DEVICEMAP</p>
</td>
<td>
<p>Path is relative to <b>\Registry\Machine\Hardware\DeviceMap</b>.</p>
</td>
</tr>
<tr>
<td>
<p>RTL_REGISTRY_USER</p>
</td>
<td>
<p>Path is relative to <b>\Registry\User\CurrentUser</b>. (For a system process, this is <b>\Users\.Default</b>.)</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param Path [in]

<dd>
<p>Specifies the registry path according to the <i>RelativeTo</i> value. </p>
</dd>
</dl>

## -returns
<p><b>RtlCreateRegistryKey</b> returns STATUS_SUCCESS if the key is created. </p>

## -remarks
<p><b>RtlCreateRegistryKey</b> creates only the keys that you specify. It does not create missing keys in the path to the specified key. If any keys in the path are missing, the call will fail. To ensure that all keys in the path exist, you must call <b>RtlCreateRegistryKey</b> once for each key in the path. </p>

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
<p>Available in Windows 2000 and later versions of Windows. </p>
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
<a href="..\wdm\nf-wdm-rtlcheckregistrykey.md">RtlCheckRegistryKey</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-rtldeleteregistryvalue.md">RtlDeleteRegistryValue</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-rtlqueryregistryvalues.md">RtlQueryRegistryValues</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-rtlwriteregistryvalue.md">RtlWriteRegistryValue</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwenumeratekey.md">ZwEnumerateKey</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwopenkey.md">ZwOpenKey</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlCreateRegistryKey routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
