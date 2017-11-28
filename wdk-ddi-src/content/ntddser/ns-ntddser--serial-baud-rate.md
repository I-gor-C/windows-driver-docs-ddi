---
UID: NS.ntddser._SERIAL_BAUD_RATE
title: SERIAL_BAUD_RATE
author: windows-driver-content
description: The SERIAL_BAUD_RATE structure specifies the baud rate at which a serial port is currently configured to transmit and receive data.
old-location: serports\serial_baud_rate.htm
old-project: serports
ms.assetid: 1534B7AC-8968-4AE2-A871-D8F4D4E45CA1
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: SERIAL_BAUD_RATE, SERIAL_BAUD_RATE, *PSERIAL_BAUD_RATE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddser.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SERIAL_BAUD_RATE
req.alt-loc: Ntddser.h
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

# SERIAL_BAUD_RATE structure



## -description
<p>The <b>SERIAL_BAUD_RATE</b> structure specifies the baud rate at which a serial port is currently configured to transmit and receive data.</p>


## -syntax

````
typedef struct _SERIAL_BAUD_RATE {
  ULONG BaudRate;
} SERIAL_BAUD_RATE, *PSERIAL_BAUD_RATE;
````


## -struct-fields
<dl>

### -field <b>BaudRate</b>

<dd>
<p>The baud rate. This parameter specifies the number of bits per second that a serial port is currently configured to transmit or receive. For example, a <b>BaudRate</b> value of 115200 indicates that the port is configured to transfer 115,200 bits per second.</p>
</dd>
</dl>

## -remarks
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff546554">IOCTL_SERIAL_GET_BAUD_RATE</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff546672">IOCTL_SERIAL_SET_BAUD_RATE</a> I/O control requests use the <b>SERIAL_BAUD_RATE</b> structure to specify the baud rate of a serial port. The <b>IOCTL_SERIAL_SET_BAUD_RATE</b> request configures a serial port to operate at a specified baud rate. The <b>IOCTL_SERIAL_GET_BAUD_RATE</b> request queries a serial port for the baud rate that it is currently configured to operate at.</p>

<p>For more information about some of the possible baud rates that a serial controller driver might support, see the description of the <b>MaxBaud</b> member in <a href="https://msdn.microsoft.com/library/windows/hardware/jj680684">SERIAL_COMMPROP</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddser.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546554">IOCTL_SERIAL_GET_BAUD_RATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546672">IOCTL_SERIAL_SET_BAUD_RATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj680684">SERIAL_COMMPROP</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [serports\serports]:%20SERIAL_BAUD_RATE structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
