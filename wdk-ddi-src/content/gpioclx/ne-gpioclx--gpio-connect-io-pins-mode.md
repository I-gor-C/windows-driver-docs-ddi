---
UID: NE.gpioclx._GPIO_CONNECT_IO_PINS_MODE
title: GPIO_CONNECT_IO_PINS_MODE
author: windows-driver-content
description: The GPIO_CONNECT_IO_PINS_MODE enumeration indicates whether a set of general-purpose I/O (GPIO) pins is configured as inputs or outputs.
old-location: gpio\gpio_connect_io_pins_mode.htm
old-project: GPIO
ms.assetid: 17E98D35-8C63-4EEC-B8DD-896FA2B084A8
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.keywords: PGNSS_V2UPL_NI_INFO, GNSS_V2UPL_NI_INFO, *PGNSS_V2UPL_NI_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: gpioclx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GPIO_CONNECT_IO_PINS_MODE
req.alt-loc: Gpioclx.h
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

# GPIO_CONNECT_IO_PINS_MODE enumeration



## -description
<p>The <b>GPIO_CONNECT_IO_PINS_MODE</b> enumeration indicates whether a set of general-purpose I/O (GPIO) pins is configured as inputs or outputs.</p>


## -syntax

````
typedef enum _GPIO_CONNECT_IO_PINS_MODE { 
  ConnectModeInvalid,
  ConnectModeInput,
  ConnectModeOutput,
  ConnectModeMaximum  = ConnectModeOutput
} GPIO_CONNECT_IO_PINS_MODE;
````


## -enum-fields
<dl>

### -field <a id="ConnectModeInvalid"></a><a id="connectmodeinvalid"></a><a id="CONNECTMODEINVALID"></a><b>ConnectModeInvalid</b>

<dd>
<p>The connection mode (input or output) for this set of GPIO pins is uninitialized.</p>
</dd>

### -field <a id="ConnectModeInput"></a><a id="connectmodeinput"></a><a id="CONNECTMODEINPUT"></a><b>ConnectModeInput</b>

<dd>
<p>This set of GPIO pins is configured as data inputs.</p>
</dd>

### -field <a id="ConnectModeOutput"></a><a id="connectmodeoutput"></a><a id="CONNECTMODEOUTPUT"></a><b>ConnectModeOutput</b>

<dd>
<p>This set of GPIO pins is configured as data outputs.</p>
</dd>

### -field <a id="ConnectModeMaximum"></a><a id="connectmodemaximum"></a><a id="CONNECTMODEMAXIMUM"></a><b>ConnectModeMaximum</b>

<dd>
<p>The maximum value in the enumeration.</p>
</dd>
</dl>

## -remarks
<p>The <b>ConnectMode</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439502">GPIO_CONNECT_IO_PINS_PARAMETERS</a> structure contains a <b>GPIO_CONNECT_IO_PINS_MODE</b> enumeration constant.</p>

<p>The <b>ConnectModeInput</b> enumeration constant labels a set of GPIO pins that can be read by an <a href="https://msdn.microsoft.com/library/windows/hardware/hh406483">IOCTL_GPIO_READ_PINS</a> request. <b>ConnectModeOutput</b> labels a set of GPIO pins that can be written to by an <a href="https://msdn.microsoft.com/library/windows/hardware/hh406487">IOCTL_GPIO_WRITE_PINS</a> request.</p>

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
<dt>Gpioclx.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439502">GPIO_CONNECT_IO_PINS_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406483">IOCTL_GPIO_READ_PINS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406487">IOCTL_GPIO_WRITE_PINS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [GPIO\parports]:%20GPIO_CONNECT_IO_PINS_MODE enumeration%20 RELEASE:%20(11/3/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
