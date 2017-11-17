---
UID: NS.dot11wdi._NDIS_WDI_INIT_PARAMETERS
title: NDIS_WDI_INIT_PARAMETERS
author: windows-driver-content
description: The NDIS_WDI_INIT_PARAMETERS structure specifies the WDI functions provided by the operating system and called by the IHV WDI driver.
old-location: netvista\ndis_wdi_init_parameters.htm
ms.assetid: 871D266C-55DF-4113-9714-92AB129303E5
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
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
ms.keywords: NDIS_WDI_INIT_PARAMETERS, NDIS_WDI_INIT_PARAMETERS, *PNDIS_WDI_INIT_PARAMETERS
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

### -field <b>Header</b>

<dd>
<p>The 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure for the
     NDIS_WDI_INIT_PARAMETERS structure. Set the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_WDI_INIT_PARAMETERS.
     </p>
<p>To indicate the version of the NDIS_WDI_INIT_PARAMETERS structure, set the 
     <b>Revision</b> member to the following value:</p>
<p></p>
<dl>

### -field <a id="NDIS_OBJECT_TYPE_WDI_INIT_PARAMETERS_REVISION_1"></a><a id="ndis_object_type_wdi_init_parameters_revision_1"></a>NDIS_OBJECT_TYPE_WDI_INIT_PARAMETERS_REVISION_1

<dd>
<p>Set the 
        <b>Size</b> member to NDIS_SIZEOF_WDI_INIT_PARAMETERS_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field <b>WdiVersion</b>

<dd>
<p>The version of WDI used by the driver. Set this member to one of the following values:</p>
<p></p>
<dl>

### -field <a id="WDI_VERSION_1_0"></a><a id="wdi_version_1_0"></a>WDI_VERSION_1_0

<dd>
<p>WDI version 1.0</p>
</dd>
</dl>
</dd>

### -field <b>OpenAdapterCompleteHandler</b>

<dd>
<p>The entry point of the <a href="https://msdn.microsoft.com/FD6FF134-A8D7-433E-9353-88965E67749E">NdisWdiOpenAdapterComplete</a> callback function.</p>
</dd>

### -field <b>CloseAdapterCompleteHandler</b>

<dd>
<p>The entry point of the <a href="https://msdn.microsoft.com/42500F6F-8E97-454F-819F-8EA3785C0D04">NdisWdiCloseAdapterComplete</a> callback function.</p>
</dd>

### -field <b>UeIdleNotificationConfirm</b>

<dd>
<p>The entry point of the <a href="https://msdn.microsoft.com/39D070BE-FF6F-4EC8-A4E4-DF45C5089AA7">NdisWdiIdleNotificationConfirm</a> callback function.</p>
</dd>

### -field <b>UeIdleNotificationComplete</b>

<dd>
<p>The entry point of the <a href="https://msdn.microsoft.com/22622545-F92E-4FEE-8F5D-64EC792490C7">NdisWdiIdleNotificationComplete</a> callback function.</p>
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