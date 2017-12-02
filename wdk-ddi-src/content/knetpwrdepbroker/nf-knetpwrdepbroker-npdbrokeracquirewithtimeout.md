---
UID: NF.knetpwrdepbroker.NpdBrokerAcquireWithTimeout
title: NpdBrokerAcquireWithTimeout
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\npdbrokeracquirewithtimeout.htm
old-project: netvista
ms.assetid: D2067A72-0FF5-4D77-A1F6-0A6984A1735A
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NpdBrokerAcquireWithTimeout
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: knetpwrdepbroker.h
req.include-header: KNetPwrDepBroker.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NpdBrokerAcquireWithTimeout
req.alt-loc: KNetPwrDepBroker.h
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
req.iface: 
---

# NpdBrokerAcquireWithTimeout function



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
NTSTATUS NpdBrokerAcquireWithTimeout(
  _In_ HANDLE hBroker,
  _In_ LONG   lTimeoutMS
);
````


## -parameters
<dl>

### -param hBroker [in]

<dd>
<p>Reserved.</p>
</dd>

### -param lTimeoutMS [in]

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
<p>Windows 10, version 1709</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>KNetPwrDepBroker.h (include KNetPwrDepBroker.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>