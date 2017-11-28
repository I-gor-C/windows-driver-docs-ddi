---
UID: NS.pepfx._PEP_ACPI_SPB_UART_RESOURCE
title: PEP_ACPI_SPB_UART_RESOURCE
author: windows-driver-content
description: The PEP_ACPI_SPB_UART_RESOURCE structure describes an ACPI UART serial bus resource.
old-location: kernel\pep_acpi_spb_uart_resource.htm
old-project: kernel
ms.assetid: 3E8C7E47-EFCD-4261-9258-61C6A262287A
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: PEP_ACPI_SPB_UART_RESOURCE, PEP_ACPI_SPB_UART_RESOURCE, *PPEP_ACPI_SPB_UART_RESOURCE
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
req.alt-api: PEP_ACPI_SPB_UART_RESOURCE
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

# PEP_ACPI_SPB_UART_RESOURCE structure



## -description
<p>The <b>PEP_ACPI_SPB_UART_RESOURCE</b> structure describes an ACPI UART serial bus resource.</p>


## -syntax

````
typedef struct _PEP_ACPI_SPB_UART_RESOURCE {
  PEP_ACPI_SPB_RESOURCE SpbCommon;
  ULONG                 BaudRate;
  USHORT                RxBufferSize;
  USHORT                TxBufferSize;
  UCHAR                 Parity;
  UCHAR                 LinesInUse;
} PEP_ACPI_SPB_UART_RESOURCE, *PPEP_ACPI_SPB_UART_RESOURCE;
````


## -struct-fields
<dl>

### -field <b>SpbCommon</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/mt186695">PEP_ACPI_SPB_RESOURCE</a> structure describing this resource.</p>
</dd>

### -field <b>BaudRate</b>

<dd>
<p>The baud rate of the connection.</p>
</dd>

### -field <b>RxBufferSize</b>

<dd>
<p>The maximum receive buffer size, in bytes, that is supported by this connection.</p>
</dd>

### -field <b>TxBufferSize</b>

<dd>
<p>The maximum transmit buffer size, in bytes, that is supported by this connection.</p>
</dd>

### -field <b>Parity</b>

<dd>
<p>Indicates the parity of the connection.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%">
<dl>

### -field 0x00

</dl>
</td>
<td width="60%">
<p>None</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 0x01

</dl>
</td>
<td width="60%">
<p>Even</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 0x02

</dl>
</td>
<td width="60%">
<p>Odd</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 0x03

</dl>
</td>
<td width="60%">
<p>Mark</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 0x04

</dl>
</td>
<td width="60%">
<p>Space</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>LinesInUse</b>

<dd>
<p>Flag indicating the serial lines that are enabled. A value of 1 in the bit positions indicates that the line is enabled.</p>
<table>
<tr>
<th>Bit</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="0"></a><dl>

### -field <b>0</b>

</dl>
</td>
<td width="60%">
<p>This bit is reserved and must be set to zero.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="1"></a><dl>

### -field <b>1</b>

</dl>
</td>
<td width="60%">
<p>This bit is reserved and must be set to zero.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="2"></a><dl>

### -field <b>2</b>

</dl>
</td>
<td width="60%">
<p>Data Carrier Detect (DTD)</p>
</td>
</tr>
<tr>
<td width="40%"><a id="3"></a><dl>

### -field <b>3</b>

</dl>
</td>
<td width="60%">
<p>Ring Indicator (RI)</p>
</td>
</tr>
<tr>
<td width="40%"><a id="4"></a><dl>

### -field <b>4</b>

</dl>
</td>
<td width="60%">
<p>Data Set Ready (DSR)</p>
</td>
</tr>
<tr>
<td width="40%"><a id="5"></a><dl>

### -field <b>5</b>

</dl>
</td>
<td width="60%">
<p>Data Terminal Ready (DTR)</p>
</td>
</tr>
<tr>
<td width="40%"><a id="6"></a><dl>

### -field <b>6</b>

</dl>
</td>
<td width="60%">
<p>Clear to Send (CTS)</p>
</td>
</tr>
<tr>
<td width="40%"><a id="7"></a><dl>

### -field <b>7</b>

</dl>
</td>
<td width="60%">
<p>Request to Send (RTS)</p>
</td>
</tr>
</table>
<p> </p>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_ACPI_SPB_UART_RESOURCE structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
