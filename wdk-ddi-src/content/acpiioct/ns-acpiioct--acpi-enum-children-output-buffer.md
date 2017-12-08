---
UID: NS.acpiioct._ACPI_ENUM_CHILDREN_OUTPUT_BUFFER
title: ACPI_ENUM_CHILDREN_OUTPUT_BUFFER
author: windows-driver-content
description: The ACPI_ENUM_CHILDREN_OUTPUT_BUFFER structure contains an array of object names in an ACPI namespace.
old-location: acpi\acpi_enum_children_output_buffer.htm
old-project: acpi
ms.assetid: e7e9fdae-4951-4878-a5b6-81d681eca472
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: ACPI_ENUM_CHILDREN_OUTPUT_BUFFER, ACPI_ENUM_CHILDREN_OUTPUT_BUFFER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: acpiioct.h
req.include-header: Acpiioct.h
req.target-type: Windows
req.target-min-winverclnt: Windows Vista and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ACPI_ENUM_CHILDREN_OUTPUT_BUFFER
req.alt-loc: Acpiioct.h
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
---

# ACPI_ENUM_CHILDREN_OUTPUT_BUFFER structure



## -description
<p>The ACPI_ENUM_CHILDREN_OUTPUT_BUFFER structure contains an array of object names in an ACPI namespace. </p>


## -syntax

````
typedef struct _ACPI_ENUM_CHILDREN_OUTPUT_BUFFER {
  ULONG           Signature;
  ULONG           NumberOfChildren;
  ACPI_ENUM_CHILD Children[ANYSIZE_ARRAY];
} ACPI_ENUM_CHILDREN_OUTPUT_BUFFER;
````


## -struct-fields
<dl>

### -field Signature

<dd>
<p>The signature of the output buffer, which must be set to ACPI_ENUM_CHILDREN_OUTPUT_BUFFER_SIGNATURE.</p>
</dd>

### -field NumberOfChildren

<dd>
<p>The number of elements of type <a href="..\acpiioct\ns-acpiioct--acpi-enum-child.md">ACPI_ENUM_CHILD</a> in the <b>Children</b> array.</p>
</dd>

### -field Children

<dd>
<p>An array of elements of type ACPI_ENUM_CHILD. Each ACPI_ENUM_CHILD structure contains the path and name of an object in the ACPI namespace.</p>
</dd>
</dl>

## -remarks
<p>A driver for a device uses an <a href="..\acpiioct\ni-acpiioct-ioctl-acpi-enum-children.md">IOCTL_ACPI_ENUM_CHILDREN</a> request to enumerate the child objects of the device. The enumerated child objects can be devices or any object of a supplied name. This request returns an ACPI_ENUM_CHILDREN_OUTPUT_BUFFER structure, which includes the <b>Children</b> member that contains an array of <a href="..\acpiioct\ns-acpiioct--acpi-enum-child.md">ACPI_ENUM_CHILD</a> structures. </p>

<p>For information about how to enumerate child objects of a device, see <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/acpi/enumerating-child-devices-and-control-methods">Enumerating Child Devices and Control Methods</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Windows Vista and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Acpiioct.h (include Acpiioct.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\acpiioct\ns-acpiioct--acpi-enum-child.md">ACPI_ENUM_CHILD</a>
</dt>
<dt>
<a href="..\acpiioct\ni-acpiioct-ioctl-acpi-enum-children.md">IOCTL_ACPI_ENUM_CHILDREN</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [acpi\acpi]:%20ACPI_ENUM_CHILDREN_OUTPUT_BUFFER structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
