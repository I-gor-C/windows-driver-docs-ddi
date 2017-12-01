---
UID: NS.windot11._DOT11_WFD_DEVICE_CAPABILITY_CONFIG
title: DOT11_WFD_DEVICE_CAPABILITY_CONFIG
author: windows-driver-content
description: The device capability configuration structure sent with an OID_DOT11_WFD_DEVICE_CAPABILITY request.
old-location: netvista\_dot11_wfd_device_capability_config.htm
old-project: netvista
ms.assetid: 918307D4-0952-4FF0-8591-522C7E92194A
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: DOT11_WFD_DEVICE_CAPABILITY_CONFIG,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: windot11.h
req.include-header: Windot11.h
req.target-type: Windows
req.target-min-winverclnt: Versions: Supported in Windows 8
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_WFD_DEVICE_CAPABILITY_CONFIG
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

# DOT11_WFD_DEVICE_CAPABILITY_CONFIG structure



## -description

## -syntax

````
typedef struct _DOT11_WFD_DEVICE_CAPABILITY_CONFIG {
  NDIS_OBJECT_HEADER Header;
  BOOLEAN            bServiceDiscoveryEnabled;
  BOOLEAN            bClientDiscoverabilityEnabled;
  BOOLEAN            bConcurrentOperationSupported;
  BOOLEAN            bInfrastructureManagementEnabled;
  BOOLEAN            bDeviceLimitReached;
  BOOLEAN            bInvitationProcedureEnabled;
  ULONG              WPSVersionsEnabled;
} DOT11_WFD_DEVICE_CAPABILITY_CONFIG, *PDOT11_WFD_DEVICE_CAPABILITY_CONFIG;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>Specifies the type, revision and size of the <b>DOT11_WFD_DEVICE_CAPABILITY_CONFIG</b> structure. The required settings for the members of <b>Header</b> are the following:</p>
<table>
<tr>
<th>Member</th>
<th>Setting</th>
</tr>
<tr>
<td><b>Type</b></td>
<td>NDIS_OBJECT_TYPE_DEFAULT</td>
</tr>
<tr>
<td><b>Revision</b></td>
<td>DOT11_WFD_DEVICE_CAPABILITY_CONFIG_REVISION_1</td>
</tr>
<tr>
<td><b>Size</b></td>
<td>DOT11_SIZEOF_WFD_DEVICE_CAPABILITY_CONFIG_1</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>bServiceDiscoveryEnabled</b>

<dd>
<p>When set to TRUE, the miniport must enable Service Discovery support. The miniport must also set the Service Discovery bit in the P2P Device Capability Bitmap. If <b>bServiceDiscoveryEnabled</b> is FALSE, Service Discovery support must be disabled and the miniport must ignore all Service Discovery packets it receives.</p>
<p> The system will set this to TRUE only if the miniport also sets TRUE for the <b>bServiceDiscoverySupported</b> member of <a href="..\windot11\ns-windot11--dot11-wfd-attributes.md">DOT11_WFD_ATTRIBUTES</a>. The default value for this member is FALSE.</p>
</dd>

### -field <b>bClientDiscoverabilityEnabled</b>

<dd>
<p>When set to TRUE, the miniport must enable Client Discoverability support. The miniport must also set the Client Discoverability bit in the P2P Device Capability Bitmap. If <b>bClientDiscoveryEnabled</b> is FALSE,  Client Discoverability support must be disabled and the miniport must ignore all Client Discovery packets it receives.</p>
<p>The system will set this to TRUE only if the miniport also sets TRUE for the <b>bClientDiscoverabilitySupported</b> member of <a href="..\windot11\ns-windot11--dot11-wfd-attributes.md">DOT11_WFD_ATTRIBUTES</a>. The default value for this member is FALSE.</p>
</dd>

### -field <b>bConcurrentOperationSupported</b>

<dd>
<p>When set to TRUE, the miniport must set the Concurrent Operation bit in the P2P Device Capability Bitmask. Otherwise, the Concurrent Operation bit must be cleared. The default value for this member is TRUE.</p>
</dd>

### -field <b>bInfrastructureManagementEnabled</b>

<dd>
<p>When set to TRUE, the miniport must enable P2P Managed Device support. The miniport must also set the P2P Infrastructure Managed bit in the P2P Device Capability Bitmap. Otherwise, the P2P Managed Device support must be disabled.</p>
<p>The system will set this member to TRUE only if the miniport also sets TRUE for the  <b>bInfrastructureManagementSupported</b> member of <a href="..\windot11\ns-windot11--dot11-wfd-attributes.md">DOT11_WFD_ATTRIBUTES</a>. The default value for this member is FALSE</p>
</dd>

### -field <b>bDeviceLimitReached</b>

<dd>
<p>When set to TRUE, the miniport must set the Device Limit bit of the P2P Device Capability Bitmask. Otherwise, this bit must be cleared. The default value for this member is FALSE.</p>
</dd>

### -field <b>bInvitationProcedureEnabled</b>

<dd>
<p>When set to TRUE, the miniport must set the P2P Invitation Procedure bit of the P2P Device Capability Bitmask. Otherwise, this bit must be cleared and the miniport must ignore all Invitation request/response packets it receives. The default value for this member is TRUE.</p>
</dd>

### -field <b>WPSVersionsEnabled</b>

<dd>
<p>The versions of WPS enabled for the Wi-Fi Direct Device</p>
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
<p>Versions: Supported in Windows 8</p>
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