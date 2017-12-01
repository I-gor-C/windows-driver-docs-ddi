---
UID: NS.pepfx._PEP_ACPI_EXTENDED_ADDRESS
title: PEP_ACPI_EXTENDED_ADDRESS
author: windows-driver-content
description: The PEP_ACPI_EXTENDED_ADDRESS structure is used to report resource usage in the address space such as memory and IO.
old-location: kernel\pep_acpi_extended_address.htm
old-project: kernel
ms.assetid: E784765E-E346-4D57-B334-D0A0A823DAA8
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PEP_ACPI_EXTENDED_ADDRESS, PEP_ACPI_EXTENDED_ADDRESS, *PPEP_ACPI_EXTENDED_ADDRESS
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
req.alt-api: PEP_ACPI_EXTENDED_ADDRESS
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

# PEP_ACPI_EXTENDED_ADDRESS structure



## -description
<p>The <b>PEP_ACPI_EXTENDED_ADDRESS</b> structure is used to report resource usage in the address space such as memory and IO.</p>


## -syntax

````
typedef struct _PEP_ACPI_EXTENDED_ADDRESS {
  PEP_ACPI_RESOURCE_TYPE  Type;
  PEP_ACPI_RESOURCE_FLAGS Flags;
  UCHAR                   ResourceFlags;
  UCHAR                   GeneralFlags;
  UCHAR                   TypeSpecificFlags;
  UCHAR                   RevisionId;
  UCHAR                   Reserved;
  ULONGLONG               Granularity;
  ULONGLONG               MinimumAddress;
  ULONGLONG               MaximumAddress;
  ULONGLONG               TranslationAddress;
  ULONGLONG               AddressLength;
  ULONGLONG               TypeAttribute;
  PUNICODE_STRING         DescriptorName;
} PEP_ACPI_EXTENDED_ADDRESS, *PPEP_ACPI_EXTENDED_ADDRESS;
````


## -struct-fields
<dl>

### -field <b>Type</b>

<dd>
<p>A <a href="..\pepfx\ne-pepfx--pep-acpi-resource-type.md">PEP_ACPI_RESOURCE_TYPE</a> enumeration value describing this resource.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A <a href="..\pepfx\ns-pepfx--pep-acpi-resource-flags.md">PEP_ACPI_RESOURCE_FLAGS</a> structure describing this resource.</p>
</dd>

### -field <b>ResourceFlags</b>

<dd>
<p>Indicates the type of resource this structure describes.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%">
<dl>

### -field 0

</dl>
</td>
<td width="60%">
<p>Indicates that this resource is a memory range.</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 1

</dl>
</td>
<td width="60%">
<p>Indicates that this resource is an IO range.</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 2

</dl>
</td>
<td width="60%">
<p>Indicates that this resource is a bus number range.</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 3-191

</dl>
</td>
<td width="60%">
<p>These values are reserved for future use.</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 192-255

</dl>
</td>
<td width="60%">
<p>These values are reserved for use by the hardware vendor.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>GeneralFlags</b>

<dd>
<p>A value containing the bit flags that are common to all resource types. </p>
<table>
<tr>
<th>Bit(s)</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="0_-_Consumer_Producer_flag"></a><a id="0_-_consumer_producer_flag"></a><a id="0_-_CONSUMER_PRODUCER_FLAG"></a><dl>

### -field <b>0 - Consumer/Producer flag</b>

</dl>
</td>
<td width="60%">
<p>When set, this indicates that the device consumes this resource.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="1_-_Decode_type"></a><a id="1_-_decode_type"></a><a id="1_-_DECODE_TYPE"></a><dl>

### -field <b>1 - Decode type</b>

</dl>
</td>
<td width="60%">
<p>When set, indicates that this bridge subtractively decodes the address. This applies to top level bridges only. </p>
<p>When not set, indicates that this bridge positively decodes this address.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="2_-_Minimum_address_fixed"></a><a id="2_-_minimum_address_fixed"></a><a id="2_-_MINIMUM_ADDRESS_FIXED"></a><dl>

### -field <b>2 - Minimum address fixed</b>

</dl>
</td>
<td width="60%">
<p>When set, indicates that the minimum address is fixed.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="3_-_Max_address_fixed"></a><a id="3_-_max_address_fixed"></a><a id="3_-_MAX_ADDRESS_FIXED"></a><dl>

### -field <b>3 - Max address fixed</b>

</dl>
</td>
<td width="60%">
<p>When set, indicates that the maximum address is fixed. </p>
</td>
</tr>
<tr>
<td width="40%"><a id="4_to_7_-_Reserved"></a><a id="4_to_7_-_reserved"></a><a id="4_TO_7_-_RESERVED"></a><dl>

### -field <b>4 to 7 - Reserved</b>

</dl>
</td>
<td width="60%">
<p>These bits are reserved and must be set to zero.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>TypeSpecificFlags</b>

<dd>
<p>The value of this member is dependent on the value in <b>ResourceFlags</b> member. The flags for each resource type are described in the tables below.</p>
<p>
<p>Memory Resource (<b>ResourceFlags</b> = <b>0</b>)</p>
</p>
<table>
<tr>
<th>Bit(s)</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="0_-_Write_status"></a><a id="0_-_write_status"></a><a id="0_-_WRITE_STATUS"></a><dl>

### -field <b>0 - Write status</b>

</dl>
</td>
<td width="60%">
<p>When set, indicates that this memory range is available for reading and writing. Otherwise, this indicates that this memory range is read-only.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="1_to_2_-_Memory_attributes__MEM_"></a><a id="1_to_2_-_memory_attributes__mem_"></a><a id="1_TO_2_-_MEMORY_ATTRIBUTES__MEM_"></a><dl>

### -field <b>1 to 2 - Memory attributes (MEM)</b>

</dl>
</td>
<td width="60%">
<p><b>0</b> - Indicates the memory is non-cacheable.</p>
<p><b>1</b> - Indicates the memory is cacheable.</p>
<p><b>2</b> - Indicates the memory is cacheable and supports write combining.</p>
<p><b>3</b>  - The memory is cacheable and prefetchable.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="3_to_4_-_Memory_attributes__MTP_"></a><a id="3_to_4_-_memory_attributes__mtp_"></a><a id="3_TO_4_-_MEMORY_ATTRIBUTES__MTP_"></a><dl>

### -field <b>3 to 4 - Memory attributes (MTP)</b>

</dl>
</td>
<td width="60%">
<p>These bits are only defined if this memory resource describes system RAM.  </p>
<p><b>0</b> - Address range memory: This range is available RAM usable by the operating system.</p>
<p><b>1</b> - Address range reserved: This range of addresses is in use or reserved by the system
and is not to be included in the allocatable memory pool of the
operating system's memory manager.</p>
<p><b>2</b> - Address range ACPI: ACPI Reclaim Memory. This range is available RAM usable by
the OS after it reads the ACPI tables. </p>
<p><b>3</b> - Address Range NVS: ACPI NVS Memory. This range of addresses is in use or
reserved by the system and must not be used by the operating
system. This range is required to be saved and restored across
an NVS sleep.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="5_-_Memory_to_IO_translation"></a><a id="5_-_memory_to_io_translation"></a><a id="5_-_MEMORY_TO_IO_TRANSLATION"></a><dl>

### -field <b>5 - Memory to IO translation</b>

</dl>
</td>
<td width="60%">
<p><b>0</b> - Type-static: This resource is memory on the primary and secondary sides of the bridge.</p>
<p><b>1</b> - Type-translation: This resource is memory on the secondary side of the bridge and IO on the primary side of the bridge.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="6_to_7_-_Reserved"></a><a id="6_to_7_-_reserved"></a><a id="6_TO_7_-_RESERVED"></a><dl>

### -field <b>6 to 7 - Reserved</b>

</dl>
</td>
<td width="60%">
<p>These bits are reserved and must be set to zero.</p>
</td>
</tr>
</table>
<p> </p>
<p>
<p>IO Resource (<b>ResourceFlags</b> = <b>1</b>)</p>
</p>
<table>
<tr>
<th>Bit(s)</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="0_to_1_-_Range"></a><a id="0_to_1_-_range"></a><a id="0_TO_1_-_RANGE"></a><dl>

### -field <b>0 to 1 - Range</b>

</dl>
</td>
<td width="60%">
<p><b>0</b> - Reserved.</p>
<p><b>1</b> - Non-ISA ranges only. This flag is for bridges on systems with multiple bridges. Setting this
bit means the memory window specified in this descriptor is limited to the non-ISA IO
addresses that fall within the specified window. The non-ISA IO ranges are: n100-n3FF,
n500-n7FF, n900-nBFF, nD00-nFFF. This bit can only be set for bridges entirely
configured through the ACPI namespace.
</p>
<p><b>2</b> - ISA ranges only. This flag is for bridges on systems with multiple bridges. Setting this bit
means the memory window specified in this descriptor is limited to the ISA IO addresses
that fall within the specified window. The ISA IO ranges are: n000-n0FF, n400-n4FF,
n800-n8FF, nC00-nCFF. This bit can only be set for bridges entirely configured through
the ACPI namespace.
</p>
<p><b>3</b> - The memory window covers the entire range
</p>
</td>
</tr>
<tr>
<td width="40%"><a id="2_to_3_-_Reserved"></a><a id="2_to_3_-_reserved"></a><a id="2_TO_3_-_RESERVED"></a><dl>

### -field <b>2 to 3 - Reserved</b>

</dl>
</td>
<td width="60%">
<p>These bits are reserved and must be set to zero.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="4_-_IO_to_memory_translation"></a><a id="4_-_io_to_memory_translation"></a><a id="4_-_IO_TO_MEMORY_TRANSLATION"></a><dl>

### -field <b>4 - IO to memory translation</b>

</dl>
</td>
<td width="60%">
<p><b>0</b> - Type-static: This resource is IO on the primary and secondary sides of the bridge.</p>
<p><b>1</b> - Type-translation: This resource is IO on the secondary side of the bridge and memory on the primary side of the bridge.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="5_-_Sparse_translation"></a><a id="5_-_sparse_translation"></a><a id="5_-_SPARSE_TRANSLATION"></a><dl>

### -field <b>5 - Sparse translation</b>

</dl>
</td>
<td width="60%">
<p>This bit is only meaningful if bit 4 (IO to memory translation) is set.
</p>
<p><b>0</b> - Dense translation: The primary-side memory address of any specific IO port within the
secondary-side range can be found using the following function. </p>
<p><i>     address = port + TranslationAddress</i></p>
<p><b>1</b> - Sparse translation: The primary-side memory address of any specific IO port within the
secondary-side range can be found using the following function.</p>
<p><i>address = (((port &amp; 0xFFFc) &lt;&lt; 10) || (port &amp; 0xFFF)) + TranslationAddress</i></p>
<p>In the address used to access the IO port, bits 2 to 11 must be identical
to bits 12 to 21, this gives four bytes of IO ports on each 4 KB page.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="6_to_7_-_Reserved"></a><a id="6_to_7_-_reserved"></a><a id="6_TO_7_-_RESERVED"></a><dl>

### -field <b>6 to 7 - Reserved</b>

</dl>
</td>
<td width="60%">
<p>These bits are reserved and must be set to zero.</p>
</td>
</tr>
</table>
<p> </p>
<p>
<p>Bus Number Range Resource (<b>ResourceFlags</b> = <b>2</b>)</p>
</p>
<table>
<tr>
<th>Bit(s)</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="0_to_7_-_Reserved"></a><a id="0_to_7_-_reserved"></a><a id="0_TO_7_-_RESERVED"></a><dl>

### -field <b>0 to 7 - Reserved</b>

</dl>
</td>
<td width="60%">
<p>These bits are reserved and must be set to zero.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>RevisionId</b>

<dd>
<p>Indicates the revision of the extended address space descriptor detailed by this structure. For ACPI 3.0, this value is 1.</p>
</dd>

### -field <b>Reserved</b>

<dd>Reserved. Must be set to zero.</dd>

### -field <b>Granularity</b>

<dd>
<p>A bit mask indicating which bits have been decoded.</p>
</dd>

### -field <b>MinimumAddress</b>

<dd>
<p>The minimum starting address. For bridges that translate addresses, this is the address space on the secondary side of the bridge.</p>
</dd>

### -field <b>MaximumAddress</b>

<dd>
<p>The maximum starting address. For bridges that translate addresses, this is the address space
on the secondary side of the bridge.</p>
</dd>

### -field <b>TranslationAddress</b>

<dd>
<p>For bridges that translate addresses across the bridge, this is the
address on the primary side. </p>
</dd>

### -field <b>AddressLength</b>

<dd>
<p>The address length.</p>
</dd>

### -field <b>TypeAttribute</b>

<dd>
<p>Indicates attributes that are specific to the resource type that is specified in the <b>ResourceFlags</b> member. If <b>ResourceFlags</b> is zero, this value is zero, otherwise the meaning of the value can be found in the <i>UEFI Specification</i> in the section titled <b>GetMemoryMap()</b>. </p>
</dd>

### -field <b>DescriptorName</b>

<dd>
<p>The name of this resource descriptor.</p>
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