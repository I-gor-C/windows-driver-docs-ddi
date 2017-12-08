---
UID: NE.ucmtcpciportcontroller._UCMTCPCI_PORT_CONTROLLER_ALERT_TYPE
title: UCMTCPCI_PORT_CONTROLLER_ALERT_TYPE
author: windows-driver-content
description: Defines generic alert values that are used to indicate the type of hardware alert received on the port controller.
old-location: buses\ucmtcpci_port_controller_alert_type.htm
old-project: usbref
ms.assetid: 77162a25-b5aa-45d0-ac4d-6500df9782de
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UCMTCPCI_DRIVER_GLOBALS, UCMTCPCI_DRIVER_GLOBALS, *PUCMTCPCI_DRIVER_GLOBALS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ucmtcpciportcontroller.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UCMTCPCI_PORT_CONTROLLER_ALERT_TYPE
req.alt-loc: ucmtcpciportcontroller.h
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

# UCMTCPCI_PORT_CONTROLLER_ALERT_TYPE enumeration



## -description
<p>
                    
                Defines generic alert values that are used to indicate the type of hardware alert received on the port controller.</p>


## -syntax

````
typedef enum _UCMTCPCI_PORT_CONTROLLER_ALERT_TYPE { 
  UcmTcpciPortControllerAlertInvalid                       = = 0x0,
  UcmTcpciPortControllerAlertCCStatus,
  UcmTcpciPortControllerAlertPowerStatus,
  UcmTcpciPortControllerAlertReceiveSOPMessageStatus,
  UcmTcpciPortControllerAlertReceivedHardReset,
  UcmTcpciPortControllerAlertTransmitSOPMessageFailed,
  UcmTcpciPortControllerAlertTransmitSOPMessageDiscarded,
  UcmTcpciPortControllerAlertTransmitSOPMessageSuccessful,
  UcmTcpciPortControllerAlertVbusVoltageAlarmHi,
  UcmTcpciPortControllerAlertVbusVoltageAlarmLo,
  UcmTcpciPortControllerAlertFault,
  UcmTcpciPortControllerAlertRxBufferOverflow,
  UcmTcpciPortControllerAlertVbusSinkDisconnectDetected
} UCMTCPCI_PORT_CONTROLLER_ALERT_TYPE;
````


## -enum-fields
<dl>

### -field UcmTcpciPortControllerAlertInvalid

<dd>
<p>
                        
                    The alert is invalid.</p>
</dd>

### -field UcmTcpciPortControllerAlertCCStatus

<dd>
<p>Indicates a
                        
                    CC status change alert.</p>
</dd>

### -field UcmTcpciPortControllerAlertPowerStatus

<dd>
<p>Indicates a
                        
                    power status change alert.
                        
                    </p>
</dd>

### -field UcmTcpciPortControllerAlertReceiveSOPMessageStatus

<dd>
<p>
                        
                    Indicates an SOP message alert.</p>
</dd>

### -field UcmTcpciPortControllerAlertReceivedHardReset

<dd>
<p>
                        
                    Indicates a hard Reset alert.</p>
</dd>

### -field UcmTcpciPortControllerAlertTransmitSOPMessageFailed

<dd>
<p>
                        
                    Indicates that the SOP message transmission was not successful.</p>
</dd>

### -field UcmTcpciPortControllerAlertTransmitSOPMessageDiscarded

<dd>
<p>Indicates that the
                        
                    SOP message transmission was not sent due to an incoming receive message. </p>
</dd>

### -field UcmTcpciPortControllerAlertTransmitSOPMessageSuccessful

<dd>
<p>
                        
                    Indicates that the SOP message transmission was successful.</p>
</dd>

### -field UcmTcpciPortControllerAlertVbusVoltageAlarmHi

<dd>
<p>
                        
                    Indicates a high-voltage alarm.</p>
</dd>

### -field UcmTcpciPortControllerAlertVbusVoltageAlarmLo

<dd>
<p>
                        
                    Indicates a low-voltage alarm.</p>
</dd>

### -field UcmTcpciPortControllerAlertFault

<dd>
<p>
                        
                    Indicates that a Fault has occurred. </p>
</dd>

### -field UcmTcpciPortControllerAlertRxBufferOverflow

<dd>
<p>Indicates that the
                        
                     TCPC Rx buffer has overflowed.</p>
</dd>

### -field UcmTcpciPortControllerAlertVbusSinkDisconnectDetected

<dd>
<p>
                        
                    Indicates that a VBUS Sink Disconnect Threshold crossing has been detected </p>
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
<dt>Ucmtcpciportcontroller.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ucmtcpciportcontroller\ns-ucmtcpciportcontroller--ucmtcpci-port-controller-alert-data.md">UCMTCPCI_PORT_CONTROLLER_ALERT_DATA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UCMTCPCI_PORT_CONTROLLER_ALERT_TYPE enumeration%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
