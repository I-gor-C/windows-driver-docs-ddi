---
UID: NE.pepfx._PEP_ACPI_OBJECT_TYPE
title: PEP_ACPI_OBJECT_TYPE
author: windows-driver-content
description: The PEP_ACPI_OBJECT_TYPE enumeration indicates the type of ACPI object.
old-location: kernel\pep_acpi_object_type.htm
old-project: kernel
ms.assetid: 81875C20-8E0E-4BAC-B85F-3D275F8B4708
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: VPCI_PNP_ID, VPCI_PNP_ID, *PVPCI_PNP_ID
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: pepfx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PEP_ACPI_OBJECT_TYPE
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
req.irql: See Remarks.
req.iface: 
---

# PEP_ACPI_OBJECT_TYPE enumeration



## -description
<p>The <b>PEP_ACPI_OBJECT_TYPE</b> enumeration indicates the type of ACPI object.</p>


## -syntax

````
typedef enum _PEP_ACPI_OBJECT_TYPE { 
  PepAcpiObjectTypeMethod,
  PepAcpiObjectTypeMaximum
} PEP_ACPI_OBJECT_TYPE;
````


## -enum-fields
<dl>

### -field <a id="PepAcpiObjectTypeMethod"></a><a id="pepacpiobjecttypemethod"></a><a id="PEPACPIOBJECTTYPEMETHOD"></a><b>PepAcpiObjectTypeMethod</b>

<dd>
<p>The object is an ACPI control method.</p>
</dd>

### -field <a id="PepAcpiObjectTypeMaximum"></a><a id="pepacpiobjecttypemaximum"></a><a id="PEPACPIOBJECTTYPEMAXIMUM"></a><b>PepAcpiObjectTypeMaximum</b>

<dd>
<p>Reserved for use by the operating system.</p>
</dd>
</dl>

## -remarks
<p>The <b>Type</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt186688">PEP_ACPI_QUERY_OBJECT_INFORMATION</a> structure is an <b>PEP_ACPI_OBJECT_TYPE</b> enumeration value.</p>

<p>The <b>Type</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt186688">PEP_ACPI_QUERY_OBJECT_INFORMATION</a> structure is an <b>PEP_ACPI_OBJECT_TYPE</b> enumeration value.</p>

<p>The <b>Type</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt186688">PEP_ACPI_QUERY_OBJECT_INFORMATION</a> structure is an <b>PEP_ACPI_OBJECT_TYPE</b> enumeration value.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186688">PEP_ACPI_QUERY_OBJECT_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_ACPI_OBJECT_TYPE enumeration%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
