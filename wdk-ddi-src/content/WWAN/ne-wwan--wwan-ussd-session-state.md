---
UID: NE.wwan._WWAN_USSD_SESSION_STATE
title: WWAN_USSD_SESSION_STATE
author: windows-driver-content
description: The WWAN_USSD_SESSION_STATE enumeration lists the different types of USSD session states.
old-location: netvista\wwan_ussd_session_state.htm
ms.assetid: 5111A10F-F66F-4667-A77E-63691CCD282D
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: wwan.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with  Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_USSD_SESSION_STATE
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

# WWAN_USSD_SESSION_STATE enumeration



## -description
<p>The WWAN_USSD_SESSION_STATE enumeration lists the different types of USSD session states.</p>


## -syntax

````
typedef enum _WWAN_USSD_SESSION_STATE { 
  WwanUssdSessionStateNew       = 0,
  WwanUssdSessionStateExisting  = 1
} WWAN_USSD_SESSION_STATE;
````


## -enum-fields
<dl>

### -field <a id="WwanUssdSessionStateNew"></a><a id="wwanussdsessionstatenew"></a><a id="WWANUSSDSESSIONSTATENEW"></a><b>WwanUssdSessionStateNew</b>

<dd>
<p>The USSD string is the first message of a USSD session.</p>
</dd>

### -field <a id="WwanUssdSessionStateExisting"></a><a id="wwanussdsessionstateexisting"></a><a id="WWANUSSDSESSIONSTATEEXISTING"></a><b>WwanUssdSessionStateExisting</b>

<dd>
<p>The USSD string is not the first message of a USSD session.</p>
</dd>
</dl>

## -remarks
<p>Miniport drivers use the WWAN_USSD_SESSION_STATE enumeration to indicate whether a USSD string is the first message of a USSD session. Miniport drivers must use <i>WwanUssdSessionStateNew</i> for the first message of a network-initiated USSD session. Miniport drivers should use <i>WwanUssdSessionStateExisting</i> in all other cases.</p>

<p>Miniport drivers use the WWAN_USSD_SESSION_STATE enumeration to indicate whether a USSD string is the first message of a USSD session. Miniport drivers must use <i>WwanUssdSessionStateNew</i> for the first message of a network-initiated USSD session. Miniport drivers should use <i>WwanUssdSessionStateExisting</i> in all other cases.</p>

<p>Miniport drivers use the WWAN_USSD_SESSION_STATE enumeration to indicate whether a USSD string is the first message of a USSD session. Miniport drivers must use <i>WwanUssdSessionStateNew</i> for the first message of a network-initiated USSD session. Miniport drivers should use <i>WwanUssdSessionStateExisting</i> in all other cases.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with  Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wwan.h</dt>
</dl>
</td>
</tr>
</table>