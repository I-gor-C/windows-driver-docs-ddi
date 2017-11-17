---
UID: NE.wwan._WWAN_MODEM_CONFIG_REASON
title: WWAN_MODEM_CONFIG_REASON
author: windows-driver-content
description: The WWAN_MODEM_CONFIG_REASON enumeration lists definitions for reasons why a modem's configuration state change was triggered.
old-location: netvista\wwan_modem_config_reason.htm
ms.assetid: 2CF2C69B-A5DF-4A78-BC15-EB80FAC51831
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_MODEM_CONFIG_REASON
req.alt-loc: wwan.h
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
ms.keywords: WUDF_WORKITEM_CONFIG, WUDF_WORKITEM_CONFIG, *PWUDF_WORKITEM_CONFIG
req.iface: 
req.product: Windows 10 or later.
---

# WWAN_MODEM_CONFIG_REASON enumeration



## -description
<p>The <b>WWAN_MODEM_CONFIG_REASON</b> enumeration lists definitions for reasons why a modem's configuration state change was triggered.</p>


## -syntax

````
typedef enum _WWAN_MODEM_CONFIG_REASON { 
  WwanModemConfigReasonNone               = 0,
  WwanModemConfigReasonSIMDetected,
  WwanModemConfigReasonSIMRemoved,
  WwanModemConfigReasonNOSIM,
  WwanModemConfigReasonIMSIReset,
  WwanModemConfigReasonActivationFailure,
  WwanModemConfigReasonConfigFileUpdate,
  WwanModemConfigReasonModemReset,
  WwanModemConfigReasonModemRecovery,
  WwanModemConfigReasonMax
} WWAN_MODEM_CONFIG_REASON, *PWWAN_MODEM_CONFIG_REASON;
````


## -enum-fields
<dl>

### -field <a id="WwanModemConfigReasonNone"></a><a id="wwanmodemconfigreasonnone"></a><a id="WWANMODEMCONFIGREASONNONE"></a><b>WwanModemConfigReasonNone</b>

<dd>
<p>Default value that can be used if other optional reasons are not supported.</p>
</dd>

### -field <a id="WwanModemConfigReasonSIMDetected"></a><a id="wwanmodemconfigreasonsimdetected"></a><a id="WWANMODEMCONFIGREASONSIMDETECTED"></a><b>WwanModemConfigReasonSIMDetected</b>

<dd>
<p>Required. A SIM card was detected by a modem.</p>
</dd>

### -field <a id="WwanModemConfigReasonSIMRemoved"></a><a id="wwanmodemconfigreasonsimremoved"></a><a id="WWANMODEMCONFIGREASONSIMREMOVED"></a><b>WwanModemConfigReasonSIMRemoved</b>

<dd>
<p>Optional. A SIM card was removed.</p>
</dd>

### -field <a id="WwanModemConfigReasonNOSIM"></a><a id="wwanmodemconfigreasonnosim"></a><a id="WWANMODEMCONFIGREASONNOSIM"></a><b>WwanModemConfigReasonNOSIM</b>

<dd>
<p>Optional. There is no SIM card.</p>
</dd>

### -field <a id="WwanModemConfigReasonIMSIReset"></a><a id="wwanmodemconfigreasonimsireset"></a><a id="WWANMODEMCONFIGREASONIMSIRESET"></a><b>WwanModemConfigReasonIMSIReset</b>

<dd>
<p>Optional. A SIM card was reset with new IMSI programmed into it.</p>
</dd>

### -field <a id="WwanModemConfigReasonActivationFailure"></a><a id="wwanmodemconfigreasonactivationfailure"></a><a id="WWANMODEMCONFIGREASONACTIVATIONFAILURE"></a><b>WwanModemConfigReasonActivationFailure</b>

<dd>
<p>Optional. Activation of a new configuration failed.</p>
</dd>

### -field <a id="WwanModemConfigReasonConfigFileUpdate"></a><a id="wwanmodemconfigreasonconfigfileupdate"></a><a id="WWANMODEMCONFIGREASONCONFIGFILEUPDATE"></a><b>WwanModemConfigReasonConfigFileUpdate</b>

<dd>
<p>Optional. A new configuration file was updated by the host.</p>
</dd>

### -field <a id="WwanModemConfigReasonModemReset"></a><a id="wwanmodemconfigreasonmodemreset"></a><a id="WWANMODEMCONFIGREASONMODEMRESET"></a><b>WwanModemConfigReasonModemReset</b>

<dd>
<p>Optional. The modem reset and configuration was not lost.</p>
</dd>

### -field <a id="WwanModemConfigReasonModemRecovery"></a><a id="wwanmodemconfigreasonmodemrecovery"></a><a id="WWANMODEMCONFIGREASONMODEMRECOVERY"></a><b>WwanModemConfigReasonModemRecovery</b>

<dd>
<p>Required. The modem reset and configuration was restored to default.</p>
</dd>

### -field <a id="WwanModemConfigReasonMax"></a><a id="wwanmodemconfigreasonmax"></a><a id="WWANMODEMCONFIGREASONMAX"></a><b>WwanModemConfigReasonMax</b>

<dd>
<p>The maximum value for this enumeration. This value might change in future versions of the NDIS
     header files and binaries.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Windows 10, version 1709</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wwan.h (include Wwan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/3A13CFBC-DBB4-4BB1-ABA4-AB145AED07AA">WWAN_MODEM_CONFIG_STATUS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_MODEM_CONFIG_REASON enumeration%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
