---
UID: NS.pepfx._PEP_ACPI_REQUEST_CONVERT_TO_BIOS_RESOURCES
title: PEP_ACPI_REQUEST_CONVERT_TO_BIOS_RESOURCES
author: windows-driver-content
description: The PEP_ACPI_REQUEST_CONVERT_TO_BIOS_RESOURCES structure is used in the process of converting ACPI resources to BIOS resources by one of the PEP initialization functions.
old-location: kernel\pep_acpi_request_convert_to_bios_resources.htm
old-project: kernel
ms.assetid: DF9FD748-88E8-4E32-B698-0E8A3BE319DB
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: PEP_ACPI_REQUEST_CONVERT_TO_BIOS_RESOURCES,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: pepfx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PEP_ACPI_REQUEST_CONVERT_TO_BIOS_RESOURCES
req.alt-loc: pepfx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# PEP_ACPI_REQUEST_CONVERT_TO_BIOS_RESOURCES structure



## -description
<p>The <b>PEP_ACPI_REQUEST_CONVERT_TO_BIOS_RESOURCES</b> structure is used in the process of converting ACPI resources to BIOS resources by one of the <a href="kernel.pep_initialization_functions">PEP initialization functions</a>.</p>


## -syntax

````
typedef struct _PEP_ACPI_REQUEST_CONVERT_TO_BIOS_RESOURCES {
  NTSTATUS           TranslationStatus;
  PPEP_ACPI_RESOURCE InputBuffer;
  SIZE_T             InputBufferSize;
  PVOID              OutputBuffer;
  SIZE_T             OutputBufferSize;
  ULONG              Flags;
} PEP_ACPI_REQUEST_CONVERT_TO_BIOS_RESOURCES, *PPEP_ACPI_REQUEST_CONVERT_TO_BIOS_RESOURCES;
````


## -struct-fields
<dl>

### -field <b>TranslationStatus</b>

<dd>
<p>The result code from the resource translation call.</p>
</dd>

### -field <b>InputBuffer</b>

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/mt186691">PEP_ACPI_RESOURCE</a> containing the input buffer.</p>
</dd>

### -field <b>InputBufferSize</b>

<dd>
<p>The size of the input buffer.</p>
</dd>

### -field <b>OutputBuffer</b>

<dd>
<p>A pointer to the output buffer containing the translated structure.</p>
</dd>

### -field <b>OutputBufferSize</b>

<dd>
<p>The size of the output buffer.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>The value contained in the <a href="https://msdn.microsoft.com/library/windows/hardware/mt186692">PEP_ACPI_RESOURCE_FLAGS</a> structure.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with Windows 10.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Pepfx.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.pep_initialization_functions">PEP initialization functions</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186691">PEP_ACPI_RESOURCE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186692">PEP_ACPI_RESOURCE_FLAGS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_ACPI_REQUEST_CONVERT_TO_BIOS_RESOURCES structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
