---
UID: NE.pepfx._PEP_ACPI_RESOURCE_TYPE
title: PEP_ACPI_RESOURCE_TYPE
author: windows-driver-content
description: The PEP_ACPI_RESOURCE_TYPE enumeration is used to identify the type of ACPI resource that is contained in the PEP_ACPI_RESOURCE union.
old-location: kernel\pep_acpi_resource_type.htm
old-project: kernel
ms.assetid: C67FA5DF-D2E4-4F00-B22F-9218F0012708
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
req.alt-api: PEP_ACPI_RESOURCE_TYPE
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

# PEP_ACPI_RESOURCE_TYPE enumeration



## -description
<p>The <b>PEP_ACPI_RESOURCE_TYPE</b> enumeration is used to identify the type of ACPI resource that is contained in the <a href="https://msdn.microsoft.com/library/windows/hardware/mt186691">PEP_ACPI_RESOURCE</a> union. </p>


## -syntax

````
typedef enum _PEP_ACPI_RESOURCE_TYPE { 
  PepAcpiMemory,
  PepAcpiIoPort,
  PepAcpiInterrupt,
  PepAcpiGpioIo,
  PepAcpiGpioInt,
  PepAcpiSpbI2c,
  PepAcpiSpbSpi,
  PepAcpiSpbUart,
  PepAcpiExtendedMemory,
  PepAcpiExtendedIo
} PEP_ACPI_RESOURCE_TYPE;
````


## -enum-fields
<dl>

### -field <a id="PepAcpiMemory"></a><a id="pepacpimemory"></a><a id="PEPACPIMEMORY"></a><b>PepAcpiMemory</b>

<dd>
<p>Indicates that the resource is an ACPI memory resource.</p>
</dd>

### -field <a id="PepAcpiIoPort"></a><a id="pepacpiioport"></a><a id="PEPACPIIOPORT"></a><b>PepAcpiIoPort</b>

<dd>
<p>Indicates that the resource is an ACPI IO port resource.</p>
</dd>

### -field <a id="PepAcpiInterrupt"></a><a id="pepacpiinterrupt"></a><a id="PEPACPIINTERRUPT"></a><b>PepAcpiInterrupt</b>

<dd>
<p>Indicates that the resource is an ACPI interrupt resource.</p>
</dd>

### -field <a id="PepAcpiGpioIo"></a><a id="pepacpigpioio"></a><a id="PEPACPIGPIOIO"></a><b>PepAcpiGpioIo</b>

<dd>
<p>Indicates that the resource is an ACPI GPIO resource.</p>
</dd>

### -field <a id="PepAcpiGpioInt"></a><a id="pepacpigpioint"></a><a id="PEPACPIGPIOINT"></a><b>PepAcpiGpioInt</b>

<dd>
<p>Indicates that the resource is an ACPI GPIO interrupt resource.</p>
</dd>

### -field <a id="PepAcpiSpbI2c"></a><a id="pepacpispbi2c"></a><a id="PEPACPISPBI2C"></a><b>PepAcpiSpbI2c</b>

<dd>
<p>Indicates that the resource is an ACPI I2C serial bus resource.</p>
</dd>

### -field <a id="PepAcpiSpbSpi"></a><a id="pepacpispbspi"></a><a id="PEPACPISPBSPI"></a><b>PepAcpiSpbSpi</b>

<dd>
<p>Indicates that the resource is an ACPI SPI serial bus resource.</p>
</dd>

### -field <a id="PepAcpiSpbUart"></a><a id="pepacpispbuart"></a><a id="PEPACPISPBUART"></a><b>PepAcpiSpbUart</b>

<dd>
<p>Indicates that the resource is an ACPI UART serial bus resource.</p>
</dd>

### -field <a id="PepAcpiExtendedMemory"></a><a id="pepacpiextendedmemory"></a><a id="PEPACPIEXTENDEDMEMORY"></a><b>PepAcpiExtendedMemory</b>

<dd>
<p>Indicates that the resource is an ACPI extended memory resource.</p>
</dd>

### -field <a id="PepAcpiExtendedIo"></a><a id="pepacpiextendedio"></a><a id="PEPACPIEXTENDEDIO"></a><b>PepAcpiExtendedIo</b>

<dd>
<p>Indicates that the resource is an ACPI extended IO resource.</p>
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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186691">PEP_ACPI_RESOURCE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186690">PEP_ACPI_REQUEST_CONVERT_TO_BIOS_RESOURCES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_ACPI_RESOURCE_TYPE enumeration%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
