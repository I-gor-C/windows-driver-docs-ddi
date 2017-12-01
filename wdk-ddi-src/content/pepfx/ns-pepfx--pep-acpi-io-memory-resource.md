---
UID: NS.pepfx._PEP_ACPI_IO_MEMORY_RESOURCE
title: PEP_ACPI_IO_MEMORY_RESOURCE
author: windows-driver-content
description: The PEP_ACPI_IO_MEMORY_RESOURCE structure describes an ACPI IO port descriptor resource.
old-location: kernel\pep_acpi_io_memory_resource.htm
old-project: kernel
ms.assetid: 7438C120-9CFB-4D5D-9323-8A5D84D02449
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PEP_ACPI_IO_MEMORY_RESOURCE, PEP_ACPI_IO_MEMORY_RESOURCE, *PPEP_ACPI_IO_MEMORY_RESOURCE
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
req.alt-api: PEP_ACPI_IO_MEMORY_RESOURCE
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

# PEP_ACPI_IO_MEMORY_RESOURCE structure



## -description
<p>The <b>PEP_ACPI_IO_MEMORY_RESOURCE</b> structure describes an ACPI IO port descriptor resource.</p>


## -syntax

````
typedef struct _PEP_ACPI_IO_MEMORY_RESOURCE {
  PEP_ACPI_RESOURCE_TYPE Type;
  UCHAR                  Information;
  PHYSICAL_ADDRESS       MinimumAddress;
  PHYSICAL_ADDRESS       MaximumAddress;
  ULONG                  Alignment;
  ULONG                  Length;
} PEP_ACPI_IO_MEMORY_RESOURCE, *PPEP_ACPI_IO_MEMORY_RESOURCE;
````


## -struct-fields
<dl>

### -field <b>Type</b>

<dd>
<p>A <a href="..\pepfx\ne-pepfx--pep-acpi-resource-type.md">PEP_ACPI_RESOURCE_TYPE</a> enumeration value that identifies the resource type for this ACPI resource.</p>
</dd>

### -field <b>Information</b>

<dd>
<p>If bit 0 is a 1, this indicates that the logical device decodes 16-bit addresses. If bit 0 is 0, this indicates that the logical device only decodes the first 10 bits of the address.</p>
<p>Bits 1 to 7 of this member are reserved and must be set to zero.</p>
</dd>

### -field <b>MinimumAddress</b>

<dd>
<p>Specifies the minimum acceptable starting address for the IO range.</p>
</dd>

### -field <b>MaximumAddress</b>

<dd>
<p>Specifies the maximum acceptable starting address for the IO range.</p>
</dd>

### -field <b>Alignment</b>

<dd>
<p>Specifies the alignment granularity for the IO address assigned.</p>
</dd>

### -field <b>Length</b>

<dd>
<p>Specifies the number of bytes in the IO range.</p>
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
<a href="..\pepfx\ne-pepfx--pep-acpi-resource-type.md">PEP_ACPI_RESOURCE_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_ACPI_IO_MEMORY_RESOURCE structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
