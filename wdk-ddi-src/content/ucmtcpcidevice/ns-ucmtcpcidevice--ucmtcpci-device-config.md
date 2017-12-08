---
UID: NS.ucmtcpcidevice._UCMTCPCI_DEVICE_CONFIG
title: UCMTCPCI_DEVICE_CONFIG
author: windows-driver-content
description: Used in the client driver's call to UcmTcpciDeviceInitialize. Call UCMTCPCI_DEVICE_CONFIG_INIT to initialize this structure.
old-location: buses\ucmtcpci_device_config.htm
old-project: usbref
ms.assetid: 74de7f2a-8738-472b-8a22-983a82e29fcb
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UCMTCPCI_DEVICE_CONFIG, UCMTCPCI_DEVICE_CONFIG, *PUCMTCPCI_DEVICE_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ucmtcpcidevice.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UCMTCPCI_DEVICE_CONFIG
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

# UCMTCPCI_DEVICE_CONFIG structure



## -description
<p>
                 Used in the client driver's call to <a href="..\ucmtcpcidevice\nf-ucmtcpcidevice-ucmtcpcideviceinitialize.md">UcmTcpciDeviceInitialize</a>. 
             Call <a href="..\ucmtcpcidevice\nf-ucmtcpcidevice-ucmtcpci-device-config-init.md">UCMTCPCI_DEVICE_CONFIG_INIT</a> to initialize this structure.
             </p>


## -syntax

````
typedef struct _UCMTCPCI_DEVICE_CONFIG {
  ULONG Size;
} UCMTCPCI_DEVICE_CONFIG, *PUCMTCPCI_DEVICE_CONFIG;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>Size of this structure.
                 </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="..\ucmtcpcidevice\nf-ucmtcpcidevice-ucmtcpcideviceinitialize.md">UcmTcpciDeviceInitialize</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UCMTCPCI_DEVICE_CONFIG structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
