---
UID: NF.wdm.RtlWriteRegistryValue
title: RtlWriteRegistryValue
author: windows-driver-content
description: The RtlWriteRegistryValue routine writes caller-supplied data into the registry along the specified relative path at the given value name.
old-location: kernel\rtlwriteregistryvalue.htm
old-project: kernel
ms.assetid: 97bcd205-ffc0-4645-87d4-659651ed579a
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: RtlWriteRegistryValue
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
req.alt-api: RtlWriteRegistryValue
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

# RtlWriteRegistryValue function



## -description
<p>The <b>RtlWriteRegistryValue</b> routine writes caller-supplied data into the registry along the specified relative path at the given value name.</p>


## -syntax

````
NTSTATUS RtlWriteRegistryValue(
  _In_     ULONG  RelativeTo,
  _In_     PCWSTR Path,
  _In_     PCWSTR ValueName,
  _In_     ULONG  ValueType,
  _In_opt_ PVOID  ValueData,
  _In_     ULONG  ValueLength
);
````


## -parameters
<dl>

### -param <i>RelativeTo</i> [in]

<dd>
<p>Specifies whether <i>Path</i> is an absolute registry path or is relative to a predefined path as one of the following.</p>
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
<tr>
<td>
<p>RTL_REGISTRY_OPTIONAL</p>
</td>
<td>
<p>Specifies that the key referenced by this parameter and the <i>Path</i> parameter are optional.</p>
</td>
</tr>
<tr>
<td>
<p>RTL_REGISTRY_HANDLE</p>
</td>
<td>
<p>Specifies that the <i>Path</i> parameter is actually a registry handle to use. This value is optional.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>Path</i> [in]

<dd>
<p>Pointer to either an absolute registry path or a path relative to the known location specified by the <i>RelativeTo</i> parameter. If the RTL_REGISTRY_HANDLE flag is specified, this parameter is a registry handle for an already opened key to be used directly.</p>
</dd>

### -param <i>ValueName</i> [in]

<dd>
<p>Pointer to the name of a subkey or value entry to be written into the registry.</p>
</dd>

### -param <i>ValueType</i> [in]

<dd>
<p>Specifies a REG_<i>XXX</i> value that determines the type of the <i>ValueName</i> parameter. For a list of the possible values, see the <i>Type</i> parameter of <a href="https://msdn.microsoft.com/library/windows/hardware/ff567109">ZwSetValueKey</a>.</p>
</dd>

### -param <i>ValueData</i> [in, optional]

<dd>
<p>Pointer to the name of a subkey or values for its value entries (or both) to be written into the registry.</p>
</dd>

### -param <i>ValueLength</i> [in]

<dd>
<p>Specifies the number of bytes of <i>ValueData</i> to be written into the registry.</p>
</dd>
</dl>

## -returns
<p><b>RtlWriteRegistryValue</b> returns the status of the operation, either STATUS_SUCCESS or an error status.</p>

## -remarks
<p>If the specified key does not exist, the routine attempts to create the key. For this attempt to succeed, the new key must be a direct subkey of the key that is referred to by the <i>Path</i> parameter, and the key that <i>Path</i> refers to must have been opened for KEY_CREATE_SUB_KEY access.</p>

<p>If the specified key does not exist, the routine attempts to create the key. For this attempt to succeed, the new key must be a direct subkey of the key that is referred to by the <i>Path</i> parameter, and the key that <i>Path</i> refers to must have been opened for KEY_CREATE_SUB_KEY access.</p>

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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561754">RtlCheckRegistryKey</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561822">RtlCreateRegistryKey</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561829">RtlDeleteRegistryValue</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562046">RtlQueryRegistryValues</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566425">ZwCreateKey</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567014">ZwOpenKey</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567109">ZwSetValueKey</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlWriteRegistryValue routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
