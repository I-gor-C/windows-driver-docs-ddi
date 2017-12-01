---
UID: NF.aux_klib.AuxKlibEnumerateSystemFirmwareTables
title: AuxKlibEnumerateSystemFirmwareTables
author: windows-driver-content
description: The AuxKlibEnumerateSystemFirmwareTables routine enumerates all system firmware tables of the specified type.
old-location: kernel\auxklibenumeratesystemfirmwaretables.htm
old-project: kernel
ms.assetid: EEAB636B-5565-4C2A-9EC7-4DC63EBB286F
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: AuxKlibEnumerateSystemFirmwareTables
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: aux_klib.h
req.include-header: Aux_klib.h
req.target-type: Universal
req.target-min-winverclnt: Supported starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: AuxKlibEnumerateSystemFirmwareTables
req.alt-loc: Aux_Klib.lib,Aux_Klib.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Aux_Klib.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# AuxKlibEnumerateSystemFirmwareTables function



## -description
<p>The <b>AuxKlibEnumerateSystemFirmwareTables</b> routine enumerates all system firmware tables of the specified type.</p>


## -syntax

````
NTSTATUS AuxKlibEnumerateSystemFirmwareTables(
  _In_      ULONG  FirmwareTableProviderSignature,
  _Out_opt_ PVOID  FirmwareTableBuffer,
  _In_      ULONG  BufferLength,
  _Out_opt_ PULONG ReturnLength
);
````


## -parameters
<dl>

### -param <i>FirmwareTableProviderSignature</i> [in]

<dd>
<p>The identifier of the firmware table provider to which the query is to be directed. This parameter can be one of the following values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>'ACPI'</p>
</td>
<td>
<p>The ACPI firmware table provider.</p>
</td>
</tr>
<tr>
<td>
<p>'FIRM'</p>
</td>
<td>
<p>The raw firmware table provider.</p>
</td>
</tr>
<tr>
<td>
<p>'RSMB'</p>
</td>
<td>
<p>The raw SMBIOS firmware table provider.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>FirmwareTableBuffer</i> [out, optional]

<dd>
<p>A pointer to a caller-allocated buffer to which the routine writes the list of firmware tables. If this parameter is NULL, the value written to *<i>ReturnLength</i> is the required buffer size. For more information about the contents of this buffer, see the Remarks section.</p>
</dd>

### -param <i>BufferLength</i> [in]

<dd>
<p>The size, in bytes, of the buffer pointed to by <i>FirmwareTableBuffer</i>.</p>
</dd>

### -param <i>ReturnLength</i> [out, optional]

<dd>
<p>A pointer to a location to which the routine writes the number of bytes of data written to the buffer pointed to by <i>FirmwareTableBuffer</i>.</p>
</dd>
</dl>

## -returns
<p><b>AuxKlibEnumerateSystemFirmwareTables</b> returns STATUS_SUCCESS if the call is successful. Possible return values include the following error codes.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid parameter was supplied to the routine.</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The caller-allocated buffer is too small, but the required buffer size has been written to the <i>ReturnLength</i> output parameter.</p>

<p> </p>

## -remarks
<p>If the call is successful, this routine writes an array of one or more table identifiers to the buffer pointed to by the <i>FirmwareTableBuffer</i> parameter. Each element of this array is a DWORD value that identifies a firmware table that is available from the provider specified by the <i>FirmwareTableProviderSignature</i> parameter.</p>

<p>The raw SMBIOS table provider ('RSMB') currently returns a single table identifier, 0x00000000. This corresponds to the raw SMBIOS firmware table.</p>

<p>The raw firmware table provider ('FIRM') retrieves a list of DWORD table identifiers. Each identifier corresponds to the beginning of a physical address range. Currently, this provider returns two identifiers, 0x000C0000 and 0x000E0000. These identifiers represent physical memory from 0x000C0000 to 0x000DFFFF and from 0x000E0000 to 0x000FFFFF, respectively.</p>

<p>The ACPI table provider ('ACPI') returns a list of DWORD table identifiers. Each identifier returned corresponds to <b>Signature</b> field of the <b>DESCRIPTION_HEADER</b> structure for an ACPI table currently in the ACPI namespace of the system. For more information about this structure, see the Advanced Configuration and Power Interface Specification at the <a href="http://go.microsoft.com/fwlink/p/?linkid=57185">Advanced Configuration and Power Interface</a> website.</p>

<p>For ACPI, if the system firmware contains multiple tables with the same name, <b>AuxKlibEnumerateSystemFirmwareTables</b> enumerates them all. However, <a href="..\aux_klib\nf-aux-klib-auxklibgetsystemfirmwaretable.md">AuxKlibGetSystemFirmwareTable</a> retrieves only the first table in the list that has this name.</p>

<p><b>AuxKlibEnumerateSystemFirmwareTables</b> is the kernel-mode equivalent of the Win32 <a href="https://msdn.microsoft.com/library/windows/hardware/hh802466">EnumSystemFirmwareTables</a> function.</p>

<p>Drivers must call <a href="..\aux_klib\nf-aux-klib-auxklibinitialize.md">AuxKlibInitialize</a> before calling <b>AuxKlibEnumerateSystemFirmwareTable</b>.</p>

<p><b>AuxKlibEnumerateSystemFirmwareTables</b> is defined in the Aux_klib.h header file that is included in the WDK for Windows 8 and later versions of Windows. To use this routine, drivers should link to the version of Aux_klib.lib that is included in the WDK for Windows 8 and later versions of Windows. The implementation of <b>AuxKlibEnumerateSystemFirmwareTables</b> in these versions of the WDK can be used in versions of Windows starting with Windows Vista.</p>

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
<p>Supported starting with Windows Vista.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Aux_klib.h (include Aux_klib.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Aux_Klib.lib</dt>
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
<a href="..\aux_klib\nf-aux-klib-auxklibgetsystemfirmwaretable.md">AuxKlibGetSystemFirmwareTable</a>
</dt>
<dt>
<a href="..\aux_klib\nf-aux-klib-auxklibinitialize.md">AuxKlibInitialize</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh802466">EnumSystemFirmwareTables</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20AuxKlibEnumerateSystemFirmwareTables routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
