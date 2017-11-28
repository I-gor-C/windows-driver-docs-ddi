---
UID: NF.ucmtcpcidevice.UCMTCPCI_DEVICE_CONFIG_INIT
title: UCMTCPCI_DEVICE_CONFIG_INIT
author: windows-driver-content
description: Initializes the UCMTCPCI_DEVICE_CONFIG structure.
old-location: buses\ucmtcpci_device_config_init.htm
old-project: usbref
ms.assetid: 8845f8f7-683e-487b-924b-596dbbfb98f2
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UCMTCPCI_DEVICE_CONFIG_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ucmtcpcidevice.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UCMTCPCI_DEVICE_CONFIG_INIT
req.alt-loc: ucmtcpcidevice.h
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
req.product: Windows 10 or later.
---

# UCMTCPCI_DEVICE_CONFIG_INIT function



## -description
<p>
                        Initializes the <a href="https://msdn.microsoft.com/library/windows/hardware/mt805896">UCMTCPCI_DEVICE_CONFIG</a> structure.
                </p>


## -syntax

````
VOID UCMTCPCI_DEVICE_CONFIG_INIT(
  _Out_ PUCMTCPCI_DEVICE_CONFIG Config
);
````


## -parameters
<dl>

### -param <i>Config</i> [out]

<dd>
<p>A pointer to the driver-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/mt805896">UCMTCPCI_DEVICE_CONFIG</a> structure.</p>
</dd>
</dl>

## -returns
<p>This method does not return a value.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ucmtcpcidevice.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt805841">UcmTcpciDeviceInitialize</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UCMTCPCI_DEVICE_CONFIG_INIT method%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
