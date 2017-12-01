---
UID: NS.ucmtcpciportcontrollerrequests._UCMTCPCI_PORT_CONTROLLER_GET_CONTROL_OUT_PARAMS
title: UCMTCPCI_PORT_CONTROLLER_GET_CONTROL_OUT_PARAMS
author: windows-driver-content
description: Stores the values of all control registers of the port controller retrieved by the IOCTL_UCMTCPCI_PORT_CONTROLLER_GET_CONTROL request.
old-location: buses\ucmtcpci_port_controller_get_control_out_params.htm
old-project: usbref
ms.assetid: c75167cb-14c9-4189-961a-97a50c84d6be
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UCMTCPCI_PORT_CONTROLLER_GET_CONTROL_OUT_PARAMS, UCMTCPCI_PORT_CONTROLLER_GET_CONTROL_OUT_PARAMS, *PUCMTCPCI_PORT_CONTROLLER_GET_CONTROL_OUT_PARAMS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ucmtcpciportcontrollerrequests.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UCMTCPCI_PORT_CONTROLLER_GET_CONTROL_OUT_PARAMS
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
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# UCMTCPCI_PORT_CONTROLLER_GET_CONTROL_OUT_PARAMS structure



## -description
<p>
             Stores the values of all control registers of the port controller retrieved by the 
             <a href="buses.ioctl_ucmtcpci_port_controller_get_control">IOCTL_UCMTCPCI_PORT_CONTROLLER_GET_CONTROL</a> request.</p>


## -syntax

````
typedef struct _UCMTCPCI_PORT_CONTROLLER_GET_CONTROL_OUT_PARAMS {
  UCMTCPCI_PORT_CONTROLLER_TCPC_CONTROL  TCPCControl;
  UCMTCPCI_PORT_CONTROLLER_ROLE_CONTROL  RoleControl;
  UCMTCPCI_PORT_CONTROLLER_FAULT_CONTROL FaultControl;
  UCMTCPCI_PORT_CONTROLLER_POWER_CONTROL PowerControl;
} UCMTCPCI_PORT_CONTROLLER_GET_CONTROL_OUT_PARAMS, *PUCMTCPCI_PORT_CONTROLLER_GET_CONTROL_OUT_PARAMS;
````


## -struct-fields
<dl>

### -field <b>TCPCControl</b>

<dd>
<p>
                     A 
                 <b>UCMTCPCI_PORT_CONTROLLER_TCPC_CONTROL</b> structure that describes the TCPC_CONTROL Register defined as per the Universal Serial Bus Type-C Port Controller Interface Specification. This structure is declared in UcmTcpciSpec.h.</p>
</dd>

### -field <b>RoleControl</b>

<dd>
<p>
                     A 
                 <b>UCMTCPCI_PORT_CONTROLLER_ROLE_CONTROL</b> structure that describes the ROLE_CONTROL Register defined as per the Universal Serial Bus Type-C Port Controller Interface Specification. This structure is declared in UcmTcpciSpec.h.</p>
</dd>

### -field <b>FaultControl</b>

<dd>
<p>
                     A 
                 <b>UCMTCPCI_PORT_CONTROLLER_FAULT_CONTROL</b> structure that describes the FAULT_CONTROL Register defined as per the Universal Serial Bus Type-C Port Controller Interface Specification. This structure is declared in UcmTcpciSpec.h.</p>
</dd>

### -field <b>PowerControl</b>

<dd>
<p>
                     A 
                 <b>UCMTCPCI_PORT_CONTROLLER_POWER_CONTROL</b> structure that describes the FAULT_POWER Register defined as per the Universal Serial Bus Type-C Port Controller Interface Specification. This structure is declared in UcmTcpciSpec.h.</p>
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
<dt>Ucmtcpciportcontrollerrequests.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses.ioctl_ucmtcpci_port_controller_get_control">IOCTL_UCMTCPCI_PORT_CONTROLLER_GET_CONTROL</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UCMTCPCI_PORT_CONTROLLER_GET_CONTROL_OUT_PARAMS structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
