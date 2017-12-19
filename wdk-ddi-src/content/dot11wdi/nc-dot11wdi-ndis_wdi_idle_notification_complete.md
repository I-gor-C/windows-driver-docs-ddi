---
UID: NC.dot11wdi.NDIS_WDI_IDLE_NOTIFICATION_COMPLETE
title: NDIS_WDI_IDLE_NOTIFICATION_COMPLETE
author: windows-driver-content
description: Miniport drivers call NdisWdiIdleNotificationComplete callback function to complete a pending idle notification for an NDIS selective suspend operation. NDIS begins the operation when it calls the driver's MiniportWdiIdleNotification handler function.
old-location: netvista\ndiswdiidlenotificationcomplete.htm
old-project: NetVista
ms.assetid: 22622545-F92E-4FEE-8F5D-64EC792490C7
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: _SYNTH_STATS, *PSYNTH_STATS, SYNTH_STATS, PSYNTH_STATS
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
req.alt-api: NdisWdiIdleNotificationComplete
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
---

# NDIS_WDI_IDLE_NOTIFICATION_COMPLETE callback



## -description
Miniport drivers call NdisWdiIdleNotificationComplete callback function to complete a pending idle notification for an NDIS selective suspend operation. NDIS begins the operation when it calls the driver's <a href="..\dot11wdi\nc-dot11wdi-miniport_wdi_idle_notification.md">MiniportWdiIdleNotification</a> handler function.

This is a control path callback inside <a href="netvista.ndis_wdi_init_parameters">NDIS_WDI_INIT_PARAMETERS</a>.



## -prototype

````
NDIS_WDI_IDLE_NOTIFICATION_COMPLETE NdisWdiIdleNotificationComplete;

VOID NdisWdiIdleNotificationComplete(
  _In_ NDIS_HANDLE MiniportAdapterHandle
)
{ ... }
````


## -parameters

### -param MiniportAdapterHandle [in]

The miniport handle.


## -returns
This callback function does not return a value.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows 10

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2016

</td>
</tr>
<tr>
<th width="30%">
Header

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
<a href="netvista.completing_the_ndis_selective_suspend_idle_notification">Completing the NDIS Selective Suspend Idle Notification</a>
</dt>
<dt>
<a href="..\dot11wdi\nc-dot11wdi-miniport_wdi_idle_notification.md">MiniportWdiIdleNotification</a>
</dt>
<dt>
<a href="netvista.ndis_wdi_init_parameters">NDIS_WDI_INIT_PARAMETERS</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20NDIS_WDI_IDLE_NOTIFICATION_COMPLETE callback function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

