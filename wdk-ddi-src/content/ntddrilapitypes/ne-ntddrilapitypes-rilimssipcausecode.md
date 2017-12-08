---
UID: NE.ntddrilapitypes.RILIMSSIPCAUSECODE
title: RILIMSSIPCAUSECODE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilimssipcausecode.htm
old-project: netvista
ms.assetid: b76ea0fb-8139-4272-b9a0-2daa5b660c7d
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: RILIMSSIPCAUSECODE, RILIMSSIPCAUSECODE
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
---

# RILIMSSIPCAUSECODE enumeration



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.


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

### -field RIL_IMSSIPCAUSE_UNAUTHORIZED


### -field RIL_IMSSIPCAUSE_PAYMENT_REQUIRED


### -field RIL_IMSSIPCAUSE_FORBIDDEN


### -field RIL_IMSSIPCAUSE_NOT_FOUND


### -field RIL_IMSSIPCAUSE_METHOD_NOT_ALLOWED


### -field RIL_IMSSIPCAUSE_NOT_ACCEPTABLE


### -field RIL_IMSSIPCAUSE_PROXY_AUTHENTICATION_REQUIRED


### -field RIL_IMSSIPCAUSE_REQUEST_TIMEOUT


### -field RIL_IMSSIPCAUSE_GONE


### -field RIL_IMSSIPCAUSE_REQUEST_ENTITY_TOO_LARGE


### -field RIL_IMSSIPCAUSE_REQUEST_URI_TOO_LONG


### -field RIL_IMSSIPCAUSE_UNSUPPORTED_MEDIA_TYPE


### -field RIL_IMSSIPCAUSE_UNSUPPORTED_URI_SCHEME


### -field RIL_IMSSIPCAUSE_BAD_EXTENSION


### -field RIL_IMSSIPCAUSE_EXTENSION_REQUIRED


### -field RIL_IMSSIPCAUSE_INTERVAL_TOO_BRIEF


### -field RIL_IMSSIPCAUSE_TEMPORARILY_UNAVAILABLE


### -field RIL_IMSSIPCAUSE_CALL_OR_TRANSACTION_DOES_NOT_EXIST


### -field RIL_IMSSIPCAUSE_LOOP_DETECTED


### -field RIL_IMSSIPCAUSE_TOO_MANY_HOPS


### -field RIL_IMSSIPCAUSE_ADDRESS_INCOMPLETE


### -field RIL_IMSSIPCAUSE_AMBIGUOUS


### -field RIL_IMSSIPCAUSE_BUSY_HERE


### -field RIL_IMSSIPCAUSE_REQUEST_TERMINATED


### -field RIL_IMSSIPCAUSE_NOT_ACCEPTABLE_HERE


### -field RIL_IMSSIPCAUSE_REQUEST_PENDING


### -field RIL_IMSSIPCAUSE_UNDECIPHERABLE


### -field RIL_IMSSIPCAUSE_SERVER_INTERNAL_ERROR


### -field RIL_IMSSIPCAUSE_NOT_IMPLEMENTED


### -field RIL_IMSSIPCAUSE_BAD_GATEWAY


### -field RIL_IMSSIPCAUSE_SERVICE_UNAVAILABLE


### -field RIL_IMSSIPCAUSE_SERVER_TIMEOUT


### -field RIL_IMSSIPCAUSE_VERSION_NOT_SUPPORTED


### -field RIL_IMSSIPCAUSE_MESSAGE_TOO_LARGE


### -field RIL_IMSSIPCAUSE_BUSY_EVERYWHERE


### -field RIL_IMSSIPCAUSE_DECLINE


### -field RIL_IMSSIPCAUSE_DOES_NOT_EXIST_ANYWHERE


### -field RIL_IMSSIPCAUSE_NOT_ACCEPTABLE_PARTIAL


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ntddrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>