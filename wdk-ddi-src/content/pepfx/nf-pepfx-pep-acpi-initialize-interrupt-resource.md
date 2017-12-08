---
UID: NF.pepfx.PEP_ACPI_INITIALIZE_INTERRUPT_RESOURCE
title: PEP_ACPI_INITIALIZE_INTERRUPT_RESOURCE
author: windows-driver-content
description: The PEP_ACPI_INITIALIZE_INTERRUPT_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_INTERRUPT_RESOURCE structure.
old-location: kernel\pep_acpi_initialize_interrupt_resource.htm
old-project: kernel
ms.assetid: A89AB86B-4DC9-43ED-9EE6-1D4B693DAB91
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PEP_ACPI_INITIALIZE_INTERRUPT_RESOURCE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: pepfx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PEP_ACPI_INITIALIZE_INTERRUPT_RESOURCE
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
req.iface: 
---

# PEP_ACPI_INITIALIZE_INTERRUPT_RESOURCE function



## -description
<p>The <b>PEP_ACPI_INITIALIZE_INTERRUPT_RESOURCE</b> function initializes a platform extension plug-in's (PEP) <a href="..\pepfx\ns-pepfx--pep-acpi-interrupt-resource.md">PEP_ACPI_INTERRUPT_RESOURCE</a> structure.</p>


## -syntax

````
FORCEINLINE VOID PEP_ACPI_INITIALIZE_INTERRUPT_RESOURCE(
  _In_  BOOLEAN             ResourceUsage,
  _In_  KINTERRUPT_MODE     EdgeLevel,
  _In_  KINTERRUPT_POLARITY InterruptLevel,
  _In_  BOOLEAN             ShareType,
  _In_  BOOLEAN             Wake,
  _In_  PULONG              PinTable,
  _In_  UCHAR               PinCount,
  _Out_ PPEP_ACPI_RESOURCE  Resource
);
````


## -parameters
<dl>

### -param ResourceUsage [in]

<dd>
<p>Indicates if this device is in use.</p>
</dd>

### -param EdgeLevel [in]

<dd>
<p>A <a href="..\wdm\ne-wdm--kinterrupt-mode.md">KINTERRUPT_MODE</a> enumeration value that identifies the interrupt type.</p>
</dd>

### -param InterruptLevel [in]

<dd>
<p>A <a href="..\wdm\ne-wdm--kinterrupt-polarity.md">KINTERRUPT_POLARITY</a> enumeration value that identifies how a device signals an interrupt request on an interrupt line.</p>
</dd>

### -param ShareType [in]

<dd>
<p>Indicates if the device can be shared.</p>
</dd>

### -param Wake [in]

<dd>
<p>Indicates if the device can be woken from a low-power state.</p>
</dd>

### -param PinTable [in]

<dd>
<p>A list of pin numbers on the resource. </p>
</dd>

### -param PinCount [in]

<dd>
<p>The number of pins described by the <i>PinTable</i> parameter.</p>
</dd>

### -param Resource [out]

<dd>
<p>A pointer to the resource. The structure behind the pointer is of type <a href="..\pepfx\ns-pepfx--pep-acpi-interrupt-resource.md">PEP_ACPI_INTERRUPT_RESOURCE</a>.</p>
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
<a href="..\pepfx\ns-pepfx--pep-acpi-interrupt-resource.md">PEP_ACPI_INTERRUPT_RESOURCE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_ACPI_INITIALIZE_INTERRUPT_RESOURCE function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
