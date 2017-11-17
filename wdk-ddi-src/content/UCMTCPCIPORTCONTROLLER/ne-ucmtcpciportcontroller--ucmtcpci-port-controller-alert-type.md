---
UID: NE.ucmtcpciportcontroller._UCMTCPCI_PORT_CONTROLLER_ALERT_TYPE
title: UCMTCPCI_PORT_CONTROLLER_ALERT_TYPE
author: windows-driver-content
description: Defines generic alert values that are used to indicate the type of hardware alert received on the port controller.
old-location: buses\ucmtcpci_port_controller_alert_type.htm
ms.assetid: 77162a25-b5aa-45d0-ac4d-6500df9782de
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: usbref
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
ms.keywords: UCMTCPCI_DRIVER_GLOBALS, UCMTCPCI_DRIVER_GLOBALS, *PUCMTCPCI_DRIVER_GLOBALS
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

### -field <a id="UcmTcpciPortControllerAlertInvalid"></a><a id="ucmtcpciportcontrolleralertinvalid"></a><a id="UCMTCPCIPORTCONTROLLERALERTINVALID"></a><b>UcmTcpciPortControllerAlertInvalid</b>

<dd>
<p>
                        
                    The alert is invalid.</p>
</dd>

### -field <a id="UcmTcpciPortControllerAlertCCStatus"></a><a id="ucmtcpciportcontrolleralertccstatus"></a><a id="UCMTCPCIPORTCONTROLLERALERTCCSTATUS"></a><b>UcmTcpciPortControllerAlertCCStatus</b>

<dd>
<p>Indicates a
                        
                    CC status change alert.</p>
</dd>

### -field <a id="UcmTcpciPortControllerAlertPowerStatus"></a><a id="ucmtcpciportcontrolleralertpowerstatus"></a><a id="UCMTCPCIPORTCONTROLLERALERTPOWERSTATUS"></a><b>UcmTcpciPortControllerAlertPowerStatus</b>

<dd>
<p>Indicates a
                        
                    power status change alert.
                        
                    </p>
</dd>

### -field <a id="UcmTcpciPortControllerAlertReceiveSOPMessageStatus"></a><a id="ucmtcpciportcontrolleralertreceivesopmessagestatus"></a><a id="UCMTCPCIPORTCONTROLLERALERTRECEIVESOPMESSAGESTATUS"></a><b>UcmTcpciPortControllerAlertReceiveSOPMessageStatus</b>

<dd>
<p>
                        
                    Indicates an SOP message alert.</p>
</dd>

### -field <a id="UcmTcpciPortControllerAlertReceivedHardReset"></a><a id="ucmtcpciportcontrolleralertreceivedhardreset"></a><a id="UCMTCPCIPORTCONTROLLERALERTRECEIVEDHARDRESET"></a><b>UcmTcpciPortControllerAlertReceivedHardReset</b>

<dd>
<p>
                        
                    Indicates a hard Reset alert.</p>
</dd>

### -field <a id="UcmTcpciPortControllerAlertTransmitSOPMessageFailed"></a><a id="ucmtcpciportcontrolleralerttransmitsopmessagefailed"></a><a id="UCMTCPCIPORTCONTROLLERALERTTRANSMITSOPMESSAGEFAILED"></a><b>UcmTcpciPortControllerAlertTransmitSOPMessageFailed</b>

<dd>
<p>
                        
                    Indicates that the SOP message transmission was not successful.</p>
</dd>

### -field <a id="UcmTcpciPortControllerAlertTransmitSOPMessageDiscarded"></a><a id="ucmtcpciportcontrolleralerttransmitsopmessagediscarded"></a><a id="UCMTCPCIPORTCONTROLLERALERTTRANSMITSOPMESSAGEDISCARDED"></a><b>UcmTcpciPortControllerAlertTransmitSOPMessageDiscarded</b>

<dd>
<p>Indicates that the
                        
                    SOP message transmission was not sent due to an incoming receive message. </p>
</dd>

### -field <a id="UcmTcpciPortControllerAlertTransmitSOPMessageSuccessful"></a><a id="ucmtcpciportcontrolleralerttransmitsopmessagesuccessful"></a><a id="UCMTCPCIPORTCONTROLLERALERTTRANSMITSOPMESSAGESUCCESSFUL"></a><b>UcmTcpciPortControllerAlertTransmitSOPMessageSuccessful</b>

<dd>
<p>
                        
                    Indicates that the SOP message transmission was successful.</p>
</dd>

### -field <a id="UcmTcpciPortControllerAlertVbusVoltageAlarmHi"></a><a id="ucmtcpciportcontrolleralertvbusvoltagealarmhi"></a><a id="UCMTCPCIPORTCONTROLLERALERTVBUSVOLTAGEALARMHI"></a><b>UcmTcpciPortControllerAlertVbusVoltageAlarmHi</b>

<dd>
<p>
                        
                    Indicates a high-voltage alarm.</p>
</dd>

### -field <a id="UcmTcpciPortControllerAlertVbusVoltageAlarmLo"></a><a id="ucmtcpciportcontrolleralertvbusvoltagealarmlo"></a><a id="UCMTCPCIPORTCONTROLLERALERTVBUSVOLTAGEALARMLO"></a><b>UcmTcpciPortControllerAlertVbusVoltageAlarmLo</b>

<dd>
<p>
                        
                    Indicates a low-voltage alarm.</p>
</dd>

### -field <a id="UcmTcpciPortControllerAlertFault"></a><a id="ucmtcpciportcontrolleralertfault"></a><a id="UCMTCPCIPORTCONTROLLERALERTFAULT"></a><b>UcmTcpciPortControllerAlertFault</b>

<dd>
<p>
                        
                    Indicates that a Fault has occurred. </p>
</dd>

### -field <a id="UcmTcpciPortControllerAlertRxBufferOverflow"></a><a id="ucmtcpciportcontrolleralertrxbufferoverflow"></a><a id="UCMTCPCIPORTCONTROLLERALERTRXBUFFEROVERFLOW"></a><b>UcmTcpciPortControllerAlertRxBufferOverflow</b>

<dd>
<p>Indicates that the
                        
                     TCPC Rx buffer has overflowed.</p>
</dd>

### -field <a id="UcmTcpciPortControllerAlertVbusSinkDisconnectDetected"></a><a id="ucmtcpciportcontrolleralertvbussinkdisconnectdetected"></a><a id="UCMTCPCIPORTCONTROLLERALERTVBUSSINKDISCONNECTDETECTED"></a><b>UcmTcpciPortControllerAlertVbusSinkDisconnectDetected</b>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/mt805898">UCMTCPCI_PORT_CONTROLLER_ALERT_DATA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UCMTCPCI_PORT_CONTROLLER_ALERT_TYPE enumeration%20 RELEASE:%20(11/3/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
