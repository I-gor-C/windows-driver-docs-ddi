---
UID: NE.wwan._WWAN_MODEM_CONFIG_STATE
title: WWAN_MODEM_CONFIG_STATE
author: windows-driver-content
description: The WWAN_MODEM_CONFIG_STATE enumeration lists definitions used by the modem to inform the OS about its modem configuration state.
old-location: netvista\wwan_modem_config_state.htm
old-project: netvista
ms.assetid: A22EA7A7-2C28-4117-A2B8-A7D3D4C9F11B
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
req.alt-api: WWAN_MODEM_CONFIG_STATE
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

# WWAN_MODEM_CONFIG_STATE enumeration



## -description
<p>The <b>WWAN_MODEM_CONFIG_STATE</b> enumeration lists definitions used by the modem to inform the OS about its modem configuration state.</p>


## -syntax

````
typedef enum _WWAN_MODEM_CONFIG_STATE { 
  WwanModemConfigStateUnknown    = 0,
  WwanModemConfigStatePending,
  WwanModemConfigStateActivated,
  WwanModemConfigStateMax
} WWAN_MODEM_CONFIG_STATE, *PWWAN_MODEM_CONFIG_STATE;
````


## -enum-fields
<dl>

### -field <a id="WwanModemConfigStateUnknown"></a><a id="wwanmodemconfigstateunknown"></a><a id="WWANMODEMCONFIGSTATEUNKNOWN"></a><b>WwanModemConfigStateUnknown</b>

<dd>
<p>The modem configuration state is currently not available.</p>
</dd>

### -field <a id="WwanModemConfigStatePending"></a><a id="wwanmodemconfigstatepending"></a><a id="WWANMODEMCONFIGSTATEPENDING"></a><b>WwanModemConfigStatePending</b>

<dd>
<p>The modem is currently selecting the best suitable configuration file that matches the UICC info.</p>
</dd>

### -field <a id="WwanModemConfigStateActivated"></a><a id="wwanmodemconfigstateactivated"></a><a id="WWANMODEMCONFIGSTATEACTIVATED"></a><b>WwanModemConfigStateActivated</b>

<dd>
<p>The modem has completed its configuration and modem subcomponents are aware of the new configuration.</p>
</dd>

### -field <a id="WwanModemConfigStateMax"></a><a id="wwanmodemconfigstatemax"></a><a id="WWANMODEMCONFIGSTATEMAX"></a><b>WwanModemConfigStateMax</b>

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
<a href="..\wwan\ns-wwan--wwan-modem-config-status.md">WWAN_MODEM_CONFIG_STATUS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_MODEM_CONFIG_STATE enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
