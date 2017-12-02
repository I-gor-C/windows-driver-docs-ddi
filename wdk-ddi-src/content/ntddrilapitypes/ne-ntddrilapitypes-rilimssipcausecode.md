---
UID: NE.ntddrilapitypes.RILIMSSIPCAUSECODE
title: RILIMSSIPCAUSECODE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilimssipcausecode.htm
old-project: netvista
ms.assetid: b76ea0fb-8139-4272-b9a0-2daa5b660c7d
ms.author: windowsdriverdev
ms.date: 11/30/2017
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

### -field RIL_IMSSIPCAUSE_UNAUTHORIZED

<dd></dd>

### -field RIL_IMSSIPCAUSE_PAYMENT_REQUIRED

<dd></dd>

### -field RIL_IMSSIPCAUSE_FORBIDDEN

<dd></dd>

### -field RIL_IMSSIPCAUSE_NOT_FOUND

<dd></dd>

### -field RIL_IMSSIPCAUSE_METHOD_NOT_ALLOWED

<dd></dd>

### -field RIL_IMSSIPCAUSE_NOT_ACCEPTABLE

<dd></dd>

### -field RIL_IMSSIPCAUSE_PROXY_AUTHENTICATION_REQUIRED

<dd></dd>

### -field RIL_IMSSIPCAUSE_REQUEST_TIMEOUT

<dd></dd>

### -field RIL_IMSSIPCAUSE_GONE

<dd></dd>

### -field RIL_IMSSIPCAUSE_REQUEST_ENTITY_TOO_LARGE

<dd></dd>

### -field RIL_IMSSIPCAUSE_REQUEST_URI_TOO_LONG

<dd></dd>

### -field RIL_IMSSIPCAUSE_UNSUPPORTED_MEDIA_TYPE

<dd></dd>

### -field RIL_IMSSIPCAUSE_UNSUPPORTED_URI_SCHEME

<dd></dd>

### -field RIL_IMSSIPCAUSE_BAD_EXTENSION

<dd></dd>

### -field RIL_IMSSIPCAUSE_EXTENSION_REQUIRED

<dd></dd>

### -field RIL_IMSSIPCAUSE_INTERVAL_TOO_BRIEF

<dd></dd>

### -field RIL_IMSSIPCAUSE_TEMPORARILY_UNAVAILABLE

<dd></dd>

### -field RIL_IMSSIPCAUSE_CALL_OR_TRANSACTION_DOES_NOT_EXIST

<dd></dd>

### -field RIL_IMSSIPCAUSE_LOOP_DETECTED

<dd></dd>

### -field RIL_IMSSIPCAUSE_TOO_MANY_HOPS

<dd></dd>

### -field RIL_IMSSIPCAUSE_ADDRESS_INCOMPLETE

<dd></dd>

### -field RIL_IMSSIPCAUSE_AMBIGUOUS

<dd></dd>

### -field RIL_IMSSIPCAUSE_BUSY_HERE

<dd></dd>

### -field RIL_IMSSIPCAUSE_REQUEST_TERMINATED

<dd></dd>

### -field RIL_IMSSIPCAUSE_NOT_ACCEPTABLE_HERE

<dd></dd>

### -field RIL_IMSSIPCAUSE_REQUEST_PENDING

<dd></dd>

### -field RIL_IMSSIPCAUSE_UNDECIPHERABLE

<dd></dd>

### -field RIL_IMSSIPCAUSE_SERVER_INTERNAL_ERROR

<dd></dd>

### -field RIL_IMSSIPCAUSE_NOT_IMPLEMENTED

<dd></dd>

### -field RIL_IMSSIPCAUSE_BAD_GATEWAY

<dd></dd>

### -field RIL_IMSSIPCAUSE_SERVICE_UNAVAILABLE

<dd></dd>

### -field RIL_IMSSIPCAUSE_SERVER_TIMEOUT

<dd></dd>

### -field RIL_IMSSIPCAUSE_VERSION_NOT_SUPPORTED

<dd></dd>

### -field RIL_IMSSIPCAUSE_MESSAGE_TOO_LARGE

<dd></dd>

### -field RIL_IMSSIPCAUSE_BUSY_EVERYWHERE

<dd></dd>

### -field RIL_IMSSIPCAUSE_DECLINE

<dd></dd>

### -field RIL_IMSSIPCAUSE_DOES_NOT_EXIST_ANYWHERE

<dd></dd>

### -field RIL_IMSSIPCAUSE_NOT_ACCEPTABLE_PARTIAL

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