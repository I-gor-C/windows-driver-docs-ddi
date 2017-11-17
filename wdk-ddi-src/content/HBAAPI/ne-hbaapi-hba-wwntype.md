---
UID: NE.hbaapi.HBA_wwntype
title: HBA_wwntype
author: windows-driver-content
description: The HBA_wwntype enumerator indicates whether a worldwide name specifies a port or a node (machine).
old-location: storage\hba_wwntype.htm
ms.assetid: 30ce30db-e030-43c3-bf8d-2f6ef86087ab
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: Storage
req.header: hbaapi.h
req.include-header: Hbaapi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HBA_WWNTYPE
req.alt-loc: hbaapi.h
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
ms.keywords: GPIO_WRITE_PINS_PARAMETERS, GPIO_WRITE_PINS_PARAMETERS, *PGPIO_WRITE_PINS_PARAMETERS
req.iface: 
---

# HBA_wwntype enumeration



## -description
<p>The HBA_wwntype enumerator indicates whether a worldwide name specifies a port or a node (machine).</p>


## -syntax

````
typedef enum HBA_wwntype { 
  NODE_WWN  = 0,
  PORT_WWN  = 1
} HBA_WWNTYPE;
````


## -enum-fields
<dl>

### -field <a id="NODE_WWN"></a><a id="node_wwn"></a><b>NODE_WWN</b>

<dd>
<p>Indicates that the world wide name specifies a node..</p>
</dd>

### -field <a id="PORT_WWN"></a><a id="port_wwn"></a><b>PORT_WWN</b>

<dd>
<p>Indicates that the world wide name specifies a port. </p>
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
<dt>Hbaapi.h (include Hbaapi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557216">HBA_SendRNID</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20HBA_wwntype enumeration%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
