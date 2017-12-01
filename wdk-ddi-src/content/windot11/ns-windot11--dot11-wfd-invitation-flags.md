---
UID: NS.windot11._DOT11_WFD_INVITATION_FLAGS
title: DOT11_WFD_INVITATION_FLAGS
author: windows-driver-content
description: The DOT11_WFD_INVITATION_FLAGS structure represents the Invitation Attributes used during the Invitation procedure.
old-location: netvista\dot11_wfd_invitation_flags.htm
old-project: netvista
ms.assetid: 9743FF37-0E8A-499F-AADB-9CD7BDC381E0
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: DOT11_WFD_INVITATION_FLAGS,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: windot11.h
req.include-header: Windot11.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with   Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_WFD_INVITATION_FLAGS
req.alt-loc: Windot11.h
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

# DOT11_WFD_INVITATION_FLAGS structure



## -description

## -syntax

````
typedef struct _DOT11_WFD_INVITATION_FLAGS {
  UCHAR InvitationType:1;
  UCHAR Reserved:7;
} DOT11_WFD_INVITATION_FLAGS, *PDOT11_WFD_INVITATION_FLAGS;
````


## -struct-fields
<dl>

### -field <b>InvitationType:1</b>

<dd>
<p>The type of group invitation. The invitation types have the following meanings.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="Join"></a><a id="join"></a><a id="JOIN"></a><dl>

### -field <b>Join</b>


### -field 0

</dl>
</td>
<td width="60%">
<p>An invitiation to join an active group.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="Reinvoke"></a><a id="reinvoke"></a><a id="REINVOKE"></a><dl>

### -field <b>Reinvoke</b>


### -field 1

</dl>
</td>
<td width="60%">
<p>The invitation is reinvoked.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Reserved:7</b>

<dd>
<p>Reserved.</p>
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
<p>Supported starting with   Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Windot11.h (include Windot11.h)</dt>
</dl>
</td>
</tr>
</table>