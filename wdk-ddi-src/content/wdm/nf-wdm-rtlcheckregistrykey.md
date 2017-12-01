---
UID: NF.wdm.RtlCheckRegistryKey
title: RtlCheckRegistryKey
author: windows-driver-content
description: The RtlCheckRegistryKey routine checks for the existence of a given named key in the registry.
old-location: kernel\rtlcheckregistrykey.htm
old-project: kernel
ms.assetid: b752a764-1f7d-4768-9fa2-c8976560f840
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlCheckRegistryKey
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
req.alt-api: RtlCheckRegistryKey
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

# RtlCheckRegistryKey function



## -description
<p>The <b>RtlCheckRegistryKey</b> routine checks for the existence of a given named key in the registry.</p>


## -syntax

````
NTSTATUS RtlCheckRegistryKey(
  _In_ ULONG RelativeTo,
  _In_ PWSTR Path
);
````


## -parameters
<dl>

### -param <i>RelativeTo</i> [in]

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
<p>RTL_REGISTRY_CONTROL</p>
</td>
<td>
<p>Path is relative to <b>\Registry\Machine\System\CurrentControlSet\Control</b>.</p>
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
<p>RTL_REGISTRY_SERVICES</p>
</td>
<td>
<p>Path is relative to <b>\Registry\Machine\System\CurrentControlSet\Services</b>.</p>
</td>
</tr>
<tr>
<td>
<p>RTL_REGISTRY_USER</p>
</td>
<td>
<p>Path is relative to the registry settings for the current user. (For a system process, this is <b>\Users\.Default</b>.)  This is equivalent to HKEY_CURRENT_USER in user mode.</p>
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
<p>RTL_REGISTRY_HANDLE</p>
</td>
<td>
<p>This value should not be passed into this routine. Despite the redundancy of a check for the existence of an already-opened key, it has the side effect of closing the passed handle.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>Path</i> [in]

<dd>
<p>Specifies the registry path according to the <i>RelativeTo</i> value. If RTL_REGISTRY_HANDLE is set, <i>Path</i> is a handle to be used directly.</p>
</dd>
</dl>

## -returns
<p>If the given named key exists in the registry along the given relative path, <b>RtlCheckRegistryKey</b> returns STATUS_SUCCESS.</p>

## -remarks


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
<a href="..\wdm\nf-wdm-rtlqueryregistryvalues.md">RtlQueryRegistryValues</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlCheckRegistryKey routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
