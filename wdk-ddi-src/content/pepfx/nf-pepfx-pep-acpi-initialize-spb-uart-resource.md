---
UID: NF.pepfx.PEP_ACPI_INITIALIZE_SPB_UART_RESOURCE
title: PEP_ACPI_INITIALIZE_SPB_UART_RESOURCE
author: windows-driver-content
description: The PEP_ACPI_INITIALIZE_SPB_UART_RESOURCE function initializes a platform extension plug-in's (PEP) PEP_ACPI_SPB_UART_RESOURCE structure.
old-location: kernel\pep_acpi_initialize_spb_uart_resource.htm
old-project: kernel
ms.assetid: C1018E89-D3EC-49A0-B02E-254378000378
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PEP_ACPI_INITIALIZE_SPB_UART_RESOURCE
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
req.alt-api: PEP_ACPI_INITIALIZE_SPB_UART_RESOURCE
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

# PEP_ACPI_INITIALIZE_SPB_UART_RESOURCE function



## -description
<p>The <b>PEP_ACPI_INITIALIZE_SPB_UART_RESOURCE</b> function initializes a platform extension plug-in's (PEP) <a href="..\pepfx\ns-pepfx--pep-acpi-spb-uart-resource.md">PEP_ACPI_SPB_UART_RESOURCE</a> structure.</p>


## -syntax

````
FORCEINLINE VOID PEP_ACPI_INITIALIZE_SPB_UART_RESOURCE(
  _In_  ULONG              BaudRate,
  _In_  UCHAR              BitsPerByte,
  _In_  UCHAR              StopBits,
  _In_  UCHAR              LinesInUse,
  _In_  UCHAR              IsBigEndian,
  _In_  UCHAR              Parity,
  _In_  UCHAR              FlowControl,
  _In_  USHORT             RxSize,
  _In_  USHORT             TxSize,
  _In_  PUNICODE_STRING    ResourceSource,
  _In_  UCHAR              ResourceSourceIndex,
  _In_  BOOLEAN            ResourceUsage,
  _In_  BOOLEAN            SharedMode,
  _In_  PCHAR              VendorData,
  _In_  USHORT             VendorDataLength,
  _Out_ PPEP_ACPI_RESOURCE Resource
);
````


## -parameters
<dl>

### -param BaudRate [in]

<dd>
<p>Specifies the baud rate of the connection.</p>
</dd>

### -param BitsPerByte [in]

<dd>
<p>Specifies the number of bits per byte of data.</p>
</dd>

### -param StopBits [in]

<dd>
<p>Specifies the stop bits used in the connection.</p>
</dd>

### -param LinesInUse [in]

<dd>
<p>Flag indicating the serial lines that are enabled. A value of 1 in the bit positions indicates that the line is enabled.</p>
<table>
<tr>
<th>Bit</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="0"></a><dl>

### -param 0

</dl>
</td>
<td width="60%">
<p>This bit is reserved and must be set to zero.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="1"></a><dl>

### -param 1

</dl>
</td>
<td width="60%">
<p>This bit is reserved and must be set to zero.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="2"></a><dl>

### -param 2

</dl>
</td>
<td width="60%">
<p>Data Carrier Detect (DTD)</p>
</td>
</tr>
<tr>
<td width="40%"><a id="3"></a><dl>

### -param 3

</dl>
</td>
<td width="60%">
<p>Ring Indicator (RI)</p>
</td>
</tr>
<tr>
<td width="40%"><a id="4"></a><dl>

### -param 4

</dl>
</td>
<td width="60%">
<p>Data Set Ready (DSR)</p>
</td>
</tr>
<tr>
<td width="40%"><a id="5"></a><dl>

### -param 5

</dl>
</td>
<td width="60%">
<p>Data Terminal Ready (DTR)</p>
</td>
</tr>
<tr>
<td width="40%"><a id="6"></a><dl>

### -param 6

</dl>
</td>
<td width="60%">
<p>Clear to Send (CTS)</p>
</td>
</tr>
<tr>
<td width="40%"><a id="7"></a><dl>

### -param 7

</dl>
</td>
<td width="60%">
<p>Request to Send (RTS)</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param IsBigEndian [in]

<dd>
<p>Indicates if the most significant bits of data are in the lowest address. </p>
</dd>

### -param Parity [in]

<dd>
<p>Specifies the parity of the connection.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%">
<dl>

### -param 0x00

</dl>
</td>
<td width="60%">
<p>None</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -param 0x01

</dl>
</td>
<td width="60%">
<p>Even</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -param 0x02

</dl>
</td>
<td width="60%">
<p>Odd</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -param 0x03

</dl>
</td>
<td width="60%">
<p>Mark</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -param 0x04

</dl>
</td>
<td width="60%">
<p>Space</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param FlowControl [in]

<dd>
<p>Specifies the type of flow control used by the connection.</p>
</dd>

### -param RxSize [in]

<dd>
<p>Specifies the maximum receive buffer size, in bytes, that is supported by this connection.</p>
</dd>

### -param TxSize [in]

<dd>
<p>Specifies the maximum transmit buffer size, in bytes, that is supported by this connection.</p>
</dd>

### -param ResourceSource [in]

<dd>
<p>The name of the serial bus controller device to which this
connection descriptor applies. The name can be a fully
qualified path, a relative path, or a simple name segment
that utilizes the namespace search rules.</p>
</dd>

### -param ResourceSourceIndex [in]

<dd>
<p>This parameter should always be zero.</p>
</dd>

### -param ResourceUsage [in]

<dd>
<p>Indicates if this resource is in use.</p>
</dd>

### -param SharedMode [in]

<dd>
<p>Indicates if this resource is shared.</p>
</dd>

### -param VendorData [in]

<dd>
<p>A pointer to optional data that is specific to the serial bus connection type.</p>
</dd>

### -param VendorDataLength [in]

<dd>
<p>The length of the buffer pointed to by the <i>VendorData</i> parameter.</p>
</dd>

### -param Resource [out]

<dd>
<p>A pointer to the resource. The structure behind the pointer is of type <a href="..\pepfx\ns-pepfx--pep-acpi-spb-uart-resource.md">PEP_ACPI_SPB_UART_RESOURCE</a>.</p>
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
<a href="..\pepfx\ns-pepfx--pep-acpi-spb-uart-resource.md">PEP_ACPI_SPB_UART_RESOURCE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_ACPI_INITIALIZE_SPB_UART_RESOURCE function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
