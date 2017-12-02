---
UID: NF.ucmmanager.UCM_CONNECTOR_TYPEC_CONFIG_INIT
title: UCM_CONNECTOR_TYPEC_CONFIG_INIT
author: windows-driver-content
description: Initializes the UCM_CONNECTOR_TYPEC_CONFIG structure.
old-location: buses\ucm_connector_type_c_config_init.htm
old-project: usbref
ms.assetid: 10E155C2-907D-4D0E-87E9-A6B32E99D133
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UCM_CONNECTOR_TYPEC_CONFIG_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ucmmanager.h
req.include-header: Ucmcx.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.15
req.umdf-ver: 2.15
req.alt-api: UCM_CONNECTOR_TYPE_C_CONFIG_INIT
req.alt-loc: Ucmmanager.h
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

# UCM_CONNECTOR_TYPEC_CONFIG_INIT function



## -description
<p>Initializes the <a href="..\ucmmanager\ns-ucmmanager--ucm-connector-typec-config.md">UCM_CONNECTOR_TYPEC_CONFIG</a> structure.</p>


## -syntax

````
__inline
void UCM_CONNECTOR_TYPE_C_CONFIG_INIT(
  _Out_ PUCM_CONNECTOR_TYPEC_CONFIG Config,
  _In_  ULONG                       SupportedOperatingModes,
  _In_  ULONG                       SupportedPowerSourcingCapabilities
);
````


## -parameters
<dl>

### -param Config [out]

<dd>
<p>Pointer to a caller-allocated <a href="..\ucmmanager\ns-ucmmanager--ucm-connector-typec-config.md">UCM_CONNECTOR_TYPEC_CONFIG</a> structure to initialize.</p>
</dd>

### -param SupportedOperatingModes [in]

<dd>
<p>Indicates the operating mode of the connector. This value is a bitwise OR of <a href="..\ucmtypes\ne-ucmtypes--ucm-typec-operating-mode.md">UCM_TYPEC_OPERATING_MODE</a>-typed flags.</p>
</dd>

### -param SupportedPowerSourcingCapabilities [in]

<dd>
<p>Indicates the power source capabilities of the connector. This value is a bitwise OR of <a href="..\ucmtypes\ne-ucmtypes--ucm-typec-current.md">UCM_TYPEC_CURRENT</a>-typed flags.</p>
</dd>
</dl>

## -returns
<p>This function does not return a value.</p>

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
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.15</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.15</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ucmmanager.h (include Ucmcx.h)</dt>
</dl>
</td>
</tr>
</table>