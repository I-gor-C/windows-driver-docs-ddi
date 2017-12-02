---
UID: NE.ntddrilapitypes.RILUNSOLICITEDSSINFONOTIFICATIONCODE
title: RILUNSOLICITEDSSINFONOTIFICATIONCODE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilunsolicitedssinfonotificationcode.htm
old-project: netvista
ms.assetid: 03dd4659-29fc-4426-8d30-2bbc0b71f899
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
req.alt-api: RILUNSOLICITEDSSINFONOTIFICATIONCODE
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

# RILUNSOLICITEDSSINFONOTIFICATIONCODE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILUNSOLICITEDSSINFONOTIFICATIONCODE { 
  RIL_UNSSSCODE_CUGCALL,
  RIL_UNSSSCODE_CALLPUTONHOLD,
  RIL_UNSSSCODE_CALLRETRIEVED,
  RIL_UNSSSCODE_ENTEREDMULTIPARTY,
  RIL_UNSSSCODE_HELDCALLRELEASED,
  RIL_UNSSSCODE_FORWARDCHECKSS,
  RIL_UNSSSCODE_ALERTINGEXPLICITCALLXFER,
  RIL_UNSSSCODE_CONNECTEDEXPLICITCALLXFER,
  RIL_UNSSSCODE_DEFLECTEDCALL,
  RIL_UNSSSCODE_ADDITIONALINCOMINGCF,
  RIL_UNSSSCODE_UNCONDITIONALCFACTIVE,
  RIL_UNSSSCODE_SOMECONDITIONALCFACTIVE,
  RIL_UNSSSCODE_CALLWASFORWARDED,
  RIL_UNSSSCODE_CALLISWAITING,
  RIL_UNSSSCODE_OUTGOINGCALLSBARRED,
  RIL_UNSSSCODE_INCOMINGCALLSBARRED,
  RIL_UNSSSCODE_CLIRSUPPRESSREJECT,
  RIL_UNSSSCODE_MAX
} RILUNSOLICITEDSSINFONOTIFICATIONCODE;
````


## -enum-fields
<dl>

### -field RIL_UNSSSCODE_CUGCALL

<dd></dd>

### -field RIL_UNSSSCODE_CALLPUTONHOLD

<dd></dd>

### -field RIL_UNSSSCODE_CALLRETRIEVED

<dd></dd>

### -field RIL_UNSSSCODE_ENTEREDMULTIPARTY

<dd></dd>

### -field RIL_UNSSSCODE_HELDCALLRELEASED

<dd></dd>

### -field RIL_UNSSSCODE_FORWARDCHECKSS

<dd></dd>

### -field RIL_UNSSSCODE_ALERTINGEXPLICITCALLXFER

<dd></dd>

### -field RIL_UNSSSCODE_CONNECTEDEXPLICITCALLXFER

<dd></dd>

### -field RIL_UNSSSCODE_DEFLECTEDCALL

<dd></dd>

### -field RIL_UNSSSCODE_ADDITIONALINCOMINGCF

<dd></dd>

### -field RIL_UNSSSCODE_UNCONDITIONALCFACTIVE

<dd></dd>

### -field RIL_UNSSSCODE_SOMECONDITIONALCFACTIVE

<dd></dd>

### -field RIL_UNSSSCODE_CALLWASFORWARDED

<dd></dd>

### -field RIL_UNSSSCODE_CALLISWAITING

<dd></dd>

### -field RIL_UNSSSCODE_OUTGOINGCALLSBARRED

<dd></dd>

### -field RIL_UNSSSCODE_INCOMINGCALLSBARRED

<dd></dd>

### -field RIL_UNSSSCODE_CLIRSUPPRESSREJECT

<dd></dd>

### -field RIL_UNSSSCODE_MAX

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