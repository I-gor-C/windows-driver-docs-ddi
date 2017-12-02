---
UID: NC.dot11wdi.MINIPORT_WDI_TAL_TXRX_START
title: MINIPORT_WDI_TAL_TXRX_START
author: windows-driver-content
description: The MiniportWdiTalTxRxStart handler function provides TXRX configuration parameters to the TAL.
old-location: netvista\miniportwditaltxrxstart.htm
old-project: netvista
ms.assetid: 6F88F4B1-8D2A-41CC-8D60-C1CF91ED072A
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: SYNTHVOICEPRIORITY_INSTANCE, SYNTHVOICEPRIORITY_INSTANCE, *PSYNTHVOICEPRIORITY_INSTANCE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: dot11wdi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MiniportWdiTalTxRxStart
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
req.irql: 
req.iface: ISynthSinkDMus
---

# MINIPORT_WDI_TAL_TXRX_START callback



## -description
<p>The 
  MiniportWdiTalTxRxStart handler function provides TXRX configuration parameters to the TAL.   The configuration parameters include the TX/RX capabilities specified by the target device as part of its initialization. It is issued in the context of driver initialization after obtaining device capabilities.</p>
<p>This is a WDI miniport handler inside <a href="..\dot11wdi\ns-dot11wdi--ndis-miniport-wdi-data-handlers.md">NDIS_MINIPORT_WDI_DATA_HANDLERS</a>.</p>


## -prototype

````
MINIPORT_WDI_TAL_TXRX_START MiniportWdiTalTxRxStart;

NDIS_STATUS MiniportWdiTalTxRxStart(
  _In_  TAL_TXRX_HANDLE                MiniportTalTxRxContext,
  _In_  PWDI_TXRX_TARGET_CONFIGURATION pWifiTxRxConfiguration,
  _Out_ PTAL_TXRX_PARAMETERS           pTalTxRxParameters
)
{ ... }
````


## -parameters
<dl>

### -param MiniportTalTxRxContext [in]

<dd>
<p>TAL device handle returned by the IHV miniport in <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-tal-txrx-initialize.md">MiniportWdiTalTxRxInitialize</a>.</p>
</dd>

### -param pWifiTxRxConfiguration [in]

<dd>
<p>Pointer to the <a href="..\dot11wdi\ns-dot11wdi--wdi-txrx-target-configuration.md">WDI_TXRX_TARGET_CONFIGURATION</a> structure specified by the target device as part of initialization.</p>
</dd>

### -param pTalTxRxParameters [out]

<dd>
<p>Pointer to a <a href="..\dot11wdi\ns-dot11wdi--tal-txrx-parameters.md">TAL_TXRX_PARAMETERS</a> structure that specifies the TAL parameters used by the TxMgr or RxMgr.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>Indicates that the miniport driver successfully started the datapath components.</p>

<p> </p>

<p>To define a MiniportWdiTalTxRxStart function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="https://msdn.microsoft.com/2F3549EF-B50F-455A-BDC7-1F67782B8DCA">Code Analysis for Drivers</a>, <a href="https://msdn.microsoft.com/74feeb16-387c-4796-987a-aff3fb79b556">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a MiniportWdiTalTxRxStart function that is named "MyTalTxRxStart", use the <b>MINIPORT_WDI_TAL_TXRX_START</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>MINIPORT_WDI_TAL_TXRX_START</b> function type is defined in the dot11wdi.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>MINIPORT_WDI_TAL_TXRX_START</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="https://msdn.microsoft.com/232c4272-0bf0-4a4e-9560-3bceeca8a3e3">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

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
<dt>Dot11wdi.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\dot11wdi\ns-dot11wdi--ndis-miniport-wdi-data-handlers.md">NDIS_MINIPORT_WDI_DATA_HANDLERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt297625">TAL_TXRX_HANDLE</a>
</dt>
<dt>
<a href="..\dot11wdi\ns-dot11wdi--tal-txrx-parameters.md">TAL_TXRX_PARAMETERS</a>
</dt>
<dt>
<a href="..\dot11wdi\ns-dot11wdi--wdi-txrx-target-configuration.md">WDI_TXRX_TARGET_CONFIGURATION</a>
</dt>
<dt>
<a href="netvista.wdi_general_datapath_interfaces">WDI general datapath interfaces</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20MINIPORT_WDI_TAL_TXRX_START callback function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
