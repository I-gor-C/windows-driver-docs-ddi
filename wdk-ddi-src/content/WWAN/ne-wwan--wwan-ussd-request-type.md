---
UID: NE.wwan._WWAN_USSD_REQUEST_TYPE
title: WWAN_USSD_REQUEST_TYPE
author: windows-driver-content
description: The WWAN_USSD_REQUEST_TYPE enumeration lists the different types of Unstructured Supplementary Service Data (USSD) session requests.
old-location: netvista\wwan_ussd_request_type.htm
ms.assetid: 773490EE-ECFC-4089-869D-19683A76E4FA
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
req.alt-api: WWAN_USSD_REQUEST_TYPE
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

# WWAN_USSD_REQUEST_TYPE enumeration



## -description
<p>The WWAN_USSD_REQUEST_TYPE enumeration lists the different types of Unstructured Supplementary Service Data (USSD) session requests.</p>


## -syntax

````
typedef enum _WWAN_USSD_REQUEST_TYPE { 
  WwanUssdRequestInitiate  = 0,
  WwanUssdRequestContinue  = 1,
  WwanUssdRequestCancel    = 2
} WWAN_USSD_REQUEST_TYPE;
````


## -enum-fields
<dl>

### -field <a id="WwanUssdRequestInitiate"></a><a id="wwanussdrequestinitiate"></a><a id="WWANUSSDREQUESTINITIATE"></a><b>WwanUssdRequestInitiate</b>

<dd>
<p>Indicates a request to create a new USSD session and to transmit the accompanying USSD string.</p>
</dd>

### -field <a id="WwanUssdRequestContinue"></a><a id="wwanussdrequestcontinue"></a><a id="WWANUSSDREQUESTCONTINUE"></a><b>WwanUssdRequestContinue</b>

<dd>
<p>Indicates a request to send the accompanying USSD string using the existing USSD session.</p>
</dd>

### -field <a id="WwanUssdRequestCancel"></a><a id="wwanussdrequestcancel"></a><a id="WWANUSSDREQUESTCANCEL"></a><b>WwanUssdRequestCancel</b>

<dd>
<p>Indicates a request to terminate the existing USSD session.</p>
</dd>
</dl>

## -remarks
<p>The USSD protocol only allows a single USSD session at any time. If the miniport driver receives a <i>WwanUssdRequestInitiate</i> request to create a new USSD session when one already exists, the miniport driver must fail the request and specify <i>WwanUssdEventOtherLocalClient</i> as the reason.</p>

<p>When responding to a <i>WwanUssdRequestCancel</i> request, miniport drivers must return <i>WwanUssdEventTerminated</i> as the reason even if no session existed (which may happen during a concurrent release of the session from the network and the local client). The content of the accompanying USSD string must be ignored for WwanUssdRequestCancel requests and the string length should be set to zero to indicate that there is no accompanying USSD string.</p>

<p>The USSD protocol only allows a single USSD session at any time. If the miniport driver receives a <i>WwanUssdRequestInitiate</i> request to create a new USSD session when one already exists, the miniport driver must fail the request and specify <i>WwanUssdEventOtherLocalClient</i> as the reason.</p>

<p>When responding to a <i>WwanUssdRequestCancel</i> request, miniport drivers must return <i>WwanUssdEventTerminated</i> as the reason even if no session existed (which may happen during a concurrent release of the session from the network and the local client). The content of the accompanying USSD string must be ignored for WwanUssdRequestCancel requests and the string length should be set to zero to indicate that there is no accompanying USSD string.</p>

<p>The USSD protocol only allows a single USSD session at any time. If the miniport driver receives a <i>WwanUssdRequestInitiate</i> request to create a new USSD session when one already exists, the miniport driver must fail the request and specify <i>WwanUssdEventOtherLocalClient</i> as the reason.</p>

<p>When responding to a <i>WwanUssdRequestCancel</i> request, miniport drivers must return <i>WwanUssdEventTerminated</i> as the reason even if no session existed (which may happen during a concurrent release of the session from the network and the local client). The content of the accompanying USSD string must be ignored for WwanUssdRequestCancel requests and the string length should be set to zero to indicate that there is no accompanying USSD string.</p>

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