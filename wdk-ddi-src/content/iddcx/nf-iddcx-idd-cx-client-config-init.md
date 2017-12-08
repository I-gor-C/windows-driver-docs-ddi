---
UID: NF.iddcx.IDD_CX_CLIENT_CONFIG_INIT
title: IDD_CX_CLIENT_CONFIG_INIT
author: windows-driver-content
description: Initializes the IDD_CX_CLIENT_CONFIG structure.
old-location: display\idd_cx_client_config_init.htm
old-project: display
ms.assetid: 0b2cf0d6-1d69-4917-9e97-f8f2563e6d3c
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IDD_CX_CLIENT_CONFIG_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: iddcx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDD_CX_CLIENT_CONFIG_INIT
req.alt-loc: iddcx.h
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

# IDD_CX_CLIENT_CONFIG_INIT function



## -description
<p>
                        Initializes the IDD_CX_CLIENT_CONFIG structure.
                </p>


## -syntax

````
VOID IDD_CX_CLIENT_CONFIG_INIT(
  _Out_ IDD_CX_CLIENT_CONFIG *Config
);
````


## -parameters
<dl>

### -param Config [out]

<dd>
<p>A pointer to the driver-allocated IDD_CX_CLIENT_CONFIG structure.</p>
</dd>
</dl>

## -returns
<p>This method does not return a value.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Iddcx.h</dt>
</dl>
</td>
</tr>
</table>