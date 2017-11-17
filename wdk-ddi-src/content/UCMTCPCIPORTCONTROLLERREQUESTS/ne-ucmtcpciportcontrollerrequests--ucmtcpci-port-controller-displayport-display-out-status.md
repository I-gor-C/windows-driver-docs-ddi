---
UID: NE.ucmtcpciportcontrollerrequests._UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS
title: UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS
author: windows-driver-content
description: Defines values to determine whether a display out status for a DisplayPort device is enabled.
old-location: buses\_ucmtcpci_port_controller_displayport_display_out_status.htm
ms.assetid: c57da7f2-d484-479c-9d8a-626789d8b23e
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: usbref
req.header: ucmtcpciportcontrollerrequests.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS
req.alt-loc: Ucmtcpciportcontrollerrequests.h
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
ms.keywords: UCMTCPCI_PORT_CONTROLLER_IDENTIFICATION, UCMTCPCI_PORT_CONTROLLER_IDENTIFICATION, *PUCMTCPCI_PORT_CONTROLLER_IDENTIFICATION
req.iface: 
req.product: Windows 10 or later.
---

# UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS enumeration



## -description
<p>Defines values to determine whether a display out status for a DisplayPort device is enabled</p>


## -syntax

````
typedef enum _UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS { 
  UcmTcpciPortControllerDisplayOutStatusOff  = 0x0,
  UcmTcpciPortControllerDisplayOutStatusOn   = 0x1
} UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS;
````


## -enum-fields
<dl>

### -field <a id="UcmTcpciPortControllerDisplayOutStatusOff"></a><a id="ucmtcpciportcontrollerdisplayoutstatusoff"></a><a id="UCMTCPCIPORTCONTROLLERDISPLAYOUTSTATUSOFF"></a><b>UcmTcpciPortControllerDisplayOutStatusOff</b>

<dd>
<p>Display out status is enabled.</p>
</dd>

### -field <a id="UcmTcpciPortControllerDisplayOutStatusOn"></a><a id="ucmtcpciportcontrollerdisplayoutstatuson"></a><a id="UCMTCPCIPORTCONTROLLERDISPLAYOUTSTATUSON"></a><b>UcmTcpciPortControllerDisplayOutStatusOn</b>

<dd>
<p>Display out status is enabled.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1709</p>
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
<dt>Ucmtcpciportcontrollerrequests.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/5f174c0a-43aa-48eb-999b-077f1d68c0cb">IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS_CHANGED</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/c808f607-b121-4406-bb9f-4c5be3f179e3">UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS_CHANGED_IN_PARAMS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS enumeration%20 RELEASE:%20(11/3/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
