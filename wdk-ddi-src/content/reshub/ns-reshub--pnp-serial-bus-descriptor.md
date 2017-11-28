---
UID: NS.reshub._PNP_SERIAL_BUS_DESCRIPTOR
title: PNP_SERIAL_BUS_DESCRIPTOR
author: windows-driver-content
description: The PNP_SERIAL_BUS_DESCRIPTOR structure describes the physical connection of a target device to a serial bus (I2C, SPI, or UART).
old-location: spb\pnp_serial_bus_descriptor.htm
old-project: SPB
ms.assetid: 7516B493-F86E-44C5-ABCD-450B6F66AA15
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PNP_SERIAL_BUS_DESCRIPTOR, PNP_SERIAL_BUS_DESCRIPTOR, *PPNP_SERIAL_BUS_DESCRIPTOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: reshub.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PNP_SERIAL_BUS_DESCRIPTOR
req.alt-loc: Reshub.h
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
req.product: Windows 10 or later.
---

# PNP_SERIAL_BUS_DESCRIPTOR structure



## -description
<p>The <b>PNP_SERIAL_BUS_DESCRIPTOR</b> structure describes the physical connection of a target device to a serial bus (I2C, SPI, or UART).</p>


## -syntax

````
typedef struct _PNP_SERIAL_BUS_DESCRIPTOR {
  UCHAR  Tag;
  USHORT Length;
  UCHAR  RevisionId;
  UCHAR  ResourceSourceIndex;
  UCHAR  SerialBusType;
  UCHAR  GeneralFlags;
  USHORT TypeSpecificFlags;
  UCHAR  TypeSpecificRevisionId;
  USHORT TypeDataLength;
} PNP_SERIAL_BUS_DESCRIPTOR, *PPNP_SERIAL_BUS_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>Tag</b>

<dd>
<p>The serial bus type. This member is set to 0x8e for a serial bus (I2C, SPI, or UART) connection. For more information, see the description of the serial bus connection descriptor in revision 5.0 of the the Advanced Configuration and Power Interface Specification (ACPI 5.0) at the <a href="http://www.acpi.info">ACPI</a> website.</p>
</dd>

### -field <b>Length</b>

<dd>
<p>The length, in bytes, of the serial bus connection descriptor. To be consistent with the ACPI 5.0 specification, the byte count in the <b>Length</b> member of the <b>PNP_SERIAL_BUS_DESCRIPTOR</b> structure equals the structure size, minus the three bytes in the <b>Tag</b> and <b>Length</b> members at the start of the structure, plus the number of bytes of bus-type-specific data and Resource Source string that follow the structure. The Resource Source string, which is a required field, has a minimum size of two bytes (for a one-character Resource Source name and a terminating null). Thus, the minimum valid <b>Length</b> value is 11. For more information, see the ACPI 5.0 specification.</p>
</dd>

### -field <b>RevisionId</b>

<dd>
<p>The revision ID of the serial bus connection descriptor. This member is set to the SERIAL_BUS_DESCRIPTOR_REVISION constant, which is defined in the Reshub.h header file.</p>
</dd>

### -field <b>ResourceSourceIndex</b>

<dd>
<p>Reserved for future use. This member is unused and set to zero.</p>
</dd>

### -field <b>SerialBusType</b>

<dd>
<p>The serial bus type. This member is set to 1 (for I2C), 2 (for SPI), or 3 (for UART). Other values are either reserved for future use, or are defined by the hardware vendor. For more information, see the ACPI 5.0 specification.</p>
</dd>

### -field <b>GeneralFlags</b>

<dd>
<p>Flags that are common to all serial bus types. Bit 0 is the slave-mode flag. If this bit is set to 1, the communication of this connection is initiated by the bus controller; otherwise, the communication is initiated by the target device. Bit 1 is the consumer/producer flag, and is always set to 1. No other flag bits are currently defined. For more information, see the ACPI 5.0 specification.</p>
</dd>

### -field <b>TypeSpecificFlags</b>

<dd>
<p>Flags that are specific to the serial bus type. For an I2C bus, bit 0 is set if the connection uses 10-bit addresses; otherwise, the connection uses 7-bit addresses. No other flag bits are currently defined for I2C. For more information, see the ACPI 5.0 specification.</p>
</dd>

### -field <b>TypeSpecificRevisionId</b>

<dd>
<p>The revision ID of the variant of this structure that is used for the serial bus type (I2C, SPI, and UART) that is specified by the <b>Tag</b> member. Each serial bus type extends the <b>PNP_SERIAL_BUS_DESCRIPTOR</b> structure by adding fields that are specific to the bus type. For more information, see the ACPI 5.0 specification.</p>
</dd>

### -field <b>TypeDataLength</b>

<dd>
<p>The length, in bytes, of the bus-type-specific data that follows the <b>PNP_SERIAL_BUS_DESCRIPTOR</b> structure. This length value includes the data between the end of the <b>TypeDataLength</b> member and the start of the Resource Source string, but does not include the Resource Source string. For more information, see the ACPI 5.0 specification.</p>
</dd>
</dl>

## -remarks
<p>This structure defines the data fields in a serial bus connection descriptor, as described in section 6.4.3.8.2 of the ACPI 5.0 specification. This descriptor describes the bus connection to a target device that is connected to a serial bus (I2C, SPI, or UART).</p>

<p>For example, for a device on an I2C bus, the <b>PNP_SERIAL_BUS_DESCRIPTOR</b> structure (and its bus-type-specific extension) specify the bus address of the device, the address mode (7-bit or 10-bit), and the frequency at which to run the bus clock when the device is accessed. For a code example that shows how an I2C controller driver extracts this information from the structure, see <a href="NULL">How to Get the Connection Settings for a Device</a>.</p>

<p>The <b>PNP_SERIAL_BUS_DESCRIPTOR</b> structure definition in the Reshub.h header file is preceded by an include statement for the Pshpack1.h header file, which configures the compiler to pack adjacent structure members to byte boundaries, without intervening gaps. Software can then overlay the packed structure over the memory image of the serial bus connection descriptor to access the individual fields of this descriptor. The USHORT members of the structure might not be aligned to even byte boundaries in memory. The bytes in the USHORT members are stored in little-endian order for the x86, x64, and ARM processor architectures.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Reshub.h</dt>
</dl>
</td>
</tr>
</table>