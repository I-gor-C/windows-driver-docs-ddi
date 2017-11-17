---
UID: NS.ndiswwan._NDIS_WWAN_CONTEXT_STATE
title: NDIS_WWAN_CONTEXT_STATE
author: windows-driver-content
description: The NDIS_WWAN_CONTEXT_STATE structure represents the Packet Data Protocol (PDP) context state of the MB device.
old-location: netvista\ndis_wwan_context_state.htm
ms.assetid: 7918ee03-c1cb-4a38-8773-4a01832357d2
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndiswwan.h
req.include-header: Ndiswwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_WWAN_CONTEXT_STATE
req.alt-loc: ndiswwan.h
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
ms.keywords: NDIS_WWAN_CONTEXT_STATE, NDIS_WWAN_CONTEXT_STATE, *PNDIS_WWAN_CONTEXT_STATE
req.iface: 
---

# NDIS_WWAN_CONTEXT_STATE structure



## -description
<p>The NDIS_WWAN_CONTEXT_STATE structure represents the Packet Data Protocol (PDP) context state of the
  MB device.</p>


## -syntax

````
typedef struct _NDIS_WWAN_CONTEXT_STATE {
  NDIS_OBJECT_HEADER Header;
  WWAN_STATUS        uStatus;
  WWAN_CONTEXT_STATE ContextState;
} NDIS_WWAN_CONTEXT_STATE, *PNDIS_WWAN_CONTEXT_STATE;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The header with type, revision, and size information about the NDIS_WWAN_CONTEXT_STATE structure.
     The MB Service sets the header with the values that are shown in the following table when it sends the
     data structure to the miniport driver for 
     <i>set</i> operations. Miniport drivers must set the header with the same values when they send the data
     structure to the MB service.
     </p>
<table>
<tr>
<th>Header submember</th>
<th>Value</th>
</tr>
<tr>
<td>
<p>Type</p>
</td>
<td>
<p>NDIS_OBJECT_TYPE_DEFAULT</p>
</td>
</tr>
<tr>
<td>
<p>Revision</p>
</td>
<td>
<p>Windows 8 miniport drivers should set this to NDIS_WWAN_CONTEXT_STATE_REVISION_2. Windows 7 miniport drivers should set this to NDIS_WWAN_CONTEXT_STATE_REVISION_1.</p>
</td>
</tr>
<tr>
<td>
<p>Size</p>
</td>
<td>
<p>sizeof(NDIS_WWAN_CONTEXT_STATE)</p>
</td>
</tr>
</table>
<p> </p>
<p>For more information about these members, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>.</p>
</dd>

### -field <b>uStatus</b>

<dd>
<p>The status of context activation or deactivation operation. The following table shows the possible
     values for this member.
     </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>WWAN_STATUS_SUCCESS</p>
</td>
<td>
<p>Context activation or deactivation succeeded.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_FAILURE</p>
</td>
<td>
<p>The operation failed. Miniport drivers can return this value if the context has already been
        activated.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_PIN_REQUIRED</p>
</td>
<td>
<p>The operation failed because the device requires a PIN.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_BAD_SIM</p>
</td>
<td>
<p>The operation failed because a bad SIM card was detected.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_SIM_NOT_INSERTED</p>
</td>
<td>
<p>The operation failed because the SIM card was not inserted fully into the device.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_NOT_INITIALIZED</p>
</td>
<td>
<p>The operation failed because the device is in the process of initializing. Retry the operation
        after the ready-state of the device changes to 
        <b>WwanReadyStateInitialized</b>.</p>
</td>
</tr>
</table>
<p> </p>
<p>Miniport drivers can return the following error codes (in addition to those previously described)
     only in the event of a failed set PDP activation operation.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>WWAN_STATUS_RADIO_POWER_OFF</p>
</td>
<td>
<p>The operation failed because the radio is currently turned off. This error code should be returned
        only in response to a OID_WWAN_CONNECT 
        <i>set</i> request. If the radio state is off then the miniport driver should respond to
        OID_WWAN_CONNECT 
        <i>query</i> requests with WWAN_STATUS_SUCCESS and specify the current context state as 
        <b>WwanActivationStateDeactivated</b>.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_SERVICE_NOT_ACTIVATED</p>
</td>
<td>
<p>The operation failed because either the subscription has expired, or the device does not allow PDP
        activation.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_PROVIDER_NOT_VISIBLE</p>
</td>
<td>
<p>The operation failed because the service provider is not currently visible.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_MAX_ACTIVATED_CONTEXTS</p>
</td>
<td>
<p>The operation failed because the maximum number of activated contexts has been reached.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_INVALID_ACCESS_STRING</p>
</td>
<td>
<p>The operation failed because the access string is invalid.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_INVALID_USER_NAME_PWD</p>
</td>
<td>
<p>The operation failed because the user name and/or password supplied are invalid. Network specific
        error code may be available in 
        <b>uNwError</b> .</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_PACKET_SVC_DETACHED</p>
</td>
<td>
<p>The operation failed because packet service is detached.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_NOT_REGISTERED</p>
</td>
<td>
<p>The operation failed because the device is not in the registered state to perform PDP
        activation.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_VOICE_CALL_IN_PROGRESS</p>
</td>
<td>
<p>The operation failed and cannot proceed with PDP activation because a voice call is currently in
        progress. This value applies only to devices with voice class is set to 
        <b>WwanVoiceClassSeparateVoiceData</b>.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_CONTEXT_NOT_ACTIVATED</p>
</td>
<td>
<p>The operation failed because the context identified by 
        <b>ConnectionId</b> is not the currently activated context.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>ContextState</b>

<dd>
<p>A formatted 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571202">WWAN_CONTEXT_STATE</a> object that
     represents the Packet Data Protocol (PDP) context state of the device.</p>
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
<p>Available in Windows 7 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndiswwan.h (include Ndiswwan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571202">WWAN_CONTEXT_STATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_WWAN_CONTEXT_STATE structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
