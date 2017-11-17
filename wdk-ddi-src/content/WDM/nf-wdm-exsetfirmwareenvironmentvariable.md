---
UID: NF.wdm.ExSetFirmwareEnvironmentVariable
title: ExSetFirmwareEnvironmentVariable
author: windows-driver-content
description: The ExSetFirmwareEnvironmentVariable routine sets the value of the specified system firmware environment variable.
old-location: kernel\exsetfirmwareenvironmentvariable.htm
ms.assetid: 04447D92-EB9E-400B-A018-E70B186EA3DB
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ExSetFirmwareEnvironmentVariable
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
ms.keywords: ExSetFirmwareEnvironmentVariable
req.iface: 
req.product: Windows 10 or later.
---

# ExSetFirmwareEnvironmentVariable function



## -description
<p>The <b>ExSetFirmwareEnvironmentVariable</b> routine sets the value of the specified system firmware environment variable.</p>


## -syntax

````
NTSTATUS ExSetFirmwareEnvironmentVariable(
  _In_ PUNICODE_STRING VariableName,
  _In_ LPGUID          VendorGuid,
  _In_ PVOID           Value,
  _In_ ULONG           ValueLength,
  _In_ ULONG           Attributes
);
````


## -parameters
<dl>

### -param <i>VariableName</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a> structure that contains the name of the specified environment variable.</p>
</dd>

### -param <i>VendorGuid</i> [in]

<dd>
<p>A pointer to a GUID that identifies the vendor associated with the specified environment variable. Environment variables are grouped into namespaces based on their vendor GUIDs. Some hardware platforms might not support vendor GUIDs. On these platforms, all variables are grouped into one, common namespace, and the <i>VendorGuid</i> parameter is ignored.</p>
</dd>

### -param <i>Value</i> [in]

<dd>
<p>A pointer to a caller-allocated buffer that contains the data value to write to the specified environment variable.</p>
</dd>

### -param <i>ValueLength</i> [in]

<dd>
<p>The size, in bytes, of the data value contained in the <i>Value</i> buffer.</p>
</dd>

### -param <i>Attributes</i> [in]

<dd>
<p>The attributes to assign to the specified environment variable. The VARIABLE_ATTRIBUTE_NON_VOLATILE attribute bit must be set or this call will fail. For more information about the attribute bits that are defined for this parameter, see Remarks in <a href="https://msdn.microsoft.com/library/windows/hardware/jj151553">ExGetFirmwareEnvironmentVariable</a>.</p>
</dd>
</dl>

## -returns
<p><b>ExSetFirmwareEnvironmentVariable</b> returns STATUS_SUCCESS if it is successful. Possible return values include the following error status codes.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>Available system resources are insufficient to complete the requested operation.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>One of the parameters is not valid.</p><dl>
<dt><b>STATUS_NOT_IMPLEMENTED</b></dt>
</dl><p>This routine is not supported on this platform.</p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>The firmware returned an unrecognized error.</p>

<p> </p>

## -remarks
<p>The caller requires the system environment privilege (SE_SYSTEM_ENVIRONMENT_PRIVILEGE) to use this routine.</p>

<p>System firmware environment variables contain data values that are passed between the boot firmware environment implemented in the hardware platform and the operating-system loaders and other software that runs in the firmware environment.  For more information, see Remarks in <a href="https://msdn.microsoft.com/library/windows/hardware/jj151553">ExGetFirmwareEnvironmentVariable</a>.</p>

<p>If you create a backup datastore, you can use the  <a href="https://msdn.microsoft.com/library/windows/hardware/jj151553">ExGetFirmwareEnvironmentVariable</a> routine to save all the boot settings for the platform. Later, you can use <b>ExSetFirmwareEnvironmentVariable</b> to restore these settings if needed.</p>

<p><b>ExSetFirmwareEnvironmentVariable</b> is the kernel-mode equivalent of the Win32 <a href="base.setfirmwareenvironmentvariable">SetFirmwareEnvironmentVariable</a> function.</p>

<p>The caller requires the system environment privilege (SE_SYSTEM_ENVIRONMENT_PRIVILEGE) to use this routine.</p>

<p>System firmware environment variables contain data values that are passed between the boot firmware environment implemented in the hardware platform and the operating-system loaders and other software that runs in the firmware environment.  For more information, see Remarks in <a href="https://msdn.microsoft.com/library/windows/hardware/jj151553">ExGetFirmwareEnvironmentVariable</a>.</p>

<p>If you create a backup datastore, you can use the  <a href="https://msdn.microsoft.com/library/windows/hardware/jj151553">ExGetFirmwareEnvironmentVariable</a> routine to save all the boot settings for the platform. Later, you can use <b>ExSetFirmwareEnvironmentVariable</b> to restore these settings if needed.</p>

<p><b>ExSetFirmwareEnvironmentVariable</b> is the kernel-mode equivalent of the Win32 <a href="base.setfirmwareenvironmentvariable">SetFirmwareEnvironmentVariable</a> function.</p>

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
<p>Available starting with Windows 8.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/jj151553">ExGetFirmwareEnvironmentVariable</a>
</dt>
<dt>
<a href="base.setfirmwareenvironmentvariable">SetFirmwareEnvironmentVariable</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ExSetFirmwareEnvironmentVariable routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
