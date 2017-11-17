---
UID: NS.ucmmanager._UCM_CONNECTOR_TYPEC_CONFIG
title: UCM_CONNECTOR_TYPEC_CONFIG
author: windows-driver-content
description: Describes the configuration options for a Type-C connector.
old-location: buses\ucm_connector_type_c_config.htm
ms.assetid: F3C17CD8-F423-46E7-891F-E428235CEF3D
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: usbref
req.header: ucmmanager.h
req.include-header: Ucmcx.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.15
req.umdf-ver: 2.15
req.alt-api: UCM_CONNECTOR_TYPEC_CONFIG
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
ms.keywords: UCM_CONNECTOR_TYPEC_CONFIG, UCM_CONNECTOR_TYPEC_CONFIG, *PUCM_CONNECTOR_TYPEC_CONFIG
req.iface: 
req.product: Windows 10 or later.
---

# UCM_CONNECTOR_TYPEC_CONFIG structure



## -description
<p>Describes the configuration options for a Type-C connector. </p>


## -syntax

````
typedef struct _UCM_CONNECTOR_TYPEC_CONFIG {
  ULONG                           Size;
  BOOLEAN                         IsSupported;
  ULONG                           SupportedOperatingModes;
  ULONG                           SupportedPowerSourcingCapabilities;
  BOOLEAN                         AudioAccessoryCapable;
  PFN_UCM_CONNECTOR_SET_DATA_ROLE EvtSetDataRole;
} UCM_CONNECTOR_TYPEC_CONFIG, *PUCM_CONNECTOR_TYPEC_CONFIG;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Size of the <b>UCM_CONNECTOR_TYPEC_CONFIG</b> structure. </p>
</dd>

### -field <b>IsSupported</b>

<dd>
<p>TRUE indicates a Type-C connector. FALSE, otherwise.  is supported. </p>
</dd>

### -field <b>SupportedOperatingModes</b>

<dd>
<p>Indicates the supported operating mode of the connector. This value is a bitwise OR of <a href="https://msdn.microsoft.com/library/windows/hardware/mt187946">UCM_TYPEC_OPERATING_MODE</a>-typed flags.</p>
</dd>

### -field <b>SupportedPowerSourcingCapabilities</b>

<dd>
<p>Indicates the supported power source capabilities of the connector. This value is a bitwise OR of <a href="https://msdn.microsoft.com/library/windows/hardware/mt187945">UCM_TYPEC_CURRENT</a>-typed flags.</p>
</dd>

### -field <b>AudioAccessoryCapable</b>

<dd>
<p>Indicates whether the connector is capable of detecting a USB Type-C analog input as 3.5 mm audio jack.</p>
</dd>

### -field <b>EvtSetDataRole</b>

<dd>
<p>A pointer to the client driver's implementation of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187818">EVT_UCM_CONNECTOR_SET_DATA_ROLE</a> callback function.</p>
</dd>
</dl>

## -remarks
<p>Initialize this structure by calling <a href="https://msdn.microsoft.com/library/windows/hardware/mt187931">UCM_CONNECTOR_TYPEC_CONFIG_INIT</a>. An initialized <b>UCM_CONNECTOR_TYPEC_CONFIG</b> structure is an input parameter value to <a href="https://msdn.microsoft.com/library/windows/hardware/mt187909">UcmConnectorCreate</a> that is used by Policy Manager to create a connector object.</p>

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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UCM_CONNECTOR_TYPEC_CONFIG structure%20 RELEASE:%20(11/3/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
