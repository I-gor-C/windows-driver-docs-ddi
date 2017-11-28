---
UID: NS.pepfx._PEP_ACPI_OBJECT_NAME
title: PEP_ACPI_OBJECT_NAME
author: windows-driver-content
description: The PEP_ACPI_OBJECT_NAME union contains the four-character name of an ACPI object.
old-location: kernel\pep_acpi_object_name.htm
old-project: kernel
ms.assetid: 55D8A977-DA91-4CB5-8549-E1CB1731256C
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: PEP_ACPI_OBJECT_NAME, PEP_ACPI_OBJECT_NAME, *PPEP_ACPI_OBJECT_NAME
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
req.alt-api: PEP_ACPI_OBJECT_NAME
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

# PEP_ACPI_OBJECT_NAME structure



## -description
<p>The <b>PEP_ACPI_OBJECT_NAME</b> union contains the four-character name of an ACPI object.</p>


## -syntax

````
typedef union _PEP_ACPI_OBJECT_NAME {
  UCHAR ObjectName[4];
  ULONG ObjectNameAsUlong;
} PEP_ACPI_OBJECT_NAME;
````


## -struct-fields
<dl>

### -field <b>ObjectName</b>

<dd>
<p>The object name stored as an array of four 8-bit unsigned characters.</p>
</dd>

### -field <b>ObjectNameAsUlong</b>

<dd>
<p>The object name stored as a single 32-bit unsigned integer value.</p>
</dd>
</dl>

## -remarks
<p>The <i>Name</i> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt186684">PEP_ACPI_OBJECT_NAME_WITH_TYPE</a> structure is a <b>PEP_ACPI_OBJECT_NAME</b> union. Also, the <i>Name</i> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt186688">PEP_ACPI_QUERY_OBJECT_INFORMATION</a> structure is a <b>PEP_ACPI_OBJECT_NAME</b> union.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186684">PEP_ACPI_OBJECT_NAME_WITH_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186688">PEP_ACPI_QUERY_OBJECT_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_ACPI_OBJECT_NAME union%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
