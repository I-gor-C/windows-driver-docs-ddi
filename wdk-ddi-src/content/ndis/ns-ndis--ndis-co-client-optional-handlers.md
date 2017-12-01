---
UID: NS.ndis._NDIS_CO_CLIENT_OPTIONAL_HANDLERS
title: NDIS_CO_CLIENT_OPTIONAL_HANDLERS
author: windows-driver-content
description: The NDIS_CO_CLIENT_OPTIONAL_HANDLERS structure specifies entry points for CoNDIS client ProtocolXxx functions for the protocol driver that passes this structure to the NdisSetOptionalHandlers function.
old-location: netvista\ndis_co_client_optional_handlers.htm
old-project: netvista
ms.assetid: 1f2285bb-be70-4496-905d-89106bf3712a
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_CO_CLIENT_OPTIONAL_HANDLERS, NDIS_CO_CLIENT_OPTIONAL_HANDLERS, *PNDIS_CO_CLIENT_OPTIONAL_HANDLERS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_CO_CLIENT_OPTIONAL_HANDLERS
req.alt-loc: ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section
req.iface: 
---

# NDIS_CO_CLIENT_OPTIONAL_HANDLERS structure



## -description
<p>The NDIS_CO_CLIENT_OPTIONAL_HANDLERS structure specifies entry points for CoNDIS client 
  <i>ProtocolXxx</i> functions for the protocol driver that passes this structure to the 
  <a href="..\ndis\nf-ndis-ndissetoptionalhandlers.md">
  NdisSetOptionalHandlers</a> function.</p>


## -syntax

````
typedef struct _NDIS_CO_CLIENT_OPTIONAL_HANDLERS {
  NDIS_OBJECT_HEADER                  Header;
  ULONG                               Reserved;
  CO_CREATE_VC_HANDLER                ClCreateVcHandler;
  CO_DELETE_VC_HANDLER                ClDeleteVcHandler;
  CO_OID_REQUEST_HANDLER              ClOidRequestHandler;
  CO_OID_REQUEST_COMPLETE_HANDLER     ClOidRequestCompleteHandler;
  CL_OPEN_AF_COMPLETE_HANDLER_EX      ClOpenAfCompleteHandlerEx;
  CL_CLOSE_AF_COMPLETE_HANDLER        ClCloseAfCompleteHandler;
  CL_REG_SAP_COMPLETE_HANDLER         ClRegisterSapCompleteHandler;
  CL_DEREG_SAP_COMPLETE_HANDLER       ClDeregisterSapCompleteHandler;
  CL_MAKE_CALL_COMPLETE_HANDLER       ClMakeCallCompleteHandler;
  CL_MODIFY_CALL_QOS_COMPLETE_HANDLER ClModifyCallQoSCompleteHandler;
  CL_CLOSE_CALL_COMPLETE_HANDLER      ClCloseCallCompleteHandler;
  CL_ADD_PARTY_COMPLETE_HANDLER       ClAddPartyCompleteHandler;
  CL_DROP_PARTY_COMPLETE_HANDLER      ClDropPartyCompleteHandler;
  CL_INCOMING_CALL_HANDLER            ClIncomingCallHandler;
  CL_INCOMING_CALL_QOS_CHANGE_HANDLER ClIncomingCallQoSChangeHandler;
  CL_INCOMING_CLOSE_CALL_HANDLER      ClIncomingCloseCallHandler;
  CL_INCOMING_DROP_PARTY_HANDLER      ClIncomingDropPartyHandler;
  CL_CALL_CONNECTED_HANDLER           ClCallConnectedHandler;
  CL_NOTIFY_CLOSE_AF_HANDLER          ClNotifyCloseAfHandler;
} NDIS_CO_CLIENT_OPTIONAL_HANDLERS, *PNDIS_CO_CLIENT_OPTIONAL_HANDLERS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure for the
     protocol driver CoNDIS characteristics structure (NDIS_CO_CLIENT_OPTIONAL_HANDLERS). The driver sets the
     
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_CO_CLIENT_OPTIONAL_HANDLERS, the 
     <b>Revision</b> member to NDIS_CO_CLIENT_OPTIONAL_HANDLERS_REVISION_1, and the 
     <b>Size</b> member to NDIS_SIZEOF_CO_CLIENT_OPTIONAL_HANDLERS_REVISION_1.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field <b>ClCreateVcHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-co-create-vc.md">ProtocolCoCreateVc</a> function.</p>
</dd>

### -field <b>ClDeleteVcHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-co-delete-vc.md">ProtocolCoDeleteVc</a> function.</p>
</dd>

### -field <b>ClOidRequestHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-co-oid-request.md">
     ProtocolCoOidRequest</a> function.</p>
</dd>

### -field <b>ClOidRequestCompleteHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-co-oid-request-complete.md">
     ProtocolCoOidRequestComplete</a> function.</p>
</dd>

### -field <b>ClOpenAfCompleteHandlerEx</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-cl-open-af-complete-ex.md">
     ProtocolClOpenAfCompleteEx</a> function.</p>
</dd>

### -field <b>ClCloseAfCompleteHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-cl-close-af-complete.md">
     ProtocolClCloseAfComplete</a> function.</p>
</dd>

### -field <b>ClRegisterSapCompleteHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-cl-register-sap-complete.md">
     ProtocolClRegisterSapComplete</a> function. A client uses this function to accept incoming calls from
     remote machines.</p>
</dd>

### -field <b>ClDeregisterSapCompleteHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-cl-deregister-sap-complete.md">
     ProtocolClDeregisterSapComplete</a> function.</p>
</dd>

### -field <b>ClMakeCallCompleteHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-cl-make-call-complete.md">
     ProtocolClMakeCallComplete</a> function. A client uses this function to make outgoing calls to remote
     machines.</p>
</dd>

### -field <b>ClModifyCallQoSCompleteHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-cl-modify-call-qos-complete.md">
     ProtocolClModifyCallQoSComplete</a> function. A client uses this function to dynamically make changes
     in the quality of service (QoS) on an established virtual connection (VC) or to negotiate with the call
     manager to establish the QoS when the client sets up an incoming call.</p>
</dd>

### -field <b>ClCloseCallCompleteHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-cl-close-call-complete.md">
     ProtocolClCloseCallComplete</a> function.</p>
</dd>

### -field <b>ClAddPartyCompleteHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-cl-add-party-complete.md">
     ProtocolClAddPartyComplete</a> function. A client uses this function to establish point-to-multipoint
     VCs for outgoing calls to remote machines.</p>
</dd>

### -field <b>ClDropPartyCompleteHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-cl-drop-party-complete.md">
     ProtocolClDropPartyComplete</a> function.</p>
</dd>

### -field <b>ClIncomingCallHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-cl-incoming-call.md">
     ProtocolClIncomingCall</a> function. A client uses this function to accept incoming calls from remote
     machines.</p>
</dd>

### -field <b>ClIncomingCallQoSChangeHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-cl-incoming-call-qos-change.md">
     ProtocolClIncomingCallQoSChange</a> function. A client uses this function to accept incoming calls
     from remote machines on which the sending client can dynamically change the QoS.</p>
</dd>

### -field <b>ClIncomingCloseCallHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-cl-incoming-close-call.md">
     ProtocolClIncomingCloseCall</a> function.</p>
</dd>

### -field <b>ClIncomingDropPartyHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-cl-incoming-drop-party.md">
     ProtocolClIncomingDropParty</a> function.</p>
</dd>

### -field <b>ClCallConnectedHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-cl-call-connected.md">
     ProtocolClCallConnected</a> function. A client uses this function to accept incoming calls from remote
     machines.</p>
</dd>

### -field <b>ClNotifyCloseAfHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-cl-notify-close-af.md">
     ProtocolClNotifyCloseAf</a> function.</p>
</dd>
</dl>

## -remarks
<p>To specify entry points as a CoNDIS client, a protocol driver initializes an
    NDIS_CO_CLIENT_OPTIONAL_HANDLERS structure and passes it to the 
    <a href="..\ndis\nf-ndis-ndissetoptionalhandlers.md">
    NdisSetOptionalHandlers</a> function.</p>

<p>The client calls 
    <b>NdisSetOptionalHandlers</b> from the 
    <a href="..\ndis\nc-ndis-set-options.md">ProtocolSetOptions</a> function. The
    client must set every 
    <b>Cl</b><i>Xxx</i> member in the NDIS_CO_CLIENT_OPTIONAL_HANDLERS structure to a caller-supplied 
    <i>ProtocolXxx</i> function, even if the call manager does not support incoming calls, outgoing calls, or
    point-to-multipoint connections. For whatever subset of connection-oriented functionality that a client
    does not support, its placeholder 
    <i>ProtocolXxx</i> functions should return NDIS_STATUS_NOT_SUPPORTED.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndissetoptionalhandlers.md">NdisSetOptionalHandlers</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cl-add-party-complete.md">ProtocolClAddPartyComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cl-call-connected.md">ProtocolClCallConnected</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cl-close-af-complete.md">ProtocolClCloseAfComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cl-close-call-complete.md">ProtocolClCloseCallComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cl-deregister-sap-complete.md">
   ProtocolClDeregisterSapComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cl-drop-party-complete.md">ProtocolClDropPartyComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cl-incoming-call.md">ProtocolClIncomingCall</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cl-incoming-call-qos-change.md">
   ProtocolClIncomingCallQoSChange</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cl-incoming-close-call.md">ProtocolClIncomingCloseCall</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cl-incoming-drop-party.md">ProtocolClIncomingDropParty</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cl-make-call-complete.md">ProtocolClMakeCallComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cl-modify-call-qos-complete.md">
   ProtocolClModifyCallQoSComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cl-open-af-complete-ex.md">ProtocolClOpenAfCompleteEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cl-register-sap-complete.md">
   ProtocolClRegisterSapComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-co-af-register-notify.md">ProtocolCoAfRegisterNotify</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-co-create-vc.md">ProtocolCoCreateVc</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-co-delete-vc.md">ProtocolCoDeleteVc</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-co-oid-request.md">ProtocolCoOidRequest</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-co-oid-request-complete.md">
   ProtocolCoOidRequestComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-set-options.md">ProtocolSetOptions</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_CO_CLIENT_OPTIONAL_HANDLERS structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
