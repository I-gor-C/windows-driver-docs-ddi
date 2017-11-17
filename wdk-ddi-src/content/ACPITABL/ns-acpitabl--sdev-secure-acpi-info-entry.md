---
UID: NS.acpitabl._SDEV_SECURE_ACPI_INFO_ENTRY
title: SDEV_SECURE_ACPI_INFO_ENTRY
author: windows-driver-content
description: Defines an information entry for a secure ACPI device for use in a secure device table.
old-location: acpi\sdev_secure_acpi_info_entry.htm
ms.assetid: A3FDE9B0-DD6E-4FF5-AD9A-7DF7BF276EFA
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: acpi
req.header: acpitabl.h
req.include-header: Acpitabl.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SDEV_SECURE_ACPI_INFO_ENTRY
req.alt-loc: acpitabl.h
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
ms.keywords: SDEV_SECURE_ACPI_INFO_ENTRY, SDEV_SECURE_ACPI_INFO_ENTRY, *PSDEV_SECURE_ACPI_INFO_ENTRY
---

# SDEV_SECURE_ACPI_INFO_ENTRY structure



## -description
<p>Defines an information entry for a secure ACPI device for use in a secure device table.</p>


## -syntax

````
typedef struct _SDEV_SECURE_ACPI_INFO_ENTRY {
  SDEV_ENTRY_HEADER Header;
  USHORT            IdentifierOffset;
  USHORT            IdentifierLength;
  USHORT            VendorInfoOffset;
  USHORT            VendorInfoLength;
} SDEV_SECURE_ACPI_INFO_ENTRY, *PSDEV_SECURE_ACPI_INFO_ENTRY;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>A header. </p>
</dd>

### -field <b>IdentifierOffset</b>

<dd>
<p>An identifier offset value.</p>
</dd>

### -field <b>IdentifierLength</b>

<dd>
<p>The length of the identifier.</p>
</dd>

### -field <b>VendorInfoOffset</b>

<dd>
<p>A vendor information offset value.</p>
</dd>

### -field <b>VendorInfoLength</b>

<dd>
<p>The length of the vendor information. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Acpitabl.h (include Acpitabl.h)</dt>
</dl>
</td>
</tr>
</table>