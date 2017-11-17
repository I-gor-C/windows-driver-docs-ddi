---
UID: NE.ucmtypes._UCM_TYPEC_PARTNER
title: UCM_TYPEC_PARTNER
author: windows-driver-content
description: Defines the state of the Type-C connector.
old-location: buses\ucm_type_c_port_state.htm
ms.assetid: 4779E943-5C13-4DE2-AF8F-37657F0F99C0
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: usbref
req.header: ucmtypes.h
req.include-header: Ucmcx.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.15
req.umdf-ver: 2.15
req.alt-api: UCM_TYPEC_PARTNER
req.alt-loc: Ucmtypes.h
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
ms.keywords: UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT_IN_PARAMS, UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT_IN_PARAMS, *PUCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT_IN_PARAMS
req.iface: 
req.product: Windows 10 or later.
---

# UCM_TYPEC_PARTNER enumeration



## -description
<p>Defines the state of the Type-C connector.</p>


## -syntax

````
typedef enum _UCM_TYPEC_PARTNER { 
  UcmTypeCPartnerStateInvalid               = 0,
  UcmTypeCPartnerStateUfp ,
  UcmTypeCPartnerStateDfp ,
  UcmTypeCPartnerStatePoweredCableNoUfp ,
  UcmTypeCPartnerStatePoweredCableWithUfp ,
  UcmTypeCPartnerStateAudioAccessory,
  UcmTypeCPartnerStateDebugAccessory
} UCM_TYPEC_PARTNER;
````


## -enum-fields
<dl>

### -field <a id="UcmTypeCPartnerStateInvalid_"></a><a id="ucmtypecpartnerstateinvalid_"></a><a id="UCMTYPECPARTNERSTATEINVALID_"></a><b>UcmTypeCPartnerStateInvalid </b>

<dd>
<p>The partner port state is invalid.</p>
</dd>

### -field <a id="UcmTypeCPartnerStateUfp_"></a><a id="ucmtypecpartnerstateufp_"></a><a id="UCMTYPECPARTNERSTATEUFP_"></a><b>UcmTypeCPartnerStateUfp </b>

<dd>
<p>The partner is an Upstream Facing Port (UFP).</p>
</dd>

### -field <a id="UcmTypeCPartnerStateDfp_"></a><a id="ucmtypecpartnerstatedfp_"></a><a id="UCMTYPECPARTNERSTATEDFP_"></a><b>UcmTypeCPartnerStateDfp </b>

<dd>
<p>The partner is a Downstream Facing Port (DFP).</p>
</dd>

### -field <a id="UcmTypeCPartnerStatePoweredCableNoUfp_"></a><a id="ucmtypecpartnerstatepoweredcablenoufp_"></a><a id="UCMTYPECPARTNERSTATEPOWEREDCABLENOUFP_"></a><b>UcmTypeCPartnerStatePoweredCableNoUfp </b>

<dd>
<p>The partner is a powered cable that requires VConn, that currently does not have a UFP attached on the other end.</p>
</dd>

### -field <a id="UcmTypeCPartnerStatePoweredCableWithUfp_"></a><a id="ucmtypecpartnerstatepoweredcablewithufp_"></a><a id="UCMTYPECPARTNERSTATEPOWEREDCABLEWITHUFP_"></a><b>UcmTypeCPartnerStatePoweredCableWithUfp </b>

<dd>
<p>The partner is a powered and upstream facing.</p>
</dd>

### -field <a id="UcmTypeCPartnerStateAudioAccessory"></a><a id="ucmtypecpartnerstateaudioaccessory"></a><a id="UCMTYPECPARTNERSTATEAUDIOACCESSORY"></a><b>UcmTypeCPartnerStateAudioAccessory</b>

<dd>
<p>The partner is used as an audio accessory.</p>
</dd>

### -field <a id="UcmTypeCPartnerStateDebugAccessory"></a><a id="ucmtypecpartnerstatedebugaccessory"></a><a id="UCMTYPECPARTNERSTATEDEBUGACCESSORY"></a><b>UcmTypeCPartnerStateDebugAccessory</b>

<dd>
<p>The partner is a debug accessory.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.15</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.15</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ucmtypes.h (include Ucmcx.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt187928">UCM_CONNECTOR_TYPEC_ATTACH_PARAMS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt187915">UcmConnectorTypeCAttach</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UCM_TYPEC_PARTNER enumeration%20 RELEASE:%20(11/3/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
