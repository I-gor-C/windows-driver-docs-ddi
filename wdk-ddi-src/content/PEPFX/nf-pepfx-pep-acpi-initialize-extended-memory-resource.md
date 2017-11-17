---
UID: NF.pepfx.PEP_ACPI_INITIALIZE_EXTENDED_MEMORY_RESOURCE
title: PEP_ACPI_INITIALIZE_EXTENDED_MEMORY_RESOURCE
author: windows-driver-content
description: The PEP_ACPI_INITIALIZE_EXTENDED_MEMORY_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_EXTENDED_ADDRESS structure.
old-location: kernel\pep_acpi_initialize_extended_memory_resource.htm
ms.assetid: F566E078-9446-49E1-9325-AF65F3ABB6B9
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: pepfx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PEP_ACPI_INITIALIZE_EXTENDED_MEMORY_RESOURCE
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
req.irql: 
ms.keywords: PEP_ACPI_INITIALIZE_EXTENDED_MEMORY_RESOURCE
req.iface: 
---

# PEP_ACPI_INITIALIZE_EXTENDED_MEMORY_RESOURCE function



## -description
<p>The <b>PEP_ACPI_INITIALIZE_EXTENDED_MEMORY_RESOURCE</b> function initializes a platform extension plug-in's (PEP) <a href="https://msdn.microsoft.com/library/windows/hardware/mt186670">PEP_ACPI_EXTENDED_ADDRESS</a> structure.</p>


## -syntax

````
FORCEINLINE VOID PEP_ACPI_INITIALIZE_EXTENDED_MEMORY_RESOURCE(
  _In_  BOOLEAN            ResourceUsage,
  _In_  UCHAR              Decode,
  _In_  BOOLEAN            IsMinFixed,
  _In_  BOOLEAN            IsMaxFixed,
  _In_  UCHAR              Cacheable,
  _In_  BOOLEAN            ReadWrite,
  _In_  ULONGLONG          AddressGranularity,
  _In_  ULONGLONG          AddressMinimum,
  _In_  ULONGLONG          AddressMaximum,
  _In_  ULONGLONG          AddressTranslation,
  _In_  ULONGLONG          RangeLength,
  _In_  ULONGLONG          TypeSpecificAttributes,
  _In_  PUNICODE_STRING    DescriptorName,
  _In_  UCHAR              MemoryRangeType,
  _In_  BOOLEAN            TanslationTypeNonStatic,
  _Out_ PPEP_ACPI_RESOURCE Resource
);
````


## -parameters
<dl>

### -param <i>ResourceUsage</i> [in]

<dd>
<p>This parameter is copied into the <b>GeneralFlags</b> member of the initialized <a href="https://msdn.microsoft.com/library/windows/hardware/mt186670">PEP_ACPI_EXTENDED_ADDRESS</a> structure.</p>
</dd>

### -param <i>Decode</i> [in]

<dd>
<p>When set, indicates that this bridge subtractively decodes the address. This applies to top level bridges only. </p>
<p>When not set, indicates that this bridge positively decodes this address.</p>
</dd>

### -param <i>IsMinFixed</i> [in]

<dd>
<p>When set, indicates that the minimum address is fixed.</p>
</dd>

### -param <i>IsMaxFixed</i> [in]

<dd>
<p>When set, indicates that the maximum address is fixed.</p>
</dd>

### -param <i>Cacheable</i> [in]

<dd>
<p>The caching flag for the resource.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%">
<dl>

### -param 0

</dl>
</td>
<td width="60%">
<p>Indicates the memory is non-cacheable.</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -param 1

</dl>
</td>
<td width="60%">
<p>Indicates the memory is cacheable.</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -param 2

</dl>
</td>
<td width="60%">
<p>Indicates the memory is cacheable and supports write combining.</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -param 3

</dl>
</td>
<td width="60%">
<p>The memory is cacheable and prefetchable.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>ReadWrite</i> [in]

<dd>
<p>When true, indicates that the resource is available for read/write access. Otherwise, it's read-only.</p>
</dd>

### -param <i>AddressGranularity</i> [in]

<dd>
<p>A bit mask indicating which bits have been decoded.</p>
</dd>

### -param <i>AddressMinimum</i> [in]

<dd>
<p>For bridges that translate addresses, this indicates the minimum starting address on the secondary side of the bridge.</p>
</dd>

### -param <i>AddressMaximum</i> [in]

<dd>
<p>For bridges that translate addresses, this indicates the maximum starting address on the secondary side of the bridge.</p>
</dd>

### -param <i>AddressTranslation</i> [in]

<dd>
<p>For bridges that translate addresses across the bridge, this is the
address on the primary side. </p>
</dd>

### -param <i>RangeLength</i> [in]

<dd>
<p>The length of the address range. </p>
</dd>

### -param <i>TypeSpecificAttributes</i> [in]

<dd>
<p>The type-specific attributes for this resource.</p>
</dd>

### -param <i>DescriptorName</i> [in]

<dd>
<p>The name of the resource descriptor.</p>
</dd>

### -param <i>MemoryRangeType</i> [in]

<dd>
<p>This parameter identifies the type of memory range provided by this resource.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%">
<dl>

### -param 0

</dl>
</td>
<td width="60%">
<p>Address range memory: This range is available RAM usable by the operating system.</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -param 1

</dl>
</td>
<td width="60%">
<p>Address range reserved: This range of addresses is in use or reserved by the system
and is not to be included in the allocatable memory pool of the
operating system's memory manager.</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -param 2

</dl>
</td>
<td width="60%">
<p>Address range ACPI: ACPI Reclaim Memory. This range is available RAM usable by
the OS after it reads the ACPI tables.</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -param 3

</dl>
</td>
<td width="60%">
<p>Address Range NVS: ACPI NVS Memory. This range of addresses is in use or
reserved by the system and must not be used by the operating
system. This range is required to be saved and restored across
an NVS sleep.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>TanslationTypeNonStatic</i> [in]

<dd>
<p>When true, indicates that the resource uses type translation. Otherwise, it uses type-static translation.</p>
</dd>

### -param <i>Resource</i> [out]

<dd>
<p>This is cast to *<a href="https://msdn.microsoft.com/library/windows/hardware/mt186670">PEP_ACPI_EXTENDED_ADDRESS</a>.</p>
</dd>
</dl>

## -returns
<p>This function does not return a value.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186670">PEP_ACPI_EXTENDED_ADDRESS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_ACPI_INITIALIZE_EXTENDED_MEMORY_RESOURCE function%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
