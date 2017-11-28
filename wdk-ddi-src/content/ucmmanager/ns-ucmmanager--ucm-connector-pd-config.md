---
UID: NS.ucmmanager._UCM_CONNECTOR_PD_CONFIG
title: UCM_CONNECTOR_PD_CONFIG
author: windows-driver-content
description: Describes the Power Delivery 2.0 capabilities of the connector.
old-location: buses\ucm_connector_pd_config.htm
old-project: usbref
ms.assetid: 9DE2AF2D-D6B5-4FC4-8871-246F3661980F
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UCM_CONNECTOR_PD_CONFIG, UCM_CONNECTOR_PD_CONFIG, *PUCM_CONNECTOR_PD_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ucmmanager.h
req.include-header: Ucmcx.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.15
req.umdf-ver: 2.15
req.alt-api: UCM_CONNECTOR_PD_CONFIG
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

# UCM_CONNECTOR_PD_CONFIG structure



## -description
<p>Describes the Power Delivery 2.0 capabilities of the connector.</p>


## -syntax

````
typedef struct _UCM_CONNECTOR_PD_CONFIG {
  ULONG                            Size;
  BOOLEAN                          IsSupported;
  ULONG                            SupportedPowerRoles;
  PFN_UCM_CONNECTOR_SET_POWER_ROLE EvtSetPowerRole;
} UCM_CONNECTOR_PD_CONFIG, *PUCM_CONNECTOR_PD_CONFIG;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Size of the <b>UCM_CONNECTOR_PD_CONFIG</b> structure. </p>
</dd>

### -field <b>IsSupported</b>

<dd>
<p>If TRUE, a PD role is supported. (Default).</p>
<p>If FALSE, a PD role is not supported.</p>
</dd>

### -field <b>SupportedPowerRoles</b>

<dd>
<p>Indicates the operating mode of the connector. This value is a bitwise OR of <a href="https://msdn.microsoft.com/library/windows/hardware/mt187944">UCM_POWER_ROLE</a>-typed flags.</p>
</dd>

### -field <b>EvtSetPowerRole</b>

<dd>
<p>A pointer to the Policy Manager's implementation of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187819">EVT_UCM_CONNECTOR_SET_POWER_ROLE</a> event callback.</p>
</dd>
</dl>

## -remarks
<p>Initialize this structure by calling <a href="https://msdn.microsoft.com/library/windows/hardware/mt187925">UCM_CONNECTOR_PD_CONFIG_INIT</a>. An initialized <a href="https://msdn.microsoft.com/library/windows/hardware/mt187930">UCM_CONNECTOR_TYPEC_CONFIG</a> structure is set to the <b>PdConfig</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187922">UCM_CONNECTOR_CONFIG</a> structure, which is an input parameter value to <a href="https://msdn.microsoft.com/library/windows/hardware/mt187909">UcmConnectorCreate</a> that is called by Policy Manager to create a connector object.</p>

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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt187909">UcmConnectorCreate</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UCM_CONNECTOR_PD_CONFIG structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
