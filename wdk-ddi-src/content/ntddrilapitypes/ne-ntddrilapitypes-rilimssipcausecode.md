---
UID: NE.ntddrilapitypes.RILIMSSIPCAUSECODE
title: RILIMSSIPCAUSECODE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilimssipcausecode.htm
old-project: netvista
ms.assetid: b76ea0fb-8139-4272-b9a0-2daa5b660c7d
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: TUPLE_REQUEST, TUPLE_REQUEST, *PTUPLE_REQUEST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILIMSSIPCAUSECODE
req.alt-loc: ntddrilapitypes.h
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
---

# RILIMSSIPCAUSECODE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILIMSSIPCAUSECODE { 
  RIL_IMSSIPCAUSE_UNAUTHORIZED,
  RIL_IMSSIPCAUSE_PAYMENT_REQUIRED,
  RIL_IMSSIPCAUSE_FORBIDDEN,
  RIL_IMSSIPCAUSE_NOT_FOUND,
  RIL_IMSSIPCAUSE_METHOD_NOT_ALLOWED,
  RIL_IMSSIPCAUSE_NOT_ACCEPTABLE,
  RIL_IMSSIPCAUSE_PROXY_AUTHENTICATION_REQUIRED,
  RIL_IMSSIPCAUSE_REQUEST_TIMEOUT,
  RIL_IMSSIPCAUSE_GONE,
  RIL_IMSSIPCAUSE_REQUEST_ENTITY_TOO_LARGE,
  RIL_IMSSIPCAUSE_REQUEST_URI_TOO_LONG,
  RIL_IMSSIPCAUSE_UNSUPPORTED_MEDIA_TYPE,
  RIL_IMSSIPCAUSE_UNSUPPORTED_URI_SCHEME,
  RIL_IMSSIPCAUSE_BAD_EXTENSION,
  RIL_IMSSIPCAUSE_EXTENSION_REQUIRED,
  RIL_IMSSIPCAUSE_INTERVAL_TOO_BRIEF,
  RIL_IMSSIPCAUSE_TEMPORARILY_UNAVAILABLE,
  RIL_IMSSIPCAUSE_CALL_OR_TRANSACTION_DOES_NOT_EXIST,
  RIL_IMSSIPCAUSE_LOOP_DETECTED,
  RIL_IMSSIPCAUSE_TOO_MANY_HOPS,
  RIL_IMSSIPCAUSE_ADDRESS_INCOMPLETE,
  RIL_IMSSIPCAUSE_AMBIGUOUS,
  RIL_IMSSIPCAUSE_BUSY_HERE,
  RIL_IMSSIPCAUSE_REQUEST_TERMINATED,
  RIL_IMSSIPCAUSE_NOT_ACCEPTABLE_HERE,
  RIL_IMSSIPCAUSE_REQUEST_PENDING,
  RIL_IMSSIPCAUSE_UNDECIPHERABLE,
  RIL_IMSSIPCAUSE_SERVER_INTERNAL_ERROR,
  RIL_IMSSIPCAUSE_NOT_IMPLEMENTED,
  RIL_IMSSIPCAUSE_BAD_GATEWAY,
  RIL_IMSSIPCAUSE_SERVICE_UNAVAILABLE,
  RIL_IMSSIPCAUSE_SERVER_TIMEOUT,
  RIL_IMSSIPCAUSE_VERSION_NOT_SUPPORTED,
  RIL_IMSSIPCAUSE_MESSAGE_TOO_LARGE,
  RIL_IMSSIPCAUSE_BUSY_EVERYWHERE,
  RIL_IMSSIPCAUSE_DECLINE,
  RIL_IMSSIPCAUSE_DOES_NOT_EXIST_ANYWHERE,
  RIL_IMSSIPCAUSE_NOT_ACCEPTABLE_PARTIAL
} RILIMSSIPCAUSECODE;
````


## -enum-fields
<dl>

### -field <a id="RIL_IMSSIPCAUSE_UNAUTHORIZED"></a><a id="ril_imssipcause_unauthorized"></a><b>RIL_IMSSIPCAUSE_UNAUTHORIZED</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_PAYMENT_REQUIRED"></a><a id="ril_imssipcause_payment_required"></a><b>RIL_IMSSIPCAUSE_PAYMENT_REQUIRED</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_FORBIDDEN"></a><a id="ril_imssipcause_forbidden"></a><b>RIL_IMSSIPCAUSE_FORBIDDEN</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_NOT_FOUND"></a><a id="ril_imssipcause_not_found"></a><b>RIL_IMSSIPCAUSE_NOT_FOUND</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_METHOD_NOT_ALLOWED"></a><a id="ril_imssipcause_method_not_allowed"></a><b>RIL_IMSSIPCAUSE_METHOD_NOT_ALLOWED</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_NOT_ACCEPTABLE"></a><a id="ril_imssipcause_not_acceptable"></a><b>RIL_IMSSIPCAUSE_NOT_ACCEPTABLE</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_PROXY_AUTHENTICATION_REQUIRED"></a><a id="ril_imssipcause_proxy_authentication_required"></a><b>RIL_IMSSIPCAUSE_PROXY_AUTHENTICATION_REQUIRED</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_REQUEST_TIMEOUT"></a><a id="ril_imssipcause_request_timeout"></a><b>RIL_IMSSIPCAUSE_REQUEST_TIMEOUT</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_GONE"></a><a id="ril_imssipcause_gone"></a><b>RIL_IMSSIPCAUSE_GONE</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_REQUEST_ENTITY_TOO_LARGE"></a><a id="ril_imssipcause_request_entity_too_large"></a><b>RIL_IMSSIPCAUSE_REQUEST_ENTITY_TOO_LARGE</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_REQUEST_URI_TOO_LONG"></a><a id="ril_imssipcause_request_uri_too_long"></a><b>RIL_IMSSIPCAUSE_REQUEST_URI_TOO_LONG</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_UNSUPPORTED_MEDIA_TYPE"></a><a id="ril_imssipcause_unsupported_media_type"></a><b>RIL_IMSSIPCAUSE_UNSUPPORTED_MEDIA_TYPE</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_UNSUPPORTED_URI_SCHEME"></a><a id="ril_imssipcause_unsupported_uri_scheme"></a><b>RIL_IMSSIPCAUSE_UNSUPPORTED_URI_SCHEME</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_BAD_EXTENSION"></a><a id="ril_imssipcause_bad_extension"></a><b>RIL_IMSSIPCAUSE_BAD_EXTENSION</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_EXTENSION_REQUIRED"></a><a id="ril_imssipcause_extension_required"></a><b>RIL_IMSSIPCAUSE_EXTENSION_REQUIRED</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_INTERVAL_TOO_BRIEF"></a><a id="ril_imssipcause_interval_too_brief"></a><b>RIL_IMSSIPCAUSE_INTERVAL_TOO_BRIEF</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_TEMPORARILY_UNAVAILABLE"></a><a id="ril_imssipcause_temporarily_unavailable"></a><b>RIL_IMSSIPCAUSE_TEMPORARILY_UNAVAILABLE</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_CALL_OR_TRANSACTION_DOES_NOT_EXIST"></a><a id="ril_imssipcause_call_or_transaction_does_not_exist"></a><b>RIL_IMSSIPCAUSE_CALL_OR_TRANSACTION_DOES_NOT_EXIST</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_LOOP_DETECTED"></a><a id="ril_imssipcause_loop_detected"></a><b>RIL_IMSSIPCAUSE_LOOP_DETECTED</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_TOO_MANY_HOPS"></a><a id="ril_imssipcause_too_many_hops"></a><b>RIL_IMSSIPCAUSE_TOO_MANY_HOPS</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_ADDRESS_INCOMPLETE"></a><a id="ril_imssipcause_address_incomplete"></a><b>RIL_IMSSIPCAUSE_ADDRESS_INCOMPLETE</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_AMBIGUOUS"></a><a id="ril_imssipcause_ambiguous"></a><b>RIL_IMSSIPCAUSE_AMBIGUOUS</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_BUSY_HERE"></a><a id="ril_imssipcause_busy_here"></a><b>RIL_IMSSIPCAUSE_BUSY_HERE</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_REQUEST_TERMINATED"></a><a id="ril_imssipcause_request_terminated"></a><b>RIL_IMSSIPCAUSE_REQUEST_TERMINATED</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_NOT_ACCEPTABLE_HERE"></a><a id="ril_imssipcause_not_acceptable_here"></a><b>RIL_IMSSIPCAUSE_NOT_ACCEPTABLE_HERE</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_REQUEST_PENDING"></a><a id="ril_imssipcause_request_pending"></a><b>RIL_IMSSIPCAUSE_REQUEST_PENDING</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_UNDECIPHERABLE"></a><a id="ril_imssipcause_undecipherable"></a><b>RIL_IMSSIPCAUSE_UNDECIPHERABLE</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_SERVER_INTERNAL_ERROR"></a><a id="ril_imssipcause_server_internal_error"></a><b>RIL_IMSSIPCAUSE_SERVER_INTERNAL_ERROR</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_NOT_IMPLEMENTED"></a><a id="ril_imssipcause_not_implemented"></a><b>RIL_IMSSIPCAUSE_NOT_IMPLEMENTED</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_BAD_GATEWAY"></a><a id="ril_imssipcause_bad_gateway"></a><b>RIL_IMSSIPCAUSE_BAD_GATEWAY</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_SERVICE_UNAVAILABLE"></a><a id="ril_imssipcause_service_unavailable"></a><b>RIL_IMSSIPCAUSE_SERVICE_UNAVAILABLE</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_SERVER_TIMEOUT"></a><a id="ril_imssipcause_server_timeout"></a><b>RIL_IMSSIPCAUSE_SERVER_TIMEOUT</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_VERSION_NOT_SUPPORTED"></a><a id="ril_imssipcause_version_not_supported"></a><b>RIL_IMSSIPCAUSE_VERSION_NOT_SUPPORTED</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_MESSAGE_TOO_LARGE"></a><a id="ril_imssipcause_message_too_large"></a><b>RIL_IMSSIPCAUSE_MESSAGE_TOO_LARGE</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_BUSY_EVERYWHERE"></a><a id="ril_imssipcause_busy_everywhere"></a><b>RIL_IMSSIPCAUSE_BUSY_EVERYWHERE</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_DECLINE"></a><a id="ril_imssipcause_decline"></a><b>RIL_IMSSIPCAUSE_DECLINE</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_DOES_NOT_EXIST_ANYWHERE"></a><a id="ril_imssipcause_does_not_exist_anywhere"></a><b>RIL_IMSSIPCAUSE_DOES_NOT_EXIST_ANYWHERE</b>

<dd></dd>

### -field <a id="RIL_IMSSIPCAUSE_NOT_ACCEPTABLE_PARTIAL"></a><a id="ril_imssipcause_not_acceptable_partial"></a><b>RIL_IMSSIPCAUSE_NOT_ACCEPTABLE_PARTIAL</b>

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>