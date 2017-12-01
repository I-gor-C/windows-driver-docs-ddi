---
UID: NS.ndis._NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS
title: NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS
author: windows-driver-content
description: The NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS structure specifies CoNDIS call manager ProtocolXxx functions for the driver that passes this structure to the NdisSetOptionalHandlers function.
old-location: netvista\ndis_co_call_manager_optional_handlers.htm
old-project: netvista
ms.assetid: 12d541e1-04dd-4512-827e-d27f16260fe3
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS, NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS, *PNDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS
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
req.alt-api: NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS
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

# NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS structure



## -description
<p>The NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS structure specifies CoNDIS call manager 
  <i>ProtocolXxx</i> functions for the driver that passes this structure to the 
  <a href="..\ndis\nf-ndis-ndissetoptionalhandlers.md">
  NdisSetOptionalHandlers</a> function.</p>


## -syntax

````
typedef struct _NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS {
  NDIS_OBJECT_HEADER                  Header;
  ULONG                               Reserved;
  CO_CREATE_VC_HANDLER                CmCreateVcHandler;
  CO_DELETE_VC_HANDLER                CmDeleteVcHandler;
  CM_OPEN_AF_HANDLER                  CmOpenAfHandler;
  CM_CLOSE_AF_HANDLER                 CmCloseAfHandler;
  CM_REG_SAP_HANDLER                  CmRegisterSapHandler;
  CM_DEREG_SAP_HANDLER                CmDeregisterSapHandler;
  CM_MAKE_CALL_HANDLER                CmMakeCallHandler;
  CM_CLOSE_CALL_HANDLER               CmCloseCallHandler;
  CM_INCOMING_CALL_COMPLETE_HANDLER   CmIncomingCallCompleteHandler;
  CM_ADD_PARTY_HANDLER                CmAddPartyHandler;
  CM_DROP_PARTY_HANDLER               CmDropPartyHandler;
  CM_ACTIVATE_VC_COMPLETE_HANDLER     CmActivateVcCompleteHandler;
  CM_DEACTIVATE_VC_COMPLETE_HANDLER   CmDeactivateVcCompleteHandler;
  CM_MODIFY_CALL_QOS_HANDLER          CmModifyCallQoSHandler;
  CO_OID_REQUEST_HANDLER              CmOidRequestHandler;
  CO_OID_REQUEST_COMPLETE_HANDLER     CmOidRequestCompleteHandler;
  CM_NOTIFY_CLOSE_AF_COMPLETE_HANDLER CmNotifyCloseAfCompleteHandler;
} NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS, *PNDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure for the
     call manager CoNDIS characteristics structure (NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS). Set the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_CO_CALL_MANAGER_OPTIONAL_HANDLERS, the 
     <b>Revision</b> member to NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS_REVISION_1, and the 
     <b>Size</b> member to NDIS_SIZEOF_CO_CALL_MANAGER_OPTIONAL_HANDLERS_REVISION_1.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field <b>CmCreateVcHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-co-create-vc.md">ProtocolCoCreateVc</a> function.</p>
</dd>

### -field <b>CmDeleteVcHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-co-delete-vc.md">ProtocolCoDeleteVc</a> function.</p>
</dd>

### -field <b>CmOpenAfHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-cm-open-af.md">ProtocolCmOpenAf</a> function.</p>
</dd>

### -field <b>CmCloseAfHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-cm-close-af.md">ProtocolCmCloseAf</a> function.</p>
</dd>

### -field <b>CmRegisterSapHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-cm-reg-sap.md">
     ProtocolCmRegisterSap</a> function.</p>
</dd>

### -field <b>CmDeregisterSapHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-cm-deregister-sap.md">
     ProtocolCmDeregisterSap</a> function.</p>
</dd>

### -field <b>CmMakeCallHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-cm-make-call.md">ProtocolCmMakeCall</a> function.</p>
</dd>

### -field <b>CmCloseCallHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-cm-close-call.md">
     ProtocolCmCloseCall</a> function.</p>
</dd>

### -field <b>CmIncomingCallCompleteHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-cm-incoming-call-complete.md">
     ProtocolCmIncomingCallComplete</a> function.</p>
</dd>

### -field <b>CmAddPartyHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-cm-add-party.md">ProtocolCmAddParty</a> function.</p>
</dd>

### -field <b>CmDropPartyHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-cm-drop-party.md">
     ProtocolCmDropParty</a> function.</p>
</dd>

### -field <b>CmActivateVcCompleteHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-cm-activate-vc-complete.md">
     ProtocolCmActivateVcComplete</a> function.</p>
</dd>

### -field <b>CmDeactivateVcCompleteHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-cm-deactivate-vc-complete.md">
     ProtocolCmDeactivateVcComplete</a> function.</p>
</dd>

### -field <b>CmModifyCallQoSHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-cm-modify-qos-call.md">
     ProtocolCmModifyCallQoS</a> function.</p>
</dd>

### -field <b>CmOidRequestHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-co-oid-request.md">
     ProtocolCoOidRequest</a> function.</p>
</dd>

### -field <b>CmOidRequestCompleteHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-co-oid-request-complete.md">
     ProtocolCoOidRequestComplete</a> function.</p>
</dd>

### -field <b>CmNotifyCloseAfCompleteHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-cm-notify-close-af-complete.md">
     ProtocolCmNotifyCloseAfComplete</a> function.</p>
</dd>
</dl>

## -remarks
<p>To specify entry points as a CoNDIS call manager, a protocol driver or miniport call manager (MCM)
    initializes an NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS structure and passes it to the 
    <a href="..\ndis\nf-ndis-ndissetoptionalhandlers.md">
    NdisSetOptionalHandlers</a> function.</p>

<p>A stand-alone call manager calls 
     <b>NdisSetOptionalHandlers</b> from the 
     <a href="..\ndis\nc-ndis-set-options.md">ProtocolSetOptions</a> function. The
     call manager must set every entry point in the NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS structure to a
     driver-supplied 
     <i>ProtocolXxx</i> function when it calls 
     <a href="..\ndis\nf-ndis-ndissetoptionalhandlers.md">NdisSetOptionalHandlers</a>, even if
     the call manager does not support incoming calls, outgoing calls, or point-to-multipoint connections.
     For whatever subset of connection-oriented functionality that such a call manager does not support, its
     placeholder 
     <i>ProtocolXxx</i> functions should simply return NDIS_STATUS_NOT_SUPPORTED.</p>

<p>After a stand-alone call manager calls the 
     <a href="..\ndis\nf-ndis-ndiscmregisteraddressfamilyex.md">
     NdisCmRegisterAddressFamilyEx</a> function successfully, NDIS ignores any entry point that the call
     manager previously specified for the 
     <a href="..\ndis\nc-ndis-protocol-oid-request-complete.md">
     ProtocolOidRequestComplete</a> function of the 
     <a href="..\ndis\ns-ndis--ndis-protocol-driver-characteristics.md">
     NDIS_PROTOCOL_DRIVER_CHARACTERISTICS</a> structure that it passed to the 
     <a href="..\ndis\nf-ndis-ndisregisterprotocoldriver.md">
     NdisRegisterProtocolDriver</a> function.</p>

<p>An MCM calls the 
     <a href="..\ndis\nf-ndis-ndissetoptionalhandlers.md">NdisSetOptionalHandlers</a> function
     from the 
     <a href="netvista.miniportsetoptions">MiniportSetOptions</a> function. The
     MCM must set every 
     <b>Cm</b><i>Xxx</i> member in the NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS structure to a MCM-supplied 
     <i>ProtocolXxx</i> function even if the MCM does not support incoming calls, outgoing calls, or
     point-to-multipoint connections. For whatever subset of connection-oriented functionality that such an
     MCM driver does not support, its 
     <i>ProtocolXxx</i> functions should simply return NDIS_STATUS_NOT_SUPPORTED. For example, NDIS never
     calls an MCM driver's registered 
     <a href="..\ndis\nc-ndis-protocol-cm-activate-vc-complete.md">
     ProtocolCmActivateVcComplete</a> or 
     <a href="..\ndis\nc-ndis-protocol-cm-deactivate-vc-complete.md">
     ProtocolCmDeactivateVcComplete</a> function, so these functions can return NDIS_STATUS_NOT_SUPPORTED
     but must have entry points in the NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS structure.</p>

<p>An MCM driver must specify entry points for the 
     <a href="..\ndis\nc-ndis-protocol-co-create-vc.md">ProtocolCoCreateVc</a> and 
     <a href="..\ndis\nc-ndis-protocol-co-delete-vc.md">ProtocolCoDeleteVc</a> functions. If
     the MCM previously registered a 
     <a href="..\ndis\nc-ndis-miniport-co-create-vc.md">MiniportCoCreateVc</a> or 
     <a href="..\ndis\nc-ndis-miniport-co-delete-vc.md">MiniportCoDeleteVc</a> function. NDIS
     ignores the entry points for these functions, whenever NDIS calls the MCM driver to create or delete a
     virtual connection (VC). Therefore, NDIS passes in an 
     <i>NdisAfHandle</i> value for the initial parameter to the MCM-supplied 
     <i>ProtocolCoCreateVc</i> or 
     <i>ProtocolCoDeleteVc</i> function, rather than the 
     <i>MiniportAdapterContext</i> value that it would pass to the 
     <i>MiniportCoCreateVc</i> or 
     <i>MiniportCoDeleteVc</i> function of a non-MCM miniport driver.</p>

<p>An MCM driver cannot set the 
     <b>CmOidRequestHandler</b> member of NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS to its 
     <a href="..\ndis\nc-ndis-miniport-co-oid-request.md">MiniportCoOidRequest</a> function.
     The driver must provide a separate entry point for a 
     <a href="..\ndis\nc-ndis-protocol-co-oid-request.md">ProtocolCoOidRequest</a> function. An
     MCM driver must have a 
     <i>ProtocolCoOidRequest</i> function to handle call manager requests from CoNDIS clients and must have a 
     <a href="..\ndis\nc-ndis-protocol-co-oid-request-complete.md">
     ProtocolCoOidRequestComplete</a> function.</p>

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
<a href="..\ndis\nc-ndis-miniport-co-create-vc.md">MiniportCoCreateVc</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-co-delete-vc.md">MiniportCoDeleteVc</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-co-oid-request.md">MiniportCoOidRequest</a>
</dt>
<dt>
<a href="netvista.miniportsetoptions">MiniportSetOptions</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-protocol-driver-characteristics.md">
   NDIS_PROTOCOL_DRIVER_CHARACTERISTICS</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndiscmregisteraddressfamilyex.md">
   NdisCmRegisterAddressFamilyEx</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisregisterprotocoldriver.md">NdisRegisterProtocolDriver</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndissetoptionalhandlers.md">NdisSetOptionalHandlers</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cm-activate-vc-complete.md">
   ProtocolCmActivateVcComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cm-add-party.md">ProtocolCmAddParty</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cm-close-af.md">ProtocolCmCloseAf</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cm-close-call.md">ProtocolCmCloseCall</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cm-deactivate-vc-complete.md">
   ProtocolCmDeactivateVcComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cm-deregister-sap.md">ProtocolCmDeregisterSap</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cm-drop-party.md">ProtocolCmDropParty</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cm-incoming-call-complete.md">
   ProtocolCmIncomingCallComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cm-make-call.md">ProtocolCmMakeCall</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cm-modify-qos-call.md">ProtocolCmModifyCallQoS</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cm-open-af.md">ProtocolCmOpenAf</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cm-reg-sap.md">ProtocolCmRegisterSap</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-oid-request-complete.md">ProtocolOidRequestComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-set-options.md">ProtocolSetOptions</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
