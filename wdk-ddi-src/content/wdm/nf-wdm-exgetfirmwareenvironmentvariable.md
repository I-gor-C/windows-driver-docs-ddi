---
UID: NF.wdm.ExGetFirmwareEnvironmentVariable
title: ExGetFirmwareEnvironmentVariable
author: windows-driver-content
description: The ExGetFirmwareEnvironmentVariable routine gets the value of the specified system firmware environment variable.
old-location: kernel\exgetfirmwareenvironmentvariable.htm
old-project: kernel
ms.assetid: 5AD76955-A44C-4231-9394-0B6595CFB33D
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ExGetFirmwareEnvironmentVariable
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ExGetFirmwareEnvironmentVariable
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

# ExGetFirmwareEnvironmentVariable function



## -description
<p>The <b>ExGetFirmwareEnvironmentVariable</b> routine gets the value of the specified system firmware environment variable.</p>


## -syntax

````
NTSTATUS ExGetFirmwareEnvironmentVariable(
  _In_      PUNICODE_STRING VariableName,
  _In_      LPGUID          VendorGuid,
  _Out_opt_ PVOID           Value,
  _Inout_   PULONG          ValueLength,
  _Out_opt_ PULONG          Attributes
);
````


## -parameters
<dl>

### -param VariableName [in]

<dd>
<p>A pointer to a <a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a> structure that contains the name of the specified environment variable.</p>
</dd>

### -param VendorGuid [in]

<dd>
<p>A pointer to a GUID that identifies the vendor associated with the specified environment variable. Environment variables are grouped into namespaces based on their vendor GUIDs. Some hardware platforms might not support vendor GUIDs. On these platforms, all variables are grouped into one, common namespace, and the <i>VendorGuid</i> parameter is ignored.</p>
</dd>

### -param Value [out, optional]

<dd>
<p>A pointer to a caller-allocated buffer to which the routine writes the value of the specified environment variable.</p>
</dd>

### -param ValueLength [in, out]

<dd>
<p>A pointer to a location that contains the buffer size. On entry, the location pointed to by this parameter contains the size, in bytes, of the caller-supplied <i>Value</i> buffer. Before exiting, the routine writes to this location the size, in bytes, of the variable value. If the routine returns STATUS_SUCCESS, the *<i>ValueLength</i> output value is the number of bytes of data written to the <i>Value</i> buffer. If the routine returns STATUS_BUFFER_TOO_SMALL, *<i>ValueLength</i> is the required buffer size.</p>
</dd>

### -param Attributes [out, optional]

<dd>
<p>A pointer to a location to which the routine writes the attributes of the specified environment variable. This parameter is optional and can be set to NULL if the caller does not need the attributes. For more information, see Remarks.</p>
</dd>
</dl>

## -returns
<p><b>ExGetFirmwareEnvironmentVariable</b> returns STATUS_SUCCESS if it is successful. Possible return values include the following error status codes.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>Available system resources are insufficient to complete the requested operation.</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The <i>Value</i> buffer is too small.</p><dl>
<dt><b>STATUS_VARIABLE_NOT_FOUND</b></dt>
</dl><p>The requested variable does not exist.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>One of the parameters is not valid.</p><dl>
<dt><b>STATUS_NOT_IMPLEMENTED</b></dt>
</dl><p>This routine is not supported on this platform.</p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>The firmware returned an unrecognized error.</p>

<p> </p>

## -remarks
<p>System firmware environment variables contain data values that are passed between the boot firmware environment implemented in the hardware platform and the operating-system loaders and other software that runs in the firmware environment.</p>

<p>The set of firmware environment variables that is available in a hardware platform depends on the boot firmware. The location of these environment variables is also specified by the firmware. For example, on a UEFI-based platform, NVRAM contains firmware environment variables that specify system boot settings. For information about specific variables used, see the Unified Extensible Firmware Interface Specification at the <a href="http://go.microsoft.com/fwlink/p/?linkid=183072">UEFI</a> website. For more information about UEFI and Windows, see <a href="http://go.microsoft.com/fwlink/p/?linkid=183071">UEFI and Windows</a>.</p>

<p>Firmware environment variables are not supported on a legacy BIOS-based platform. Calls to <b>ExGetFirmwareEnvironmentVariable</b> always fail on a legacy BIOS-based platform; they also fail if Windows was installed using the legacy BIOS on a platform that supports both legacy BIOS and UEFI. To identify these conditions, call the function with a dummy <i>VariableName</i> string (for example, an empty string) and a dummy GUID such as</p>

<p><code>"{00000000-0000-0000-0000-000000000000}"</code></p>

<p>for the <i>VendorGuid</i> parameter. On a legacy BIOS-based platform, or on a platform that supports both legacy BIOS and UEFI but in which Windows was installed using the legacy BIOS, the function will fail with STATUS_NOT_IMPLEMENTED. On a UEFI-based platform, the function will fail with an error specific to the firmware, such as STATUS_VARIABLE_NOT_FOUND, to indicate that the dummy GUID namespace does not exist.</p>

<p>If the caller specifies a non-NULL <i>Attributes</i> parameter, the routine writes the attributes of the specified system firmware environment variable to the location pointed to by <i>Attributes</i>. Version 2.3.1 of the UEFI specification defines the following attributes for firmware environment variables.</p>

<p>These attribute values are defined as flag bits. The value written to the ULONG variable pointed to by <i>Attributes</i> is either zero or the bitwise OR of one or more attributes in the preceding table. For more information, see the UEFI specification at the <a href="http://go.microsoft.com/fwlink/p/?linkid=183072">UEFI</a> website.</p>

<p>If you create a backup datastore, you can use this function to save all the boot settings for the platform so they can be restored by calling the <a href="..\wdm\nf-wdm-exsetfirmwareenvironmentvariable.md">ExSetFirmwareEnvironmentVariable</a> routine if needed.</p>

<p><b>ExGetFirmwareEnvironmentVariable</b> is the kernel-mode equivalent of the Win32 <a href="base.getfirmwareenvironmentvariable">GetFirmwareEnvironmentVariable</a> function.</p>

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
<a href="..\wdm\nf-wdm-exsetfirmwareenvironmentvariable.md">ExSetFirmwareEnvironmentVariable</a>
</dt>
<dt>
<a href="base.getfirmwareenvironmentvariable">GetFirmwareEnvironmentVariable</a>
</dt>
<dt>
<a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ExGetFirmwareEnvironmentVariable routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
