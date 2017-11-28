---
UID: NS.pepfx._PEP_ACPI_RESOURCE
title: PEP_ACPI_RESOURCE
author: windows-driver-content
description: The PEP_ACPI_RESOURCE structure contains hardware details for a specific ACPI resource.
old-location: kernel\pep_acpi_resource.htm
old-project: kernel
ms.assetid: 534F736D-906C-48B5-9CEE-0E37459DA03F
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: PEP_ACPI_RESOURCE, PEP_ACPI_RESOURCE, *PPEP_ACPI_RESOURCE
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
req.alt-api: PEP_ACPI_RESOURCE
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

# PEP_ACPI_RESOURCE structure



## -description
<p>The <b>PEP_ACPI_RESOURCE</b> structure contains hardware details for a specific ACPI resource.</p>


## -syntax

````
typedef union _PEP_ACPI_RESOURCE {
  PEP_ACPI_RESOURCE_TYPE      Type;
  PEP_ACPI_IO_MEMORY_RESOURCE IoMemory;
  PEP_ACPI_INTERRUPT_RESOURCE Interrupt;
  PEP_ACPI_GPIO_RESOURCE      Gpio;
  PEP_ACPI_SPB_I2C_RESOURCE   SpbI2c;
  PEP_ACPI_SPB_SPI_RESOURCE   SpbSpi;
  PEP_ACPI_SPB_UART_RESOURCE  SpbUart;
  PEP_ACPI_EXTENDED_ADDRESS   ExtendedAddress;
} PEP_ACPI_RESOURCE, *PPEP_ACPI_RESOURCE;
````


## -struct-fields
<dl>

### -field <b>Type</b>

<dd>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/mt186693">PEP_ACPI_RESOURCE_TYPE</a> enumeration value that is applicable to  this resource.</p>
</dd>

### -field <b>IoMemory</b>

<dd>
<p>If <b>Type</b> is <b>PepAcpiMemory</b> or <b>PepAcpiIoPort</b>, this union contains a <a href="https://msdn.microsoft.com/library/windows/hardware/mt186683">PEP_ACPI_IO_MEMORY_RESOURCE</a> structure describing an ACPI IO or memory resource. </p>
</dd>

### -field <b>Interrupt</b>

<dd>
<p>If <b>Type</b> is <b>PepAcpiInterrupt</b>, this union contains a <a href="https://msdn.microsoft.com/library/windows/hardware/mt186682">PEP_ACPI_INTERRUPT_RESOURCE</a> structure describing an ACPI interrupt resource. </p>
</dd>

### -field <b>Gpio</b>

<dd>
<p>If <b>Type</b> is <b>PepAcpiGpioIo</b> or <b>PepAcpiGpioInt</b>, this union contains a <a href="https://msdn.microsoft.com/library/windows/hardware/mt186671">PEP_ACPI_GPIO_RESOURCE</a> structure describing an ACPI GPIO resource. </p>
</dd>

### -field <b>SpbI2c</b>

<dd>
<p>If <b>Type</b> is <b>PepAcpiSpbI2c</b>, this union contains a <a href="https://msdn.microsoft.com/library/windows/hardware/mt186694">PEP_ACPI_SPB_I2C_RESOURCE</a> structure describing an ACPI I2C serial bus resource. </p>
</dd>

### -field <b>SpbSpi</b>

<dd>
<p>If <b>Type</b> is <b>PepAcpiSpbSpi</b>, this union contains a <a href="https://msdn.microsoft.com/library/windows/hardware/mt186696">PEP_ACPI_SPB_SPI_RESOURCE</a> structure describing an ACPI SPI serial bus resource. </p>
</dd>

### -field <b>SpbUart</b>

<dd>
<p>If <b>Type</b> is <b>PepAcpiSpbUart</b>, this union contains a <a href="https://msdn.microsoft.com/library/windows/hardware/mt186697">PEP_ACPI_SPB_UART_RESOURCE</a> structure describing an ACPI SPB serial bus resource. </p>
</dd>

### -field <b>ExtendedAddress</b>

<dd>
<p>If <b>Type</b> is <b>PepAcpiExtendedMemory</b> or <b>PepAcpiExtendedIo</b>, this union contains a <a href="https://msdn.microsoft.com/library/windows/hardware/mt186670">PEP_ACPI_EXTENDED_ADDRESS</a> structure describing an ACPI extended memory or extended IO resource. </p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186693">PEP_ACPI_RESOURCE_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186683">PEP_ACPI_IO_MEMORY_RESOURCE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186682">PEP_ACPI_INTERRUPT_RESOURCE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186671">PEP_ACPI_GPIO_RESOURCE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186694">PEP_ACPI_SPB_I2C_RESOURCE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186696">PEP_ACPI_SPB_SPI_RESOURCE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186697">PEP_ACPI_SPB_UART_RESOURCE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186670">PEP_ACPI_EXTENDED_ADDRESS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_ACPI_RESOURCE union%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
