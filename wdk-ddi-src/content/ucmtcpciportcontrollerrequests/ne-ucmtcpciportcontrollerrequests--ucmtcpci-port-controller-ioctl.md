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

### -field _IOCTL_UCMTCPCI_PORT_CONTROLLER_GET_STATUS

<dd>
<p>
                        
                    The <a href="..\ucmtcpciportcontrollerrequests\ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-get-status.md">IOCTL_UCMTCPCI_PORT_CONTROLLER_GET_STATUS</a> request.</p>
</dd>

### -field _IOCTL_UCMTCPCI_PORT_CONTROLLER_GET_CONTROL

<dd>
<p>
                        
                    The <a href="..\ucmtcpciportcontrollerrequests\ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-get-control.md">IOCTL_UCMTCPCI_PORT_CONTROLLER_GET_CONTROL</a> request.</p>
</dd>

### -field _IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_CONTROL

<dd>
<p>
                        
                    The <a href="..\ucmtcpciportcontrollerrequests\ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-set-control.md">IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_CONTROL</a> request.</p>
</dd>

### -field _IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT

<dd>
<p>
                        
                    The <a href="..\ucmtcpciportcontrollerrequests\ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-set-transmit.md">IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT</a> request.</p>
</dd>

### -field _IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT_BUFFER

<dd>
<p>
                        
                    The  <a href="..\ucmtcpciportcontrollerrequests\ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-set-transmit-buffer.md">IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT_BUFFER</a> request.</p>
</dd>

### -field _IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_RECEIVE_DETECT

<dd>
<p>
                        
                    The <a href="..\ucmtcpciportcontrollerrequests\ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-set-receive-detect.md">IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_RECEIVE_DETECT</a> request.</p>
</dd>

### -field _IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_CONFIG_STANDARD_OUTPUT

<dd>
<p>
                        
                    The <a href="..\ucmtcpciportcontrollerrequests\ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-set-config-standard-output.md">IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_CONFIG_STANDARD_OUTPUT</a> request.</p>
</dd>

### -field _IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_COMMAND

<dd>
<p>
                        
                    The <a href="..\ucmtcpciportcontrollerrequests\ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-set-command.md">IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_COMMAND</a> request.</p>
</dd>

### -field _IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_MESSAGE_HEADER_INFO

<dd>
<p>
                        
                    The <a href="..\ucmtcpciportcontrollerrequests\ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-set-message-header-info.md">IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_MESSAGE_HEADER_INFO</a> request.</p>
</dd>

### -field _IOCTL_UCMTCPCI_PORT_CONTROLLER_ALTERNATE_MODE_ENTERED

<dd>
<p>The <a href="..\ucmtcpciportcontrollerrequests\ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-alternate-mode-entered.md">IOCTL_UCMTCPCI_PORT_CONTROLLER_ALTERNATE_MODE_ENTERED</a> request.</p>
</dd>

### -field _IOCTL_UCMTCPCI_PORT_CONTROLLER_ALTERNATE_MODE_EXITED

<dd>
<p>The <a href="..\ucmtcpciportcontrollerrequests\ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-alternate-mode-exited.md">IOCTL_UCMTCPCI_PORT_CONTROLLER_ALTERNATE_MODE_EXITED</a> request.</p>
</dd>

### -field _IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_CONFIGURED

<dd>
<p>The <a href="..\ucmtcpciportcontrollerrequests\ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-displayport-configured.md">IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_CONFIGURED</a> request.</p>
</dd>

### -field _IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_HPD_STATUS_CHANGED

<dd>
<p>The  <a href="..\ucmtcpciportcontrollerrequests\ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-displayport-hpd-status-changed.md">IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_HPD_STATUS_CHANGED</a> request.</p>
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