---
UID: NS.wlanihv._DOT11EXT_IHV_HANDLERS
title: DOT11EXT_IHV_HANDLERS
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11ext_ihv_handlers.htm
old-project: netvista
ms.assetid: 6dacd330-45f1-46f8-b2bf-2006c89f664f
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: DOT11EXT_IHV_HANDLERS,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wlanihv.h
req.include-header: Wlanihv.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11EXT_IHV_HANDLERS
req.alt-loc: wlanihv.h
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

# DOT11EXT_IHV_HANDLERS structure



## -description

## -syntax

````
typedef struct _DOT11EXT_IHV_HANDLERS {
  DOT11EXTIHV_DEINIT_SERVICE            Dot11ExtIhvDeinitService;
  DOT11EXTIHV_INIT_ADAPTER              Dot11ExtIhvInitAdapter;
  DOT11EXTIHV_DEINIT_ADAPTER            Dot11ExtIhvDeinitAdapter;
  DOT11EXTIHV_PERFORM_PRE_ASSOCIATE     Dot11ExtIhvPerformPreAssociate;
  DOT11EXTIHV_ADAPTER_RESET             Dot11ExtIhvAdapterReset;
  DOT11EXTIHV_PERFORM_POST_ASSOCIATE    Dot11ExtIhvPerformPostAssociate;
  DOT11EXTIHV_STOP_POST_ASSOCIATE       Dot11ExtIhvStopPostAssociate;
  DOT11EXTIHV_VALIDATE_PROFILE          Dot11ExtIhvValidateProfile;
  DOT11EXTIHV_PERFORM_CAPABILITY_MATCH  Dot11ExtIhvPerformCapabilityMatch;
  DOT11EXTIHV_CREATE_DISCOVERY_PROFILES Dot11ExtIhvCreateDiscoveryProfiles;
  DOT11EXTIHV_PROCESS_SESSION_CHANGE    Dot11ExtIhvProcessSessionChange;
  DOT11EXTIHV_RECEIVE_INDICATION        Dot11ExtIhvReceiveIndication;
  DOT11EXTIHV_RECEIVE_PACKET            Dot11ExtIhvReceivePacket;
  DOT11EXTIHV_SEND_PACKET_COMPLETION    Dot11ExtIhvSendPacketCompletion;
  DOT11EXTIHV_IS_UI_REQUEST_PENDING     Dot11ExtIhvIsUIRequestPending;
  DOT11EXTIHV_PROCESS_UI_RESPONSE       Dot11ExtIhvProcessUIResponse;
  DOT11EXTIHV_QUERY_UI_REQUEST          Dot11ExtIhvQueryUIRequest;
  DOT11EXTIHV_ONEX_INDICATE_RESULT      Dot11ExtIhvOnexIndicateResult;
  DOT11EXTIHV_CONTROL                   Dot11ExtIhvControl;
} DOT11EXT_IHV_HANDLERS, *PDOT11EXT_IHV_HANDLERS;
````


## -struct-fields
<dl>

### -field Dot11ExtIhvDeinitService

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv-deinit-service.md">
     Dot11ExtIhvDeinitService</a> function.</p>
</dd>

### -field Dot11ExtIhvInitAdapter

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv-init-adapter.md">
     Dot11ExtIhvInitAdapter</a> function.</p>
</dd>

### -field Dot11ExtIhvDeinitAdapter

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv-deinit-adapter.md">
     Dot11ExtIhvDeinitAdapter</a> function.</p>
</dd>

### -field Dot11ExtIhvPerformPreAssociate

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv-perform-pre-associate.md">
     Dot11ExtIhvPerformPreAssociate</a> function.</p>
</dd>

### -field Dot11ExtIhvAdapterReset

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv-adapter-reset.md">
     Dot11ExtIhvAdapterReset</a> function.</p>
</dd>

### -field Dot11ExtIhvPerformPostAssociate

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv-perform-post-associate.md">
     Dot11ExtIhvPerformPostAssociate</a> function.</p>
</dd>

### -field Dot11ExtIhvStopPostAssociate

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv-stop-post-associate.md">
     Dot11ExtIhvStopPostAssociate</a> function.</p>
</dd>

### -field Dot11ExtIhvValidateProfile

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv-validate-profile.md">
     Dot11ExtIhvValidateProfile</a> function.</p>
</dd>

### -field Dot11ExtIhvPerformCapabilityMatch

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv-perform-capability-match.md">
     Dot11ExtIhvPerformCapabilityMatch</a> function.</p>
</dd>

### -field Dot11ExtIhvCreateDiscoveryProfiles

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv-create-discovery-profiles.md">
     Dot11ExtIhvCreateDiscoveryProfiles</a> function.</p>
</dd>

### -field Dot11ExtIhvProcessSessionChange

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv-process-session-change.md">
     Dot11ExtIhvProcessSessionChange</a> function.</p>
</dd>

### -field Dot11ExtIhvReceiveIndication

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv-receive-indication.md">
     Dot11ExtIhvReceiveIndication</a> function.</p>
</dd>

### -field Dot11ExtIhvReceivePacket

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv-receive-packet.md">
     Dot11ExtIhvReceivePacket</a> function.</p>
</dd>

### -field Dot11ExtIhvSendPacketCompletion

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv-send-packet-completion.md">
     Dot11ExtIhvSendPacketCompletion</a> function.</p>
</dd>

### -field Dot11ExtIhvIsUIRequestPending

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv-is-ui-request-pending.md">
     Dot11ExtIhvIsUIRequestPending</a> function.</p>
</dd>

### -field Dot11ExtIhvProcessUIResponse

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv-process-ui-response.md">
     Dot11ExtIhvProcessUIResponse</a> function.</p>
</dd>

### -field Dot11ExtIhvQueryUIRequest

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv-query-ui-request.md">
     Dot11ExtIhvQueryUIRequest</a> function.</p>
</dd>

### -field Dot11ExtIhvOnexIndicateResult

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv-onex-indicate-result.md">
     Dot11ExtIhvOneXIndicateResult</a> function.</p>
</dd>

### -field Dot11ExtIhvControl

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv-control.md">Dot11ExtIhvControl</a> function.</p>
</dd>
</dl>

## -remarks
<p>The IHV handler functions are a set of callback functions supported by the IHV Extensions DLL. When
    the operating system calls the 
    <a href="..\wlanihv\nc-wlanihv-dot11extihv-init-service.md">Dot11ExtIhvInitService</a> IHV
    handler function, the IHV Extensions DLL returns the list of pointers to the IHV handler functions
    through the 
    <i>pDot11IHVHandlers</i> parameter.</p>

<p>All of the function pointers are required and must not be set to <b>NULL</b>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating
   systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wlanihv.h (include Wlanihv.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-adapter-reset.md">Dot11ExtIhvAdapterReset</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-control.md">Dot11ExtIhvControl Function</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-create-discovery-profiles.md">
   Dot11ExtIhvCreateDiscoveryProfiles</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-deinit-adapter.md">Dot11ExtIhvDeinitAdapter</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-deinit-service.md">Dot11ExtIhvDeinitService</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-get-version-info.md">Dot11ExtIhvGetVersionInfo</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-init-adapter.md">Dot11ExtIhvInitAdapter</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-init-service.md">Dot11ExtIhvInitService</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-is-ui-request-pending.md">
   Dot11ExtIhvIsUIRequestPending</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-onex-indicate-result.md">
   Dot11ExtIhvOneXIndicateResult</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-perform-capability-match.md">
   Dot11ExtIhvPerformCapabilityMatch</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-perform-post-associate.md">
   Dot11ExtIhvPerformPostAssociate</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-perform-pre-associate.md">
   Dot11ExtIhvPerformPreAssociate</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-process-session-change.md">
   Dot11ExtIhvProcessSessionChange</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-process-ui-response.md">
   Dot11ExtIhvProcessUIResponse</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-query-ui-request.md">Dot11ExtIhvQueryUIRequest</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-receive-indication.md">
   Dot11ExtIhvReceiveIndication</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-receive-packet.md">Dot11ExtIhvReceivePacket</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-send-packet-completion.md">
   Dot11ExtIhvSendPacketCompletion</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-stop-post-associate.md">
   Dot11ExtIhvStopPostAssociate</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-validate-profile.md">Dot11ExtIhvValidateProfile</a>
</dt>
<dt>
<a href="netvista.native_802_11_ihv_extensibility_functions">Native 802.11 IHV
   Extensibility Functions</a>
</dt>
<dt>
<a href="netvista.native_802_11_ihv_handler_functions">Native 802.11 IHV Handler
   Functions</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11EXT_IHV_HANDLERS structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
