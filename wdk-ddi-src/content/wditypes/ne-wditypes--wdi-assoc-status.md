---
UID: NE.wditypes._WDI_ASSOC_STATUS
title: WDI_ASSOC_STATUS
author: windows-driver-content
description: The WDI_ASSOC_STATUS enumeration defines the association status values.
old-location: netvista\wdi_assoc_status.htm
old-project: netvista
ms.assetid: 8268031A-7493-4A42-9211-D02B8AA50F34
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDF_WORKITEM_CONFIG, WDF_WORKITEM_CONFIG, *PWDF_WORKITEM_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wditypes.hpp
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WDI_ASSOC_STATUS
req.alt-loc: wditypes.hpp
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WDI_ASSOC_STATUS enumeration



## -description
<p>The WDI_ASSOC_STATUS enumeration defines the association status values.</p>


## -syntax

````
typedef enum _WDI_ASSOC_STATUS { 
  WDI_ASSOC_STATUS_SUCCESS                             = 0,
  WDI_ASSOC_STATUS_FAILURE                             = 1,
  WDI_ASSOC_STATUS_UNREACHABLE                         = 2,
  WDI_ASSOC_STATUS_RADIO_OFF                           = 3,
  WDI_ASSOC_STATUS_ABORTED                             = 5,
  WDI_ASSOC_STATUS_CANDIDATE_LIST_EXHAUSTED            = 6,
  WDI_ASSOC_STATUS_DISASSOCIATED_BY_HOST               = 7,
  WDI_ASSOC_STATUS_ROAMING_BETTER_AP_FOUND             = 10,
  WDI_ASSOC_STATUS_ROAMING_ASSOCIATION_LOST            = 11,
  WDI_ASSOC_STATUS_PEER_DEAUTHENTICATED                = 13,
  WDI_ASSOC_STATUS_PEER_DISASSOCIATED                  = 14,
  WDI_ASSOC_STATUS_ROAMING_LOW_LINK_QUALITY            = 15,
  WDI_ASSOC_STATUS_PROBE_TX_FAILURE                    = 30,
  WDI_ASSOC_STATUS_NO_BEACON_PROBE_RESPONSE            = 31,
  WDI_ASSOC_STATUS_AUTH_REQUEST_TX_NO_ACK              = 40,
  WDI_ASSOC_STATUS_NO_AUTH_RESPONSE                    = 41,
  WDI_ASSOC_STATUS_AUTH_RESPONSE_CAPABILITY_MISMATCH   = 42,
  WDI_ASSOC_STATUS_BAD_AUTH_RESPONSE                   = 43,
  WDI_ASSOC_STATUS_AUTH_FAILED_BY_PEER                 = 44,
  WDI_ASSOC_STATUS_AUTH_EXCHANGE_FAILURE               = 45,
  WDI_ASSOC_STATUS_ASSOC_REQUEST_TX_NO_ACK             = 50,
  WDI_ASSOC_STATUS_NO_ASSOC_RESPONSE                   = 51,
  WDI_ASSOC_STATUS_ASSOC_RESPONSE_CAPABILITY_MISMATCH  = 52,
  WDI_ASSOC_STATUS_BAD_ASSOC_RESPONSE                  = 53,
  WDI_ASSOC_STATUS_ASSOC_FAILED_BY_PEER                = 54,
  WDI_ASSOC_STATUS_ASSOC_EXCHANGE_FAILURE              = 55,
  WDI_ASSOC_STATUS_DISASSOCIATE_BY_DEVICE_RESET        = 60,
  WDI_ASSOC_STATUS_DISASSOCIATE_UNABLE_TO_MAINTAIN     = 61,
  WDI_ASSOC_STATUS_DISASSOCIATE_NOT_VISIBLE            = 62,
  WDI_ASSOC_STATUS_DISASSOCIATE_NEEDED_REASSOC         = 63
} WDI_ASSOC_STATUS;
````


## -enum-fields
<dl>

### -field <a id="WDI_ASSOC_STATUS_SUCCESS"></a><a id="wdi_assoc_status_success"></a><b>WDI_ASSOC_STATUS_SUCCESS</b>

<dd>
<p>The operation completed successfully.</p>
</dd>

### -field <a id="WDI_ASSOC_STATUS_FAILURE"></a><a id="wdi_assoc_status_failure"></a><b>WDI_ASSOC_STATUS_FAILURE</b>

<dd>
<p>The operation completed with a failure and none of the other status codes apply.</p>
</dd>

### -field <a id="WDI_ASSOC_STATUS_UNREACHABLE"></a><a id="wdi_assoc_status_unreachable"></a><b>WDI_ASSOC_STATUS_UNREACHABLE</b>

<dd>
<p>The operation failed because the peer is unreachable. The detection of an unreachable peer is up to the port. For example, a peer can be considered unreachable if the port does not receive responses to management requests such as probe requests or association requests. If the device has more specific information, it should use one of the more specific reason codes.</p>
</dd>

### -field <a id="WDI_ASSOC_STATUS_RADIO_OFF"></a><a id="wdi_assoc_status_radio_off"></a><b>WDI_ASSOC_STATUS_RADIO_OFF</b>

<dd>
<p>The operation failed because the radio is off. This can be used if the hardware radio switch is turned off.</p>
</dd>

### -field <a id="WDI_ASSOC_STATUS_ABORTED"></a><a id="wdi_assoc_status_aborted"></a><b>WDI_ASSOC_STATUS_ABORTED</b>

<dd>
<p>The operation was cancelled due to a request from the host. If the request from the host was for disassociation, WDI_ASSOC_STATUS_DISASSOCIATED_BY_HOST should be used.</p>
</dd>

### -field <a id="WDI_ASSOC_STATUS_CANDIDATE_LIST_EXHAUSTED"></a><a id="wdi_assoc_status_candidate_list_exhausted"></a><b>WDI_ASSOC_STATUS_CANDIDATE_LIST_EXHAUSTED</b>

<dd>
<p>The connect or roaming operation failed because the post could not successfully associate.</p>
</dd>

### -field <a id="WDI_ASSOC_STATUS_DISASSOCIATED_BY_HOST"></a><a id="wdi_assoc_status_disassociated_by_host"></a><b>WDI_ASSOC_STATUS_DISASSOCIATED_BY_HOST</b>

<dd>
<p>The host requested that the port disassociate.</p>
</dd>

### -field <a id="WDI_ASSOC_STATUS_ROAMING_BETTER_AP_FOUND"></a><a id="wdi_assoc_status_roaming_better_ap_found"></a><b>WDI_ASSOC_STATUS_ROAMING_BETTER_AP_FOUND</b>

<dd>
<p>The connection was torn down because a better access point was found.</p>
</dd>

### -field <a id="WDI_ASSOC_STATUS_ROAMING_ASSOCIATION_LOST"></a><a id="wdi_assoc_status_roaming_association_lost"></a><b>WDI_ASSOC_STATUS_ROAMING_ASSOCIATION_LOST</b>

<dd>
<p>The port lost the link with the peer. If device has more specific information, it should use one of the more specific reason codes such as WDI_ASSOC_STATUS_DISASSOCIATE_NOT_VISIBLE.</p>
</dd>

### -field <a id="WDI_ASSOC_STATUS_PEER_DEAUTHENTICATED"></a><a id="wdi_assoc_status_peer_deauthenticated"></a><b>WDI_ASSOC_STATUS_PEER_DEAUTHENTICATED</b>

<dd>
<p>The port received a deauthentication frame from the peer. The deauthentication frame must be included in the indication.</p>
</dd>

### -field <a id="WDI_ASSOC_STATUS_PEER_DISASSOCIATED"></a><a id="wdi_assoc_status_peer_disassociated"></a><b>WDI_ASSOC_STATUS_PEER_DISASSOCIATED</b>

<dd>
<p>The port received a disassociation frame from the peer. The disassociation frame must be included in the indication.</p>
</dd>

### -field <a id="WDI_ASSOC_STATUS_ROAMING_LOW_LINK_QUALITY"></a><a id="wdi_assoc_status_roaming_low_link_quality"></a><b>WDI_ASSOC_STATUS_ROAMING_LOW_LINK_QUALITY</b>

<dd>
<p>The link quality to the peer is low.</p>
</dd>

### -field <a id="WDI_ASSOC_STATUS_PROBE_TX_FAILURE"></a><a id="wdi_assoc_status_probe_tx_failure"></a><b>WDI_ASSOC_STATUS_PROBE_TX_FAILURE</b>

<dd>
<p>The association failed because the port was not able to successfully send a 802.11 probe request to the peer.</p>
</dd>

### -field <a id="WDI_ASSOC_STATUS_NO_BEACON_PROBE_RESPONSE"></a><a id="wdi_assoc_status_no_beacon_probe_response"></a><b>WDI_ASSOC_STATUS_NO_BEACON_PROBE_RESPONSE</b>

<dd>
<p>The association failed because no beacon or probe response was received from the peer.</p>
</dd>

### -field <a id="WDI_ASSOC_STATUS_AUTH_REQUEST_TX_NO_ACK"></a><a id="wdi_assoc_status_auth_request_tx_no_ack"></a><b>WDI_ASSOC_STATUS_AUTH_REQUEST_TX_NO_ACK</b>

<dd>
<p>The association failed because the port was unable to get an ACK for the 802.11 authentication request frame.</p>
</dd>

### -field <a id="WDI_ASSOC_STATUS_NO_AUTH_RESPONSE"></a><a id="wdi_assoc_status_no_auth_response"></a><b>WDI_ASSOC_STATUS_NO_AUTH_RESPONSE</b>

<dd>
<p>The association failed because an 802.11 authentication response frame was not received after a successful send of an 802.11 authentication request.</p>
</dd>

### -field <a id="WDI_ASSOC_STATUS_AUTH_RESPONSE_CAPABILITY_MISMATCH"></a><a id="wdi_assoc_status_auth_response_capability_mismatch"></a><b>WDI_ASSOC_STATUS_AUTH_RESPONSE_CAPABILITY_MISMATCH</b>

<dd>
<p>The association failed because an 802.11 authentication response was received with a status of success, but was rejected due to capability mismatch.</p>
</dd>

### -field <a id="WDI_ASSOC_STATUS_BAD_AUTH_RESPONSE"></a><a id="wdi_assoc_status_bad_auth_response"></a><b>WDI_ASSOC_STATUS_BAD_AUTH_RESPONSE</b>

<dd>
<p>The association failed because an 802.11 authentication response was received with a status of success, but was rejected due to a reason other than capability mismatch (for example, because of invalid content).</p>
</dd>

### -field <a id="WDI_ASSOC_STATUS_AUTH_FAILED_BY_PEER"></a><a id="wdi_assoc_status_auth_failed_by_peer"></a><b>WDI_ASSOC_STATUS_AUTH_FAILED_BY_PEER</b>

<dd>
<p>The association failed because the peer failed the 802.11 authentication with a failure reason. The authentication response frame must be included in the indication.</p>
</dd>

### -field <a id="WDI_ASSOC_STATUS_AUTH_EXCHANGE_FAILURE"></a><a id="wdi_assoc_status_auth_exchange_failure"></a><b>WDI_ASSOC_STATUS_AUTH_EXCHANGE_FAILURE</b>

<dd>
<p>The association failed because the 802.11 authentication did not finish successfully. This reason should only be used if the port is not able to use one of the specific 802.11 authentication exchange failure codes.</p>
</dd>

### -field <a id="WDI_ASSOC_STATUS_ASSOC_REQUEST_TX_NO_ACK"></a><a id="wdi_assoc_status_assoc_request_tx_no_ack"></a><b>WDI_ASSOC_STATUS_ASSOC_REQUEST_TX_NO_ACK</b>

<dd>
<p>The association failed because port was unable to get an ACK for the 802.11 association request frame.</p>
</dd>

### -field <a id="WDI_ASSOC_STATUS_NO_ASSOC_RESPONSE"></a><a id="wdi_assoc_status_no_assoc_response"></a><b>WDI_ASSOC_STATUS_NO_ASSOC_RESPONSE</b>

<dd>
<p>The association failed because an 802.11 association response frame was not received after a successful send of an 802.11 association request.</p>
</dd>

### -field <a id="WDI_ASSOC_STATUS_ASSOC_RESPONSE_CAPABILITY_MISMATCH"></a><a id="wdi_assoc_status_assoc_response_capability_mismatch"></a><b>WDI_ASSOC_STATUS_ASSOC_RESPONSE_CAPABILITY_MISMATCH</b>

<dd>
<p>The association failed because an 802.11 association response was received with a status of success, but was rejected due to capability mismatch. The association response frame should be included in the indication.</p>
</dd>

### -field <a id="WDI_ASSOC_STATUS_BAD_ASSOC_RESPONSE"></a><a id="wdi_assoc_status_bad_assoc_response"></a><b>WDI_ASSOC_STATUS_BAD_ASSOC_RESPONSE</b>

<dd>
<p>The association failed because an 802.11 association response was received with a status of success, but was rejected due to a reason other than capability mismatch (for example, because of invalid content). The association response frame should be included in the indication.</p>
</dd>

### -field <a id="WDI_ASSOC_STATUS_ASSOC_FAILED_BY_PEER"></a><a id="wdi_assoc_status_assoc_failed_by_peer"></a><b>WDI_ASSOC_STATUS_ASSOC_FAILED_BY_PEER</b>

<dd>
<p>The association failed because the peer failed the 802.11 association request with a failure reason. The association response frame should be included in the indication.</p>
</dd>

### -field <a id="WDI_ASSOC_STATUS_ASSOC_EXCHANGE_FAILURE"></a><a id="wdi_assoc_status_assoc_exchange_failure"></a><b>WDI_ASSOC_STATUS_ASSOC_EXCHANGE_FAILURE</b>

<dd>
<p>The association failed because the 802.11 association did not finish successfully. This reason should only be used if the port is not able to use one of the specific 802.11 association exchange failure codes.</p>
</dd>

### -field <a id="WDI_ASSOC_STATUS_DISASSOCIATE_BY_DEVICE_RESET"></a><a id="wdi_assoc_status_disassociate_by_device_reset"></a><b>WDI_ASSOC_STATUS_DISASSOCIATE_BY_DEVICE_RESET</b>

<dd>
<p>The disassociation is  because the device was reset (for example, due to a hang, NdisReset, or a reset that the miniport did internally).</p>
</dd>

### -field <a id="WDI_ASSOC_STATUS_DISASSOCIATE_UNABLE_TO_MAINTAIN"></a><a id="wdi_assoc_status_disassociate_unable_to_maintain"></a><b>WDI_ASSOC_STATUS_DISASSOCIATE_UNABLE_TO_MAINTAIN</b>

<dd>
<p>The disassociation is because the port is unable to maintain the connection due to other operations being performed on the port (for example, Bluetooth coexistence reasons). This should only be used if the port is not able to use one of the specific failure codes.</p>
</dd>

### -field <a id="WDI_ASSOC_STATUS_DISASSOCIATE_NOT_VISIBLE"></a><a id="wdi_assoc_status_disassociate_not_visible"></a><b>WDI_ASSOC_STATUS_DISASSOCIATE_NOT_VISIBLE</b>

<dd>
<p>The operation failed because the peer is not being heard from. The detection of an unreachable peer is up to the port. For example, a peer can be considered unreachable if the port misses multiple beacons from the peer.</p>
</dd>

### -field <a id="WDI_ASSOC_STATUS_DISASSOCIATE_NEEDED_REASSOC"></a><a id="wdi_assoc_status_disassociate_needed_reassoc"></a><b>WDI_ASSOC_STATUS_DISASSOCIATE_NEEDED_REASSOC</b>

<dd>
<p>The disassociation is because the port believes it needs to reassociate to the peer. This may be because the port determines that the peer thinks the association is no longer valid. This should only be used if the port is not able to use one of the specific failure codes (for example, WDI_ASSOC_STATUS_PEER_DEAUTHENTICATED).</p>
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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wditypes.hpp</dt>
</dl>
</td>
</tr>
</table>