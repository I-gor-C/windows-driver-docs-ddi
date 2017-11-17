---
UID: NC.ndis.MINIPORT_IDLE_NOTIFICATION
title: MINIPORT_IDLE_NOTIFICATION
author: windows-driver-content
description: NDIS calls the MiniportIdleNotification handler function to start the NDIS selective suspend operation on an idle network adapter. Through this operation, the network adapter is suspended and transitioned to a low-power state.
old-location: netvista\miniportidlenotification.htm
ms.assetid: D679DEF0-1229-4731-8024-4DEDAE5B0185
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MiniportIdleNotification
req.alt-loc: Ndis.h
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
ms.keywords: RxNameCacheInitialize
req.iface: 
---

# MINIPORT_IDLE_NOTIFICATION callback



## -description
<p>
<p>NDIS calls the  <i>MiniportIdleNotification</i> handler function to start the NDIS selective suspend operation on an idle network adapter. Through this operation, the network adapter is suspended and transitioned to a low-power state.</p>
</p>
<p>NDIS calls the  <i>MiniportIdleNotification</i> handler function to start the NDIS selective suspend operation on an idle network adapter. Through this operation, the network adapter is suspended and transitioned to a low-power state.</p>


## -prototype

````
MINIPORT_IDLE_NOTIFICATION MiniportIdleNotification;

NDIS_STATUS MiniportIdleNotification(
  _In_ NDIS_HANDLE MiniportAdapterContext,
  _In_ BOOLEAN     ForceIdle
)
{ ... }
````


## -parameters
<dl>

### -param <i>MiniportAdapterContext</i> [in]

<dd>
<p>A handle to a context area that the miniport driver allocated in its <a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a> function. The miniport driver uses this context area to maintain state information for a network adapter.</p>
</dd>

### -param <i>ForceIdle</i> [in]

<dd>
<p>A <b>BOOLEAN</b> value that, when set to <b>TRUE</b>, specifies that the miniport driver must not veto the idle notification and must continue with the low-power state transition.</p>
<p>For more information about the <i>ForceIdle</i> parameter, see the Remarks section.</p>
</dd>
</dl>

## -returns
<p><i>MiniportIdleNotification</i> returns one of the following status values:</p><dl>
<dt><b>NDIS_STATUS_PENDING</b></dt>
</dl><p>The miniport driver successfully handled the idle notification. The notification is left in a pending state until the miniport driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/hh451491">NdisMIdleNotificationComplete</a>.</p><dl>
<dt><b>NDIS_STATUS_BUSY</b></dt>
</dl><p>
       The miniport driver vetoed the idle notification because the network adapter is still being used.</p><dl>
<dt><b>NDIS_STATUS_FAILURE</b></dt>
</dl><p>The miniport driver could not issue a bus-specific IRP successfully.</p>

<p> </p>

## -remarks
<p>The <i>MiniportIdleNotification</i> handler function is required for miniport drivers that support the NDIS selective suspend interface. For more information about how the driver registers its selective suspend handler functions, see <a href="NULL">Registering NDIS Selective Suspend Handler Functions</a>.</p>

<p>NDIS sets the <i>ForceIdle</i> parameter to <b>FALSE</b> when the network adapter has been inactive for longer than the idle time-out period. Therefore, NDIS <i>selectively suspends</i> only the network adapter.

</p>

<p>The duration of the idle time-out period is specified by the value of the <b>*SSIdleTimeout</b> INF keyword. For more information about this keyword, see <a href="NULL">Standardized INF Keywords for NDIS Selective Suspend</a>. 

</p>

<p>If the miniport driver determines that the network adapter is being used, it can veto the idle notification request by returning NDIS_STATUS_BUSY. This causes NDIS to restart the monitor of activity on the network adapter. 

If the adapter becomes inactive again within the idle time-out period, NDIS calls <i>MiniportIdleNotification</i>. </p>

<p>After the idle notification is issued, it can be canceled and completed in the following way:</p>

<p>NDIS can cancel the outstanding idle notification if the following conditions are true:</p>

<p>An overlying protocol or filter driver issues either a send packet request or an OID request to the miniport driver. 
</p>

<p>The underlying adapter signals a wake-up event, such as receiving a packet that matches a wake-on-LAN (WOL) pattern or detecting a change in its media connection status. 
</p>

<p>NDIS cancels the idle notification by calling <a href="https://msdn.microsoft.com/9965E4EA-10E3-4240-9E4F-D3B49B8F9593">MiniportCancelIdleNotification</a>. When this handler function is called, the miniport driver cancels any bus-specific IRPs that it may have previously issued for the idle notification. 
Finally, the miniport driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/hh451491">NdisMIdleNotificationComplete</a> to complete the idle notification.</p>

<p> After the network adapter is in a low-power state, the miniport driver can complete the idle notification itself in order to resume the adapter to a full-power state. The reasons for doing this are specific to the design and requirements of the driver and adapter. </p>

<p>The miniport driver completes the idle notification  by calling <a href="https://msdn.microsoft.com/library/windows/hardware/hh451491">NdisMIdleNotificationComplete</a>. For more information about how the miniport driver completes the idle notification, see <a href="NULL">Completing the NDIS Selective Suspend Idle Notification</a>.</p>

<p>For more information on how to handle idle notifications for NDIS selective suspend, see <a href="NULL">Handling the NDIS Selective Suspend Idle Notification</a>.</p>

<p>For guidelines on how to implement the <i>MiniportIdleNotification</i> handler function, see <a href="NULL">Implementing a MiniportIdleNotification Handler Function</a>.</p>

<p>The <i>MiniportIdleNotification</i> handler function is required for miniport drivers that support the NDIS selective suspend interface. For more information about how the driver registers its selective suspend handler functions, see <a href="NULL">Registering NDIS Selective Suspend Handler Functions</a>.</p>

<p>NDIS sets the <i>ForceIdle</i> parameter to <b>FALSE</b> when the network adapter has been inactive for longer than the idle time-out period. Therefore, NDIS <i>selectively suspends</i> only the network adapter.

</p>

<p>The duration of the idle time-out period is specified by the value of the <b>*SSIdleTimeout</b> INF keyword. For more information about this keyword, see <a href="NULL">Standardized INF Keywords for NDIS Selective Suspend</a>. 

</p>

<p>If the miniport driver determines that the network adapter is being used, it can veto the idle notification request by returning NDIS_STATUS_BUSY. This causes NDIS to restart the monitor of activity on the network adapter. 

If the adapter becomes inactive again within the idle time-out period, NDIS calls <i>MiniportIdleNotification</i>. </p>

<p>After the idle notification is issued, it can be canceled and completed in the following way:</p>

<p>NDIS can cancel the outstanding idle notification if the following conditions are true:</p>

<p>An overlying protocol or filter driver issues either a send packet request or an OID request to the miniport driver. 
</p>

<p>The underlying adapter signals a wake-up event, such as receiving a packet that matches a wake-on-LAN (WOL) pattern or detecting a change in its media connection status. 
</p>

<p>NDIS cancels the idle notification by calling <a href="https://msdn.microsoft.com/9965E4EA-10E3-4240-9E4F-D3B49B8F9593">MiniportCancelIdleNotification</a>. When this handler function is called, the miniport driver cancels any bus-specific IRPs that it may have previously issued for the idle notification. 
Finally, the miniport driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/hh451491">NdisMIdleNotificationComplete</a> to complete the idle notification.</p>

<p> After the network adapter is in a low-power state, the miniport driver can complete the idle notification itself in order to resume the adapter to a full-power state. The reasons for doing this are specific to the design and requirements of the driver and adapter. </p>

<p>The miniport driver completes the idle notification  by calling <a href="https://msdn.microsoft.com/library/windows/hardware/hh451491">NdisMIdleNotificationComplete</a>. For more information about how the miniport driver completes the idle notification, see <a href="NULL">Completing the NDIS Selective Suspend Idle Notification</a>.</p>

<p>For more information on how to handle idle notifications for NDIS selective suspend, see <a href="NULL">Handling the NDIS Selective Suspend Idle Notification</a>.</p>

<p>For guidelines on how to implement the <i>MiniportIdleNotification</i> handler function, see <a href="NULL">Implementing a MiniportIdleNotification Handler Function</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.30 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
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

## -see-also
<dl>
<dt><b></b></dt>
<dt>
<a href="https://msdn.microsoft.com/9965E4EA-10E3-4240-9E4F-D3B49B8F9593">MiniportCancelIdleNotification</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451491">NdisMIdleNotificationComplete</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20MINIPORT_IDLE_NOTIFICATION callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
