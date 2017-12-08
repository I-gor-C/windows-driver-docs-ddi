---
UID: NS.dot11wdi._NDIS_WDI_INIT_PARAMETERS
title: NDIS_WDI_INIT_PARAMETERS
author: windows-driver-content
description: The NDIS_WDI_INIT_PARAMETERS structure specifies the WDI functions provided by the operating system and called by the IHV WDI driver.
old-location: netvista\ndis_wdi_init_parameters.htm
old-project: netvista
ms.assetid: 871D266C-55DF-4113-9714-92AB129303E5
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NDIS_WDI_INIT_PARAMETERS, NDIS_WDI_INIT_PARAMETERS, *PNDIS_WDI_INIT_PARAMETERS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dot11wdi.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_WDI_INIT_PARAMETERS
req.alt-loc: dot11wdi.h
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

# NDIS_WDI_INIT_PARAMETERS structure



## -description
<p>The NDIS_WDI_INIT_PARAMETERS structure specifies the WDI functions provided by the operating system and called by the IHV WDI driver.</p>


## -syntax

````
typedef struct _NDIS_WDI_INIT_PARAMETERS {
  NDIS_OBJECT_HEADER                          Header;
  ULONG                                       WdiVersion;
  NDIS_WDI_OPEN_ADAPTER_COMPLETE_HANDLER      OpenAdapterCompleteHandler;
  NDIS_WDI_CLOSE_ADAPTER_COMPLETE_HANDLER     CloseAdapterCompleteHandler;
  NDIS_WDI_IDLE_NOTIFICATION_CONFIRM_HANDLER  UeIdleNotificationConfirm;
  NDIS_WDI_IDLE_NOTIFICATION_COMPLETE_HANDLER UeIdleNotificationComplete;
} NDIS_WDI_INIT_PARAMETERS, *PNDIS_WDI_INIT_PARAMETERS;
````


## -struct-fields
<dl>

### -field Header

<dd>
<p>The 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure for the
     NDIS_WDI_INIT_PARAMETERS structure. Set the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_WDI_INIT_PARAMETERS.
     </p>
<p>To indicate the version of the NDIS_WDI_INIT_PARAMETERS structure, set the 
     <b>Revision</b> member to the following value:</p>
<p></p>
<dl>

### -field NDIS_OBJECT_TYPE_WDI_INIT_PARAMETERS_REVISION_1

<dd>
<p>Set the 
        <b>Size</b> member to NDIS_SIZEOF_WDI_INIT_PARAMETERS_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field WdiVersion

<dd>
<p>The version of WDI used by the driver. Set this member to one of the following values:</p>
<p></p>
<dl>

### -field WDI_VERSION_1_0

<dd>
<p>WDI version 1.0</p>
</dd>
</dl>
</dd>

### -field OpenAdapterCompleteHandler

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-ndis-wdi-open-adapter-complete.md">NdisWdiOpenAdapterComplete</a> callback function.</p>
</dd>

### -field CloseAdapterCompleteHandler

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-ndis-wdi-close-adapter-complete.md">NdisWdiCloseAdapterComplete</a> callback function.</p>
</dd>

### -field UeIdleNotificationConfirm

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-ndis-wdi-idle-notification-confirm.md">NdisWdiIdleNotificationConfirm</a> callback function.</p>
</dd>

### -field UeIdleNotificationComplete

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-ndis-wdi-idle-notification-complete.md">NdisWdiIdleNotificationComplete</a> callback function.</p>
</dd>
</dl>

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
<dt>Dot11wdi.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>