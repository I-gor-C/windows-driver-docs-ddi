---
UID: NE.d3dkmddi._DXGK_PROTECTED_SESSION_STATUS
title: DXGK_PROTECTED_SESSION_STATUS
author: windows-driver-content
description: Used to indicate the status of the current session.
old-location: display\dxgk_protected_session_status.htm
ms.assetid: B6FCA052-FFAE-4F7D-8BDE-CDB84772B5E5
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_PROTECTED_SESSION_STATUS
req.alt-loc: d3dkmddi.h
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
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
req.iface: 
---

# DXGK_PROTECTED_SESSION_STATUS enumeration



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>Used to indicate the status of the current session.</p>


## -syntax

````
typedef enum _DXGK_PROTECTED_SESSION_STATUS { 
  DXGK_PROTECTED_SESSION_STATUS_OK       = 0,
  DXGK_PROTECTED_SESSION_STATUS_INVALID  = 1
} DXGK_PROTECTED_SESSION_STATUS;
````


## -enum-fields
<dl>

### -field <a id="DXGK_PROTECTED_SESSION_STATUS_OK"></a><a id="dxgk_protected_session_status_ok"></a><b>DXGK_PROTECTED_SESSION_STATUS_OK</b>

<dd>
<p>Indicates that the status is okay.</p>
</dd>

### -field <a id="DXGK_PROTECTED_SESSION_STATUS_INVALID"></a><a id="dxgk_protected_session_status_invalid"></a><b>DXGK_PROTECTED_SESSION_STATUS_INVALID</b>

<dd>
<p>Indicates that the status is invalid.</p>
</dd>
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
<dt>D3dkmddi.h</dt>
</dl>
</td>
</tr>
</table>