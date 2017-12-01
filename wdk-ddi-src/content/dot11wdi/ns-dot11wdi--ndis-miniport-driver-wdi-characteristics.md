---
UID: NS.dot11wdi._NDIS_MINIPORT_DRIVER_WDI_CHARACTERISTICS
title: NDIS_MINIPORT_DRIVER_WDI_CHARACTERISTICS
author: windows-driver-content
description: The NDIS_MINIPORT_DRIVER_WDI_CHARACTERISTICS structure defines the set of handlers that a WDI miniport driver must implement.
old-location: netvista\ndis_miniport_driver_wdi_characteristics.htm
old-project: netvista
ms.assetid: 2F69C228-FF2D-4277-A4C9-14FBADA1CD31
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_MINIPORT_DRIVER_WDI_CHARACTERISTICS, NDIS_MINIPORT_DRIVER_WDI_CHARACTERISTICS, *PNDIS_MINIPORT_DRIVER_WDI_CHARACTERISTICS
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
req.alt-api: NDIS_MINIPORT_DRIVER_WDI_CHARACTERISTICS
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

# NDIS_MINIPORT_DRIVER_WDI_CHARACTERISTICS structure



## -description
<p>The NDIS_MINIPORT_DRIVER_WDI_CHARACTERISTICS structure defines the set of handlers that a WDI miniport driver must implement. It is used by the IHV driver to register additional handlers for the control path and the full set of handlers for the data path.</p>


## -syntax

````
typedef struct _NDIS_MINIPORT_DRIVER_WDI_CHARACTERISTICS {
  NDIS_OBJECT_HEADER                            Header;
  ULONG                                         WdiVersion;
  MINIPORT_WDI_ALLOCATE_ADAPTER_HANDLER         AllocateAdapterHandler;
  MINIPORT_WDI_FREE_ADAPTER_HANDLER             FreeAdapterHandler;
  MINIPORT_WDI_OPEN_ADAPTER_HANDLER             OpenAdapterHandler;
  MINIPORT_WDI_CLOSE_ADAPTER_HANDLER            CloseAdapterHandler;
  MINIPORT_WDI_START_OPERATION_HANDLER          StartOperationHandler;
  MINIPORT_WDI_STOP_OPERATION_HANDLER           StopOperationHandler;
  MINIPORT_WDI_POST_PAUSE_HANDLER               PostPauseHandler;
  MINIPORT_WDI_POST_RESTART_HANDLER             PostRestartHandler;
  MINIPORT_WDI_HANG_DIAGNOSE_HANDLER            HangDiagnoseHandler;
  MINIPORT_WDI_TAL_TXRX_INITIALIZE_HANDLER      TalTxRxInitializeHandler;
  MINIPORT_WDI_TAL_TXRX_DEINITIALIZE_HANDLER    TalTxRxDeinitializeHandler;
  MINIPORT_WDI_IDLE_NOTIFICATION_HANDLER        LeIdleNotificationHandler;
  MINIPORT_WDI_CANCEL_IDLE_NOTIFICATION_HANDLER LeCancelIdleNotificationHandler;
} NDIS_MINIPORT_DRIVER_WDI_CHARACTERISTICS, *PNDIS_MINIPORT_DRIVER_WDI_CHARACTERISTICS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure for the
     NDIS_MINIPORT_DRIVER_WDI_CHARACTERISTICS structure. Set the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_MINIPORT_WDI_CHARACTERISTICS.
     </p>
<p>To indicate the version of the NDIS_MINIPORT_DRIVER_WDI_CHARACTERISTICS structure, set the 
     <b>Revision</b> member to the following value:</p>
<p></p>
<dl>

### -field <a id="NDIS_MINIPORT_DRIVER_WDI_CHARACTERISTICS_REVISION_1"></a><a id="ndis_miniport_driver_wdi_characteristics_revision_1"></a>NDIS_MINIPORT_DRIVER_WDI_CHARACTERISTICS_REVISION_1

<dd>
<p>Set the 
        <b>Size</b> member to NDIS_SIZEOF_MINIPORT_WDI_CHARACTERISTICS_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field <b>WdiVersion</b>

<dd>
<p>The version of WDI used by the driver. Set this member to one of the following values:</p>
<p></p>
<dl>

### -field <a id="WDI_VERSION_LATEST"></a><a id="wdi_version_latest"></a>WDI_VERSION_LATEST

<dd>
<p>The latest WDI version</p>
</dd>

### -field <a id="WDI_VERSION_1_0_1"></a><a id="wdi_version_1_0_1"></a>WDI_VERSION_1_0_1

<dd>
<p>WDI version 1.0.1</p>
</dd>

### -field <a id="WDI_VERSION_1_0"></a><a id="wdi_version_1_0"></a>WDI_VERSION_1_0

<dd>
<p>WDI version 1.0</p>
</dd>
</dl>
</dd>

### -field <b>AllocateAdapterHandler</b>

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-allocate-adapter.md">MiniportWdiAllocateAdapter</a> handler function.</p>
</dd>

### -field <b>FreeAdapterHandler</b>

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-free-adapter.md">MiniportWdiFreeAdapter</a> handler function.</p>
</dd>

### -field <b>OpenAdapterHandler</b>

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-open-adapter.md">MiniportWdiOpenAdapter</a> handler function.</p>
</dd>

### -field <b>CloseAdapterHandler</b>

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-close-adapter.md">MiniportWdiCloseAdapter</a> handler function.</p>
</dd>

### -field <b>StartOperationHandler</b>

<dd>
<p>The entry point of the <a href="netvista.miniportwdistartoperation">MiniportWdiStartOperation</a> handler function.</p>
</dd>

### -field <b>StopOperationHandler</b>

<dd>
<p>The entry point of the <a href="netvista.miniportwdistopoperation">MiniportWdiStopOperation</a> handler function.</p>
</dd>

### -field <b>PostPauseHandler</b>

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-post-adapter-pause.md">MiniportWdiPostAdapterPause</a> handler function.</p>
</dd>

### -field <b>PostRestartHandler</b>

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-post-adapter-restart.md">MiniportWdiPostAdapterRestart</a> handler function.</p>
</dd>

### -field <b>HangDiagnoseHandler</b>

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-adapter-hang-diagnose.md">MiniportWdiAdapterHangDiagnose</a> handler function.</p>
</dd>

### -field <b>TalTxRxInitializeHandler</b>

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tal-txrx-initialize.md">MiniportWdiTalTxRxInitialize</a> handler function.

</p>
</dd>

### -field <b>TalTxRxDeinitializeHandler</b>

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tal-txrx-deinitialize.md">MiniportWdiTalTxRxDeinitialize</a> handler function.

</p>
</dd>

### -field <b>LeIdleNotificationHandler</b>

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-idle-notification.md">MiniportWdiIdleNotification</a> handler function.

</p>
</dd>

### -field <b>LeCancelIdleNotificationHandler</b>

<dd>
<p>The entry point of the <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-cancel-idle-notification.md">MiniportWdiCancelIdleNotification</a> handler function.

</p>
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