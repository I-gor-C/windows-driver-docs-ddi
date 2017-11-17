---
UID: NF.pepfx.PEP_ACPI_INITIALIZE_MEMORY_RESOURCE
title: PEP_ACPI_INITIALIZE_MEMORY_RESOURCE
author: windows-driver-content
description: The PEP_ACPI_INITIALIZE_MEMORY_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_IO_MEMORY_RESOURCE structure.
old-location: kernel\pep_acpi_initialize_memory_resource.htm
ms.assetid: 44EC5408-626A-4FDA-A777-C1A733D690F1
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
req.alt-api: PEP_ACPI_INITIALIZE_MEMORY_RESOURCE
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
ms.keywords: PEP_ACPI_INITIALIZE_MEMORY_RESOURCE
req.iface: 
---

# PEP_ACPI_INITIALIZE_MEMORY_RESOURCE function



## -description
<p>The <b>PEP_ACPI_INITIALIZE_MEMORY_RESOURCE</b> function initializes a platform extension plug-in's (PEP) <a href="https://msdn.microsoft.com/library/windows/hardware/mt186683">PEP_ACPI_IO_MEMORY_RESOURCE</a> structure.</p>


## -syntax

````
FORCEINLINE VOID PEP_ACPI_INITIALIZE_MEMORY_RESOURCE(
  _In_  UCHAR              ReadWrite,
  _In_  ULONG              MinimumAddress,
  _In_  ULONG              MaximumAddress,
  _In_  ULONG              Alignment,
  _In_  ULONG              MemorySize,
  _Out_ PPEP_ACPI_RESOURCE Resource
);
````


## -parameters
<dl>

### -param <i>ReadWrite</i> [in]

<dd>
<p>If true, indicates that the resource is read/write. Otherwise, it's read-only.</p>
</dd>

### -param <i>MinimumAddress</i> [in]

<dd>
<p>Specifies the minimum acceptable starting address for the IO range.</p>
</dd>

### -param <i>MaximumAddress</i> [in]

<dd>
<p>Specifies the maximum acceptable starting address for the IO range.</p>
</dd>

### -param <i>Alignment</i> [in]

<dd>
<p>Specifies the alignment granularity for the memory address assigned.</p>
</dd>

### -param <i>MemorySize</i> [in]

<dd>
<p>Specifies the number of bytes in the memory range.</p>
</dd>

### -param <i>Resource</i> [out]

<dd>
<p>A pointer to the resource. The structure behind the pointer is of type <a href="https://msdn.microsoft.com/library/windows/hardware/mt186683">PEP_ACPI_IO_MEMORY_RESOURCE</a>.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186683">PEP_ACPI_IO_MEMORY_RESOURCE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_ACPI_INITIALIZE_MEMORY_RESOURCE function%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
