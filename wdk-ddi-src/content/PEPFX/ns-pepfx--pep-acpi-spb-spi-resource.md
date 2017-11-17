---
UID: NS.pepfx._PEP_ACPI_SPB_SPI_RESOURCE
title: PEP_ACPI_SPB_SPI_RESOURCE
author: windows-driver-content
description: The PEP_ACPI_SPB_SPI_RESOURCE structure describes an ACPI SPI serial bus resource.
old-location: kernel\pep_acpi_spb_spi_resource.htm
ms.assetid: 75CD5462-8382-4E83-ADC1-3E1B811A0D60
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: kernel
req.header: pepfx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PEP_ACPI_SPB_SPI_RESOURCE
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
ms.keywords: PEP_ACPI_SPB_SPI_RESOURCE, PEP_ACPI_SPB_SPI_RESOURCE, *PPEP_ACPI_SPB_SPI_RESOURCE
req.iface: 
---

# PEP_ACPI_SPB_SPI_RESOURCE structure



## -description
<p>The <b>PEP_ACPI_SPB_SPI_RESOURCE</b> structure describes an ACPI SPI serial bus resource.</p>


## -syntax

````
typedef struct _PEP_ACPI_SPB_SPI_RESOURCE {
  PEP_ACPI_SPB_RESOURCE SpbCommon;
  ULONG                 ConnectionSpeed;
  UCHAR                 DataBitLength;
  UCHAR                 Phase;
  UCHAR                 Polarity;
  USHORT                DeviceSelection;
} PEP_ACPI_SPB_SPI_RESOURCE, *PPEP_ACPI_SPB_SPI_RESOURCE;
````


## -struct-fields
<dl>

### -field <b>SpbCommon</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/mt186695">PEP_ACPI_SPB_RESOURCE</a> structure describing this resource.</p>
</dd>

### -field <b>ConnectionSpeed</b>

<dd>
<p>The maximum speed, in hertz, supported by this connection.</p>
</dd>

### -field <b>DataBitLength</b>

<dd>
<p>The size, in bits, of the smallest unit of transfer.</p>
</dd>

### -field <b>Phase</b>

<dd>
<p>The phase of the clock pulse on which to capture data.</p>
</dd>

### -field <b>Polarity</b>

<dd>
<p>The polarity of the clock. If zero, this indicates the
clock is low during the first phase. If 1, this indicates the
clock is high during the first phase.</p>
</dd>

### -field <b>DeviceSelection</b>

<dd>
<p>The device selection value. This value is
specific to the device and may refer to a chip-select line, GPIO
line, or other line selection mechanism.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186695">PEP_ACPI_SPB_RESOURCE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_ACPI_SPB_SPI_RESOURCE structure%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
