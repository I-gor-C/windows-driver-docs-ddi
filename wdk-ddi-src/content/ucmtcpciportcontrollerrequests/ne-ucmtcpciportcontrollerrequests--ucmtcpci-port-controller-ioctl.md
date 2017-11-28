---
UID: NE.ucmtcpciportcontrollerrequests._UCMTCPCI_PORT_CONTROLLER_IOCTL
title: UCMTCPCI_PORT_CONTROLLER_IOCTL
author: windows-driver-content
description: Defines the various device I/O control requests that are sent to the client driver for the port controller. This indicates the type of IOCTL in WPP.
old-location: buses\ucmtcpci_port_controller_ioctl.htm
old-project: usbref
ms.assetid: 61dcd4d9-cfd9-4878-96f5-c95465e0949e
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UCMTCPCI_PORT_CONTROLLER_IDENTIFICATION, UCMTCPCI_PORT_CONTROLLER_IDENTIFICATION, *PUCMTCPCI_PORT_CONTROLLER_IDENTIFICATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ucmtcpciportcontrollerrequests.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UCMTCPCI_PORT_CONTROLLER_IOCTL
req.alt-loc: UcmTcpciPortControllerRequests.h
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

# UCMTCPCI_PORT_CONTROLLER_IOCTL enumeration



## -description
<p>Defines the various device I/O control requests that are sent to the client driver for the port controller. This indicates the type of IOCTL in WPP.
                </p>


## -syntax

````
typedef enum _UCMTCPCI_PORT_CONTROLLER_IOCTL { 
  _IOCTL_UCMTCPCI_PORT_CONTROLLER_GET_STATUS                      = = IOCTL_UCMTCPCI_PORT_CONTROLLER_GET_STATUS,
  _IOCTL_UCMTCPCI_PORT_CONTROLLER_GET_CONTROL                     = = IOCTL_UCMTCPCI_PORT_CONTROLLER_GET_CONTROL,
  _IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_CONTROL                     = = IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_CONTROL,
  _IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT                    = = IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT,
  _IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT_BUFFER             = = IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT_BUFFER,
  _IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_RECEIVE_DETECT              = = IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_RECEIVE_DETECT,
  _IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_CONFIG_STANDARD_OUTPUT      = = IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_CONFIG_STANDARD_OUTPUT,
  _IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_COMMAND                     = = IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_COMMAND,
  _IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_MESSAGE_HEADER_INFO         = = IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_MESSAGE_HEADER_INFO,
  _IOCTL_UCMTCPCI_PORT_CONTROLLER_ALTERNATE_MODE_ENTERED          = IOCTL_UCMTCPCI_PORT_CONTROLLER_ALTERNATE_MODE_ENTERED,
  _IOCTL_UCMTCPCI_PORT_CONTROLLER_ALTERNATE_MODE_EXITED           = IOCTL_UCMTCPCI_PORT_CONTROLLER_ALTERNATE_MODE_EXITED,
  _IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_CONFIGURED          = IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_CONFIGURED,
  _IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_HPD_STATUS_CHANGED  = IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_HPD_STATUS_CHANGED
} UCMTCPCI_PORT_CONTROLLER_IOCTL;
````


## -enum-fields
<dl>

### -field <a id="_IOCTL_UCMTCPCI_PORT_CONTROLLER_GET_STATUS"></a><a id="_ioctl_ucmtcpci_port_controller_get_status"></a><b>_IOCTL_UCMTCPCI_PORT_CONTROLLER_GET_STATUS</b>

<dd>
<p>
                        
                    The <a href="https://msdn.microsoft.com/library/windows/hardware/mt805833">IOCTL_UCMTCPCI_PORT_CONTROLLER_GET_STATUS</a> request.</p>
</dd>

### -field <a id="_IOCTL_UCMTCPCI_PORT_CONTROLLER_GET_CONTROL"></a><a id="_ioctl_ucmtcpci_port_controller_get_control"></a><b>_IOCTL_UCMTCPCI_PORT_CONTROLLER_GET_CONTROL</b>

<dd>
<p>
                        
                    The <a href="https://msdn.microsoft.com/library/windows/hardware/mt805832">IOCTL_UCMTCPCI_PORT_CONTROLLER_GET_CONTROL</a> request.</p>
</dd>

### -field <a id="_IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_CONTROL"></a><a id="_ioctl_ucmtcpci_port_controller_set_control"></a><b>_IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_CONTROL</b>

<dd>
<p>
                        
                    The <a href="https://msdn.microsoft.com/library/windows/hardware/mt805836">IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_CONTROL</a> request.</p>
</dd>

### -field <a id="_IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT"></a><a id="_ioctl_ucmtcpci_port_controller_set_transmit"></a><b>_IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT</b>

<dd>
<p>
                        
                    The <a href="https://msdn.microsoft.com/library/windows/hardware/mt805839">IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT</a> request.</p>
</dd>

### -field <a id="_IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT_BUFFER"></a><a id="_ioctl_ucmtcpci_port_controller_set_transmit_buffer"></a><b>_IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT_BUFFER</b>

<dd>
<p>
                        
                    The  <a href="https://msdn.microsoft.com/library/windows/hardware/mt805840">IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT_BUFFER</a> request.</p>
</dd>

### -field <a id="_IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_RECEIVE_DETECT"></a><a id="_ioctl_ucmtcpci_port_controller_set_receive_detect"></a><b>_IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_RECEIVE_DETECT</b>

<dd>
<p>
                        
                    The <a href="https://msdn.microsoft.com/library/windows/hardware/mt805838">IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_RECEIVE_DETECT</a> request.</p>
</dd>

### -field <a id="_IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_CONFIG_STANDARD_OUTPUT"></a><a id="_ioctl_ucmtcpci_port_controller_set_config_standard_output"></a><b>_IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_CONFIG_STANDARD_OUTPUT</b>

<dd>
<p>
                        
                    The <a href="https://msdn.microsoft.com/library/windows/hardware/mt805835">IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_CONFIG_STANDARD_OUTPUT</a> request.</p>
</dd>

### -field <a id="_IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_COMMAND"></a><a id="_ioctl_ucmtcpci_port_controller_set_command"></a><b>_IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_COMMAND</b>

<dd>
<p>
                        
                    The <a href="https://msdn.microsoft.com/library/windows/hardware/mt805834">IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_COMMAND</a> request.</p>
</dd>

### -field <a id="_IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_MESSAGE_HEADER_INFO"></a><a id="_ioctl_ucmtcpci_port_controller_set_message_header_info"></a><b>_IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_MESSAGE_HEADER_INFO</b>

<dd>
<p>
                        
                    The <a href="https://msdn.microsoft.com/library/windows/hardware/mt805837">IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_MESSAGE_HEADER_INFO</a> request.</p>
</dd>

### -field <a id="_IOCTL_UCMTCPCI_PORT_CONTROLLER_ALTERNATE_MODE_ENTERED"></a><a id="_ioctl_ucmtcpci_port_controller_alternate_mode_entered"></a><b>_IOCTL_UCMTCPCI_PORT_CONTROLLER_ALTERNATE_MODE_ENTERED</b>

<dd>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/mt805828">IOCTL_UCMTCPCI_PORT_CONTROLLER_ALTERNATE_MODE_ENTERED</a> request.</p>
</dd>

### -field <a id="_IOCTL_UCMTCPCI_PORT_CONTROLLER_ALTERNATE_MODE_EXITED"></a><a id="_ioctl_ucmtcpci_port_controller_alternate_mode_exited"></a><b>_IOCTL_UCMTCPCI_PORT_CONTROLLER_ALTERNATE_MODE_EXITED</b>

<dd>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/mt805829">IOCTL_UCMTCPCI_PORT_CONTROLLER_ALTERNATE_MODE_EXITED</a> request.</p>
</dd>

### -field <a id="_IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_CONFIGURED"></a><a id="_ioctl_ucmtcpci_port_controller_displayport_configured"></a><b>_IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_CONFIGURED</b>

<dd>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/mt805830">IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_CONFIGURED</a> request.</p>
</dd>

### -field <a id="_IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_HPD_STATUS_CHANGED"></a><a id="_ioctl_ucmtcpci_port_controller_displayport_hpd_status_changed"></a><b>_IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_HPD_STATUS_CHANGED</b>

<dd>
<p>The  <a href="https://msdn.microsoft.com/library/windows/hardware/mt805831">IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_HPD_STATUS_CHANGED</a> request.</p>
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
<dt>UcmTcpciPortControllerRequests.h</dt>
</dl>
</td>
</tr>
</table>