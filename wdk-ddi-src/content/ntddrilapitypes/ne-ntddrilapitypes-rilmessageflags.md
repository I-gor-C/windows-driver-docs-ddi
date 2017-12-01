---
UID: NE.ntddrilapitypes.RILMESSAGEFLAGS
title: RILMESSAGEFLAGS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmessageflags.htm
old-project: netvista
ms.assetid: 82f36886-20bf-4981-b0f0-3871a87b6c4e
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
req.alt-api: RILMESSAGEFLAGS
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

# RILMESSAGEFLAGS enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILMESSAGEFLAGS { 
  RIL_MSGFLAG_MORETOSEND,
  RIL_MSGFLAG_REPLYPATH,
  RIL_MSGFLAG_HEADER,
  RIL_MSGFLAG_REJECTDUPS,
  RIL_MSGFLAG_STATUSREPORTRETURNED,
  RIL_MSGFLAG_STATUSREPORTREQUESTED,
  RIL_MSGFLAG_CAUSEDBYCOMMAND,
  RIL_MSGFLAG_ALL
} RILMESSAGEFLAGS;
````


## -enum-fields
<dl>

### -field <a id="RIL_MSGFLAG_MORETOSEND"></a><a id="ril_msgflag_moretosend"></a><b>RIL_MSGFLAG_MORETOSEND</b>

<dd></dd>

### -field <a id="RIL_MSGFLAG_REPLYPATH"></a><a id="ril_msgflag_replypath"></a><b>RIL_MSGFLAG_REPLYPATH</b>

<dd></dd>

### -field <a id="RIL_MSGFLAG_HEADER"></a><a id="ril_msgflag_header"></a><b>RIL_MSGFLAG_HEADER</b>

<dd></dd>

### -field <a id="RIL_MSGFLAG_REJECTDUPS"></a><a id="ril_msgflag_rejectdups"></a><b>RIL_MSGFLAG_REJECTDUPS</b>

<dd></dd>

### -field <a id="RIL_MSGFLAG_STATUSREPORTRETURNED"></a><a id="ril_msgflag_statusreportreturned"></a><b>RIL_MSGFLAG_STATUSREPORTRETURNED</b>

<dd></dd>

### -field <a id="RIL_MSGFLAG_STATUSREPORTREQUESTED"></a><a id="ril_msgflag_statusreportrequested"></a><b>RIL_MSGFLAG_STATUSREPORTREQUESTED</b>

<dd></dd>

### -field <a id="RIL_MSGFLAG_CAUSEDBYCOMMAND"></a><a id="ril_msgflag_causedbycommand"></a><b>RIL_MSGFLAG_CAUSEDBYCOMMAND</b>

<dd></dd>

### -field <a id="RIL_MSGFLAG_ALL"></a><a id="ril_msgflag_all"></a><b>RIL_MSGFLAG_ALL</b>

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