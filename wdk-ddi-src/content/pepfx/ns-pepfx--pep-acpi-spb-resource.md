---
UID: NS.pepfx._PEP_ACPI_SPB_RESOURCE
title: PEP_ACPI_SPB_RESOURCE
author: windows-driver-content
description: The PEP_ACPI_SPB_RESOURCE structure describes an ACPI serial bus connection resource.
old-location: kernel\pep_acpi_spb_resource.htm
old-project: kernel
ms.assetid: D4C0009D-A9D0-4870-86C5-60DC9B5892BC
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PEP_ACPI_SPB_RESOURCE, PEP_ACPI_SPB_RESOURCE, *PPEP_ACPI_SPB_RESOURCE
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
req.alt-api: PEP_ACPI_SPB_RESOURCE
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

# PEP_ACPI_SPB_RESOURCE structure



## -description
<p>The <b>PEP_ACPI_SPB_RESOURCE</b> structure describes an ACPI serial bus connection resource.</p>


## -syntax

````
typedef struct _PEP_ACPI_SPB_RESOURCE {
  PEP_ACPI_RESOURCE_TYPE  Type;
  PEP_ACPI_RESOURCE_FLAGS Flags;
  USHORT                  TypeSpecificFlags;
  UCHAR                   ResourceSourceIndex;
  PUNICODE_STRING         ResourceSourceName;
  PCHAR                   VendorData;
  USHORT                  VendorDataLength;
} PEP_ACPI_SPB_RESOURCE, *PPEP_ACPI_SPB_RESOURCE;
````


## -struct-fields
<dl>

### -field Type

<dd>
<p>A <a href="..\pepfx\ne-pepfx--pep-acpi-resource-type.md">PEP_ACPI_RESOURCE_TYPE</a> enumeration value describing this resource.</p>
</dd>

### -field Flags

<dd>
<p>A <a href="..\pepfx\ns-pepfx--pep-acpi-resource-flags.md">PEP_ACPI_RESOURCE_FLAGS</a> structure that describes the capabilities of this ACPI resource.</p>
</dd>

### -field TypeSpecificFlags

<dd>
<p>Specifies the bit flags that are common to all serial bus connection types.</p>
<table>
<tr>
<th>Bit(s)</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="0_-_Slave_mode"></a><a id="0_-_slave_mode"></a><a id="0_-_SLAVE_MODE"></a><dl>

### -field 0 - Slave mode

</dl>
</td>
<td width="60%">
<p><b>0x0</b> - Indicates that communication over this connection is initiated by the controller.</p>
<p><b>0x1</b> - Indicates that communication over this connection is initiated by the device.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="1_-_Consumer_producer_mode"></a><a id="1_-_consumer_producer_mode"></a><a id="1_-_CONSUMER_PRODUCER_MODE"></a><dl>

### -field 1 - Consumer/producer mode

</dl>
</td>
<td width="60%">
<p><b>0x0</b> - Indicates that this device produces and consumes this resource.</p>
<p><b>0x1</b> - Indicates that this device consumes this resource.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="2_to_7_-_Reserved"></a><a id="2_to_7_-_reserved"></a><a id="2_TO_7_-_RESERVED"></a><dl>

### -field 2 to 7 - Reserved

</dl>
</td>
<td width="60%">
<p>These bits are reserved and must be set to zero.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field ResourceSourceIndex

<dd>Reserved. Must be set to zero..</dd>

### -field ResourceSourceName

<dd>
<p>The name of the serial bus controller device to which this
connection descriptor applies. The name can be a fully
qualified path, a relative path, or a simple name segment
that utilizes the namespace search rules.</p>
</dd>

### -field VendorData

<dd>
<p>A pointer to optional data that is specific to the serial bus connection type.</p>
</dd>

### -field VendorDataLength

<dd>
<p>The length of the buffer pointed to by <b>VendorData</b>.</p>
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