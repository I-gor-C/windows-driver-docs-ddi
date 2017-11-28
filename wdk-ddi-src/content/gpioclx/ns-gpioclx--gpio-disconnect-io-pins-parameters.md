---
UID: NS.gpioclx._GPIO_DISCONNECT_IO_PINS_PARAMETERS
title: GPIO_DISCONNECT_IO_PINS_PARAMETERS
author: windows-driver-content
description: The GPIO_DISCONNECT_IO_PINS_PARAMETERS structure describes a set of general-purpose I/O (GPIO) pins that are to be disconnected.
old-location: gpio\gpio_disconnect_io_pins_parameters.htm
old-project: GPIO
ms.assetid: 79ABCF93-4EC3-49D5-9943-C820B0B8CF66
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.keywords: GPIO_DISCONNECT_IO_PINS_PARAMETERS, GPIO_DISCONNECT_IO_PINS_PARAMETERS, *PGPIO_DISCONNECT_IO_PINS_PARAMETERS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: gpioclx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GPIO_DISCONNECT_IO_PINS_PARAMETERS
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# GPIO_DISCONNECT_IO_PINS_PARAMETERS structure



## -description
<p>The <b>GPIO_DISCONNECT_IO_PINS_PARAMETERS</b> structure describes a set of general-purpose I/O (GPIO) pins that are to be disconnected.</p>


## -syntax

````
typedef struct _GPIO_DISCONNECT_IO_PINS_PARAMETERS {
  BANK_ID                       BankId;
  PPIN_NUMBER                   PinNumberTable;
  ULONG                         PinCount;
  GPIO_CONNECT_IO_PINS_MODE     DisconnectMode;
  GPIO_DISCONNECT_IO_PINS_FLAGS DisconnectFlags;
} GPIO_DISCONNECT_IO_PINS_PARAMETERS, *PGPIO_DISCONNECT_IO_PINS_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>BankId</b>

<dd>
<p>The identifier for the bank that contains the GPIO pins. If M is the number of banks in the GPIO controller, <b>BankId</b> is an integer in the range 0 to M–1. The GPIO framework extension (GpioClx) previously obtained the number of banks in the controller from the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439399">CLIENT_QueryControllerBasicInformation</a> event callback function. For more information, see Remarks in <a href="https://msdn.microsoft.com/library/windows/hardware/hh439358">CLIENT_CONTROLLER_BASIC_INFORMATION</a>.</p>
</dd>

### -field <b>PinNumberTable</b>

<dd>
<p>A pointer to an array of PIN_NUMBER values. Each array element specifies the number of a GPIO pin to disconnect from. If the GPIO controller has N pins, the pins are numbered 0 to N–1. The number of elements in this array is specified by the <b>PinCount</b> member.</p>
</dd>

### -field <b>PinCount</b>

<dd>
<p>The number of elements in the <b>PinNumberTable</b> array.</p>
</dd>

### -field <b>DisconnectMode</b>

<dd>
<p>Whether the GPIO pins in the connection that is being closed are configured as inputs or as outputs. The value of this member is <b>ConnectModeInput</b> for a read-only connection, <b>ConnectModeOutput</b> for a write-only connection, or (<b>ConnectModeInput</b> | <b>ConnectModeOutput</b>) for a read/write connection. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh439505">GPIO_CONNECT_IO_PINS_MODE</a>.</p>
</dd>

### -field <b>DisconnectFlags</b>

<dd>
<p>A set of flags that control how the GPIO pins are to be configured after they are closed. If the <b>PreserveConfiguration</b> flag bit is set, the GPIO controller driver preserves the configuration of the pins after they are disconnected. For more information, see Remarks.</p>
</dd>
</dl>

## -remarks
<p>The <i>DisconnectParameters</i> parameter to the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439374">CLIENT_DisconnectIoPins</a> event callback routine is a pointer to a <b>GPIO_CONNECT_IO_PINS_PARAMETERS</b> structure.</p>

<p>By default, when a GPIO I/O pin is disconnected, the GPIO controller driver configures the pin in a platform-specific initial state. The pin is typically configured in a low-power state to reduce the load on the battery. However, the <b>PreserveConfiguration</b> flag can be used to override this default behavior. The flag tells the GPIO controller driver to preserve the configuration of the I/O pins that are being disconnected.</p>

<p>For example, a peripheral device driver might open a logical connection to a GPIO I/O pin that is configured as an output, and then write a bit value of 1 to the pin. The <b>PreserveConfiguration</b> flag enables the driver to close the connection without altering the pin's output level. Later, if the driver needs to change the output level of the pin from 1 to 0, the driver opens a new connection to the pin.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439358">CLIENT_CONTROLLER_BASIC_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439374">CLIENT_DisconnectIoPins</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439399">CLIENT_QueryControllerBasicInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439505">GPIO_CONNECT_IO_PINS_MODE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [GPIO\parports]:%20GPIO_DISCONNECT_IO_PINS_PARAMETERS structure%20 RELEASE:%20(11/3/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
