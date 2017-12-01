---
UID: NE.wwan._WWAN_MODEM_CONFIG_MODE
title: WWAN_MODEM_CONFIG_MODE
author: windows-driver-content
description: The WWAN_MODEM_CONFIG_MODE enumeration lists modem configuration modes.
old-location: netvista\wwan_modem_config_mode.htm
old-project: netvista
ms.assetid: 1AA3EDCC-EB6E-4118-8081-CA1914140683
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WUDF_WORKITEM_CONFIG, WUDF_WORKITEM_CONFIG, *PWUDF_WORKITEM_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_MODEM_CONFIG_MODE
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
req.iface: 
req.product: Windows 10 or later.
---

# WWAN_MODEM_CONFIG_MODE enumeration



## -description
<p>The <b>WWAN_MODEM_CONFIG_MODE</b> enumeration lists modem configuration modes.</p>


## -syntax

````
typedef enum _WWAN_MODEM_CONFIG_MODE { 
  WwanModemConfigModeUnknown       = 0,
  WwanModemConfigModeModemCentric,
  WwanModemConfigModeHostCentric,
  WwanModemConfigModeMax
} WWAN_MODEM_CONFIG_MODE, *PWWAN_MODEM_CONFIG_MODE;
````


## -enum-fields
<dl>

### -field <a id="WwanModemConfigModeUnknown"></a><a id="wwanmodemconfigmodeunknown"></a><a id="WWANMODEMCONFIGMODEUNKNOWN"></a><b>WwanModemConfigModeUnknown</b>

<dd>
<p>The modem configuration mode is currently not available.</p>
</dd>

### -field <a id="WwanModemConfigModeModemCentric"></a><a id="wwanmodemconfigmodemodemcentric"></a><a id="WWANMODEMCONFIGMODEMODEMCENTRIC"></a><b>WwanModemConfigModeModemCentric</b>

<dd>
<p>The modem configuration mode is modem centric. The modem is responsible for the selection process of configuration based on UICC info or any other vendor-specified algorithm.</p>
</dd>

### -field <a id="WwanModemConfigModeHostCentric"></a><a id="wwanmodemconfigmodehostcentric"></a><a id="WWANMODEMCONFIGMODEHOSTCENTRIC"></a><b>WwanModemConfigModeHostCentric</b>

<dd>
<p>The modem configuration mode is host centric. The host will inform the modem which configuration file the modem will use.</p>
</dd>

### -field <a id="WwanModemConfigModeMax"></a><a id="wwanmodemconfigmodemax"></a><a id="WWANMODEMCONFIGMODEMAX"></a><b>WwanModemConfigModeMax</b>

<dd>
<p>The maximum value for this enumeration. This value might change in future versions of the NDIS
     header files and binaries.</p>
</dd>
</dl>

## -remarks
<p>The modem configuration mode shall not change during runtime. If a change is detected, it will be ignored by the OS.</p>

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
<a href="..\wwan\ns-wwan--wwan-modem-config-info.md">WWAN_MODEM_CONFIG_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_MODEM_CONFIG_MODE enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
