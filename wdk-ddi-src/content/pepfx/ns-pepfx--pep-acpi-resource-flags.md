---
UID: NS.pepfx._PEP_ACPI_RESOURCE_FLAGS
title: PEP_ACPI_RESOURCE_FLAGS
author: windows-driver-content
description: The PEP_ACPI_RESOURCE_FLAGS structure contains flags describing an ACPI resource.
old-location: kernel\pep_acpi_resource_flags.htm
old-project: kernel
ms.assetid: 1BB4933B-2707-4350-8D9C-E0E25A85F5CB
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PEP_ACPI_RESOURCE_FLAGS, PEP_ACPI_RESOURCE_FLAGS, *PPEP_ACPI_RESOURCE_FLAGS
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
req.alt-api: PEP_ACPI_RESOURCE_FLAGS
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

# PEP_ACPI_RESOURCE_FLAGS structure



## -description
<p>The <b>PEP_ACPI_RESOURCE_FLAGS</b> structure contains flags describing an ACPI resource.</p>


## -syntax

````
typedef union _PEP_ACPI_RESOURCE_FLAGS {
  ULONG  AsULong;
  struct {
    ULONG Shared  :1;
    ULONG Wake  :1;
    ULONG ResourceUsage  :1;
    ULONG SlaveMode  :1;
    ULONG AddressingMode  :1;
    ULONG SharedMode  :1;
    ULONG Reserved  :26;
  } DUMMYSTRUCTNAME;
} PEP_ACPI_RESOURCE_FLAGS, *PPEP_ACPI_RESOURCE_FLAGS;
````


## -struct-fields
<dl>

### -field AsULong

<dd>
<p>The consolidated values of the flags in <b>DUMMYSTRUCTNAME</b>.</p>
</dd>

### -field DUMMYSTRUCTNAME

<dd>
<p> A structure containing ACPI resource flags.</p>
<dl>

### -field Shared

<dd>
<p>When set, indicates that this is a shared device.</p>
</dd>

### -field Wake

<dd>
<p>When set, indicates that this device can be woken from a low-power state.</p>
</dd>

### -field ResourceUsage

<dd>
<p>When set, indicates that this device is in use.</p>
</dd>

### -field SlaveMode

<dd>
<p>When set, indicates that this device is in slave mode.</p>
</dd>

### -field AddressingMode

<dd>
<p>When set, indicates that this device is in addressing mode.</p>
</dd>

### -field SharedMode

<dd>
<p>When set, indicates that this device is in shared mode.</p>
</dd>

### -field Reserved

<dd>
<p>This member is reserved and should be set to zero.</p>
</dd>
</dl>
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